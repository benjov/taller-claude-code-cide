# Ruta 06 · Fuentes auditables: informalidad laboral en México

## ¿Para quién es esta ruta?
Para quien trabaja con **estadísticas oficiales** y quiere que cualquier colega, dictaminador o estudiante pueda **saber de dónde salió cada cifra, verificarla y replicarla**.

## Qué te llevas al final (≈35 min)
Un **notebook de Jupyter** (o Colab) construido por Claude Code que:

1. **Descarga** los microdatos oficiales de la ENOE (INEGI) directamente de la fuente.
2. Registra cada descarga en una **bitácora de fuentes**: URL, institución, fecha de consulta y huella digital (SHA-256) del archivo.
3. **Calcula** la Tasa de Informalidad Laboral (TIL1) nacional y por entidad.
4. **Valida** tu cálculo contra las cifras publicadas por INEGI en sus boletines.
5. **Verifica** que los enlaces sigan funcionando.
6. Exporta todo a **Excel** (y, si quieres, un **anexo metodológico en Word**).

👉 Mira `ejemplo-final/` para ver cómo luce el producto terminado. **Cuidado: es la meta, no el punto de partida.** La gracia es que tú le pidas a Claude Code que lo construya.

## Datos reales, no sintéticos
Esta ruta trabaja con **datos públicos reales**:

| Fuente | Qué es | Tamaño |
|---|---|---|
| INEGI · ENOE 2T-2026, datos abiertos | Microdatos de la encuesta de empleo | ~41 MB (zip) |
| INEGI · Boletines de prensa ENOE (25-ago-2026) | Cifras oficiales publicadas para validar | PDF |
| OIT · ILOSTAT | Serie anual de empleo informal, México | CSV pequeño |

### Dos caminos: tú decides
| Camino | Qué haces | Cuándo elegirlo |
|---|---|---|
| **A · Descarga desde la fuente** | Le pides a Claude Code que encuentre y descargue los datos del sitio de INEGI | Quieres ver a Claude Code buscar, descargar y documentar como lo haría un asistente de investigación |
| **B · Datos del repositorio** | Usas las copias que ya vienen en `datos/` (ver `datos/FUENTES.md`) | La red está lenta o prefieres dedicar el tiempo al análisis |

En **ambos caminos** la bitácora registra la URL original y la huella SHA-256. Si eliges el A, puedes comprobar que tu descarga es **idéntica** a la copia del repositorio. Eso también es auditar.

## Elige tu formato de salida
| Si trabajas en… | Pide… |
|---|---|
| Python / Jupyter en tu computadora | Un notebook `.ipynb` que Claude Code ejecute y pruebe |
| Google Colab | Un notebook `.ipynb` que luego **subes a Colab** (Claude Code no corre dentro de Colab) |
| Excel | Un libro con hojas: bitácora, resultados, validación y estado de enlaces |
| Word | Un "anexo metodológico de fuentes" listo para pegar en un artículo o reporte |

Los tres formatos salen del mismo notebook; el notebook es lo que permite **replicar**.

## ¿Quieres usar tu propio tema?
Puedes cambiar "informalidad" por otra estadística (pobreza CONEVAL, homicidios SESNSP, presupuesto SHCP, resultados electorales INE…). Usa los mismos prompts cambiando el tema. Advertencia: cada fuente tiene sus propias trampas (formatos, tokens, codificación), y eso también es aprendizaje.

## Pasos
Abre `prompts.md` y sigue los niveles en orden. Cada nivel produce algo que funciona.

## Dónde trabajar
Abre en Claude Code la carpeta del repositorio y trabaja en una subcarpeta nueva: `06-fuentes-auditables/mi-trabajo/`. Desde ahí los datos del repo están en `../datos/`.

## Requisitos técnicos
- App de escritorio de Claude con Claude Code (pestaña **Code**) y el repositorio del taller descargado (ver el `README.md` principal).
- Para ejecutar localmente: Python 3 con `pandas`, `requests`, `matplotlib`, `openpyxl` y `jupyter` (ver `ejemplo-final/requirements.txt`). Si falta algo, **pídele a Claude Code que lo instale**.
- Ruta Colab: solo necesitas una cuenta de Google.
