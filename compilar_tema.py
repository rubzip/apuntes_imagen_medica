#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compilar_tema.py
Compilador de apuntes para el Grado Superior en Imagen para el Diagnóstico y Medicina Nuclear.

Encadena en orden numérico todas las carpetas/módulos de un tema y genera un único PDF
autocontenido con portada, índice de contenidos, estilos editoriales y gráficos vectoriales SVG.

Uso:
    python3 compilar_tema.py Tema_1
    python3 compilar_tema.py 1
    ./compilar_tema.py Tema_1 -o Tema_1_Completo.pdf
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


# Plantilla CSS profesional adaptada a apuntes técnicos / médicos
CSS_TEMPLATE = """
@page {
    size: A4;
    margin: 18mm 16mm 20mm 16mm;
    @bottom-center {
        content: counter(page);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 8.5pt;
        color: #64748b;
    }
}

@media print {
    body {
        font-size: 10.5pt;
        line-height: 1.55;
    }
    .portada {
        page-break-after: always;
        height: 92vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .modulo-container {
        page-break-before: always;
    }
    .no-break {
        page-break-inside: avoid;
    }
    table, figure, .callout, blockquote {
        page-break-inside: avoid;
    }
    h1, h2, h3, h4 {
        page-break-after: avoid;
    }
}

* {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

/* PORTADA */
.portada {
    padding: 30px 20px;
    text-align: center;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
    margin-bottom: 40px;
}
.portada-header {
    margin-top: 20px;
}
.portada-institucion {
    font-size: 11pt;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #0369a1;
    margin-bottom: 8px;
}
.portada-grado {
    font-size: 13pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 35px;
}
.portada-modulo-titulo {
    font-size: 26pt;
    font-weight: 800;
    color: #1e3a8a;
    line-height: 1.25;
    margin: 25px 0 10px 0;
}
.portada-subtitulo {
    font-size: 14pt;
    color: #475569;
    margin-bottom: 40px;
}
.portada-indice {
    text-align: left;
    max-width: 520px;
    margin: 0 auto;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 18px 24px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.03);
}
.portada-indice h3 {
    margin-top: 0;
    margin-bottom: 12px;
    font-size: 12pt;
    color: #1e40af;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 6px;
}
.portada-indice ol {
    margin: 0;
    padding-left: 20px;
    font-size: 10pt;
    color: #334155;
}
.portada-indice li {
    margin-bottom: 6px;
    font-weight: 500;
}
.portada-footer {
    font-size: 9pt;
    color: #94a3b8;
    margin-top: 30px;
}

/* ENCABEZADOS */
h1 {
    font-size: 20pt;
    font-weight: 800;
    color: #1e3a8a;
    margin-top: 24px;
    margin-bottom: 12px;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 6px;
}
h2 {
    font-size: 15pt;
    font-weight: 700;
    color: #1e40af;
    margin-top: 24px;
    margin-bottom: 10px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
}
h3 {
    font-size: 12pt;
    font-weight: 600;
    color: #334155;
    margin-top: 18px;
    margin-bottom: 8px;
}
h4 {
    font-size: 11pt;
    font-weight: 600;
    color: #475569;
    margin-top: 14px;
    margin-bottom: 6px;
}

p {
    margin-top: 0;
    margin-bottom: 10px;
    text-align: justify;
}

/* LISTAS */
ul, ol {
    margin-top: 0;
    margin-bottom: 12px;
    padding-left: 24px;
}
li {
    margin-bottom: 4px;
}

/* TABLAS */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}
th, td {
    border: 1px solid #cbd5e1;
    padding: 7px 11px;
    text-align: left;
    vertical-align: top;
}
th {
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
}
tr:nth-child(even) td {
    background-color: #f8fafc;
}

/* CITAS Y BLOQUES RESALTADOS */
blockquote {
    margin: 14px 0;
    padding: 10px 16px;
    background-color: #f0f7ff;
    border-left: 4px solid #2563eb;
    border-radius: 0 6px 6px 0;
    color: #1e293b;
    page-break-inside: avoid;
}
blockquote p {
    margin-bottom: 6px;
    text-align: left;
}
blockquote p:last-child {
    margin-bottom: 0;
}
blockquote strong {
    color: #1e40af;
}

/* IMÁGENES Y DIAGRAMAS SVG */
figure {
    margin: 18px auto;
    text-align: center;
    page-break-inside: avoid;
}
figure img, p img {
    max-width: 92%;
    max-height: 380px;
    height: auto;
    display: block;
    margin: 10px auto;
    object-fit: contain;
}
figcaption, .pie-figura {
    font-size: 9pt;
    font-style: italic;
    color: #64748b;
    margin-top: 6px;
    margin-bottom: 12px;
    text-align: center;
    display: block;
}

/* SEPARADORES */
hr {
    border: 0;
    height: 1px;
    background-color: #e2e8f0;
    margin: 20px 0;
}

/* CÓDIGO INLINE */
code {
    background-color: #f1f5f9;
    padding: 2px 5px;
    border-radius: 4px;
    font-size: 9pt;
    font-family: SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}
"""


