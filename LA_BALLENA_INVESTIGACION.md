# La ballena: investigación profunda de mercado y rumbo único

> Encargo: un solo nicho, un solo producto, defendible, no genérico, para dedicarle un año. Sin complacencia.
> Método: barrido multi-fuente (jun 2026) sobre cadena de valor de IA, mercados infraservidos, vientos regulatorios con fecha, fosos defendibles y casos de fundadores pequeños. Verificado contra fuentes oficiales de la UE donde es crítico. Marco nivel de confianza donde toca.

---

## 1. Lo que dice el mercado (hechos, no opinión)

**A. El modelo se comoditiza. El valor sube.**
Los modelos base están en caída de precios y paridad (Anthropic -67%, Google -70/80%, OpenAI recortes sucesivos). El modelo crudo pasa de ventaja a utility. El valor migra a las capas que el modelo no resuelve: **ejecución de trabajo real, integración profunda en el flujo, datos propietarios y — clave — confianza/cumplimiento.** El propio foso de Anthropic en empresa no es el modelo: es **confianza + cumplimiento** (infra HIPAA, inercia institucional). *(Confianza alta — múltiples fuentes coinciden.)*

**B. "Lo aburrido es sexy."** El patrón ganador de la IA vertical: mercado enorme, fragmentado e ignorado; te metes en el primer punto de contacto; construyes un **activo de datos propietario que captura la lógica de negocio**, no solo información. Diana ideal: sectores con **alta proporción de gasto en mano de obra frente a IT**, y **trabajo de juicio sobre material desordenado** (documentos, conversaciones) que el software clásico no alcanzaba. *(Confianza alta — tesis de Amplify, Menlo, Euclid.)*

**C. Se vende trabajo, no software.** Los ganadores verticales (Sierra, Harvey, EvenUp, Hippocratic) cobran **por resultado** (ticket resuelto, reclamación completada) y capturan un % del valor del trabajo, no del gasto en software → mercados 5-10x mayores, márgenes del 90%. *(Confianza alta.)*

**D. El foso que más se repite en negocios pequeños rentables: el regulatorio.** En micro-SaaS, los fosos primarios más comunes son **regulatorio y de mundo físico (30% cada uno)**, luego datos (20%). Las herramientas de cumplimiento renuevan **>95%** porque la obligación legal no desaparece. Fundadores con dominio propio del problema: **2,3x más probables de llegar a 10k$ MRR en 12 meses.** *(Confianza media-alta.)*

**E. Hay vientos regulatorios con FECHA y mercado sin atender.** La UE ha creado una ola de obligaciones de documentación de conformidad con calendario duro (ver §4). *(Confianza alta — fuentes oficiales UE.)*

---

## 2. Lo que DESCARTO (y por qué) — para no hacer lo del 99%

- **Chatbots, "segundo cerebro", RAG genérico, wrappers de GPT:** commodity. El modelo se los come. Cero foso.
- **Agencias/consultorías de IA y venta de plantillas:** es exactamente "lo que todo el mundo hace desde 2025". No escala, no es producto, no es foso.
- **Plataformas de gobernanza de IA (AI governance / GRC):** mercado real y creciente (CAGR ~45%, ~5,8B$) **PERO ya saturado** y bien financiado: Vanta, Drata, Sprinto, Credo, Holistic AI, Splunk, Witness.ai, etc. Un fundador solo llega tarde y sin músculo. **Evitar como apuesta principal.**
- **Atención al cliente / legal / salud verticales (Sierra, Harvey, Hippocratic):** ganadores ya consolidados con cientos de millones. Mar lleno de ballenas más grandes que tú.
- **Escáneres de SBOM / AppSec (Snyk, Mend, Cycode, Anchore):** crowded. Resuelven el *escaneo*, no el *expediente de conformidad*. Importante: esto NO es el hueco (ver §3).

---

## 3. El razonamiento hasta la ballena

Cruzo los hechos: el valor está en **cumplimiento + ejecución de trabajo documental de juicio + foso regulatorio + datos propietarios**, en un **mercado aburrido con dolor y presupuesto**, con un **viento de cola con fecha**, y donde **los grandes no entran** (demasiado nicho/regulatorio/UE) y **los crowded no encajan** (las plataformas GRC son forma "certificación de organización", no "conformidad de producto").

