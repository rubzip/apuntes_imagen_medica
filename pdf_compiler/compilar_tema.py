#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compilar_tema.py
Compilador de apuntes para titulaciones técnicas y Formación Profesional.

Encadena en orden numérico todas las carpetas/módulos de un tema y genera un único
documento HTML y PDF autocontenido, con índice compacto, estilos desacoplados (style.css)
y gráficos vectoriales SVG incrustados en base64.

Uso:
    python3 compilar_tema.py Tema_1
    python3 compilar_tema.py 1
    ./compilar.sh 1
    ./compilar.sh Tema_1 -o Tema_1.pdf
"""

import sys
import os
import re
import base64
import shutil
import argparse
import subprocess
from pathlib import Path

try:
    import markdown
except ImportError:
    print("[ERROR] La librería 'markdown' de Python no está instalada.")
    print("Puedes instalarla ejecutando: pip install markdown")
    sys.exit(1)


def cargar_css(ruta_css: Path = None, tema_dir: Path = None) -> str:
    """
    Carga la hoja de estilos CSS desde un archivo externo desacoplado (style.css).
    Prioridad de búsqueda:
    1. Archivo explícito pasado por CLI (--css).
    2. style.css dentro de la carpeta del tema.
    3. style.css en el directorio del script (pdf_compiler/style.css).
    4. style.css en el directorio de trabajo actual.
    """
    candidatos = []
    if ruta_css:
        candidatos.append(Path(ruta_css).resolve())
    if tema_dir:
        candidatos.append((tema_dir / "style.css").resolve())

    script_dir = Path(__file__).resolve().parent
    candidatos.extend([
        (script_dir / "style.css").resolve(),
        (Path.cwd() / "pdf_compiler" / "style.css").resolve(),
        (Path.cwd() / "style.css").resolve(),
    ])

    for ruta in candidatos:
        if ruta.is_file():
            try:
                contenido = ruta.read_text(encoding="utf-8").strip()
                if contenido:
                    return contenido
            except Exception as e:
                print(f"  [AVISO] No se pudo leer {ruta}: {e}")

    print("  [AVISO] No se encontró 'style.css'. Usando estilos mínimos por defecto.")
    return """
    body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; line-height: 1.6; margin: 20px; }
    .indice-tema { background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px; border-radius: 6px; }
    """


def resolver_directorio_tema(arg_tema: str) -> Path:
    """Resuelve la ruta del directorio del tema a partir de argumentos como '1', 'Tema_1', etc."""
    cwd = Path.cwd()
    ruta_directa = Path(arg_tema)
    if ruta_directa.is_dir():
        return ruta_directa.resolve()

    # Si pasaron solo un número o nombre corto
    candidatos = [
        cwd / f"Tema_{arg_tema}",
        cwd / f"tema_{arg_tema}",
        cwd / f"Tema {arg_tema}",
        cwd / arg_tema,
        cwd / "Fisica" / f"Tema_{arg_tema}",
        cwd / "Fisica" / f"tema_{arg_tema}",
        cwd / "Fisica" / f"Tema {arg_tema}",
        cwd / "Fisica" / arg_tema,
    ]
    for c in candidatos:
        if c.is_dir():
            return c.resolve()

    # Buscar coincidencia insensible a mayúsculas
    for d in cwd.iterdir():
        if d.is_dir() and d.name.lower() in [f"tema_{arg_tema}".lower(), f"tema {arg_tema}".lower(), arg_tema.lower()]:
            return d.resolve()

    raise FileNotFoundError(f"No se encontró la carpeta del tema para el argumento: '{arg_tema}' en {cwd}")


def incrustar_recursos_locales(md_contenido: str, modulo_dir: Path) -> str:
    """
    Convierte referencias a imágenes locales (![alt](ruta)) en data URIs base64
    para que el HTML resultante sea 100% autocontenido y portable sin rutas rotas.
    Busca tanto en la carpeta del módulo como en subcarpetas habituales (figs/, imgs/, images/).
    """
    def reemplazo(match):
        alt = match.group(1)
        src = match.group(2).strip()

        # Si ya es un data URI o URL externa, no tocar
        if src.startswith("data:") or src.startswith("http://") or src.startswith("https://"):
            return match.group(0)

        img_path = (modulo_dir / src).resolve()
        if not (img_path.exists() and img_path.is_file()):
            for sub_img in ["figs", "imgs", "images"]:
                candidato = (modulo_dir / sub_img / src).resolve()
                if candidato.exists() and candidato.is_file():
                    img_path = candidato
                    break

        if img_path.exists() and img_path.is_file():
            ext = img_path.suffix.lower()
            if ext == ".svg":
                mime = "image/svg+xml"
            elif ext in [".png"]:
                mime = "image/png"
            elif ext in [".jpg", ".jpeg"]:
                mime = "image/jpeg"
            elif ext == ".webp":
                mime = "image/webp"
            else:
                mime = "application/octet-stream"

            try:
                b64 = base64.b64encode(img_path.read_bytes()).decode("utf-8")
                return f'![{alt}](data:{mime};base64,{b64})'
            except Exception as e:
                print(f"  [AVISO] No se pudo leer la imagen {img_path}: {e}")
                return match.group(0)
        else:
            print(f"  [AVISO] Imagen no encontrada: {src} en {modulo_dir}")
            return match.group(0)

    patron = r'!\[([^\]]*)\]\(([^)]+)\)'
    return re.sub(patron, reemplazo, md_contenido)


def envolver_figuras_html(html_contenido: str) -> str:
    """
    Agrupa pares de imagen + pie de figura (*Figura X...*) dentro de etiquetas <figure>
    para garantizar que la imagen y su descripción nunca se separen entre páginas.
    """
    patron = r'<p>\s*(<img[^>]+>)\s*</p>\s*<p>\s*<em>\s*(Figura[^<]+?)\s*</em>\s*</p>'
    reemplazo = r'<figure>\1<figcaption class="pie-figura"><em>\2</em></figcaption></figure>'
    return re.sub(patron, reemplazo, html_contenido, flags=re.IGNORECASE)


def recopilar_modulos(tema_dir: Path):
    """
    Localiza y ordena numéricamente todas las subcarpetas del tema.
    Lee el archivo Markdown principal de cada una y omite carpetas con archivos vacíos.
    """
    subcarpetas = []
    for item in tema_dir.iterdir():
        if item.is_dir() and item.name.isdigit():
            subcarpetas.append(item)

    # Orden natural por número de carpeta: 1, 2, 3, 4, etc.
    subcarpetas.sort(key=lambda d: int(d.name))

    modulos = []
    for sub in subcarpetas:
        num = int(sub.name)
        archivos_md = sorted(list(sub.glob("*.md")))
        if not archivos_md:
            print(f"  [INFO] Carpeta {sub.name}/ no contiene archivos .md (omitida)")
            continue

        md_file = archivos_md[0]
        raw_md = md_file.read_text(encoding="utf-8")
        if not raw_md.strip():
            print(f"  [INFO] Archivo {md_file.name} en {sub.name}/ está vacío (omitido)")
            continue

        # Extraer el título del módulo (primer encabezado # )
        titulo = f"Módulo {num}"
        for line in raw_md.splitlines():
            line_str = line.strip()
            if line_str.startswith("# "):
                titulo = line_str[2:].strip()
                break

        modulos.append({
            "numero": num,
            "carpeta": sub,
            "archivo": md_file,
            "titulo": titulo,
            "contenido_md": raw_md,
        })

    return modulos


def cargar_front(tema_dir: Path) -> str:
    """Busca y lee front.md dentro de la carpeta del tema si existe."""
    for nombre in ["front.md", "front.MD", "intro.md"]:
        f = tema_dir / nombre
        if f.is_file():
            try:
                contenido = f.read_text(encoding="utf-8").strip()
                if contenido:
                    return contenido
            except Exception as e:
                print(f"  [AVISO] No se pudo leer {f}: {e}")
    return ""


def generar_html_unificado(
    tema_nombre: str,
    modulos: list,
    css_contenido: str,
    front_contenido: str = "",
    tema_dir: Path = None,
    incluir_indice: bool = True
) -> str:
    """
    Genera el documento HTML completo y unificado con estilos desacoplados y recursos incrustados.
    Integra front.md y el índice compacto juntos en la cabecera, seguidos de un salto de línea.
    """
    md_parser = markdown.Markdown(extensions=["extra", "tables", "toc", "sane_lists"])

    modulos_html = []
    lista_indice = []

    for mod in modulos:
        num = mod["numero"]
        titulo = mod["titulo"]
        carpeta = mod["carpeta"]
        raw_md = mod["contenido_md"]

        titulo_limpio = re.sub(rf"^Módulo\s+{num}[\.\:\s-]*", "", titulo, flags=re.IGNORECASE).strip()
        if not titulo_limpio:
            titulo_limpio = titulo

        lista_indice.append(f'<li><a href="#modulo-{num}"><strong>Módulo {num}:</strong> {titulo_limpio}</a></li>')

        # Incrustar imágenes locales en base64
        md_con_imagenes = incrustar_recursos_locales(raw_md, carpeta)

        # Convertir a HTML
        md_parser.reset()
        cuerpo_html = md_parser.convert(md_con_imagenes)
        cuerpo_html = envolver_figuras_html(cuerpo_html)

        modulo_bloque = f"""
        <section class="modulo-container" id="modulo-{num}">
            {cuerpo_html}
        </section>
        """
        modulos_html.append(modulo_bloque)

    # 1. Bloque de front.md (si existe)
    front_html = ""
    if front_contenido:
        if tema_dir:
            front_contenido = incrustar_recursos_locales(front_contenido, tema_dir)
        md_parser.reset()
        front_html = md_parser.convert(front_contenido)
        front_html = envolver_figuras_html(front_html)

    # 2. Bloque de índice compacto (si está habilitado)
    indice_html = ""
    if incluir_indice and lista_indice:
        items_indice = "\n".join(lista_indice)
        indice_html = f"""
        <nav class="indice-tema">
            <div class="indice-titulo">Índice de contenidos</div>
            <ol>
                {items_indice}
            </ol>
        </nav>
        """

    # 3. front.md y el índice van juntos, seguidos de un salto de línea
    cabecera_inicial = ""
    if front_html or indice_html:
        cabecera_inicial = f"""
        <header class="tema-front">
            {front_html}
            {indice_html}
        </header>
        <hr class="salto-linea">
        """

    # Título limpio en <title> para evitar cabeceras ruidosas al imprimir en navegadores
    documento = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <!-- Soporte tipográfico para fórmulas matemáticas LaTeX con KaTeX -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body, {{
                delimiters: [
                    {{left: '$$', right: '$$', display: true}},
                    {{left: '$', right: '$', display: false}},
                    {{left: '\\\\(', right: '\\\\)', display: false}},
                    {{left: '\\\\[', right: '\\\\]', display: true}}
                ],
                throwOnError: false
            }});"></script>
    <style>
{css_contenido}
    </style>
</head>
<body>
{cabecera_inicial}
{"".join(modulos_html)}
</body>
</html>
"""
    return documento