def resolver_directorio_tema(arg_tema: str) -> Path:
    """Resuelve la ruta del directorio del tema a partir de argumentos como '1', 'Tema_1', etc."""
    cwd = Path.cwd()
    ruta_directa = Path(arg_tema)
    if ruta_directa.is_dir():
        return ruta_directa.resolve()

    # Si pasaron solo un número, por ejemplo '1'
    candidatos = [
        cwd / f"Tema_{arg_tema}",
        cwd / f"tema_{arg_tema}",
        cwd / f"Tema {arg_tema}",
        cwd / arg_tema,
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
    """
    def reemplazo(match):
        alt = match.group(1)
        src = match.group(2).strip()

        # Si ya es un data URI o URL externa, no tocar
        if src.startswith("data:") or src.startswith("http://") or src.startswith("https://"):
            return match.group(0)

        img_path = (modulo_dir / src).resolve()
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
    # Patrón: <p><img ...></p>\s*<p><em>(Figura.*?)</em></p>
    patron = r'<p>\s*(<img[^>]+>)\s*</p>\s*<p>\s*<em>\s*(Figura[^<]+?)\s*</em>\s*</p>'
    reemplazo = r'<figure>\1<figcaption class="pie-figura"><em>\2</em></figcaption></figure>'
    return re.sub(patron, reemplazo, html_contenido, flags=re.IGNORECASE)


def recopilar_modulos(tema_dir: Path):
    """
    Localiza y ordena numéricamente todas las subcarpetas del tema.
    Lee el archivo Markdown principal de cada una.
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


def generar_html_unificado(tema_nombre: str, modulos: list, incluir_portada: bool = True) -> str:
    """Genera el documento HTML completo y unificado con estilos y recursos incrustados."""
    md_parser = markdown.Markdown(extensions=["extra", "tables", "toc", "sane_lists"])

    modulos_html = []
    lista_indice = []

    for mod in modulos:
        num = mod["numero"]
        titulo = mod["titulo"]
        carpeta = mod["carpeta"]
        raw_md = mod["contenido_md"]

        lista_indice.append(f"<li><strong>Módulo {num}:</strong> {titulo.replace(f'Módulo {num}.', '').strip()}</li>")

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

    # Bloque de portada
    portada_html = ""
    if incluir_portada:
        items_indice = "\n".join(lista_indice)
        nombre_bonito = tema_nombre.replace("_", " ").title()
        portada_html = f"""
        <div class="portada">
            <div class="portada-header">
                <div class="portada-institucion">Ciclo Formativo de Grado Superior</div>
                <div class="portada-grado">Imagen para el Diagnóstico y Medicina Nuclear</div>
            </div>
            <div>
                <div class="portada-modulo-titulo">{nombre_bonito}</div>
                <div class="portada-subtitulo">Fundamentos Físicos y Equipos · Apuntes de Estudio</div>
                <div class="portada-indice">
                    <h3>Contenido del Tema</h3>
                    <ol>
                        {items_indice}
                    </ol>
                </div>
            </div>
            <div class="portada-footer">
                Documento generado automáticamente · Compilación unificada de módulos
            </div>
        </div>
        """

    documento = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tema_nombre} - Apuntes</title>
    <style>
{CSS_TEMPLATE}
    </style>
