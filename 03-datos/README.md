# Ruta 03 · Datos: un análisis reproducible, de la pregunta al reporte

## ¿Para quién es esta ruta?
Para quien trabaja (o quiere trabajar) con datos cuantitativos y quiere pasar de una pregunta a **gráficas y un reporte que se puedan compartir y replicar**, en Python, R o Stata.

## Qué te llevas al final (≈35 min)
- Un **notebook** (o script de R / do-file de Stata) que obtiene los datos, revisa qué falta, grafica y estima un modelo simple.
- **3 gráficas** listas para presentación, con fuente al pie.
- Un **reporte HTML sin código** para mandar a colegas, y un Excel con los datos y las tablas usadas.

👉 Mira `ejemplo-final/reporte_mexico_al.html` para ver la meta.

## El caso del kit: México en América Latina
**¿Cómo ha evolucionado la violencia en México frente a la región, y se relaciona con la desigualdad o el ingreso?**
Usa datos **reales** del Banco Mundial (17 países, 2000–2023): homicidios, PIB per cápita, Gini y desempleo.

### Dos caminos para los datos
| Camino | Qué haces |
|---|---|
| **A · Descargar de la API** | Le pides a Claude Code que consulte la API pública del Banco Mundial (sin registro) |
| **B · Copia del repositorio** | Usas `datos/wdi_latam.csv` (ver `datos/FUENTES.md`) |

### ¿Tus propios datos?
Puedes traer un CSV o Excel de tu investigación (público o anonimizado) a `03-datos/mi-trabajo/` y usar los mismos prompts con tu pregunta. **No uses datos confidenciales.**

## Python, R o Stata
| Lenguaje | Cómo funciona |
|---|---|
| **Python** | Claude Code escribe y **ejecuta** el notebook; también puedes abrirlo en Colab |
| **R** | Claude Code escribe y ejecuta un script `.R` o un documento Quarto, si tienes R instalado |
| **Stata** | Claude Code escribe el `.do`; lo ejecuta si Stata está instalado y accesible desde la terminal. Si no, lo corres tú |

## Dónde trabajar
Abre en Claude Code la carpeta del repositorio y trabaja en `03-datos/mi-trabajo/`.

## Pasos
Abre `prompts.md` y sigue los niveles en orden.

## La lección de esta ruta
Claude Code programa rápido, pero **la interpretación es tuya**. Al construir el ejemplo, la primera versión del texto final afirmaba algo que las gráficas contradecían. Revisar que cada frase del reporte coincida con los números es parte del método.