def encontrar_ejecutable_chrome() -> str:
    """Busca un ejecutable de Chrome/Chromium disponible en el sistema."""
    candidatos = [
        shutil.which("google-chrome"),
        shutil.which("google-chrome-stable"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        shutil.which("brave-browser"),
        shutil.which("microsoft-edge"),
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/opt/google/chrome/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        "/snap/bin/chromium",
    ]
    for c in candidatos:
        if c and os.path.exists(c) and os.access(c, os.X_OK):
            return c
    return None


def compilar_html_a_pdf(html_path: Path, pdf_path: Path) -> bool:
    """
    Compila el archivo HTML a PDF usando Chrome/Chromium o WeasyPrint.
    Aplica '--no-pdf-header-footer' para suprimir cabeceras por defecto (título, fechas, URLs).
    """
    # 1. Intentar con Chrome / Chromium
    chrome_bin = encontrar_ejecutable_chrome()
    if chrome_bin:
        print(f"[+] Motor detectado: Chrome/Chromium ({chrome_bin})")
        # Headless moderno con supresión explícita de cabecera y pie por defecto
        cmd_new = [
            chrome_bin,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--virtual-time-budget=5000",
            f"--print-to-pdf={pdf_path}",
            str(html_path)
        ]
        try:
            res = subprocess.run(cmd_new, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=40)
            if res.returncode == 0 and pdf_path.exists() and pdf_path.stat().st_size > 0:
                return True
        except Exception:
            pass

        # Fallback al headless clásico
        cmd_legacy = [
            chrome_bin,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--virtual-time-budget=5000",
            f"--print-to-pdf={pdf_path}",
            str(html_path)
        ]
        try:
            res = subprocess.run(cmd_legacy, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=40)
            if res.returncode == 0 and pdf_path.exists() and pdf_path.stat().st_size > 0:
                return True
        except Exception:
            pass

    # 2. Intentar con WeasyPrint si está disponible
    weasyprint_bin = shutil.which("weasyprint")
    if weasyprint_bin:
        print(f"[+] Motor detectado: WeasyPrint ({weasyprint_bin})")
        cmd_weasy = [weasyprint_bin, str(html_path), str(pdf_path)]
        try:
            res = subprocess.run(cmd_weasy, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
            if res.returncode == 0 and pdf_path.exists() and pdf_path.stat().st_size > 0:
                return True
        except Exception:
            pass

    return False


def main():
    parser = argparse.ArgumentParser(
        description="Compila todos los módulos de una carpeta en un único HTML/PDF con índice compacto y CSS desacoplado."
    )
    parser.add_argument("tema", help="Ruta o identificador de la carpeta a compilar (ej. 'Fisica/Tema_1' o '1')")
    parser.add_argument("-o", "--output", help="Directorio donde guardar el HTML y el PDF (se crea si no existe)")
    parser.add_argument("-n", "--name", help="Nombre base de los archivos generados (por defecto: nombre de la carpeta)")
    parser.add_argument("--css", help="Ruta a un archivo style.css alternativo")
    parser.add_argument("--sin-indice", action="store_true", help="Omitir el bloque de índice")
    parser.add_argument("--sin-portada", dest="sin_indice", action="store_true", help="Alias para omitir el índice")
    parser.add_argument("--solo-html", action="store_true", help="Generar únicamente el archivo HTML unificado")

    args = parser.parse_args()

    print("=========================================================")
    print(" Compilador de Apuntes - Imagen y Diagnóstico Clínico")
    print("=========================================================")

    try:
        tema_dir = resolver_directorio_tema(args.tema)
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

    tema_nombre = tema_dir.name
    print(f"[+] Carpeta del tema: {tema_dir}")

    # Determinar nombre base de los archivos resultantes
    if args.name:
        nombre_base = Path(args.name).stem
    else:
        nombre_base = tema_nombre

    # Determinar directorio de salida (crear si no existe)
    if args.output:
        ruta_salida = Path(args.output).resolve()
        # Si pasaron una ruta con extensión .pdf o .html, interpretar directorio y nombre
        if ruta_salida.suffix.lower() in [".pdf", ".html"]:
            output_dir = ruta_salida.parent
            if not args.name:
                nombre_base = ruta_salida.stem
        else:
            output_dir = ruta_salida
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = tema_dir

    html_salida = output_dir / f"{nombre_base}.html"
    pdf_salida = output_dir / f"{nombre_base}.pdf"

    # Cargar CSS desacoplado
    css_contenido = cargar_css(ruta_css=args.css, tema_dir=tema_dir)

    # Recopilar módulos
    modulos = recopilar_modulos(tema_dir)
    if not modulos:
        print(f"[ERROR] No se encontraron subcarpetas numéricas con archivos .md en {tema_dir}")
        sys.exit(1)

    print(f"[+] Se encontraron {len(modulos)} módulos ordenados:")
    for mod in modulos:
        print(f"    - [{mod['numero']}] {mod['titulo']} ({mod['archivo'].name})")

    # Cargar front.md si existe
    front_contenido = cargar_front(tema_dir)
    if front_contenido:
        print(f"[+] Se encontró 'front.md' (incluido en cabecera junto al índice)")

    # Generar HTML unificado (front.md + índice juntos, seguido de salto de línea)
    html_contenido = generar_html_unificado(
        tema_nombre=tema_nombre,
        modulos=modulos,
        css_contenido=css_contenido,
        front_contenido=front_contenido,
        tema_dir=tema_dir,
        incluir_indice=not args.sin_indice
    )

    # Guardar HTML unificado
    html_salida.write_text(html_contenido, encoding="utf-8")
    print(f"[+] Documento HTML unificado generado: {html_salida} ({len(html_contenido)} bytes)")

    if args.solo_html:
        print("[✓] Proceso finalizado (--solo-html especificado).")
        return

    print(f"[+] Compilando a PDF: {pdf_salida.name} ...")
    exito = compilar_html_a_pdf(html_salida, pdf_salida)

    if exito:
        tamano_kb = pdf_salida.stat().st_size / 1024
        print(f"\n[✓] ¡Archivos generados exitosamente!")
        print(f"    Directorio: {output_dir}")
        print(f"    HTML:       {html_salida.name}")
        print(f"    PDF:        {pdf_salida.name} ({tamano_kb:.1f} KB)")
        print(f"    Módulos incluidos: {len(modulos)}")
    else:
        print(f"\n[!] El documento HTML autocontenido está listo en:")
        print(f"    {html_salida}")
        print(f"\nPara generar el PDF sin cabeceras ni pies por defecto (sin fecha ni título arriba):")
        print(f"  google-chrome --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=5000 --print-to-pdf=\"{pdf_salida}\" \"{html_salida}\"")
        print(f"O abre el HTML en el navegador, pulsa Ctrl+P y desmarca 'Encabezados y pies de página'.")


if __name__ == "__main__":
    main()