</head>
<body>
{portada_html}
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
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/opt/google/chrome/google-chrome",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
    ]
    for c in candidatos:
        if c and os.path.exists(c) and os.access(c, os.X_OK):
            return c
    return None


def compilar_html_a_pdf(html_path: Path, pdf_path: Path) -> bool:
    """Compila el archivo HTML a PDF usando Chrome/Chromium o WeasyPrint."""
    # 1. Intentar con Chrome / Chromium
    chrome_bin = encontrar_ejecutable_chrome()
    if chrome_bin:
        print(f"[+] Motor detectado: Chrome/Chromium ({chrome_bin})")
        # Probar primero con el nuevo headless de Chrome
        cmd_new = [
            chrome_bin,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
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
        description="Compila todos los módulos de un tema en un único PDF encadenado."
    )
    parser.add_argument("tema", help="Identificador o carpeta del tema (ej. 'Tema_1' o '1')")
    parser.add_argument("-o", "--output", help="Ruta del archivo PDF de salida (opcional)")
    parser.add_argument("--sin-portada", action="store_true", help="Omitir la página de portada e índice")
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

    # Recopilar módulos
    modulos = recopilar_modulos(tema_dir)
    if not modulos:
        print(f"[ERROR] No se encontraron subcarpetas numéricas con archivos .md en {tema_dir}")
        sys.exit(1)

    print(f"[+] Se encontraron {len(modulos)} módulos ordenados:")
    for mod in modulos:
        print(f"    - [{mod['numero']}] {mod['titulo']} ({mod['archivo'].name})")

    # Generar HTML unificado
    html_contenido = generar_html_unificado(
        tema_nombre=tema_nombre,
        modulos=modulos,
        incluir_portada=not args.sin_portada
    )

    # Ruta del HTML temporal/salida
    html_salida = tema_dir / f"{tema_nombre}_completo.html"
    html_salida.write_text(html_contenido, encoding="utf-8")
    print(f"[+] Documento HTML unificado generado: {html_salida} ({len(html_contenido)} bytes)")

    if args.solo_html:
        print("[✓] Proceso finalizado (--solo-html especificado).")
        return

    # Ruta del PDF de salida
    if args.output:
        pdf_salida = Path(args.output).resolve()
    else:
        pdf_salida = tema_dir / f"{tema_nombre}.pdf"

    print(f"[+] Compilando directamente a PDF: {pdf_salida.name} ...")
    exito = compilar_html_a_pdf(html_salida, pdf_salida)

    if exito:
        tamano_kb = pdf_salida.stat().st_size / 1024
        print(f"\n[✓] ¡PDF generado exitosamente!")
        print(f"    Ruta: {pdf_salida}")
        print(f"    Tamaño: {tamano_kb:.1f} KB")
        print(f"    Módulos incluidos: {len(modulos)}")
    else:
        print(f"\n[!] El documento HTML autocontenido está listo en:")
        print(f"    {html_salida}")
        print(f"\nNo se pudo invocar directamente un motor headless en este entorno.")
        print(f"Para generar el PDF final de una pasada en tu terminal:")
        print(f"  google-chrome --headless=new --disable-gpu --print-to-pdf=\"{pdf_salida}\" \"{html_salida}\"")
        print(f"o abre el archivo HTML en tu navegador y pulsa Ctrl+P -> 'Guardar como PDF'.")


if __name__ == "__main__":
    main()
