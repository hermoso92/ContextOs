# Cosigein — El producto real (no es una base de conocimiento)

> Análisis para Antonio Hermoso. Estás dentro de Cosigein/CSG Ingeniería. Eso es un activo enorme.
> Tesis: no construyas un bot que *responde* sobre normativa. Construye un agente que *hace el trabajo de ingeniería de cumplimiento* que hoy hacen los ingenieros a mano.

---

## 1. Qué es Cosigein realmente (lo que he averiguado)

- **CSG Ingeniería / Cosigein SL.** Fundada en 2001. Parque Científico-Tecnológico Rabanales 21, Córdoba.
- **Núcleo del negocio:** ingeniería y consultoría de **seguridad industrial** y **marcado CE de maquinaria**. Certificación de máquinas, auditorías de seguridad, expedientes técnicos.
- **Defensa:** +15 años con el Ejército español y empresas europeas (Alemania). Vehículos de extinción de incendios forestales, análisis de estabilidad y antivuelco de vehículos pesados, mantenimiento predictivo de vehículos militares.
- **I+D+i:** coordinación de proyectos de investigación, colaboración +20 años con la Universidad de Córdoba.
- **Sector:** B2B técnico, regulado, intensivo en documentación y en conocimiento experto.

**Conclusión:** Cosigein vende un producto que en el fondo es **documentación técnica experta que cumple una normativa**. Expedientes, análisis de riesgos, declaraciones de conformidad, auditorías, manuales. Eso es exactamente el tipo de trabajo que la IA generativa de 2026 puede transformar — no "responder preguntas", sino **redactar el entregable**.

---

## 2. La bomba de relojería (tu ventana de mercado, con fecha)

El **Reglamento (UE) 2023/1230 de Máquinas** deroga la Directiva 2006/42/CE y es de **aplicación obligatoria desde el 20 de enero de 2027**.

Qué significa esto para el mercado de Cosigein:

- Es **reglamento**, no directiva → aplicación directa e idéntica en toda la UE. Mercado homogéneo de golpe.
- Introduce por primera vez **software, IA y ciberseguridad** como parte de la seguridad de la máquina.
- Cambian los requisitos de los expedientes técnicos, las categorías de alto riesgo (Anexo I) y las evaluaciones.
- **Cada fabricante, importador y consultora de la UE tiene que re-aprender y re-documentar.** Hay un pico de demanda con fecha de caducidad.

Traducción: hay una **ola regulatoria forzosa** llegando, y Cosigein está justo en la playa. El que tenga una herramienta para hacer ese trabajo más rápido y sin errores, gana. Esa herramienta no existe todavía como producto serio. Esa es la grieta.

---

## 3. La decisión (no genérica, un nicho real, sin humo)

> **Construir un agente vertical de IA para ingeniería de cumplimiento de máquinas (marcado CE / seguridad industrial), que redacta los entregables técnicos que hoy hacen los ingenieros a mano, usando el archivo de 20 años de Cosigein como ventaja, y aprovechando el Reglamento 2023/1230 (obligatorio enero 2027) como puerta de entrada al mercado.**

Por qué esta y no otra:

- **No es base de conocimiento.** Una base de conocimiento responde *"¿qué dice la norma EN ISO 12100?"*. Esto **produce el análisis de riesgos de ESTA máquina concreta**. Es trabajo, no consulta.
- **No es vende-humos.** Requiere conocimiento de ingeniería de seguridad real, encerrado en la cabeza de los ingenieros de Cosigein y en sus expedientes pasados. Un consultor de IA genérico no puede construir esto: no sabe de seguridad de máquinas. **Tú estás dentro y tienes acceso al conocimiento y a los ejemplos.** Ese es el foso.
- **Es la frontera de 2026** (agentes verticales que ejecutan tareas end-to-end), aplicada a un **nicho aburrido, regulado e ignorado** por la moda de la IA de consumo. Justo donde está el dinero y no la competencia.
- **Escala más allá de Córdoba.** El marcado CE es mercado UE. Cosigein es tu cliente cero y co-desarrollador; el producto sirve a toda consultora de seguridad, fabricante e importador de la UE.

---

## 4. Qué HACE el producto (agente, no chatbot)

**Entrada:** documentación técnica de una máquina (planos, especificaciones, fotos, datos del fabricante, uso previsto).

**El agente produce, en borrador, lo que hoy redacta el ingeniero:**

1. **Clasificación normativa:** qué directivas/reglamentos y normas armonizadas aplican a esa máquina. Mapeo Directiva 2006/42 → Reglamento 2023/1230.
2. **Análisis de riesgos (EN ISO 12100):** identifica peligros típicos de ese tipo de máquina, estima el riesgo, propone medidas de reducción. Estructurado, citando la cláusula. **Este es el corazón y el primer entregable a atacar.**
3. **Índice del expediente técnico** y borrador de la **Declaración CE de Conformidad**.
4. **Revisión del manual de instrucciones** contra los requisitos del reglamento.
5. **Análisis de brechas (gap analysis) 2006/42 → 2023/1230:** "esta máquina estaba certificada con la directiva vieja; esto es lo que cambia con el reglamento nuevo, esta es tu lista de tareas." **Esto se vende como servicio nuevo, con la urgencia de 2027.**

**El ingeniero revisa y firma.** El agente hace el 80% del trabajo de redacción; el humano aporta el criterio y la responsabilidad legal. Es aumento, no sustitución. Esto es clave (ver riesgos).

---

## 5. Base de conocimiento vs lo que tú vas a hacer (la diferencia que tu jefe verá)

