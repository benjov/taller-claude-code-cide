# Prompts · Ruta 02 · Syllabus

Copia y pega cada prompt en Claude Code (pestaña **Code**, con la carpeta del repositorio abierta).
Si usas tus archivos, cambia las rutas de `insumos/` por las de `mi-trabajo/`.

---

## Nivel 0 · Leer el syllabus (3 min)
```
Crea la carpeta 02-syllabus/mi-trabajo/ y trabaja ahí.
Lee 02-syllabus/insumos/syllabus_ficticio.docx y dime: cuántas sesiones tiene,
qué día y a qué hora se imparte, qué entregas hay y en qué semanas.
```

---

## Nivel 1 · Ponerle fechas (8 min)
```
Lee también 02-syllabus/insumos/calendario_academico_IFES_2027.pdf.
Asigna una fecha real a cada sesión del syllabus respetando el día de clase y los
días inhábiles del calendario. Muéstrame una tabla: sesión, fecha, tema, entrega.
Si algo no cuadra (por ejemplo, si no caben todas las sesiones), NO lo resuelvas
solo: dime el problema y propónme 2 o 3 opciones.
```
💡 *Qué aprendes:* Claude Code cruza documentos. Fíjate si detecta **todos** los días inhábiles (hay uno que solo aparece en el calendario institucional) y qué pasa con el total de sesiones.

Cuando te dé opciones, **decide tú**:
```
Elijo la opción [N]. Aplica el cambio.
```

---

## Nivel 2 · El sitio del curso (10 min)
```
Construye mi-trabajo/index.html: un sitio del curso de una sola página, autocontenido,
que se vea bien en celular y tenga modo oscuro. Secciones: descripción y objetivos,
calendario (con fechas, lecturas y entregas), evaluación, política de uso de IA,
contacto y bibliografía. Que resalte automáticamente la próxima sesión según la fecha
de hoy. Ábrelo en mi navegador.
```

---

## Nivel 3 · Calendario para los estudiantes (5 min)
```
Genera mi-trabajo/calendario_curso.ics con todas las sesiones (con hora de inicio y
fin, en hora de la Ciudad de México) y la entrega final. Pon en la descripción de cada
evento las lecturas. Agrega en el sitio un botón para descargarlo.
Verifica que el archivo sea un iCalendar válido.
```
💡 *Qué aprendes:* un archivo `.ics` lo entienden todas las agendas. Tus estudiantes ya no tienen pretexto.

---

## Nivel 4 · Verificar antes de publicar (5 min)
```
Revisa el sitio contra el syllabus original y el calendario académico:
1. ¿Alguna sesión cae en día inhábil?
2. ¿Cada lectura del syllabus aparece en el sitio, con el mismo autor, año y capítulo?
3. ¿Las referencias con DOI existen? Verifícalas en https://api.crossref.org/works/DOI
Dame una tabla con lo que encuentres.
```

---

## Retos para quien termine antes
```
Crea una rúbrica para el proyecto final con 4 criterios y 4 niveles de desempeño,
como tabla en el sitio y como documento Word para imprimir.
```
```
Agrega un botón de "versión para imprimir" que deje el calendario en una sola página.
```
```
Escribe un CLAUDE.md en mi-trabajo/ con las reglas de mi curso (formato de citas,
día de clase, políticas) para que el próximo semestre solo te pase el nuevo calendario.
```

---

## Reglas de oro
1. **Dale a Claude el calendario de tu institución**; no lo adivina.
2. **Cuando algo no cuadra, decides tú.**
3. **Verifica las lecturas**: autor, año, capítulo y enlace.