Hay un sitio donde todo esto se cruza y casi nadie lo está atacando como producto de IA:

> **La conformidad documental de productos bajo el Cyber Resilience Act (CRA) de la UE, para la cola larga de pymes que fabrican "productos con elementos digitales".**

No es gobernanza de IA (saturado). No es escaneo de SBOM (saturado). Es el **expediente de conformidad** —documentación técnica, evaluación de riesgos, proceso de gestión de vulnerabilidades, declaración UE de conformidad— que el CRA **obliga** a tener, mantener 10 años y poder enseñar a la autoridad de vigilancia. Hoy eso lo hacen consultores a mano y a precio alto, o no se hace.

---

## 4. EL RUMBO ÚNICO — nicho + producto

**Nicho:** fabricantes/desarrolladores pyme de la UE (y los de fuera que venden en la UE) de **productos con elementos digitales** — software comercial, dispositivos conectados/IoT, firmware, equipos industriales con software — que caen en autoevaluación o categoría "importante" y **no tienen ni equipo ni dinero para consultoría de cumplimiento.**

**Producto:** un sistema de IA que **genera y mantiene vivo el expediente de conformidad CRA** de un producto. Ingiere la realidad técnica del producto (repositorio, dependencias, arquitectura, prácticas de seguridad existentes) y produce:

- documentación técnica (Anexo VII),
- evaluación de riesgos de ciberseguridad,
- integración/lectura del SBOM (no compite con el escáner: lo consume),
- proceso documentado de gestión de vulnerabilidades y política de periodo de soporte,
- borrador de la Declaración UE de Conformidad,
- y lo mantiene **auditable y actualizado** durante los 10 años de retención y en cada nueva versión.

**Modelo:** services-as-software. Precio por resultado: **expediente por producto (1.500–5.000 € vs. 10–30k€ de un consultor) + cuota de mantenimiento del expediente vivo (100–400 €/producto/mes).** Recurrente + regulatorio → renovación altísima.

**Frase comercial:** *"Tu conformidad CRA, hecha y mantenida al día. Listo para la autoridad, sin un equipo de cumplimiento."*

---

## 5. Por qué es la ballena (y por qué no está saturado)

- **Obligatorio y con fecha dura:** CRA en vigor desde el 10/12/2024; obligaciones de **notificación de incidentes desde el 11/09/2026**; **obligaciones principales desde el 11/12/2027**. Multas hasta **15M€ o 2,5%** de la facturación global. La demanda no es opcional ni discrecional.
- **Alcance gigante:** *todo* producto con elementos digitales puesto en el mercado de la UE — decenas de miles de fabricantes, también de EE.UU./Asia (efecto extraterritorial). No es un nicho pequeño: es un nicho **enorme disfrazado de aburrido**.
- **Sin atender en la cola larga:** **más de la mitad de las pymes europeas ni conocen el CRA todavía.** Las herramientas existentes son escáneres AppSec (otra cosa) o GRC de organización (otra forma). El **expediente de conformidad de producto, productizado con IA y asequible para pymes, está hueco.** Hay consultoras y algún player CRA emergente, pero fragmentado y no productizado.
- **Encaja con la tesis ganadora 2026:** trabajo documental de juicio sobre material desordenado, vendido como resultado, con foso regulatorio.

---

## 6. El foso defendible (los cuatro, alineados con lo que el mercado dice que gana)

1. **Regulatorio:** la propia norma crea demanda y renovación (>95%). El foso más común en negocios pequeños rentables.
2. **Datos propietarios:** un corpus creciente de expedientes CRA reales + mapeo de estándares armonizados + bibliotecas de riesgos por tipo de producto. Cada expediente mejora las plantillas y el motor. Los labs grandes no construirán esto (demasiado nicho/UE/regulatorio).
3. **Confianza/responsabilidad:** en cumplimiento, el comprador quiere un especialista cuyo expediente aguante a un organismo notificado, no un chatbot. Es el foso de Anthropic a tu escala.
4. **Workflow + lock-in:** retención de 10 años + expediente vivo + re-evaluación por versión = recurrente y pegajoso.

---

## 7. Por qué TÚ puedes ganarlo (sin la muleta de "estar dentro")

