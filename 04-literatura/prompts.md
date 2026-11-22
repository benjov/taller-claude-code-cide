# Prompts · Ruta 04 · Literatura

Copia y pega cada prompt en Claude Code (pestaña **Code**, con la carpeta del repositorio abierta).
Si usas tus propios PDFs, cambia `04-literatura/articulos/` por `04-literatura/mi-trabajo/` y ajusta la pregunta.

---

## Nivel 0 · Inventario (3 min)
```
Crea la carpeta 04-literatura/mi-trabajo/ y trabaja ahí.
Haz un inventario de los PDFs de 04-literatura/articulos/: autor(es), año, título,
revista y DOI, en una tabla. Todavía no analices el contenido.
```
💡 *Qué aprendes:* Claude Code lee varios PDFs de una vez y extrae sus metadatos.

---

## Nivel 1 · Diseñar la matriz (4 min)
```
Mi pregunta de revisión es: ¿qué sabemos sobre los efectos de la transparencia
en la corrupción y el desempeño de los gobiernos locales?

Propón las columnas de una matriz de revisión de literatura para esta pregunta.
Deben incluir, al menos: pregunta del estudio, datos, método, tipo de evidencia
(experimental, cuasi-experimental, observacional, cualitativo, síntesis),
hallazgo principal, cita textual que lo respalde, página y limitaciones.
Espera mi visto bueno antes de llenarla.
```
💡 *Qué aprendes:* **tú** decides qué te importa de cada artículo; la IA solo lo aplica.

---

## Nivel 2 · Llenar la matriz (10 min)
```
Llena la matriz en un Excel (mi-trabajo/matriz_literatura.xlsx) con estas reglas:
1. La "cita textual" debe ser copia LITERAL de una frase del artículo, con su página.
2. Si un dato no aparece en el artículo, escribe "No reportado". No lo deduzcas.
3. En "limitaciones", distingue las que declaran los autores de las que observes tú.
Al terminar, comprueba que cada cita textual aparezca palabra por palabra en su PDF
y dime cuáles no pasaron la prueba.
```
💡 *Qué aprendes:* con reglas claras la IA es mucho más confiable, y **le pides que se autoverifique**.

---

## Nivel 3 · Lectura crítica (6 min)
```
Para cada artículo, compara lo que dice el RESUMEN con lo que muestran las secciones
de datos, de resultados y las tablas. Haz una tabla con toda contradicción o dato que no
cuadre (cifras, número de casos o países, significancia estadística, periodos).
Agrega una columna "alertas" a la matriz con lo que encuentres.
```
💡 *Qué aprendes:* los resúmenes a veces exageran. Una buena revisión cita **la tabla, no el resumen**.

---

## Nivel 4 · Verificar las referencias (7 min)
```
Extrae todas las referencias que citan los artículos (sección "Referencias").
Escribe un script en Python que consulte cada DOI en la API pública de Crossref
(https://api.crossref.org/works/DOI) y compare autor, año y título con la cita.
Clasifica cada referencia como: existe y coincide / existe pero con errores /
no existe. Ejecútalo y guarda el resultado en mi-trabajo/verificacion_referencias.csv.
```
💡 *Qué aprendes:* una referencia puede **verse perfecta y no existir**. Esto aplica a artículos publicados, a tesis de estudiantes… y a lo que escribe una IA.

---

## Nivel 5 · Elige tu salida (5 min)
**Para tu gestor de referencias (Zotero, Mendeley, LaTeX):**
```
Genera mi-trabajo/referencias.bib con los artículos de la matriz. Cuidado con los
apellidos compuestos en español: deben ir como "Apellido1 Apellido2, Nombre".
```
**Para escribir:**
```
Redacta un estado del arte de una página en Word (mi-trabajo/estado_del_arte.docx),
organizado por temas, no por artículo. Usa SOLO información de la matriz, cita como
(Autor, año, p. X) y agrega al final una sección "Notas de verificación" con las alertas.
```

---

## Retos para quien termine antes
```
Audita el estado del arte: para cada oración con una cita, muéstrame la cita textual
de la matriz que la respalda. Marca las oraciones que no tengan respaldo.
```
```
Repite el nivel 4 con una lista de referencias de un artículo o tesis mío: [ruta del archivo].
```
```
Escribe un CLAUDE.md en mi-trabajo/ con mis reglas de revisión de literatura (columnas,
formato de citas, cómo tratar los datos no reportados) para reutilizarlas en mi próximo proyecto.
```

---

## Reglas de oro
1. **Sin página no hay cita.** Si no puedes ubicarla en el PDF, no la uses.
2. **"No reportado" es una respuesta válida.** Es mejor que un dato deducido.
3. **Verifica las referencias antes de que lleguen a tu bibliografía.**
