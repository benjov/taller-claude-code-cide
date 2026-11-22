# Prompts · Ruta 01 · Web académica

Copia y pega cada prompt en Claude Code (pestaña **Code** de la app de escritorio, con la carpeta del repositorio abierta).
Donde dice `[MI CV]` escribe la ruta de tu archivo, por ejemplo `01-web-academica/mi-sitio/cv.pdf` o `01-web-academica/insumos/cv_ficticio.pdf`.

---

## Nivel 0 · Que Claude conozca tu material (3 min)
```
Crea la carpeta 01-web-academica/mi-sitio/ y trabaja ahí.
Lee [MI CV] y hazme un resumen en 5 viñetas: quién soy, qué investigo,
mis publicaciones más importantes, qué enseño y cómo contactarme.
No escribas ningún archivo todavía.
```
💡 *Qué aprendes:* Claude Code **lee tus archivos** (PDF, Word) directamente. No hace falta copiar y pegar.

---

## Nivel 1 · Planear antes de construir (4 min)
```
Quiero una página web académica personal de una sola página, a partir de mi CV.
Antes de escribir código, propónme:
1. Las secciones y su orden.
2. Un texto de presentación de 3–4 líneas en primera persona, claro para un público
   no especializado (periodistas, estudiantes, funcionarios).
3. Dos opciones de estilo visual (colores y tipografía) descritas en una línea cada una.
Espera mi visto bueno.
```
💡 *Qué aprendes:* pedir **un plan primero** te da el control. Corrige lo que no te guste antes de que exista una sola línea de código.

---

## Nivel 2 · Construir la página (8 min)
```
Me gusta el plan [agrega aquí tus ajustes, p. ej. "usa la opción 2 de estilo"].
Construye index.html en mi-sitio/:
- Un solo archivo autocontenido (HTML, CSS y JavaScript juntos), sin dependencias externas.
- Que se vea bien en celular y tenga modo oscuro automático.
- Las publicaciones guardadas como una lista de datos en JavaScript, para que sea fácil
  agregar nuevas después.
- Usa ÚNICAMENTE información que esté en mi CV.
Al terminar, ábrela en mi navegador.
```
💡 *Qué aprendes:* Claude Code **crea archivos y los abre**. Tienes un sitio funcionando en minutos.

---

## Nivel 3 · Hacerla tuya (8 min)
Elige uno o varios cambios. Pídelos **en lenguaje natural**, como se los pedirías a un asistente:
```
El azul se ve muy corporativo; usa un verde oscuro más sobrio.
```
```
La presentación suena muy formal. Reescríbela más cercana, sin perder seriedad.
```
```
Puse una foto mía en mi-sitio/foto.jpg. Úsala en lugar del círculo con iniciales.
```
```
Agrega una sección "Noticias" arriba de Publicaciones con dos entradas recientes:
[describe tus noticias].
```
💡 *Qué aprendes:* se itera conversando. No necesitas saber CSS para decir "más sobrio".

---

## Nivel 4 · Funciones útiles (6 min)
```
En Publicaciones agrega:
1. Botones para filtrar por tipo (artículos, libros, capítulos).
2. Un buscador por título, revista o coautor.
3. En cada publicación, botones para copiar la cita en formato APA y en BibTeX.
```
💡 *Qué aprendes:* Claude Code programa **interactividad real**. Pruébala en el navegador.

---

## Nivel 5 · Auditar antes de publicar (5 min) ⚠️ No te lo saltes
```
Revisa index.html contra [MI CV] y dame una tabla con TODO dato de la página
(fechas, títulos, cargos, premios, coautores, revistas) que NO aparezca tal cual en el CV,
o que esté redactado de forma que cambie su significado. No corrijas nada todavía.
```
Luego:
```
Corrige los puntos [números] de la tabla. Además revisa la accesibilidad:
contraste de colores, textos alternativos y que se pueda navegar con teclado.
```
💡 *Qué aprendes:* **la IA puede embellecer.** Tu reputación está en esa página, así que auditas antes de publicar, igual que con un artículo.

---

## Retos para quien termine antes
```
Agrega un botón para cambiar el idioma de la página entre español e inglés.
```
```
Tengo mis publicaciones en un archivo .bib: [ruta]. Haz que la página tome
la lista de publicaciones de ahí, para que solo tenga que actualizar el .bib.
```
```
Escribe un CLAUDE.md en mi-sitio/ con las reglas de mi página (estilo, tono,
cómo agregar una publicación) para que cada semestre solo te diga "agrega esto".
```
```
Explícame paso a paso cómo publicar esta página gratis en GitHub Pages.
```

---

## Reglas de oro
1. **Nada que no esté en tu CV.** Si Claude agrega algo, pregúntale de dónde lo sacó.
2. **Datos personales:** no publiques lo que no pondrías en una tarjeta de presentación.
3. **Lee antes de aprobar.** Tú decides qué se queda.
