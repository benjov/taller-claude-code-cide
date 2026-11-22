"""Construye el sitio de GitHub Pages del taller (carpeta docs/) a partir de los README.md y prompts.md de cada ruta.

Uso (desde la raíz del repositorio):   python herramientas/construir_sitio.py
Requiere: markdown
Fuente única: si cambias un prompts.md, vuelve a correr este script y haz commit de docs/.
"""
import html
import re
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
REPO = "https://github.com/benjov/taller-claude-code-cide"
ZIP = f"{REPO}/archive/refs/heads/main.zip"
BLOB = f"{REPO}/blob/main"
TREE = f"{REPO}/tree/main"
COLAB = "https://colab.research.google.com/github/benjov/taller-claude-code-cide/blob/main"

AGENDA = [  # (inicio, fin, fase, qué pasa)
    (0, 5, "Bienvenida y demo", "La persona que facilita muestra, en vivo, un CV convertido en página web en 3 minutos."),
    (5, 15, "Primeros pasos", "Todas y todos abren Claude Code, eligen la carpeta del taller, conocen los permisos y eligen ruta."),
    (15, 50, "Trabajo por rutas", "Cada quien avanza por los niveles de su ruta. Ayudantes recorren el salón."),
    (50, 57, "Galería", "3 o 4 voluntarios muestran su producto en pantalla (1–2 minutos cada uno)."),
    (57, 60, "Cierre", "Reglas de oro y cómo seguir usando Claude Code en tu trabajo."),
]

RUTAS = {
 "01-web-academica": dict(num="01", corto="Web académica", icono="🌐",
   producto="Tu página web académica personal (un solo archivo HTML), creada desde tu CV.",
   para="Quien quiere una página propia, bonita y fácil de actualizar.",
   insumos=[("CV ficticio (PDF)", f"{BLOB}/01-web-academica/insumos/cv_ficticio.pdf"),
            ("CV ficticio (Word)", f"{BLOB}/01-web-academica/insumos/cv_ficticio.docx")],
   ejemplo=[("Página de ejemplo (código)", f"{BLOB}/01-web-academica/ejemplo-final/index.html")],
   lenguaje="Ninguno (HTML lo escribe Claude)",
   checks={0: "Un resumen en 5 viñetas con la información del CV. Ningún archivo nuevo todavía.",
           1: "Claude propone secciones, un texto de presentación y 2 estilos… y <b>espera tu visto bueno</b>.",
           2: "Un archivo <code>index.html</code> en <code>mi-sitio/</code> que se abre en tu navegador (o en el panel <b>Browser</b> de la app).",
           3: "Al recargar la página (Cmd+R / Ctrl+R) ves el cambio que pediste.",
           4: "Los filtros funcionan y el botón “Copiar BibTeX” copia algo que puedes pegar.",
           5: "Una tabla con los datos de la página que NO salen del CV. Si sale vacía, pídele que revise otra vez con calma."}),
 "02-syllabus": dict(num="02", corto="Syllabus", icono="📅",
   producto="Sitio del curso con fechas reales, lecturas y entregas, más un calendario .ics para tus estudiantes.",
   para="Quien da clases y cada semestre acomoda fechas a mano.",
   insumos=[("Syllabus ficticio (Word)", f"{BLOB}/02-syllabus/insumos/syllabus_ficticio.docx"),
            ("Calendario académico ficticio (PDF)", f"{BLOB}/02-syllabus/insumos/calendario_academico_IFES_2027.pdf")],
   ejemplo=[("Sitio del curso de ejemplo (código)", f"{BLOB}/02-syllabus/ejemplo-final/index.html"),
            ("Calendario .ics de ejemplo", f"{BLOB}/02-syllabus/ejemplo-final/calendario_POL614.ics")],
   lenguaje="Ninguno",
   checks={0: "Número de sesiones, día y hora de clase, y la lista de entregas.",
           1: "Una tabla con fechas reales. Si algo no cuadra, Claude <b>te lo dice y te da opciones</b> en lugar de decidir solo.",
           2: "Un <code>index.html</code> del curso que resalta la próxima sesión.",
           3: "Un archivo <code>.ics</code>: haz doble clic y debería ofrecerte agregarlo a tu calendario.",
           4: "Una tabla de verificación: días inhábiles, lecturas y DOIs."}),
 "03-datos": dict(num="03", corto="Datos", icono="📊",
   producto="Notebook reproducible con datos del Banco Mundial, 3 gráficas, un modelo simple y un reporte HTML.",
   para="Quien trabaja con datos cuantitativos (Python, R o Stata).",
   insumos=[("Datos del Banco Mundial (CSV)", f"{BLOB}/03-datos/datos/wdi_latam.csv"),
            ("Fuentes y huella del archivo", f"{BLOB}/03-datos/datos/FUENTES.md")],
   ejemplo=[("Notebook de ejemplo", f"{BLOB}/03-datos/ejemplo-final/mexico_en_america_latina.ipynb"),
            ("Abrir el ejemplo en Colab", f"{COLAB}/03-datos/ejemplo-final/mexico_en_america_latina.ipynb")],
   lenguaje="Python (o R / Stata)",
   checks={0: "Claude te dice qué tienes instalado y qué falta, sin instalar nada.",
           1: "Los datos en tu carpeta y un FUENTES.md con URLs y fecha (opción A), o la huella del archivo verificada (opción B).",
           2: "Una tabla de cobertura con el % de años con dato por país e indicador.",
           3: "Tres archivos PNG con fuente al pie y un título que afirma algo.",
           4: "Una tabla de coeficientes y una explicación en lenguaje llano con 3 limitaciones.",
           5: "Una tabla “afirmación – número – ¿coincide?” y un reporte HTML sin código."}),
 "04-literatura": dict(num="04", corto="Literatura", icono="📚",
   producto="Matriz de revisión con citas a página, alertas de lectura crítica y referencias verificadas en Crossref.",
   para="Quien prepara un estado del arte o una propuesta de investigación.",
   insumos=[("8 artículos ficticios (carpeta)", f"{TREE}/04-literatura/articulos")],
   ejemplo=[("Carpeta del ejemplo final", f"{TREE}/04-literatura/ejemplo-final")],
   lenguaje="Ninguno (Python para verificar, lo escribe Claude)",
   checks={0: "Una tabla con los 8 artículos: autores, año, título, revista y DOI.",
           1: "Una propuesta de columnas para la matriz. Ajústala antes de seguir.",
           2: "Un Excel con la matriz y la lista de citas que no pasaron la verificación literal (idealmente ninguna).",
           3: "Una tabla de contradicciones o datos que no cuadran entre resumen y resultados.",
           4: "Un CSV con un veredicto por referencia: existe y coincide / existe con errores / no existe.",
           5: "Un archivo <code>.bib</code> y/o un estado del arte en Word con citas (Autor, año, p. X)."}),
 "05-cualitativo": dict(num="05", corto="Cualitativo", icono="🗣️",
   producto="Anonimización, libro de códigos, matriz de codificación con citas verificadas e informe de hallazgos.",
   para="Quien trabaja con entrevistas, grupos focales o documentos.",
   insumos=[("6 entrevistas ficticias (carpeta)", f"{TREE}/05-cualitativo/insumos/entrevistas"),
            ("Proyecto y guía de entrevista", f"{BLOB}/05-cualitativo/insumos/proyecto_y_guia.docx")],
   ejemplo=[("Carpeta del ejemplo final", f"{TREE}/05-cualitativo/ejemplo-final")],
   lenguaje="Ninguno",
   checks={0: "Una tabla de datos identificables <b>sin copiar el dato original</b>, y la carpeta <code>entrevistas_anon/</code>.",
           1: "Un perfil de una línea por participante y los temas, con “n de 6”.",
           2: "Un libro de códigos con definiciones y criterios de inclusión y exclusión. Revísalo antes de codificar.",
           3: "Un Excel con segmentos literales y el resultado de la verificación automática.",
           4: "Un informe en Word con conteos (n de 6), citas con entrevista y turno, y límites.",
           5: "Una tabla de afirmaciones del informe que no cuadran con los conteos."}),
 "06-fuentes-auditables": dict(num="06", corto="Fuentes auditables", icono="🔎",
   producto="Notebook que obtiene microdatos de INEGI, replica la tasa de informalidad y la valida contra lo publicado.",
   para="Quien usa estadísticas oficiales y quiere que cualquiera pueda replicarlas.",
   insumos=[("Datos de INEGI y OIT (carpeta)", f"{TREE}/06-fuentes-auditables/datos"),
            ("Fuentes y huellas", f"{BLOB}/06-fuentes-auditables/datos/FUENTES.md")],
   ejemplo=[("Notebook de ejemplo", f"{BLOB}/06-fuentes-auditables/ejemplo-final/informalidad_auditable.ipynb"),
            ("Abrir el ejemplo en Colab", f"{COLAB}/06-fuentes-auditables/ejemplo-final/informalidad_auditable.ipynb")],
   lenguaje="Python (Jupyter o Colab)",
   checks={0: "Claude te dice qué tienes instalado y qué falta.",
           1: "El zip de la ENOE en tu carpeta y una bitácora con URL, fecha y huella SHA-256 (que coincide con la del repo).",
           2: "Un notebook que corre de principio a fin, con la TIL1 nacional y una gráfica por entidad.",
           3: "Una tabla “publicado vs. replicado” con su URL de fuente.",
           4: "Un Excel con la bitácora y los resultados, o un anexo metodológico en Word."}),
}

