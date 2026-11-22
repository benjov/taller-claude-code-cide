# Prompts · Ruta 05 · Cualitativo

Copia y pega cada prompt en Claude Code (pestaña **Code**, con la carpeta del repositorio abierta).

---

## Nivel 0 · Anonimizar antes de analizar (5 min) ⚠️
```
Crea la carpeta 05-cualitativo/mi-trabajo/ y trabaja ahí.
Revisa las entrevistas de 05-cualitativo/insumos/entrevistas/ y busca cualquier dato que
permita identificar a una persona: nombres propios (de la participante o de terceros),
teléfonos, direcciones o lugares exactos, nombres de negocios.
Dame una tabla (entrevista, turno, tipo de dato, reemplazo sugerido) SIN copiar el dato
original. Después crea versiones anonimizadas en mi-trabajo/entrevistas_anon/ y
trabaja solo con esas.
```
💡 *Qué aprendes:* la anonimización es el **primer** paso, no el último.

---

## Nivel 1 · Conocer el material (3 min)
```
Lee 05-cualitativo/insumos/proyecto_y_guia.docx y las entrevistas anonimizadas.
Dame un perfil de una línea de cada participante y los temas que más se repiten,
indicando en cuántas de las 6 entrevistas aparece cada tema.
```

---

## Nivel 2 · Libro de códigos (8 min)
```
Propón un libro de códigos inicial (8 a 10 códigos) para la pregunta de investigación.
Para cada código: clave corta, nombre, definición, cuándo incluir, cuándo excluir y un
ejemplo con cita literal (entrevista y turno). Combina códigos de la guía de entrevista
(deductivos) con los que surjan del material (inductivos), y marca cuáles son cuáles.
No codifiques todavía; espera mi revisión.
```
Revisa y ajusta en lenguaje natural:
```
Fusiona [X] y [Y]. Separa [Z] en dos códigos. Cambia la definición de [W] para que excluya [...].
```
💡 *Qué aprendes:* **tú** decides las categorías analíticas; la IA las propone y las documenta.

---

## Nivel 3 · Codificar (10 min)
```
Codifica las 6 entrevistas con el libro de códigos aprobado. Guarda en
mi-trabajo/codificacion.xlsx una matriz con: entrevista, turno, segmento LITERAL y
código(s). Agrega una hoja con la presencia de cada código por entrevista.
Al terminar, verifica con un script que cada segmento aparezca palabra por palabra
en su entrevista, y dime cuáles no pasaron.
Señala también los segmentos ambiguos o contradictorios dentro de una misma entrevista.
```
💡 *Qué aprendes:* la verificación automática hace **trazable** cada cita. Fíjate qué hace Claude con una participante que se contradice.

---

## Nivel 4 · Informe de hallazgos (6 min)
```
Redacta en Word (mi-trabajo/informe_hallazgos.docx) un informe breve organizado por
temas. Para cada tema: en cuántas entrevistas aparece (n de 6), 1 o 2 citas literales
con entrevista y turno, y los casos contrastantes. Agrega una sección
"Temas con evidencia limitada" y otra de "Limitaciones y reflexividad".
No uses palabras como "todas", "la mayoría" o "en general" si no lo respaldan los conteos.
```

---

## Nivel 5 · Auditar el informe (3 min)
```
Revisa el informe contra la matriz de codificación: para cada afirmación con número
o cuantificador ("en 4 de 6", "varias", "las comerciantes…"), comprueba que coincida
con los conteos. Dame una tabla de afirmaciones que no cuadren.
```

---

## Retos para quien termine antes
```
Haz una segunda codificación independiente de 2 entrevistas sin ver la primera, compara
ambas y calcula el porcentaje de acuerdo por código. ¿Dónde difieren y por qué?
```
```
Exporta la matriz en un formato que pueda importar a [ATLAS.ti / NVivo / MAXQDA / Taguette].
```
```
Escribe un CLAUDE.md en mi-trabajo/ con mis reglas de codificación y anonimización
para reutilizarlas en mi proyecto real.
```

---

## Reglas de oro
1. **Anonimiza antes de analizar.**
2. **Toda cita, literal y con su ubicación.**
3. **Cuenta antes de generalizar.**
