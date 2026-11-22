# Taller: Claude Code para investigación en ciencias sociales · CIDE

Kit práctico para aprender a usar **Claude Code** (app de escritorio de Claude o claude.ai) en tareas reales de investigación y docencia. En 60 minutos cada participante termina **un producto útil para su trabajo**.

## Antes del taller (5 minutos)
1. Instala la **app de escritorio de Claude** e inicia sesión. Verifica que aparezca la pestaña **Code**.
2. Descarga este repositorio. Hay tres formas; elige la que te resulte más cómoda:
   - **Sin saber Git:** botón verde **Code → Download ZIP** en esta página y descomprímelo en tus Documentos.
   - **Con Claude Code:** abre la pestaña Code en cualquier carpeta y escribe:
     `Clona el repositorio https://github.com/benjov/taller-claude-code-cide en mis Documentos`
   - **Con Git:** `git clone https://github.com/benjov/taller-claude-code-cide.git`
3. En la app de Claude, pestaña **Code**, abre la carpeta `taller-claude-code-cide`.

> El repositorio pesa ~42 MB porque incluye datos oficiales. **Descárgalo antes de llegar** para no depender del wifi del salón.

## Rutas
Elige la ruta que más se parezca a tu trabajo. Cada una trae `README.md` (qué te llevas), `prompts.md` (qué escribir, por niveles) y `ejemplo-final/` (cómo luce terminado).

| Ruta | Producto | Insumos | Estado |
|---|---|---|---|
| **01 · Web académica** | Tu página web personal con publicaciones filtrables y citas/BibTeX | CV propio o ficticio (PDF/Word) | ✅ lista |
| **02 · Syllabus** | Sitio del curso con fechas reales, lecturas y entregas, más calendario `.ics` para estudiantes | Syllabus y calendario propios o ficticios | ✅ lista |
| **03 · Datos** | Análisis reproducible: cobertura, 3 gráficas, modelo de panel y reporte HTML (Python, R o Stata) | Datos reales del Banco Mundial o tus datos | ✅ lista |
| **04 · Literatura** | Matriz de revisión con citas a página, alertas de lectura crítica y **referencias verificadas en Crossref** | 8 artículos ficticios o tus PDFs | ✅ lista |
| **05 · Cualitativo** | Anonimización, libro de códigos, matriz de codificación con citas verificadas e informe | 6 entrevistas ficticias | ✅ lista |
| **06 · Fuentes auditables** | Notebook que descarga, replica y **valida** la informalidad laboral contra INEGI | Datos reales: ENOE (INEGI), ILOSTAT | ✅ lista |

**Datos propios o del kit:** en todas las rutas puedes trabajar con tus propios materiales o con los del kit. **No subas datos confidenciales** (entrevistas con datos personales, información no pública).

## Ver el ejemplo de la ruta 06 en Colab
[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/benjov/taller-claude-code-cide/blob/main/06-fuentes-auditables/ejemplo-final/informalidad_auditable.ipynb)

## Fuentes y términos de uso
Los datos de `06-fuentes-auditables/datos/` son copias sin modificar de INEGI (libre uso, citando la fuente) y de OIT/ILOSTAT (CC BY 4.0). Detalle, URLs y huellas SHA-256 en [`06-fuentes-auditables/datos/FUENTES.md`](06-fuentes-auditables/datos/FUENTES.md).