# ------------------------------------------------------------------ plantilla
NAV = [("index.html", "Inicio"), ("antes.html", "Antes del taller"), ("primeros-pasos.html", "Primeros pasos"),
       ("rutas.html", "Elige tu ruta")] + \
      [(f"ruta-{v['num']}.html", f"{v['num']} · {v['corto']}") for v in RUTAS.values()] + \
      [("cierre.html", "Cierre y cómo seguir"), ("reloj.html", "⏱ Reloj de la sesión")]

def pagina(archivo, titulo, cuerpo, subtitulo=""):
    nav = "".join(f'<a href="{a}"{" aria-current=page" if a == archivo else ""}{" class=sub" if a.startswith("ruta-") else ""}>{html.escape(t)}</a>'
                  for a, t in NAV)
    return f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)} · Taller Claude Code · CIDE</title>
<link rel="stylesheet" href="estilos.css"></head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="barra"><a class="marca" href="index.html">Taller <b>Claude Code</b> · CIDE</a>
<button class="menu" aria-expanded="false" aria-controls="nav">☰ Menú</button></header>
<div class="marco">
<nav id="nav" aria-label="Secciones del taller">{nav}<a class="repo" href="{REPO}">Repositorio en GitHub ↗</a></nav>
<main id="contenido"><h1>{html.escape(titulo)}</h1>{f'<p class="subtitulo">{subtitulo}</p>' if subtitulo else ''}
{cuerpo}
</main></div>
<footer>Taller práctico de Claude Code para investigación en ciencias sociales · Materiales en <a href="{REPO}">GitHub</a></footer>
<div class="toast" role="status" aria-live="polite"></div>
<script src="sitio.js"></script></body></html>"""

md = lambda t: markdown.markdown(t, extensions=["extra", "sane_lists"])

def caja(tipo, titulo, contenido):
    return f'<div class="caja {tipo}"><p class="caja-t">{titulo}</p>{contenido}</div>'

# ------------------------------------------------------------------ páginas de rutas
def ruta_html(carpeta, r):
    prompts = (RAIZ / carpeta / "prompts.md").read_text(encoding="utf-8")
    readme = (RAIZ / carpeta / "README.md").read_text(encoding="utf-8")
    partes = prompts.split("\n---\n")
    intro, cuerpo, total = md(partes[0].split("\n", 1)[1]), [], 0
    for parte in partes[1:]:
        m = re.search(r"^## Nivel (\d+) · (.+?)\((\d+) min\)(.*)$", parte, re.M)
        if m:
            n, nombre, mins, extra = int(m[1]), m[2].strip(), int(m[3]), m[4].strip(" .")
            total += mins
            resto = parte[m.end():]
            chk = caja("check", "✅ Deberías ver", f"<p>{r['checks'][n]}</p>") if n in r["checks"] else ""
            cuerpo.append(f"""<section class="nivel" id="nivel-{n}">