| Base de conocimiento / bot (commodity, lo que hace todo el mundo) | Agente de cumplimiento (tu producto) |
|---|---|
| Responde *"¿qué exige el Anexo I?"* | Genera *el análisis de riesgos de la máquina X* |
| El ingeniero pregunta, luego trabaja igual | El ingeniero revisa un borrador ya hecho |
| Ahorra minutos de búsqueda | Ahorra **días** de redacción por expediente |
| Valor: información | Valor: **el entregable facturable, más rápido** |
| Lo copia cualquiera en una tarde | Necesita el archivo y la experiencia de Cosigein |

Cuando le enseñes a tu jefe **un análisis de riesgos completo de una máquina real, redactado en 10 minutos donde un ingeniero tarda 2 días**, no va a pensar "otro chatbot". Va a pensar "esto multiplica nuestra capacidad de facturación".

---

## 6. Cómo lo construyes dentro de Cosigein (plan para enseñarlo en 1 mes)

**Semana 1 — Conseguir el oro (lo que solo tú puedes desde dentro):**
- Pide 5-10 expedientes técnicos antiguos ya cerrados (análisis de riesgos + declaraciones). Son tus ejemplos de oro: muestran *cómo lo hace Cosigein*.
- Elige **una sola familia de máquina** que Cosigein certifique a menudo. No todo. Una.
- Siéntate 1 hora con el ingeniero senior y graba: cómo decide los peligros, dónde mira, qué reglas no están escritas. (Aquí sí usas tu guion de extracción.)

**Semana 2-3 — Construir el prototipo de UN entregable:**
- Monta un agente que reciba la especificación de una máquina de esa familia y devuelva un **borrador de análisis de riesgos EN ISO 12100** con el estilo y estructura de Cosigein, citando normas.
- Tecnología: un LLM potente (Claude/GPT) + los expedientes pasados como contexto/ejemplos (RAG) + la plantilla de Cosigein. Sin infraestructura grande todavía.

**Semana 4 — La demo a tu jefe:**
- Coges una máquina real reciente. Le pides al ingeniero que estime cuánto tardó (o tardaría) en el análisis de riesgos.
- Le enseñas el borrador que generó el agente en minutos, al lado del que hizo el humano. Comparáis.
- El mensaje: *"esto no sustituye al ingeniero; le quita el 80% del trabajo de redactar para que dedique su tiempo al criterio. Y con el Reglamento 2027 encima, podemos ofrecer un servicio nuevo de adaptación que nadie tiene aún."*

---

## 7. Cómo se monetiza (dos caminos, no excluyentes)

1. **Interno (lo primero):** herramienta que multiplica la capacidad de Cosigein. Más expedientes por ingeniero, márgenes mayores, nuevo servicio de "adaptación a 2023/1230". Aquí tu jefe lo entiende como inversión, no gasto.
2. **Producto (después):** licenciar la herramienta a otras consultoras de seguridad y fabricantes de la UE. Aquí Cosigein pasa de vender horas a vender software. Tú eres quien lo construyó. (Negocia tu posición antes de que despegue.)

---

## 8. Por dónde NO empezar

- **NO por defensa.** Vehículos militares = datos sensibles, control de exportación, confidencialidad. Empieza por maquinaria civil/industrial. Defensa, mucho más tarde y con cuidado legal.
- **NO por "toda la empresa a la vez".** Un entregable (análisis de riesgos), una familia de máquina. Cierra eso primero.
- **NO por una base de conocimiento.** Si empiezas por ahí, habrás hecho lo que hace todo el mundo. Como mucho, es un subproducto interno del agente.

---

## 9. Riesgos (honestos)

- **Responsabilidad legal:** un documento de cumplimiento mal hecho tiene consecuencias legales y de seguridad. Por eso el producto es **borrador + ingeniero firma**. Nunca emisión automática. Posiciónalo siempre como copiloto del ingeniero.
- **Alucinación en contenido crítico de seguridad:** mitigar anclando estrictamente a las normas reales y a los expedientes de Cosigein; el agente cita la cláusula; el humano revisa. Si no está seguro, lo marca, no se lo inventa.
- **Confidencialidad / IP:** los expedientes (y sobre todo lo de defensa) son sensibles. Mantener en entorno privado/local, no subir a herramientas públicas sin permiso. Esto es condición, no opción.
- **Tu posición:** si construyes algo valioso para Cosigein siendo empleado, **acuerda por escrito qué es tuyo y qué es de la empresa antes de que valga dinero.** No lo dejes para después.

---

## 10. Veredicto

Olvida las clínicas. Tu mejor jugada está donde ya estás. Tienes acceso a un negocio técnico, regulado, intensivo en documentación, con un archivo de 20 años de experiencia, y una ola regulatoria con fecha (enero 2027) que obliga a todo el mercado europeo a re-documentar. La herramienta para surfear esa ola no existe aún como producto.

**Construye el agente de cumplimiento de máquinas. Empieza por el análisis de riesgos de una familia. Usa el archivo de Cosigein como foso. Demuéstralo con un borrador real contra el trabajo de un ingeniero. Y aprovecha el 2027.**

Eso no es una base de conocimiento más. Es un agente vertical en un nicho que los vende-humos ni saben que existe.

---

## Fuentes
- Reglamento (UE) 2023/1230 — aplicación 20/01/2027: Ministerio de Industria, TÜV SÜD, Pilz, Iberley.
- Cosigein / CSG Ingeniería: csgingenieria.es, SmartCityCluster, DatosCif, LinkedIn.
- Mercado de agentes verticales 2026: GeekWire, 8seneca, Sinequa, TechTarget.