No por estar dentro de una empresa. Por algo más sutil y real: **proximidad de dominio.** Tu empresa hace conformidad y marcado CE (expedientes técnicos, evaluación de riesgos, declaraciones de conformidad, organismos notificados). El CRA es **exactamente la misma forma de trabajo** — expediente que prueba que un producto cumple una norma — aplicada a la dimensión ciber. Tú entiendes esa maquinaria de cumplimiento por contexto, y sus clientes industriales **también van a tener que cumplir el CRA en sus productos conectados.** Eso te da:

- **Comprensión del shape del trabajo** (no partes de cero conceptualmente).
- **Un beachhead de distribución** (la red de clientes de conformidad existente).
- **Socios de validación** (gente que sabe de organismos notificados).

Pero el producto **no depende de tu empresa**: sirve a cualquier fabricante de la UE/mundo. La empresa es trampolín, no techo. Y eres técnico que construye con IA → puedes montar el pipeline de ingesta + generación tú mismo.

---

## 8. Riesgos honestos

- **El regulador mueve fechas.** El AI Act acaba de extender plazos (omnibus, mayo 2026); el CRA podría ajustarse. Mitigación: la *necesidad de hacer el trabajo* persiste aunque cambie la fecha; no vendes la fecha, vendes el expediente.
- **Responsabilidad legal del expediente.** Posición: "prepara y mantiene auditable"; revisión experta en clases de mayor riesgo; empieza por **autoevaluación** (la categoría por defecto, la mayoría de productos) donde no hace falta organismo notificado.
- **Estándares armonizados aún en desarrollo.** Riesgo y oportunidad: muévete a medida que se consolidan; el que tenga el motor listo cuando se publiquen, gana.
- **Distribución a pymes que ni saben que les aplica.** Por eso el beachhead de tu empresa y los ecosistemas de ayuda de la UE (Digital Europe, helpdesks CRA) importan. Educación = parte del marketing.
- **Competencia que vendrá.** Vendrá. Tu ventaja es entrar ahora (2026) con producto, datos y fechas a tu favor, no en 2028.

---

## 9. Cómo empezar el año (alto nivel)

1. **Mes 1-2:** elige UN arquetipo de producto (p. ej. "app/SaaS web" o "dispositivo IoT con firmware"). Domina el Anexo VII y la evaluación de conformidad de esa clase. Consigue 2-3 productos reales (de tu empresa o su red) como casos.
2. **Mes 2-4:** construye el motor que ingiere un producto y genera el expediente borrador para ese arquetipo. Validación con alguien que entienda conformidad.
3. **Mes 4-6:** 3 clientes piloto pagados a precio bajo a cambio de caso + testimonio. Empieza el corpus propietario.
4. **Mes 6-12:** producto de autoservicio + expediente vivo (retainer). Expande a un segundo arquetipo. Empuja con la urgencia de sep-2026/dic-2027.

---

## 10. Veredicto

Olvida clínicas, maquinaria y bases de conocimiento. La ballena es **el expediente de conformidad CRA como producto de IA para la cola larga de fabricantes de productos digitales de la UE.** Es aburrido, regulado, obligatorio, con fecha, enorme, infraservido en su cola larga, defendible por cuatro fosos a la vez, alineado con la única tesis de monetización que está funcionando en 2026 (vender trabajo, no software), e ignorado tanto por los labs grandes como por los startups crowded. Y tú tienes proximidad de dominio real, no inventada.

Un nicho. Un producto. Un año. Esta es la apuesta.

---

## Fuentes
- Cadena de valor / comoditización: chamath.substack, paulkedrosky, taskade "execution layer", FourWeekMBA, Menlo Ventures (vertical AI).
- Boring-is-sexy / vertical AI: Amplify Partners, Euclid Ventures, Menlo Ventures.
- Vender trabajo / outcome pricing: futurumgroup, Bessemer, getmonetizely (Sierra/Harvey/EvenUp/Hippocratic).
- Fosos: baytechconsulting, sajalsharma, buildmvpfast, entrepreneurloop (micro-SaaS moats).
- CRA: Comisión Europea (digital-strategy.ec.europa.eu CRA + CRA-MSMEs), Anchore, Kusari, Cycode, White & Case, Linux Foundation, Wikipedia.
- EU AI Act (descarte): artificialintelligenceact.eu, ai-act-service-desk.ec.europa.eu, dataguard, Latham & Watkins.
- AI governance market (descarte): centraleyes, domo, truefoundry, Gartner.
