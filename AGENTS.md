# Directrices Generales para la Elaboración y Adaptación de Temarios Didácticos (AGENTS.md)

Este documento constituye el **manual de referencia y estándar metodológico** para redactar, reorganizar, ilustrar y auditar temarios formativos en titulaciones técnicas, Formación Profesional (FP), educación superior y formación técnica aplicada.

Tanto los agentes de inteligencia artificial como los redactores humanos deben seguir estas directrices para asegurar un material pedagógicamente riguroso, accesible, visualmente impecable y directamente conectado con la realidad profesional.

---

## 1. Filosofía Pedagógica y Principios de Diseño Instruccional

### 1.1. Perfil del alumnado de referencia
- **Punto de partida:** El alumnado tipo de ciclos formativos y carreras técnicas aplicadas no cuenta generalmente con una base sólida en física teórica ni matemáticas avanzadas, y con frecuencia muestra desmotivación ante formalismos abstractos no contextualizados.
- **Motivación principal:** Interés vocacional y pragmático por el desempeño profesional (equipamiento tecnológico, procedimientos prácticos, seguridad, protocolos de actuación).
- **Necesidad formativa:** Necesitan comprender **qué ocurre físicamente, por qué ocurre y cómo influye en su trabajo cotidiano**, sin verse obligados a memorizar demostraciones algebraicas complejas.

### 1.2. Las Cuatro Reglas de Oro Didácticas

1. **Nada se usa antes de definirse (Andamiaje progresivo):**
   - Queda terminantemente prohibido emplear un concepto, magnitud física o término especializado si no ha sido explicado previamente o se define de forma explícita en ese mismo párrafo.
   - El orden de los contenidos debe ser estrictamente secuencial y acumulativo.

2. **Primero la intuición, luego la formalización:**
   Todo concepto nuevo debe seguir este itinerario pedagógico estricto:
   - **Definición llana:** Qué es en una sola frase cotidiana y memorable.
   - **Analogía o modelo mental:** Comparación con un fenómeno de la vida diaria fácil de visualizar.
   - **Apoyo gráfico:** Esquema o diagrama visual antes de introducir fórmulas.
   - **Definición formal y magnitudes:** Nombre técnico, fórmula (si procede) y unidades de medida.
   - **Ejemplo práctico/numérico resuelto:** Aplicación directa a una situación real.

3. **Lenguaje llano y estructura atómica:**
   - Escribir en tono cercano, tratando al estudiante de **tú**.
   - Frases cortas y sintaxis directa (sujeto, verbo, complementos).
   - **Un concepto por párrafo:** Si un párrafo introduce dos ideas distintas, divídelo.
   - Introducir los términos técnicos siempre acompañados de una explicación con palabras sencillas.

4. **Conexión profesional permanente:**
   - Cada apartado debe responder a la pregunta tácita del alumno: *«¿Para qué necesito saber esto en mi trabajo?»*.
   - Los ejemplos, ejercicios y recuadros deben recurrir sistemáticamente al equipamiento real, la prevención de riesgos y la práctica laboral.

---

## 2. Objetivos Educativos y Alineación Constructiva

### 2.1. Formulación de objetivos de aprendizaje
Cada tema o módulo debe iniciar con un bloque de objetivos observables bajo el encabezado:
`> **Al terminar este módulo sabrás:**`

- Debe contener entre **3 y 4 objetivos clave**.
- Cada objetivo debe iniciarse obligatoriamente con un **verbo observable y medible** (Taxonomía de Bloom aplicada):
  - *Correctos:* Explicar, distinguir, calcular, identificar, describir, clasificar, relacionar, justificar, interpretar.
  - *Prohibidos como verbo principal:* Conocer, saber, entender, comprender, aprender, familiarizarse (no son observables directamente).
- **Regla de correspondencia evaluativa:** Cada objetivo enunciado debe comprobarse directamente con al menos un ejercicio o caso práctico al final del módulo.

### 2.2. Matriz de trazabilidad curricular
Cuando se adapta un temario oficial a partir de una guía docente o Real Decreto, debe mantenerse una matriz de cobertura que relacione los Resultados de Aprendizaje / Criterios de Evaluación oficiales con los módulos correspondientes. Ningún objetivo oficial puede quedar huérfano.

---

## 3. Estructura Modular y Plantilla Estándar de Contenidos

