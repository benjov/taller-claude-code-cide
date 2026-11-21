# Prompts · Ruta 06 · Fuentes auditables

Copia y pega cada prompt en Claude Code (pestaña **Code** de la app de escritorio, con tu carpeta abierta).
**Lee lo que Claude propone antes de aprobar.** Cuando pida permiso para ejecutar algo, revisa qué va a hacer.

---

## Nivel 0 · Arranque (2 min)
```
Voy a construir un análisis auditable y replicable de la informalidad laboral en México.
Antes de hacer nada, revisa qué tengo instalado (Python y paquetes como pandas, requests,
matplotlib, openpyxl y jupyter) y dime qué falta. No instales nada todavía.
```
💡 *Qué aprendes:* Claude Code ve tu computadora y te explica antes de actuar.

---

## Nivel 1 · Conseguir los datos oficiales (8 min). Elige A o B

### Opción A · Que Claude Code los descargue de INEGI
```
Quiero calcular la Tasa de Informalidad Laboral 1 (TIL1) de México para el segundo
trimestre de 2026 usando los microdatos de la ENOE de INEGI.
Trabaja en la carpeta 06-fuentes-auditables/mi-trabajo/.

1. Encuentra en el sitio de INEGI la URL oficial de los datos abiertos de la ENOE 2T-2026.
2. Descárgala en mi-trabajo/datos/.
3. Crea un archivo bitacora_fuentes.csv con: institución, descripción, URL, fecha y hora
   de consulta, tamaño en bytes y huella SHA-256 del archivo.
4. Compara la huella con la que aparece en 06-fuentes-auditables/datos/FUENTES.md
   y dime si mi descarga es idéntica a la copia del repositorio.
5. Dime qué tablas y diccionarios contiene el zip.
```

### Opción B · Usar la copia que ya viene en el repositorio
```
Quiero calcular la Tasa de Informalidad Laboral 1 (TIL1) de México para el segundo
trimestre de 2026 usando los microdatos de la ENOE de INEGI.
Trabaja en la carpeta 06-fuentes-auditables/mi-trabajo/.

1. Lee 06-fuentes-auditables/datos/FUENTES.md: ahí están los archivos, su URL original
   y su huella SHA-256. NO descargues nada; usa los archivos de esa carpeta.
2. Verifica que la huella SHA-256 de cada archivo coincida con la de FUENTES.md.
3. Crea un archivo bitacora_fuentes.csv con: institución, descripción, URL original,
   fecha de descarga, tamaño en bytes, huella SHA-256 y si coincide.
4. Dime qué tablas y diccionarios contiene el zip de la ENOE.
```
💡 *Qué aprendes:* en los dos caminos Claude Code **documenta la procedencia**. La huella SHA-256 permite que cualquiera compruebe que usa exactamente el mismo archivo. Con la opción A, además, ves a Claude Code navegar un sitio oficial y encontrar el enlace correcto.

---

## Nivel 2 · El notebook replicable (12 min)
```
Ahora crea un notebook de Jupyter llamado informalidad_auditable.ipynb que:

1. Tenga una celda de parámetros (año y trimestre) para poder replicar otros periodos.
2. Tenga un parámetro FUENTE_DATOS: "repo" (usar ../datos/ del repositorio) u "original"
   (descargar de INEGI solo si no existe ya). En ambos casos registre todo en la bitácora.
3. Calcule la TIL1 nacional y por entidad federativa con los criterios de INEGI
   (explícalos en una celda de texto: qué variables, qué filtros, qué factor de expansión).
4. Haga una gráfica de barras de la TIL1 por entidad con la fuente al pie.
5. Explique en español cada paso para un lector que no programa.

Ejecútalo completo y dime si hay errores.
```
💡 *Qué aprendes:* Claude Code escribe, **ejecuta y corrige** el código. Si algo falla (spoiler: el archivo de INEGI trae una sorpresa de codificación), míralo diagnosticar.

**Ruta Colab:** agrega al final: *"Asegúrate de que funcione en Google Colab sin instalar nada; en Colab no existe ../datos/, así que en modo repo debe bajar los archivos de https://github.com/benjov/taller-claude-code-cide/raw/main/06-fuentes-auditables/datos/"*. Luego sube el `.ipynb` en colab.research.google.com → Archivo → Subir notebook.

---

## Nivel 3 · Auditar: ¿mi cifra es la oficial? (8 min)
```
Agrega al notebook una sección de validación:
1. Busca el boletín de prensa de INEGI de la ENOE 2T-2026 (nacional) y los boletines
   estatales de 2 o 3 entidades que me interesen: [ESCRIBE AQUÍ LAS ENTIDADES].
2. Toma de los boletines la TIL1 total, de hombres y de mujeres, y guarda la URL de cada cifra.
3. Compara con mi cálculo en una tabla: publicado, replicado, diferencia y si coincide.
4. Agrega una sección que verifique que todas las URLs del notebook siguen respondiendo.
```
💡 *Qué aprendes:* **la validación atrapa errores, incluidos los de la IA.** Al preparar este taller, el ejemplo transcribió mal el orden de las columnas *Mujeres/Hombres* del boletín, y la tabla de validación lo detectó de inmediato. Por eso se valida.

---

## Nivel 4 · Elige tu salida (5 min)
**Excel:**
```
Exporta a un Excel con hojas: bitacora_fuentes, validacion, por_entidad,
estado_enlaces y entorno (versiones de Python y paquetes).
```
**Word:**
```
Genera un documento Word "Anexo metodológico de fuentes" con: fuentes consultadas
(con fecha de consulta y URL), criterios de cálculo, tabla de validación contra cifras
oficiales y la gráfica. Redáctalo en estilo académico, listo para un artículo.
```

---

## Retos para quien termine antes
```
Agrega la serie de informalidad de ILOSTAT (OIT) para México y compárala con la de INEGI.
Explica por qué no coinciden exactamente.
```
```
Repite el cálculo para el 2T-2025 cambiando solo los parámetros y muestra el cambio por entidad.
```
```
Escribe un CLAUDE.md para este proyecto con las fuentes, criterios y decisiones
metodológicas, para que la próxima vez retomemos donde nos quedamos.
```

---

## Reglas de oro
1. **Toda cifra debe tener una fuente en la bitácora.** Si Claude te da un número sin URL, pídesela.
2. **Valida contra lo publicado.** Una réplica que no se compara no es una réplica.
3. **Lee antes de aprobar.** Tú eres la autoridad académica; Claude Code es el asistente de investigación.