<div class="nivel-cab"><label class="hecho"><input type="checkbox" data-clave="{carpeta}-n{n}"> <span>Nivel {n}</span></label>
<h2>{html.escape(nombre)}{(' <small>' + html.escape(extra) + '</small>') if extra else ''}</h2><span class="min">{mins} min</span></div>
{md(resto)}{chk}</section>""")
        else:
            cuerpo.append(f'<section class="extra">{md(parte)}</section>')
    lis = lambda xs: "".join(f'<li><a href="{u}">{html.escape(t)}</a></li>' for t, u in xs)
    resumen = f"""<div class="resumen">
<div><p class="et">Te llevas</p><p>{r['producto']}</p></div>
<div><p class="et">Ideal para</p><p>{r['para']}</p></div>
<div><p class="et">Tiempo</p><p>≈{total} min en {sum(1 for c in cuerpo if 'class="nivel"' in c)} niveles</p></div>
<div><p class="et">Programación</p><p>{r['lenguaje']}</p></div>
</div>
<div class="dos-col">
<div class="tarjeta"><p class="et">📥 Insumos</p><ul>{lis(r['insumos'])}</ul></div>
<div class="tarjeta"><p class="et">🏁 Ejemplo terminado <small>(míralo después de intentarlo)</small></p><ul>{lis(r['ejemplo'])}</ul></div>
</div>
<div class="progreso" data-ruta="{carpeta}"><div class="barra-p"><span></span></div><p></p></div>
{caja('info', 'Antes de empezar', f'<p>En Claude Code, con la carpeta del repositorio abierta, trabajarás en <code>{carpeta}/{"mi-sitio" if r["num"] == "01" else "mi-trabajo"}/</code>. '
     'Copia cada prompt con el botón <b>Copiar</b>, pégalo, <b>lee lo que Claude propone</b> y aprueba. Marca cada nivel al terminarlo.</p>')}
<details class="detalles"><summary>📖 Detalles de la ruta: opciones de insumos, ética y la lección principal</summary>{md(readme.split(chr(10), 1)[1])}</details>
{intro}"""
    return pagina(f"ruta-{r['num']}.html", f"Ruta {r['num']} · {r['corto']}", resumen + "".join(cuerpo),
                  r["icono"] + " " + r["producto"])

# ------------------------------------------------------------------ páginas fijas
def index():
    filas = "".join(f'<li data-ini="{a}" data-fin="{b}"><span class="t">{a:02d}–{b:02d}′</span><div><b>{f}</b><p>{q}</p></div></li>'
                    for a, b, f, q in AGENDA)
    rutas = "".join(f'<a class="ruta-card" href="ruta-{v["num"]}.html"><span class="ico">{v["icono"]}</span>'
                    f'<b>{v["num"]} · {v["corto"]}</b><span>{v["producto"]}</span></a>' for v in RUTAS.values())
    c = f"""
<p class="lead">En 60 minutos vas a usar <b>Claude Code</b> para terminar <b>un producto real</b> para tu trabajo académico:
una página web, el sitio de un curso, un análisis de datos, una revisión de literatura, una codificación cualitativa o
un análisis auditable con datos oficiales.</p>
<div class="pasos3">
<a href="antes.html"><span>1</span><b>Antes del taller</b><small>Instala, descarga el repo y haz la prueba (10 min)</small></a>
<a href="primeros-pasos.html"><span>2</span><b>Primeros pasos</b><small>Abre Claude Code y conoce lo básico</small></a>
<a href="rutas.html"><span>3</span><b>Elige tu ruta</b><small>Y síguela nivel por nivel</small></a>
</div>
<h2>Agenda de la sesión</h2>
<ol class="agenda" id="agenda">{filas}</ol>
<p class="nota">¿Vas a facilitar? Abre el <a href="reloj.html">reloj de la sesión</a> en el proyector.</p>
<h2>Las seis rutas</h2><div class="rutas-grid">{rutas}</div>
<h2>Qué es (y qué no es) Claude Code</h2>
<div class="dos-col">
<div class="tarjeta"><p class="et">Es…</p><ul><li>Un <b>agente</b>: lee tus archivos, escribe archivos nuevos y ejecuta programas en una carpeta de tu computadora (o en la nube).</li>
<li>Un asistente al que le das <b>tareas completas</b> en lenguaje natural: “lee este PDF, haz una tabla, verifícala”.</li>
<li>Algo que <b>te pide permiso</b> antes de editar o ejecutar, según el modo que elijas.</li></ul></div>
<div class="tarjeta"><p class="et">No es…</p><ul><li>Un chat donde copias y pegas: aquí <b>trabaja directamente</b> sobre tus archivos.</li>
<li>Infalible: puede equivocarse o “embellecer”. Por eso <b>cada ruta incluye un nivel de verificación</b>.</li>
<li>Un sustituto de tu criterio académico: <b>tú decides</b> y tú firmas.</li></ul></div></div>
"""
    return pagina("index.html", "Claude Code para investigación en ciencias sociales", c,
                  "Taller práctico · 60 minutos · cada participante sale con un producto terminado")

def antes():
    c = f"""