### 3.1. Granularidad y división modular
Los temas extensos deben subdividirse en **módulos cortos y autocontenidos**, diseñados para sesiones de estudio de 15 a 30 minutos. El orden debe responder a una lógica de dependencia natural:
$$\text{Fundamento elemental / Materia} \longrightarrow \text{Interacciones / Energía} \longrightarrow \text{Mecanismos y leyes} \longrightarrow \text{Efectos y riesgos} \longrightarrow \text{Tecnología y aplicaciones prácticas}$$

### 3.2. Plantilla obligatoria para cada módulo Markdown
Todos los módulos deben construirse siguiendo rigurosamente esta estructura y orden:

```markdown
# Módulo N. Título descriptivo

*Subtítulo breve en cursiva que despierte el interés o plantee el problema*

> **Al terminar este módulo sabrás:**
> - [Verbo observable] ...
> - [Verbo observable] ...
> - [Verbo observable] ...

---

## N.1. Primer apartado temático
(Desarrollo: concepto llano, analogía, figuras, ejemplos)

> **Idea clave:** Síntesis del concepto nuclear del apartado en una sola frase.

## N.2. Segundo apartado temático
...

> **En la práctica profesional:** Conexión con un equipo, procedimiento o protocolo laboral real.

> **Dónde falla la analogía:** Advertencia sobre los límites del modelo mental utilizado.

> **Para ir más allá:** Profundización teórica o formulación matemática opcional (no exigible).

---

## Resumen del módulo
- [Punto clave 1]
- [Punto clave 2]
- [Punto clave 3]
- [Punto clave 4]

## Glosario
| Término | Definición precisa y sencilla |
|---|---|
| **Concepto 1** | Definición en 1-2 frases sin rodeos. |
| **Concepto 2** | Definición en 1-2 frases sin rodeos. |

---

## Ejercicios propuestos
1. [Ejercicio de reconocimiento conceptual / definición]
2. [Ejercicio de cálculo numérico paso a paso con datos limpios]
3. [Ejercicio de cálculo numérico aplicado al sector profesional]
4. [Ejercicio de relación de conceptos o comparación]
5. [Ejercicio de razonamiento o Verdadero/Falso con justificación]

## Soluciones
1. [Solución explicada con justificación conceptual completa]
2. [Solución con planteamiento, fórmula despejada y resultado con unidades]
3. [Solución detallada paso a paso]
4. [Solución comparativa razonada]
5. [Solución con justificación de por qué es V o F]

---

**Siguiente módulo:** [Puente narrativo de 1-2 frases que enlaza la conclusión de este módulo con la necesidad de abrir el siguiente].
```

### 3.3. Sistema de recuadros pedagógicos (Callouts)
Se permite el uso exclusivo de cuatro tipos estandarizados de recuadro mediante bloques de cita Markdown (`>`):

| Recuadro | Rótulo exacto | Propósito pedagógico | Frecuencia recomendada |
|---|---|---|---|
| **Idea clave** | `> **Idea clave:**` | Resume el mensaje central que el estudiante debe retener. | 1 por sección nuclear |
| **Aplicación profesional** | `> **En la práctica profesional:**` (o `> **En el hospital:**`, etc.) | Enlaza la física o teoría con el puesto de trabajo, equipos o seguridad. | 1 a 2 por módulo |
| **Límite de analogía** | `> **Dónde falla la analogía:**` | Aclara dónde termina la validez del ejemplo cotidiano para no fijar conceptos erróneos. | 1 por analogía central |
| **Ampliación optativa** | `> **Para ir más allá:**` | Contiene fórmulas avanzadas, derivaciones o datos que no bloquean la comprensión general. | Solo si aporta valor extra |

---

## 4. Estándares de Redacción, Matemáticas y Notación

### 4.1. Fórmulas matemáticas y notación LaTeX
- **Soporte LaTeX nativo (KaTeX):** El compilador incorpora soporte tipográfico automático mediante KaTeX.
  - **Fórmulas en línea (inline):** Utiliza delimitadores simples `$ ... $` para fórmulas y magnitudes matemáticas dentro del párrafo (p. ej., `$v = \lambda \cdot f$`, `$E = h \cdot \nu$`, `$T = 1 / f$`, `$Z = \rho \cdot v$`).
  - **Ecuaciones en bloque (display):** Utiliza delimitadores dobles `$$ ... $$` en líneas independientes para leyes físicas fundamentales, fracciones complejas o integrales:
    $$N(t) = N_0 \cdot e^{-\lambda t}$$
  - **Compatibilidad y química:** Para moléculas comunes o variables simples en texto corrido, también es válido el uso de Markdown y Unicode directo (`H₂O`, `Z = 12`).
