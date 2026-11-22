# Prompts · Ruta 03 · Datos

Copia y pega cada prompt en Claude Code (pestaña **Code**, con la carpeta del repositorio abierta).
Si prefieres **R** o **Stata**, cambia "notebook de Python" por "script de R" o "do-file de Stata".

---

## Nivel 0 · Preparar el terreno (2 min)
```
Crea la carpeta 03-datos/mi-trabajo/ y trabaja ahí.
Revisa si tengo Python con pandas, matplotlib, statsmodels y jupyter
(o R, o Stata, según el lenguaje que elija). Dime qué falta; no instales nada todavía.
```

---

## Nivel 1 · Conseguir los datos (6 min). Elige A o B
### Opción A · API del Banco Mundial
```
Quiero comparar a México con América Latina en violencia, desigualdad e ingreso.
Usa la API pública del Banco Mundial (WDI) para descargar, de 2000 a 2023 y para
los 17 países latinoamericanos principales, estos indicadores:
homicidios por 100,000 habitantes, PIB per cápita PPA, índice de Gini y desempleo.
Si la API falla, reintenta. Guarda los datos en mi-trabajo/datos/ y anota en un
archivo FUENTES.md las URLs consultadas y la fecha.
```
### Opción B · Copia del repositorio
```
Quiero comparar a México con América Latina en violencia, desigualdad e ingreso.
Usa los datos de 03-datos/datos/wdi_latam.csv. Lee primero 03-datos/datos/FUENTES.md
y verifica la huella SHA-256 del archivo. Explícame su estructura.
```
💡 *Qué aprendes:* Claude Code sabe usar **APIs públicas** (Banco Mundial, INEGI, OCDE) y documentar de dónde salió cada dato.

---

## Nivel 2 · ¿Qué falta? (5 min)
```
Antes de graficar, crea un notebook de Python en mi-trabajo/ y haz una tabla de
cobertura: qué porcentaje de años tiene dato cada país en cada indicador.
Dime qué países o indicadores tienen huecos que podrían sesgar los promedios.
```
💡 *Qué aprendes:* revisar los datos faltantes **antes** de graficar evita conclusiones falsas.

---

## Nivel 3 · Gráficas que cuentan algo (10 min)
```
Agrega al notebook tres gráficas:
1. La tasa de homicidios de México frente a la mediana del resto de los países
   (los demás países en gris de fondo).
2. Homicidios en el último año disponible, país por país, con México resaltado.
3. Dispersión del Gini contra los homicidios (promedios 2015–2023), con la correlación
   de Spearman en el título.
Usa pocos colores (México en un solo color fuerte), títulos que digan el hallazgo,
y la fuente al pie de cada gráfica. Guárdalas como PNG.
```
Pide ajustes en lenguaje natural: *"la etiqueta del eje se corta"*, *"pon los nombres en español"*, *"quita la cuadrícula vertical"*.

💡 *Qué aprendes:* un **título que afirma algo** se lee mejor que un título descriptivo. Pero entonces el título tiene que ser cierto.

---

## Nivel 4 · Un modelo y sus límites (6 min)
```
Estima un modelo de panel con efectos fijos de país y de año: homicidios en función
de log(PIB per cápita), Gini y desempleo, con errores estándar agrupados por país.
Explícame el resultado en lenguaje llano y dime sus tres principales limitaciones.
```
💡 *Qué aprendes:* Claude Code puede estimar el modelo, pero **la discusión de identificación** te toca a ti.

---

## Nivel 5 · Revisar y compartir (6 min)
```
Escribe una sección final "Lectura y límites" con 4 viñetas. Después, verifica cada
afirmación contra los números calculados en el notebook y muéstrame una tabla:
afirmación, número que la respalda, ¿coincide?
Al final, exporta un reporte HTML sin código para compartir.
```
💡 *Qué aprendes:* **audita el texto contra los números.** Al preparar el ejemplo, esta revisión encontró una afirmación sobre El Salvador que los datos contradecían.

---

## Retos para quien termine antes
```
Contrasta la serie de homicidios de México del Banco Mundial con la de INEGI
(defunciones por homicidio). ¿Coinciden? ¿Por qué podrían diferir?
```
```
Traduce todo el análisis a un script de R con ggplot2 (o a un do-file de Stata).
```
```
Convierte las tres gráficas en una sola figura de paneles, lista para un artículo.
```

---

## Reglas de oro
1. **Mira los datos faltantes antes que las gráficas.**
2. **Un título que afirma, tiene que ser verdad.** Verifícalo.
3. **Correlación no es causalidad**, y un modelo con 17 países es exploratorio.