<p class="lead">Haz esto <b>antes de llegar</b> (10–15 minutos). Si llegas con todo listo, aprovechas los 60 minutos completos.</p>
{caja('aviso', '⚠️ Requisito indispensable', '<p>Claude Code requiere un plan de pago de Claude: <b>Pro, Max, Ultra, Team o Enterprise</b>. <b>El plan gratuito no incluye Claude Code.</b> Si tu institución te dio una cuenta, verifica con ella que incluya Claude Code.</p>')}
<ol class="checklist">
<li><label><input type="checkbox" data-clave="antes-1"> <b>Instala la app de escritorio de Claude</b></label>
<p>Descárgala de <a href="https://claude.com/download">claude.com/download</a> (macOS o Windows) e inicia sesión con tu cuenta.</p></li>
<li><label><input type="checkbox" data-clave="antes-2"> <b>Encuentra la pestaña <span class="ui">Code</span></b></label>
<p>En la app verás la pestaña <span class="ui">Code</span>. Ahí trabajaremos todo el taller (no en el chat normal).</p></li>
<li><label><input type="checkbox" data-clave="antes-3"> <b>Descarga el repositorio del taller</b> (~43 MB, incluye datos)</label>
<p>Elige <b>una</b> forma:</p>
<ul><li><b>Sin saber Git</b> (recomendado): <a class="boton" href="{ZIP}">⬇ Descargar ZIP</a> y descomprímelo en tu carpeta <i>Documentos</i>.</li>
<li><b>Con Claude Code:</b> en la pestaña Code, abre cualquier carpeta y pega:
<pre><code>Clona el repositorio https://github.com/benjov/taller-claude-code-cide en mi carpeta Documentos</code></pre></li>
<li><b>Con Git:</b> <code>git clone {REPO}.git</code></li></ul></li>
<li><label><input type="checkbox" data-clave="antes-4"> <b>Abre la carpeta del taller en Claude Code</b></label>
<p>En la pestaña <span class="ui">Code</span>, debajo del cuadro de texto, está el selector de carpeta. Elige la carpeta
<code>taller-claude-code-cide</code> (o <code>taller-claude-code-cide-main</code> si la descargaste como ZIP).</p></li>
<li><label><input type="checkbox" data-clave="antes-5"> <b>Haz la prueba de humo</b></label>
<p>Pega este prompt y envíalo:</p>
<pre><code>Hola. Lee el README.md de esta carpeta y dime en 3 líneas de qué trata este taller y qué rutas hay.</code></pre>
<p>✅ Si te responde con un resumen del taller y la lista de rutas, <b>estás lista o listo</b>.</p></li>
<li><label><input type="checkbox" data-clave="antes-6"> <b>(Solo rutas 03 y 06) Revisa Python</b></label>
<p>Pega este prompt:</p>
<pre><code>¿Tengo Python 3 instalado con pandas, matplotlib, requests, openpyxl y jupyter? Dímelo sin instalar nada.</code></pre>
<p>Si falta algo, no te preocupes: en el taller se lo pedimos a Claude Code o usamos <b>Google Colab</b> (solo necesitas una cuenta de Google).</p></li>
</ol>
<h2>¿No tienes la app de escritorio?</h2>
<p>Puedes usar <b>Claude Code en la web</b> (<a href="https://claude.ai/code">claude.ai/code</a>). Corre en la nube de Anthropic y trabaja sobre repositorios de GitHub:</p>
<ol><li>Necesitas una cuenta de GitHub y conectarla a Claude cuando te lo pida.</li>
<li>El repositorio del taller es público. Lo más sencillo es hacer un <b>fork</b> (copia en tu cuenta) desde <a href="{REPO}">la página del repo</a> con el botón <span class="ui">Fork</span>, y abrir la sesión sobre tu copia.</li>
<li>Los archivos que cree Claude quedan en la nube; pídele que los guarde en tu fork para verlos y descargarlos desde GitHub.</li></ol>
{caja('info', 'Recomendación', '<p>Para este taller la <b>app de escritorio</b> es más sencilla: trabajas con archivos de tu computadora y ves los resultados al instante.</p>')}
<h2>¿Qué ruta voy a elegir?</h2><p>No hace falta decidir ahora, pero puedes ver las opciones en <a href="rutas.html">Elige tu ruta</a>.</p>
"""
    return pagina("antes.html", "Antes del taller", c, "Lista de verificación: márcala conforme avanzas (se guarda en tu navegador)")

def primeros():
    c = f"""