- **Estructura de cálculo en ejemplos resueltos:**
  1. Enunciado con datos numéricos realistas del sector.
  2. Identificación explícita de datos con sus símbolos y unidades.
  3. Fórmula original y despeje de la incógnita.
  4. Sustitución de valores numéricos.
  5. Resultado final destacado en **negrita**, acompañado siempre de sus unidades correspondientes.

### 4.2. Notación numérica y unidades
- **Decimales y millares:** Emplear la **coma decimal** para textos en español (`0,5 mm`, `1,54 m/s`). Los miles se separan con espacio (`20 000 Hz`, no con punto).
- **Notación científica:** Escribir con superíndices estándar: `3 × 10⁸ m/s`, `1,6 × 10⁻¹⁹ C`.
- **Unidades del Sistema Internacional (SI):**
  - Siempre separadas del número por un espacio: `5 MHz`, `70 keV`, `340 m/s`, `15 cm`.
  - Cuando se introduce una unidad no habitual o un múltiplo/submúltiplo, debe aportarse de inmediato una tabla o equivalencia clara (p. ej., $1\text{ Å} = 10^{-10}\text{ m} = 0,1\text{ nm}$).

---

## 5. Estándares para Ilustraciones y Recursos Gráficos (SVG)

La carga visual no es ornamental: es una herramienta cognitiva obligatoria. Todo concepto estructural, evolutivo, cinemático o comparativo debe incorporar su propio diagrama.

### 5.1. Reglas técnicas de los gráficos
- **Formato:** Archivos vectoriales **SVG propios** (prohibido utilizar imágenes de internet con derechos o capturas rasterizadas borrosas).
- **Fondo blanco universal (`#ffffff`):** Imprescindible para garantizar una visualización perfecta tanto en modo oscuro como claro en visores web y evitar manchas en la exportación a PDF para impresión.
- **Tipografía legible:** Familias sans-serif (`Arial, Helvetica, sans-serif`). Tamaño de texto mínimo de **13 px**; títulos y etiquetas principales en **15–16 px en negrita**.
- **Sin solapamientos:** Ninguna línea o flecha puede pasar por encima de un rótulo de texto.
- **Diagramas autoexplicativos:** Los elementos deben estar rotulados directamente sobre el dibujo, sin forzar al lector a descifrar leyendas crípticas externas.
- **Pie de figura y accesibilidad:**
  - Debajo de cada imagen, incluir pie de figura en cursiva:
    `*Figura N. Descripción de lo que muestra el dibujo y qué aspecto clave debe observarse.*`
  - La numeración se reinicia en cada módulo (Figura 1, Figura 2...).
  - Toda etiqueta `![]()` debe incorporar texto alternativo descriptivo.

### 5.2. Código semántico de color
Mantener una paleta funcional y congruente en todo el temario para que el color transmita significado:
- **Azul (`#2563eb`):** Fenómenos ondulatorios, trayectorias, electrones, vectores de propagación.
- **Rojo (`#dc2626`):** Elementos destacados, crestas, núcleos positivos, zonas de calor, impactos.
- **Verde (`#15803d`):** Valles, zonas seguras, densidades reducidas, estados de equilibrio.
- **Naranja (`#ea580c`):** Cotas dimensionales, longitudes de onda, fotones de alta energía.
- **Violeta (`#7c3aed`):** Amplitudes, magnitudes electromagnéticas acopladas.
- **Gris neutro (`#555555` / `#64748b`):** Ejes de coordenadas, líneas de cota, referencias estables.

---

## 6. Organización de Archivos y Sistema de Compilación

### 6.1. Jerarquía de carpetas recomendada
Para proyectos modulares y compilación automatizada a PDF/HTML, la estructura de directorios debe ser estandarizada:

```
workspace/
├── compilar.sh                 # Script bash para compilación directa
├── pdf_compiler/               # Motor de compilación a HTML/PDF
│   ├── compilar_tema.py
│   └── style.css
└── <Disciplina>/
    └── Tema_<N>/
        ├── apuntes_originales.pdf  # Documento fuente de partida
        ├── Tema_<N>_completo.html  # Salida compilada unificada
        ├── 1/
        │   ├── content.md          # Markdown principal del módulo 1
        │   └── figs/               # Recursos vectoriales del módulo
        │       ├── fig1.svg
        │       └── fig2.svg
        ├── 2/
        │   ├── content.md
        │   └── figs/
        └── ...
```

