# Copia de los datos para el taller

`wdi_latam.csv` es una copia **sin modificar** (formato largo) de los Indicadores del Desarrollo Mundial (WDI) del Banco Mundial, descargada de su API pública el **22 de noviembre de 2026** (última actualización de la fuente: 11-nov-2026).

- **Países (17):** Argentina, Bolivia, Brasil, Chile, Colombia, Costa Rica, Ecuador, El Salvador, Guatemala, Honduras, México, Nicaragua, Panamá, Paraguay, Perú, Rep. Dominicana, Uruguay.
- **Periodo:** 2000–2023.
- **SHA-256:** `8cab73333ea1629f19928afc2d329b24779339b8d3025203b1084b4567476ec9`

| Código | Indicador | URL de la API (ejemplo con México) |
|---|---|---|
| `VC.IHR.PSRC.P5` | Homicidios intencionales por 100,000 habitantes | https://api.worldbank.org/v2/country/MEX/indicator/VC.IHR.PSRC.P5?format=json |
| `NY.GDP.PCAP.PP.KD` | PIB per cápita, PPA (dólares internacionales constantes de 2021) | https://api.worldbank.org/v2/country/MEX/indicator/NY.GDP.PCAP.PP.KD?format=json |
| `SI.POV.GINI` | Índice de Gini | https://api.worldbank.org/v2/country/MEX/indicator/SI.POV.GINI?format=json |
| `SL.UEM.TOTL.ZS` | Desempleo, % de la fuerza laboral (estimación modelada OIT) | https://api.worldbank.org/v2/country/MEX/indicator/SL.UEM.TOTL.ZS?format=json |

**Columnas:** `iso3`, `pais`, `anio`, `indicador`, `valor` (vacío = sin dato).

**Ojo:** el Banco Mundial revisa sus series. Si descargas de nuevo, algunos valores pueden cambiar; por eso se guarda la fecha y la huella del archivo.

**Términos de uso:** datos del Banco Mundial bajo licencia CC BY 4.0. Cita: Banco Mundial, *World Development Indicators*.