<p class="lead">Minutos 5 a 15. Todos juntos: lo mínimo para trabajar con seguridad y elegir ruta.</p>
<h2>1. La pantalla de Claude Code (app de escritorio)</h2>
<ul><li>Pestaña <span class="ui">Code</span>: ahí trabajamos.</li>
<li><b>Cuadro de texto</b>: donde escribes o pegas los prompts.</li>
<li>Debajo del cuadro: el <b>selector de carpeta</b> (debe decir <code>taller-claude-code-cide</code>) y el <b>selector de modo de permisos</b>.</li>
<li>Paneles útiles: <span class="ui">Browser</span> (vista previa de páginas web), <span class="ui">Changes</span> (qué archivos cambió Claude) y <span class="ui">Terminal</span>.</li></ul>
<h2>2. Los modos de permisos: quién decide qué</h2>
<table><thead><tr><th>Modo</th><th>Qué hace</th><th>¿Cuándo usarlo hoy?</th></tr></thead><tbody>
<tr><td><span class="ui">Manual</span></td><td>Pide tu permiso antes de editar archivos o ejecutar comandos.</td><td>✅ <b>Recomendado para empezar.</b> Lees y apruebas cada paso.</td></tr>
<tr><td><span class="ui">Accept edits</span></td><td>Edita archivos sin preguntar; sigue pidiendo permiso para ejecutar comandos.</td><td>Cuando ya tengas confianza (por ejemplo, en el nivel 3 de tu ruta).</td></tr>
<tr><td><span class="ui">Plan</span></td><td>Explora y propone un plan sin modificar nada.</td><td>Para pensar antes de actuar.</td></tr>
<tr><td><span class="ui">Auto</span></td><td>Un clasificador revisa las acciones y decide cuáles requieren confirmación.</td><td>No es necesario hoy.</td></tr>
<tr><td><span class="ui">Bypass permissions</span></td><td>No pide permiso para nada.</td><td>❌ <b>No lo uses</b> en el taller.</td></tr></tbody></table>
{caja('aviso', 'Regla de oro número 1', '<p><b>Lee antes de aprobar.</b> Cuando Claude pida permiso para ejecutar algo, revisa qué va a hacer. Si no lo entiendes, pregúntale: <i>“¿Qué hace este comando?”</i></p>')}
<h2>3. Anatomía de un buen prompt</h2>
<p>Todos los prompts del taller siguen esta estructura. Úsala también en tu trabajo:</p>
<div class="anatomia">
<div><b>Contexto</b><span>Qué quiero lograr y para qué.</span></div>
<div><b>Insumos</b><span>Qué archivos leer (con su ruta).</span></div>
<div><b>Tarea</b><span>Qué producir, en qué formato y dónde guardarlo.</span></div>
<div><b>Reglas</b><span>Qué no hacer (“no inventes”, “cita literal”, “espera mi visto bueno”).</span></div>
<div><b>Verificación</b><span>Cómo comprobar que quedó bien.</span></div></div>
<h2>4. Ejercicio común: que Claude te recomiende una ruta (3 min)</h2>
<p>Pega esto en Claude Code:</p>
<pre><code>Lee el README.md de esta carpeta. Hazme 3 preguntas breves sobre mi trabajo académico
(qué investigo, con qué tipo de datos o textos trabajo, qué me quita más tiempo) y,
con mis respuestas, recomiéndame una de las 6 rutas del taller explicándome por qué.</code></pre>
<p>✅ <b>Deberías ver:</b> tres preguntas. Respóndelas en lenguaje natural y Claude te recomendará una ruta.</p>
{caja('info', '¿Por qué empezamos así?', '<p>Porque muestra lo esencial: Claude Code <b>lee archivos de tu carpeta</b>, <b>usa ese contexto</b> y <b>conversa contigo</b> antes de actuar.</p>')}
<h2>5. ¿Tus datos o los del kit?</h2>
<p>En todas las rutas puedes usar tus materiales o los del kit. <b>Para hoy recomendamos los del kit</b>: así no te preocupas por datos sensibles y puedes comparar con el ejemplo terminado. Repite en casa con tus materiales.</p>
<p class="siguiente"><a class="boton" href="rutas.html">Siguiente: elige tu ruta →</a></p>
"""
    return pagina("primeros-pasos.html", "Primeros pasos", c, "Minutos 5–15 · todos juntos")

def rutas():
    filas = "".join(f'<tr><td><a href="ruta-{v["num"]}.html">{v["icono"]} <b>{v["num"]} · {v["corto"]}</b></a></td>'
                    f'<td>{v["para"]}</td><td>{v["producto"]}</td><td>{v["lenguaje"]}</td></tr>' for v in RUTAS.values())
    c = f"""
<p class="lead">Elige la ruta que más se parezca a tu trabajo. Todas duran unos 35 minutos y terminan con un producto.</p>
<h2>¿Qué te describe mejor?</h2>
<div class="elige">
<a href="ruta-01.html"><b>“Quiero que me encuentren en internet”</b><span>→ 01 · Web académica</span></a>
<a href="ruta-02.html"><b>“Cada semestre rehago mi programa a mano”</b><span>→ 02 · Syllabus</span></a>
<a href="ruta-03.html"><b>“Trabajo con bases de datos y quiero gráficas y modelos”</b><span>→ 03 · Datos</span></a>
<a href="ruta-04.html"><b>“Tengo una pila de PDFs por leer”</b><span>→ 04 · Literatura</span></a>
<a href="ruta-05.html"><b>“Hago entrevistas o análisis de textos”</b><span>→ 05 · Cualitativo</span></a>
<a href="ruta-06.html"><b>“Uso estadísticas oficiales y quiero que sean replicables”</b><span>→ 06 · Fuentes auditables</span></a>
</div>
<h2>Comparación</h2>
<div class="tabla-scroll"><table><thead><tr><th>Ruta</th><th>Ideal para</th><th>Te llevas</th><th>Programación</th></tr></thead><tbody>{filas}</tbody></table></div>
{caja('info', '¿Ninguna programa y me da miedo?', '<p>Las rutas 01, 02, 04 y 05 no requieren saber programar. Cuando hace falta código, <b>lo escribe Claude Code</b>; tú decides y verificas.</p>')}
"""
    return pagina("rutas.html", "Elige tu ruta", c, "Minuto 15 · cada quien a su ruta")

def cierre():
    c = """
<p class="lead">Minutos 50 a 60: mostramos lo que hicimos y nos llevamos hábitos para seguir.</p>
<h2>Galería (minutos 50–57)</h2>
<p>3 o 4 voluntarios, de rutas distintas, muestran su producto en 1–2 minutos:</p>
<ol><li><b>Qué construí</b> (muéstralo en pantalla).</li><li><b>Un prompt que funcionó muy bien.</b></li><li><b>Algo que Claude hizo mal y cómo lo detecté.</b></li></ol>
<h2>Las reglas de oro</h2>
<div class="reglas">
<div><b>1. Lee antes de aprobar</b><span>Tú autorizas cada acción.</span></div>
<div><b>2. Contexto completo</b><span>Dale los documentos correctos: no adivina el calendario de tu institución.</span></div>
<div><b>3. Plan primero</b><span>“Propón y espera mi visto bueno” te da el control.</span></div>
<div><b>4. Toda cifra y toda cita, con su fuente</b><span>URL, página, turno o huella del archivo.</span></div>
<div><b>5. Verifica</b><span>Contra el CV, el boletín, Crossref o los conteos. La IA puede embellecer.</span></div>
<div><b>6. Protege los datos</b><span>Anonimiza; respeta el consentimiento y a tu comité de ética.</span></div>
<div><b>7. Declara el uso de IA</b><span>En tus artículos, tesis y cursos.</span></div>
<div><b>8. Tú decides y tú firmas</b><span>El criterio académico es tuyo.</span></div></div>
<h2>Cómo seguir: tu propio CLAUDE.md</h2>
<p><code>CLAUDE.md</code> es un archivo de texto que pones en la carpeta de tu proyecto. Claude Code lo lee al inicio de <b>cada</b> sesión. Es la forma de no repetirle lo mismo cada vez. Pídeselo así:</p>
<pre><code>Crea un CLAUDE.md para este proyecto con: de qué trata, mis fuentes de datos y cómo
las cito, mis reglas de estilo (idioma, formato de citas), lo que NUNCA debes hacer
(inventar datos, modificar los datos originales) y una bitácora de decisiones.</code></pre>
<h2>Ideas para la próxima semana</h2>
<ul><li><b>Docencia:</b> generar ejercicios y rúbricas, revisar la coherencia de un programa, preparar materiales en dos idiomas.</li>
<li><b>Investigación:</b> limpiar bases de datos, documentar paquetes de replicación, verificar las referencias de un manuscrito antes de enviarlo.</li>
<li><b>Gestión:</b> convertir informes en tablas, ordenar carpetas de proyectos, preparar anexos metodológicos.</li></ul>
<h2>Recursos</h2>
<ul><li>Documentación oficial de Claude Code: <a href="https://code.claude.com/docs">code.claude.com/docs</a></li>
<li>Repositorio del taller (todas las rutas y los ejemplos): <a href="https://github.com/benjov/taller-claude-code-cide">github.com/benjov/taller-claude-code-cide</a></li></ul>
"""
    return pagina("cierre.html", "Cierre y cómo seguir", c, "Minutos 50–60")

def reloj():
    fases = "".join(f'<li data-ini="{a}" data-fin="{b}"><b>{f}</b> <span>{a}–{b} min</span><p>{q}</p></li>' for a, b, f, q in AGENDA)
    c = f"""