### 6.2. Reglas de portabilidad e incrustación
- Los módulos deben redactarse enlazando a las imágenes en su ruta relativa (`figs/fig1.svg` o `fig1.svg`).
- Los scripts de compilación deben convertir todas las imágenes locales en URIs `data:image/svg+xml;base64,...` para que el HTML y el PDF resultantes sean 100% autocontenidos e independientes del sistema de archivos local.
- Las figuras y sus pies deben envolverse semánticamente (`<figure>` y `<figcaption>`) evitando saltos de página partidos en la maquetación impresa (`page-break-inside: avoid`).

---

## 7. Protocolo de Trabajo para Agentes de Inteligencia Artificial

Cuando se asigne a un agente la creación o adaptación de un temario a partir de un texto en bruto o un PDF desordenado, se debe ejecutar el siguiente flujo de trabajo:

```
[1. Ingesta y Auditoría de la Fuente]
        │
        ▼
[2. Planificación Curricular y Matriz de Objetivos]
        │
        ▼
[3. Redacción Modular Iterativa con Plantilla Oficial]
        │
        ▼
[4. Creación y Validación de Recursos Gráficos SVG]
        │
        ▼
[5. Compilación Editorial y Chequeo de Errores]
        │
        ▼
[6. Informe Técnico de Entrega y Trazabilidad]
```

1. **Ingesta y diagnóstico de la fuente:**
   - Extraer el texto completo del documento base.
   - Analizar el índice oficial, los objetivos curriculares y detectar lagunas teóricas, conceptos desordenados o erratas científicas de partida.
2. **Planificación y secuenciación:**
   - Proponer la secuencia modular con lógica ascendente (primero materia elemental, luego energía, después interacciones y finalmente tecnología).
   - Validar que cada objetivo oficial esté cubierto por un módulo específico.
3. **Redacción estricta módulo a módulo:**
   - No omitir ninguna de las secciones de la plantilla (Objetivos, Desarrollo, Cajas pedagógicas, Resumen, Glosario, Ejercicios con soluciones y Puente).
   - Eliminar cualquier metadato, notas para el autor o artefactos de escaneo/OCR de la fuente original.
4. **Diseño de figuras vectoriales:**
   - Dibujar SVGs limpios para cada concepto que admita representación visual.
   - Validar que el XML sea conforme y no presente textos superpuestos.
5. **Compilación y verificación:**
   - Ejecutar el compilador y revisar que no existan avisos de imágenes no encontradas o errores de sintaxis.
6. **Informe técnico al usuario:**
   - Resumir con exactitud: qué módulos se han creado/revisado, qué conceptos se han añadido que faltaban en el original, qué errores de la fuente se han corregido y qué tareas quedan pendientes.

---

## 8. Lista de Comprobación de Calidad (Checklist Pre-Entrega)

Antes de dar un módulo o tema por finalizado, el redactor o agente debe verificar:

### Contenido y Didáctica
- [ ] Incorpora el bloque inicial «Al terminar este módulo sabrás…» con 3–4 verbos observables.
- [ ] Ningún término o magnitud física se utiliza sin haber sido definido previamente.
- [ ] Todo concepto nuevo cuenta con definición, analogía intuitiva y ejemplo resuelto.
- [ ] Cada analogía relevante especifica sus limitaciones en un bloque «Dónde falla la analogía».
- [ ] Al menos una caja de «En la práctica profesional» conecta el contenido con el puesto de trabajo.
- [ ] Las secciones nucleares contienen su correspondiente «Idea clave».

### Rigor Científico y Notación
- [ ] Se han auditado y corregido las erratas del documento de origen.
- [ ] Todos los cálculos numéricos están comprobados y expresados con unidades correctas.
- [ ] Las cifras empíricas y aproximadas están señaladas con «≈» o «aproximadamente».
- [ ] Las fórmulas están escritas en texto plano accesible/Unicode (sin fórmulas rotas).
- [ ] Números con coma decimal y unidades del SI normalizadas con espacio.

### Formato y Maquetación
- [ ] Respeta con exactitud la plantilla Markdown obligatoria.
- [ ] Numeración jerárquica estricta (N.1, N.2, N.3...).
- [ ] Cuenta con Resumen ejecutivo (4 a 6 puntos) y Glosario en tabla Markdown.
- [ ] Incluye entre 5 y 6 ejercicios propuestos con soluciones detalladas paso a paso.
- [ ] El puente final enlaza de forma verídica y natural con el siguiente módulo.
- [ ] Las referencias cruzadas apuntan a módulos y apartados que existen realmente.

### Gráficos y Compilación
- [ ] Cada concepto abstracto relevante dispone de su figura vectorial SVG en la subcarpeta `figs/`.
- [ ] Todos los SVG tienen fondo blanco, fuentes ≥13 px y cero solapes de texto.
- [ ] Código semántico de colores respetado en todas las figuras.
- [ ] Pie de figura descriptivo en cursiva y texto alternativo presente.
- [ ] La compilación se ejecuta con éxito sin imágenes huérfanas ni fallos de renderizado.

---

## 9. Anexo: Caso Práctico - Temario UF1 «Caracterización de las Radiaciones y las Ondas»

Este anexo recoge la **instanciación específica** de las directrices anteriores para el temario del Ciclo Formativo de Grado Superior en Imagen para el Diagnóstico y Medicina Nuclear / Radioterapia.

### 9.1. Objetivos curriculares oficiales de la unidad formativa

| Código | Objetivo oficial | Módulo asignado |
|---|---|---|
| **a** | Reconocer los diferentes tipos de energía usados en imagen para el diagnóstico y en radioterapia. | Módulos 2, 3 y 5 |
| **b** | Clasificar los materiales según su comportamiento ante un campo magnético. | Módulo 7 |
| **c** | Identificar las características de las radiaciones ionizantes de origen nuclear y no nuclear. | Módulos 3, 5 y 6 |
| **d** | Establecer diferencias entre radiación ionizante electromagnética y radiación de partículas. | Módulos 2, 5 y 6 |
| **e** | Justificar el uso en imagen y terapéutico de las radiaciones ionizantes. | Módulo 9 |
| **f** | Relacionar las características de las radiaciones no ionizantes con la obtención de imágenes diagnósticas. | Módulo 7 |
| **g** | Relacionar el uso de ondas materiales con la obtención de imágenes diagnósticas. | Módulo 4 |
| **h** | Definir las unidades y magnitudes utilizadas en radioterapia e imagen para el diagnóstico. | Módulo 8 |

### 9.2. Estructura y estado de los módulos de la unidad

| Módulo | Título | Estado | Contenido clave |
|---|---|---|---|
| **1** | La estructura de la materia | Redactado | Átomo, modelos (Dalton, Thomson, Rutherford, Bohr), niveles energéticos, Z, A, N, fuerza nuclear fuerte, isótopos e iones. |
| **2** | Métodos de transmisión de energía | Redactado (Pendiente completar glosario/ejercicios) | Prueba del espacio exterior, conducción, convección, ondas mecánicas, ondas electromagnéticas y radiación de partículas. |
| **3** | Clasificación de la radiación según su impacto | Redactado (Pendiente añadir figuras, glosario/ejercicios) | Radiación ionizante y no ionizante, umbrales energéticos (~10 eV), ionización directa (α, β) e indirecta (rayos X, neutrones). |
| **4** | El mundo de las ondas | Redactado (Modelo completo) | Ondas mecánicas transversales y longitudinales, medidas (A, λ, f, T, v), sonido audible, ultrasonidos y principios físicos de la ecografía. |
| **5** | Ondas electromagnéticas y rayos X | Pendiente de redacción | Campos E y B, espectro electromagnético, tubo de rayos X, radiación de frenado (*bremsstrahlung*), radiación característica, dualidad onda-corpúsculo. |
| **6** | Radiación de partículas y desintegración radiactiva | Pendiente de redacción | Radionucleidos, desintegración alfa, beta negativa, beta positiva, captura electrónica, emisión gamma, ley exponencial $N(t) = N_0 e^{-\lambda t}$, periodo de semidesintegración $T_{1/2}$. |
| **7** | Magnetismo y radiación no ionizante en imagen | Pendiente de redacción | Campo magnético $B$, fuerza de Lorentz, susceptibilidad magnética, materiales diamagnéticos, paramagnéticos y ferromagnéticos, dipolos atómicos, espín y base de la Resonancia Magnética (RM). |
| **8** | Magnitudes y unidades radiológicas | Pendiente de redacción | Actividad ($Bq$, $Ci$), energía ($eV$, $keV$), dosis absorbida ($Gy$), dosis equivalente y efectiva ($Sv$). |
| **9** | Aplicaciones en radiodiagnóstico, radioterapia y medicina nuclear | Pendiente de redacción | Equipos de rayos X y TC, medicina nuclear (SPECT con Tc-99m, PET con F-18), radioterapia externa (linac) y braquiterapia. Principios de protección radiológica. |