<div class="reloj" id="reloj">
<div class="reloj-fase"><p class="et">Fase actual</p><p id="fase-nombre">—</p><p id="fase-desc" class="tenue"></p></div>
<div class="reloj-num"><p class="et">Quedan en esta fase</p><p id="fase-resta">--:--</p><p class="tenue">Transcurrido: <span id="total">00:00</span> de 60:00</p></div>
<div class="reloj-barra"><span id="barra-total"></span></div>
<div class="reloj-ctrl"><button id="iniciar" class="boton">▶ Iniciar sesión</button>
<button id="pausar" class="boton sec">⏸ Pausar</button><button id="reiniciar" class="boton sec">↺ Reiniciar</button>
<button id="pantalla" class="boton sec">⛶ Pantalla completa</button></div>
</div>
<ol class="agenda" id="agenda">{fases}</ol>
{caja('info', 'Para quien facilita', '<p>Durante el trabajo por rutas (minutos 15–50), anuncia en voz alta: al minuto <b>30</b> (“deberían ir en el nivel 2”), al <b>40</b> (“pasen al nivel de verificación aunque no hayan terminado los anteriores”) y al <b>47</b> (“guarden y prepárense para la galería”). El reloj sobrevive a recargar la página.</p>')}
"""
    return pagina("reloj.html", "Reloj de la sesión", c, "Para proyectar durante el taller")

CSS = """
:root{--fondo:#fcfcfb;--sup:#ffffff;--texto:#1d232b;--tenue:#5b6573;--acento:#2a78d6;--acento2:#1c5cab;--suave:#e8f0fb;--borde:#e3e6ea;
--ok:#0b7a0b;--ok-f:#eaf6ea;--aviso:#b03a2e;--aviso-f:#fbeceb;--cod:#f3f4f6;--nav:260px}
@media (prefers-color-scheme:dark){:root{--fondo:#1a1a19;--sup:#222220;--texto:#f0efec;--tenue:#c3c2b7;--acento:#5598e7;--acento2:#86b6ef;--suave:#24303d;
--borde:#383835;--ok:#5cc85c;--ok-f:#1f2b1f;--aviso:#e7766b;--aviso-f:#2e2120;--cod:#2a2a28}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--fondo);color:var(--texto)}
a{color:var(--acento)}.saltar{position:absolute;left:-999px}.saltar:focus{left:8px;top:8px;background:var(--sup);padding:6px 10px;z-index:9}
.barra{position:sticky;top:0;z-index:5;display:flex;justify-content:space-between;align-items:center;padding:10px 20px;background:var(--sup);border-bottom:1px solid var(--borde)}
.marca{text-decoration:none;color:var(--texto);font-size:16px}.marca b{color:var(--acento)}
.menu{display:none;font:inherit;background:none;border:1px solid var(--borde);border-radius:8px;padding:4px 10px;color:var(--texto)}
.marco{display:grid;grid-template-columns:var(--nav) 1fr;max-width:1240px;margin:0 auto}
nav{position:sticky;top:53px;align-self:start;height:calc(100vh - 53px);overflow:auto;padding:20px 12px;border-right:1px solid var(--borde)}
nav a{display:block;padding:6px 10px;border-radius:8px;text-decoration:none;color:var(--tenue);font-size:15px}
nav a.sub{padding-left:22px;font-size:14px}nav a:hover{background:var(--suave);color:var(--texto)}
nav a[aria-current=page]{background:var(--suave);color:var(--acento);font-weight:600}nav .repo{margin-top:14px;border-top:1px solid var(--borde);padding-top:12px}
main{padding:28px 40px 80px;min-width:0;max-width:900px}
h1{font-size:clamp(28px,4vw,40px);line-height:1.15;margin:0 0 6px}.subtitulo{color:var(--tenue);margin:0 0 22px;font-size:18px}
h2{font-size:24px;margin:38px 0 12px;line-height:1.25}h3{font-size:19px;margin:24px 0 8px}
.lead{font-size:19px}.tenue{color:var(--tenue)}.nota{color:var(--tenue);font-size:15px}
code{background:var(--cod);padding:1px 6px;border-radius:5px;font-size:.9em}
pre{position:relative;background:var(--cod);border:1px solid var(--borde);border-radius:10px;padding:16px 16px 16px 16px;overflow:auto;white-space:pre-wrap;font-size:15px;line-height:1.55}
pre code{background:none;padding:0}
.copiar{position:absolute;top:8px;right:8px;font:600 13px system-ui;background:var(--acento);color:#fff;border:0;border-radius:6px;padding:5px 12px;cursor:pointer}
.copiar.ok{background:var(--ok)}pre:has(.copiar){padding-top:40px}
table{width:100%;border-collapse:collapse;font-size:15.5px;margin:10px 0}th{text-align:left;color:var(--tenue);font-weight:600;border-bottom:2px solid var(--borde);padding:8px}
td{border-bottom:1px solid var(--borde);padding:9px 8px;vertical-align:top}.tabla-scroll{overflow-x:auto}
.ui{display:inline-block;border:1px solid var(--borde);background:var(--sup);border-radius:6px;padding:0 7px;font-size:.92em;font-weight:600}
.boton{display:inline-block;background:var(--acento);color:#fff;border:0;border-radius:8px;padding:8px 16px;font:600 15px system-ui;text-decoration:none;cursor:pointer}
.boton.sec{background:var(--sup);color:var(--texto);border:1px solid var(--borde)}.siguiente{margin-top:30px}
.caja{border-radius:10px;padding:12px 18px;margin:18px 0;border-left:4px solid var(--acento);background:var(--suave)}
.caja p{margin:6px 0}.caja-t{font-weight:700}.caja.check{border-color:var(--ok);background:var(--ok-f)}.caja.aviso{border-color:var(--aviso);background:var(--aviso-f)}
.pasos3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:22px 0}
.pasos3 a{display:flex;flex-direction:column;gap:2px;padding:16px;border:1px solid var(--borde);border-radius:12px;background:var(--sup);text-decoration:none;color:var(--texto)}
.pasos3 a:hover{border-color:var(--acento)}.pasos3 span{font-weight:800;color:var(--acento);font-size:22px}.pasos3 small{color:var(--tenue)}
.agenda{list-style:none;padding:0;margin:0}.agenda li{display:grid;grid-template-columns:90px 1fr;gap:14px;padding:12px;border-bottom:1px solid var(--borde);border-radius:8px}
.agenda .t{font-weight:700;color:var(--acento);font-variant-numeric:tabular-nums}.agenda p{margin:2px 0 0;color:var(--tenue);font-size:15.5px}
.agenda li.actual{background:var(--suave);outline:2px solid var(--acento)}.agenda li.pasada{opacity:.5}
.rutas-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px}
.ruta-card{display:flex;flex-direction:column;gap:4px;padding:16px;border:1px solid var(--borde);border-radius:12px;background:var(--sup);text-decoration:none;color:var(--texto)}
.ruta-card:hover{border-color:var(--acento)}.ruta-card span:last-child{color:var(--tenue);font-size:15px}.ico{font-size:26px}
.dos-col{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0}.tarjeta{border:1px solid var(--borde);border-radius:12px;padding:12px 18px;background:var(--sup)}
.tarjeta ul{margin:6px 0;padding-left:20px}.et{font-size:13px;text-transform:uppercase;letter-spacing:.6px;color:var(--tenue);font-weight:700;margin:4px 0}
.resumen{display:grid;grid-template-columns:2fr 1.4fr 1fr 1.2fr;gap:14px;padding:16px;border:1px solid var(--borde);border-radius:12px;background:var(--sup)}
.resumen p{margin:2px 0}
.progreso{margin:18px 0}.barra-p{height:10px;background:var(--borde);border-radius:999px;overflow:hidden}.barra-p span{display:block;height:100%;width:0;background:var(--ok);transition:width .3s}
.progreso p{margin:6px 0;color:var(--tenue);font-size:15px}
.detalles{border:1px solid var(--borde);border-radius:10px;padding:10px 16px;margin:14px 0;background:var(--sup)}.detalles summary{cursor:pointer;font-weight:600}
.nivel{border:1px solid var(--borde);border-radius:14px;padding:6px 22px 10px;margin:22px 0;background:var(--sup);scroll-margin-top:70px}
.nivel.hecho-ok{border-color:var(--ok)}.nivel-cab{display:flex;align-items:center;gap:14px;flex-wrap:wrap;border-bottom:1px solid var(--borde);padding:10px 0;margin-bottom:6px}
.nivel-cab h2{margin:0;font-size:21px;flex:1}.nivel-cab h2 small{font-weight:500;color:var(--tenue);font-size:15px}
.min{font-weight:700;color:var(--acento);white-space:nowrap}.hecho{display:flex;align-items:center;gap:6px;font-weight:700;color:var(--tenue);font-size:14px;cursor:pointer}
.hecho input,.checklist input{width:20px;height:20px;accent-color:var(--ok)}
.extra{margin:26px 0}.checklist{padding-left:22px}.checklist>li{margin-bottom:18px}.checklist label{cursor:pointer}
.anatomia,.reglas{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px}.reglas{grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}
.anatomia div,.reglas div{border:1px solid var(--borde);border-radius:10px;padding:12px;background:var(--sup);display:flex;flex-direction:column}
.anatomia span,.reglas span{color:var(--tenue);font-size:15px}
.elige{display:grid;grid-template-columns:1fr 1fr;gap:10px}.elige a{padding:14px 16px;border:1px solid var(--borde);border-radius:12px;background:var(--sup);text-decoration:none;color:var(--texto);display:flex;flex-direction:column}
.elige a:hover{border-color:var(--acento)}.elige span{color:var(--acento);font-weight:600}
.reloj{border:1px solid var(--borde);border-radius:16px;background:var(--sup);padding:24px;display:grid;grid-template-columns:1.3fr 1fr;gap:20px}
#fase-nombre{font-size:clamp(30px,5vw,54px);font-weight:800;margin:0;line-height:1.1}#fase-resta{font-size:clamp(48px,9vw,110px);font-weight:800;margin:0;font-variant-numeric:tabular-nums;color:var(--acento);line-height:1}
.reloj-barra{grid-column:1/-1;height:14px;background:var(--borde);border-radius:999px;overflow:hidden}.reloj-barra span{display:block;height:100%;width:0;background:var(--acento)}
.reloj-ctrl{grid-column:1/-1;display:flex;gap:8px;flex-wrap:wrap}.reloj:fullscreen{padding:6vw;align-content:center}
footer{text-align:center;color:var(--tenue);font-size:14px;padding:24px;border-top:1px solid var(--borde)}
.toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--texto);color:var(--fondo);padding:8px 16px;border-radius:8px;opacity:0;transition:.2s;pointer-events:none}
.toast.ver{opacity:1}
@media (max-width:900px){.marco{grid-template-columns:1fr}nav{display:none;position:static;height:auto;border-right:0;border-bottom:1px solid var(--borde)}
nav.abierto{display:block}.menu{display:block}main{padding:20px 18px 60px}.pasos3,.dos-col,.elige,.reloj{grid-template-columns:1fr}.resumen{grid-template-columns:1fr 1fr}}
@media print{.barra,nav,.copiar,.reloj-ctrl,footer{display:none}.marco{display:block}}
"""

JS = """
// Menú en celular
const btn = document.querySelector('.menu'), nav = document.getElementById('nav');
btn?.addEventListener('click', () => { nav.classList.toggle('abierto'); btn.setAttribute('aria-expanded', nav.classList.contains('abierto')); });
const toast = m => { const t = document.querySelector('.toast'); t.textContent = m; t.classList.add('ver'); setTimeout(() => t.classList.remove('ver'), 1500); };

// Botón "Copiar" en cada bloque de código
document.querySelectorAll('main pre').forEach(pre => {
  const b = document.createElement('button'); b.className = 'copiar'; b.type = 'button'; b.textContent = 'Copiar';
  b.addEventListener('click', async () => {
    const texto = pre.querySelector('code')?.innerText ?? pre.innerText;
    try { await navigator.clipboard.writeText(texto.replace(/\\n$/, '')); b.textContent = '¡Copiado!'; b.classList.add('ok'); toast('Prompt copiado: pégalo en Claude Code'); }
    catch { b.textContent = 'Selecciona y copia'; }
    setTimeout(() => { b.textContent = 'Copiar'; b.classList.remove('ok'); }, 1800);
  });
  pre.appendChild(b);
});

// Casillas que se recuerdan (localStorage) y progreso por ruta
const casillas = document.querySelectorAll('input[data-clave]');
casillas.forEach(c => {
  c.checked = localStorage.getItem('taller:' + c.dataset.clave) === '1';
  c.addEventListener('change', () => { localStorage.setItem('taller:' + c.dataset.clave, c.checked ? '1' : '0'); progreso(); });
});
function progreso() {
  document.querySelectorAll('.nivel').forEach(n => n.classList.toggle('hecho-ok', !!n.querySelector('input:checked')));
  const p = document.querySelector('.progreso'); if (!p) return;
  const cs = document.querySelectorAll('.nivel input[data-clave]'), hechos = [...cs].filter(c => c.checked).length;
  p.querySelector('span').style.width = (100 * hechos / cs.length) + '%';
  p.querySelector('p').textContent = hechos === cs.length ? '🎉 ¡Ruta completa! Prepárate para la galería.' : `Llevas ${hechos} de ${cs.length} niveles.`;
}
progreso();

// Agenda y reloj de la sesión (sobrevive a recargar la página)
const agenda = document.getElementById('agenda'), DUR = 60 * 60 * 1000, K = 'taller:reloj';
const est = () => JSON.parse(localStorage.getItem(K) || '{"inicio":null,"pausa":null}');
const guarda = e => localStorage.setItem(K, JSON.stringify(e));
const mmss = ms => { const s = Math.max(0, Math.round(ms / 1000)); return String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'); };
function tick() {
  const e = est(); const trans = e.inicio ? ((e.pausa ?? Date.now()) - e.inicio) : 0; const min = trans / 60000;
  agenda?.querySelectorAll('li').forEach(li => {
    const a = +li.dataset.ini, b = +li.dataset.fin;
    li.classList.toggle('actual', !!e.inicio && min >= a && min < b); li.classList.toggle('pasada', !!e.inicio && min >= b);
  });
  if (!document.getElementById('reloj')) return;
  const li = [...agenda.querySelectorAll('li')].find(l => min >= +l.dataset.ini && min < +l.dataset.fin);
  document.getElementById('fase-nombre').textContent = !e.inicio ? 'Lista para empezar' : (li ? li.querySelector('b').textContent : 'Sesión terminada');
  document.getElementById('fase-desc').textContent = li && e.inicio ? li.querySelector('p').textContent : '';
  document.getElementById('fase-resta').textContent = li && e.inicio ? mmss(+li.dataset.fin * 60000 - trans) : '--:--';
  document.getElementById('total').textContent = mmss(Math.min(trans, DUR));
  document.getElementById('barra-total').style.width = Math.min(100, 100 * trans / DUR) + '%';
  document.getElementById('pausar').textContent = e.pausa ? '▶ Reanudar' : '⏸ Pausar';
}
document.getElementById('iniciar')?.addEventListener('click', () => { const e = est(); if (!e.inicio) guarda({ inicio: Date.now(), pausa: null }); tick(); });
document.getElementById('pausar')?.addEventListener('click', () => { const e = est(); if (!e.inicio) return;
  if (e.pausa) guarda({ inicio: e.inicio + (Date.now() - e.pausa), pausa: null }); else guarda({ inicio: e.inicio, pausa: Date.now() }); tick(); });
document.getElementById('reiniciar')?.addEventListener('click', () => { guarda({ inicio: null, pausa: null }); tick(); });
document.getElementById('pantalla')?.addEventListener('click', () => document.getElementById('reloj').requestFullscreen?.());
tick(); setInterval(tick, 1000);
"""

if __name__ == "__main__":
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("")
    (DOCS / "estilos.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (DOCS / "sitio.js").write_text(JS.strip() + "\n", encoding="utf-8")
    paginas = {"index.html": index(), "antes.html": antes(), "primeros-pasos.html": primeros(),
               "rutas.html": rutas(), "cierre.html": cierre(), "reloj.html": reloj()}
    for carpeta, r in RUTAS.items():
        paginas[f"ruta-{r['num']}.html"] = ruta_html(carpeta, r)
    for nombre, contenido in paginas.items():
        (DOCS / nombre).write_text(contenido, encoding="utf-8")
    print("Sitio generado en docs/:", ", ".join(sorted(paginas)))