### 9.3. Terminología técnica normalizada

| Término preferido | Evitar / Matizar | Razón técnica |
|---|---|---|
| **Ondas mecánicas** | «Ondas materiales» | El objetivo curricular oficial cita «ondas materiales», pero en física se denominan ondas mecánicas para no confundirlas con las «ondas de materia» de De Broglie. Se menciona la equivalencia una sola vez. |
| **Ondas de materia** | «Ondas materiales» para De Broglie | Designa la longitud de onda asociada a una partícula ($\lambda = h/p$). |
| **Radiación ionizante** | «Radiación peligrosa» o «dañina» | La ionización es el mecanismo físico objetivo; la peligrosidad depende de la dosis, tasa y justificación clínica. |
| **Radiación de frenado** (*bremsstrahlung*) | «Radiación de choque» | El electrón no choca contra el núcleo, frena y se desvía por atracción culombiana en su campo eléctrico. |
| **Frecuencia ($f$ o $\nu$)** | Variar de símbolo sin avisar | Mantener $f$ como estándar principal en ondas generales y $\nu$ («nu») como referencia secundaria en fórmulas de energía fotónica ($E = h \cdot \nu$). |
| **Actividad ($A$)** | «Radiactividad» como magnitud | La radiactividad es el fenómeno nuclear; la **actividad** es la magnitud cuantitativa medida en becquerelios ($Bq$). |

### 9.4. Registro de erratas y sesgos identificados en el documento fuente (`apuntes_tema_1.pdf`)
Al redactar o revisar módulos que tomen como base este documento, corregir estrictamente los siguientes fallos del original:
1. **Modelo de Thomson:** El original menciona un núcleo en Thomson. Corrección: El modelo de Thomson («pudin de pasas») no posee núcleo; la carga positiva es una masa difusa con electrones incrustados.
2. **Unidad de la masa del protón:** El original escribe $m = 1,673 \times 10^{-27}\text{ C}$ (en culombios). Corrección: La masa se expresa en kilogramos ($\text{kg}$).
3. **Energía de ligadura:** El original omite el convenio de signos. Corrección: La energía de un electrón orbital es negativa (cero = electrón libre); la energía de ionización es su valor absoluto.
4. **Clasificación magnética:** El original afirma que los materiales ferromagnéticos son «en realidad un tipo de paramagnéticos». Corrección: Son una clase magnética independiente con ordenamiento magnético espontáneo por dominios de Weiss.
5. **Comportamiento diamagnético:** El original afirma que «no se ven alterados en presencia de un campo magnético». Corrección: Sí responden al campo magnético, experimentando una repulsión débil.
6. **Mecanismo de la radiación X característica:** El original lo describe como «átomos con exceso de energía en la corteza». Corrección: Requiere el arrancamiento previo de un electrón de una capa interna (p. ej., capa K) por impacto de un electrón incidente veloz; la caída posterior de un electrón de una capa externa llena el hueco emitiendo el fotón característico.
7. **Naturaleza de la radiación de frenado:** Aunque el electrón frena cerca del núcleo, el fenómeno es puramente electromagnético externo y **no de origen nuclear**.
8. **Diferenciación entre rayos X y rayos gamma:** No se distinguen por su energía (sus espectros energéticos se solapan ampliamente), sino por su **origen físico** (los rayos gamma provienen de desexcitaciones nucleares; los rayos X se originan fuera del núcleo).
9. **Límite de radiación ionizante:** No todo el espectro ultravioleta es ionizante; el umbral comienza en el ultravioleta lejano/extremo (~10 eV).
10. **Huygens y el electromagnetismo:** El original atribuye a Huygens la descripción de la luz como «onda electromagnética». Corrección: Huygens postuló una teoría ondulatoria mecánica previa; la teoría electromagnética fue desarrollada por James Clerk Maxwell casi dos siglos después.