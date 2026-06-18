# DEFINICIÓN PROFESIONAL DEL PRODUCTO — "PersonaTécnica"

> Documento de especificación, no de motivación.
> No diagnostica. No adula. No vende humo.
> Si algo está mal planteado, aquí se dice sin suavizar.
>
> Autor del encargo: Antonio Hermoso González · Fecha: 2026-06-16

---

## 0. VEREDICTO RÁPIDO (lo que decido, arriba del todo)

| Decisión | Recomendación |
|---|---|
| **Nombre del producto** | **NO "PersonaTécnica".** Marca madre: **Manual** (o *Manual de Usuario*). Producto: **Manual — tu manual de usuario**. |
| **Categoría** | **Identity Intelligence** (inteligencia de identidad asistida por IA). Subcategoría operativa: *self-mapping*. |
| **Producto principal** | Un sistema que ingiere tu material real (textos, audios, imágenes, proyectos) y genera un **manual de usuario personal**: cómo funcionas, qué se te repite, qué entornos te encajan, qué futuros son compatibles. |
| **MVP** | Servicio *concierge* (humano + IA) que entrega 1 informe premium por encargo. Sin app. 30 días. |
| **Usuario inicial (ICP)** | Adultos 28–45, multipotenciales / técnicos-creativos en crisis vocacional o de identidad, sospecha de mente no normativa, usuarios avanzados de IA, con renta disponible. |
| **Precio inicial (piloto)** | 290–490 € por informe individual (concierge). Objetivo: validar disposición a pagar, no margen. |
| **Stack** | Next.js + FastAPI (Python) + PostgreSQL/pgvector + Redis + almacenamiento S3-compat + workers + orquestación LLM propia (no framework pesado). Claude como modelo de razonamiento principal. |
| **Primer entregable** | El informe "Este es Antonio Hermoso González" como **caso 0**, hecho a mano con el pipeline asistido. Es producto y es marketing. |
| **Frase madre** | *"Descubre cómo funcionas antes de decidir quién deberías ser."* |
| **Primer vídeo** | La IA presenta a Antonio y muestra su manual en pantalla. Antonio no aparece. |
| **Hoja de ruta** | 90 días: caso 0 → 10 informes de pago concierge → semiautomatización del pipeline → web de captación + lista de espera. |

El resto del documento justifica, especifica y desarrolla cada una de estas decisiones.

---

## 1. EVALUACIÓN DEL NOMBRE Y ARQUITECTURA DE NAMING

### 1.1 ¿Es bueno "PersonaTécnica"?

No. Y lo digo sin suavizarlo porque pediste decisión, no validación.

**Problemas concretos:**

1. **Reduce el proyecto justo a lo que NO quieres que se reduzca.** "Técnica" empuja todo hacia lo frío, lo informático, lo de RRHH. El proyecto trata de identidad, mirada, pasiones, futuros — la parte humana es el 50%. El nombre amputa esa mitad.
2. **Colisión semántica con "ficha técnica" / "persona" de marketing.** En producto digital, *"persona"* ya significa "arquetipo de usuario ficticio". Vas a competir contra un significado preexistente y perder.
3. **Suena a herramienta de empresa, no a experiencia personal.** Nadie dice "voy a usar mi PersonaTécnica" con cariño. No es abrazable. Una marca de identidad necesita calidez.
4. **CamelCase pegado ("PersonaTécnica") es frágil:** mala URL, mala pronunciación, mala memorabilidad, tilde problemática en dominios.
5. **No describe la promesa.** No dice qué recibes. "Manual de usuario" sí lo dice en tres palabras.

**Lo único bueno que tiene:** la tensión "persona + técnica" captura tu dualidad (humano/sistémico). Esa tensión es valiosa como *concepto interno*, no como *marca externa*.

**Veredicto:** descartar como nombre de producto de cara al cliente. Conservar "Persona Técnica" como nombre del **motor de perfilado interno** (el componente que produce el retrato funcional), nunca como la marca que ve el usuario.

### 1.2 El nombre que sí funciona

De tu lista, el ganador es claro: **"Manual de Usuario"**.

Razones:
- Es la promesa literal. *"Sube tu vida, recibe tu manual de usuario."* La marca = la promesa.
- Tiene calidez técnica: usa lenguaje de ingeniería ("manual de usuario") aplicado a una persona. Eso *es* tu dualidad, sin amputarla.
- Es memorable, traducible, contable ("me hicieron mi manual de usuario").
- Genera deseo: todo el mundo querría tener el manual de instrucciones de sí mismo.

Marca corta de producto: **Manual**. Marca completa / tagline-marca: **Manual de Usuario**.

### 1.3 Arquitectura de naming completa (recomendada)

| Nivel | Nombre | Función |
|---|---|---|
| **Marca madre / empresa** | **Manual** | Casa de marca. "Manual Labs" o "Manual.io" para el dominio corporativo. |
| **Producto principal** | **Manual de Usuario** | La experiencia que genera tu manual personal. |
| **Motor de identidad (interno)** | **Persona Técnica** | El engine de perfilado funcional. Aparece en docs técnicas, no en la UI del usuario. |
| **Módulo de observación** | **Aprendiendo a Observar** (público) / *Lente* (corto) | El CRM de la mirada. |
| **Módulo de las 50 perspectivas** | **El Consejo** (mejor que "El Juicio de las 50 Miradas") | 50 perfiles analizan tu caso. "Juicio" suena a tribunal/condena; "Consejo" suena a deliberación. Mantén "50 Miradas" como descriptor poético, no como nombre técnico. |
| **El informe / entregable** | **Tu Manual** | El PDF/documento vivo. |
| **Categoría de mercado** | **Identity Intelligence** | Cómo lo posicionas en el discurso de inversores/prensa. |
| **Tagline** | *"Descubre cómo funcionas antes de decidir quién deberías ser."* | Promesa emocional + diferenciación (funcionamiento ≠ identidad fija). |

> Nota sobre "Context OS": en este repositorio "Context OS" es tu **método interno** de trabajo, no un nombre de producto. No lo conviertas en marca de cara al cliente. Sirve como filosofía operativa de la empresa ("trabajamos por contexto, no por formularios"), igual que "Persona Técnica" sirve de motor interno.

**Decisión de naming:** *Manual de Usuario* como producto, *Manual* como marca madre, *El Consejo* / *Aprendiendo a Observar* como módulos, *Persona Técnica* como motor interno. "PersonaTécnica" muere como nombre comercial hoy.

---

## 2. CATEGORÍA DE MERCADO

### 2.1 Lo que NO es

No es "app de autoconocimiento" (categoría muerta, saturada de tests baratos), no es journaling, no es terapia, no es productividad, no es orientación vocacional clásica.

### 2.2 La categoría que reclamo: **Identity Intelligence**

Definición operativa propia:

> **Identity Intelligence:** sistema que convierte el rastro real de una persona (lo que escribe, dice, mira, crea y repite) en un modelo explicable de cómo funciona, para tomar mejores decisiones sobre entorno, trabajo y futuro — sin diagnosticar y sin reducir a etiquetas.

Por qué esta categoría y no las alternativas que propusiste:

- **"Personal Operating System"** — buena metáfora, pero ya muy usada por apps de productividad (Notion, etc.). Confunde con gestión de tareas.
- **"Personal analytics / Quantified Self"** — implica métricas y wearables. Tú trabajas con material cualitativo, narrativo, estético. No encaja.
- **"Personal knowledge graph"** — es una *técnica interna* tuya (sí, lo usarás), no una categoría que el mercado entienda.
- **"AI-assisted self-mapping"** — es el *mecanismo*, buen subtítulo, pero poco potente como categoría de prensa/inversión.

**"Identity Intelligence"** gana porque: (a) es nueva (puedes liderarla), (b) suena seria y defendible ante inversores, (c) abarca tanto la parte humana como la sistémica, (d) la palabra "Intelligence" señala IA sin reducirse a ella, (e) "Identity" recoge mirada + pasiones + futuro sin caer en "personalidad" (tests) ni "salud" (clínica).

Posicionamiento de una línea: **"Manual — Identity Intelligence. Tu manual de usuario, generado a partir de tu vida real."**

---

## 3. ANÁLISIS DE MERCADO

Tabla de adyacencias. Para cada categoría: qué hacen, por qué están cerca, por qué no es lo mismo, cómo nos diferenciamos.

| Categoría | Qué hacen | Por qué están cerca | Por qué NO es lo mismo | Diferenciación nuestra |
|---|---|---|---|---|
| **Journaling con IA** (Day One, Rosebud, Mindsera) | Diario + reflexiones generadas | Usan texto personal + IA | Son reactivos, día a día; no construyen un modelo global de la persona | Nosotros sintetizamos un **manual estructural**, no entradas sueltas |
| **Mood tracking** (Daylio) | Registran estado de ánimo | Datos personales longitudinales | Métricas emocionales, no identidad ni futuro | Trabajamos significado y patrón, no humor diario |
| **Terapia digital** (BetterHelp, Wysa) | Conectan con terapeutas / chatbot clínico | Tocan lo emocional profundo | Es salud mental regulada; nosotros NO | Explícitamente no-clínico; aliados, no sustitutos |
| **Coaching** (CoachHub, BetterUp) | Coach humano + plan | Apuntan a desarrollo personal | Caro, lento, depende del coach | Entregamos un artefacto reutilizable (el manual) en días |
| **Tests de personalidad** (16Personalities, CliftonStrengths) | Cuestionario → tipo/etiqueta | Prometen "saber cómo eres" | Auto-reporte, etiquetas fijas, cero evidencia real | Usamos tu **material real**, con trazabilidad de evidencias |
| **Orientación vocacional** (career tests) | Sugieren profesiones | Proponen futuros | Anticuada, basada en encuestas | "Futuros compatibles" con evidencia y prueba de 7 días |
| **Personal CRM** (Clay, Dex) | Gestionan tu red de contactos | Idea de "CRM personal" | Gestionan *a otros*, no a ti | Nuestro "CRM de la mirada" te observa **a ti** |
| **Second brain** (Notion, Obsidian, Mem) | Almacén de notas/conocimiento | Acumulan tu material | Guardan, no interpretan identidad | Nosotros interpretamos quién eres a partir del archivo |
| **Quantified Self** (Oura, Whoop) | Métricas biológicas | Datos personales | Cuerpo/fisiología, no mente/identidad | Cualitativo, estético, narrativo |
| **Memoria personal con IA** (Rewind/Limitless, Personal.ai) | Graban todo, recuperan | Modelo de "tú" a partir de datos | Recuperación/búsqueda, no síntesis de identidad | Producimos un retrato, no un buscador |
| **Productivity AI** (Reclaim, Motion) | Optimizan tiempo/tareas | "Trabajar mejor" | No tocan identidad | No optimizamos la agenda; revelamos el funcionamiento |
| **Career guidance AI** (LinkedIn, Sonara) | Match empleo/skills | Futuros profesionales | Centrado en empleabilidad/CV | Integramos lo creativo + lo humano + lo técnico |

**Lectura del mercado:** no hay un líder claro en "Identity Intelligence". Hay mucho ruido alrededor (journaling con IA está caliente, memoria personal con IA está emergiendo con dinero detrás). El hueco real: **síntesis estructural explicable de identidad funcional a partir de material real y multimodal, con disciplina ética anti-diagnóstico**. Nadie posee ese cruce hoy. Riesgo: Big Tech (memoria personal con IA) podría rozarlo; nuestra defensa es el método, la curación humana y el posicionamiento de marca, no la tecnología base.

---

## 4. USUARIO IDEAL

### 4.1 Segmentos candidatos (priorizados)

| Segmento | Tracción | ¿Paga? | Notas |
|---|---|---|---|
| Multipotenciales / técnicos-creativos en crisis vocacional | Alta | Sí | **ICP inicial.** Sienten que "no encajan en una sola caja". |
| Usuarios avanzados de IA (early adopters) | Alta | Sí | Entienden el valor, perdonan la falta de pulido |
| Sospecha de mente no normativa (TDAH/AuDHD/altas capacidades) | Alta | Sí | Sensibles; máximo cuidado ético, gran motivación |
| Creativos / artistas / fotógrafos | Media | A veces | Resuenan con "Aprendiendo a Observar" |
| Profesionales con burnout | Media | Sí | Riesgo de esperar terapia; encuadrar bien |
| Personas en transición de carrera | Media | Sí | Buen ángulo "futuros compatibles" |
| Curiosos de autoconocimiento sin terapia | Baja-media | Poco | Volumen, baja disposición a pagar |

### 4.2 ICP inicial (a quién perseguir el día 1)

**Adulto 28–45, perfil multipotencial técnico-creativo, alta intensidad cognitiva, en un punto de inflexión vital o profesional, usuario fluido de IA, con renta disponible (≥ informe de 300 €) y vocabulario para hablar de sí mismo.** Es decir: gente como tú, Antonio. Tu caso 0 *es* el ICP.

### 4.3 Quién paga vs. quién no

- **Pagan:** los que viven el "no encajo en una caja" como dolor activo y tienen dinero. Pagan por *claridad* y por *legitimación* de su complejidad.
- **No conviene atender (de momento):**
  - **Menores.** Fuera del MVP. Riesgo legal y ético desproporcionado.
  - **Personas en crisis de salud mental aguda.** No somos terapia. Derivar.
  - **Quien busca un diagnóstico.** Hay que reencuadrar o rechazar: no diagnosticamos.
  - **Empresas que quieran cribar/seleccionar empleados con esto.** Riesgo regulatorio y ético grave (ver §11). Rechazar este uso explícitamente.

### 4.4 B2C / B2B / aliados

- **B2C (núcleo):** individuos. Es donde empieza y donde está el alma.
- **Creadores:** versión "creator" para construir marca personal a partir del manual.
- **B2B (futuro, con cuidado):** coaches, consultores de carrera, escuelas de negocio — como *herramienta para sus clientes*, jamás para vigilar empleados.
- **Universidades:** orientación y autoconocimiento de estudiantes adultos (no menores).
- **Clínicas/psicólogos:** **aliados, nunca sustituidos.** El manual puede ser material de partida que el paciente lleva a su profesional. Posible canal de derivación bidireccional.

---

## 5. EL PRODUCTO COMPLETO

Flujo de extremo a extremo.

1. **Onboarding y consentimiento.** Explicación honesta de qué es y qué NO es (no diagnóstico). Consentimiento granular: qué datos, para qué, cuánto tiempo, derecho a borrar. Define objetivo ("entender mi funcionamiento", "explorar futuros", "decidir un cambio").
2. **Captación de contexto.** Entrevista conversacional guiada por IA (no formulario). Preguntas adaptativas. Captura frases núcleo, recuerdos, obsesiones, hiperfocos, bloqueos.
3. **Carga de material.** Textos, notas, diarios, CV, conversaciones, proyectos; audios; fotos/vídeos; enlaces. Etiquetado de origen y de sensibilidad.
4. **Transcripción.** Audios/vídeos → texto con marcas de tiempo y hablante.
5. **Análisis de imagen.** Descripción, temas, estética, patrones visuales (qué se repite en lo que miras/guardas).
6. **Aprendiendo a Observar (CRM de la mirada).** El usuario añade imágenes/referencias que le atraen; la IA pregunta (¿qué te detuvo?, ¿qué emoción?, ¿qué parte de ti mira esto?) y acumula un *corpus de mirada*.
7. **Grafo de identidad.** Todo el material se conecta: señales → evidencias → patrones → hipótesis → pasiones → futuros. Es el cerebro del sistema.
8. **El Consejo (50 perspectivas).** 50 perfiles analizan el caso; cada uno aporta patrón, riesgo, punto ciego, pregunta, futuro propuesto y prueba de 7 días.
9. **Matriz de consenso.** Cruza las 50 miradas: señales fuertes/débiles, contradicciones, hipótesis nuevas, caminos descartados, finalistas, riesgos críticos, próximos pasos. **Aquí está el valor**, no en las opiniones sueltas.
10. **Futuros compatibles.** Top 10 → top 3, cada uno con evidencia, encaje, riesgo y un experimento de 7 días.
11. **Generación del manual / informe.** Versión corta/media/extrema (§10).
12. **Planes de acción.** Plan de 30 días + experimentos semanales.
13. **Seguimiento semanal.** Check-ins; el manual evoluciona con nueva evidencia (manual *vivo*, versionado).
14. **Exportación.** PDF cuidado; opción de versión pública/anonimizada.
15. **Privacidad y control.** Ver todo lo que el sistema sabe, por qué lo afirma (trazabilidad), editar, exportar, **borrar todo** (borrado real).

---

## 6. EL MVP (30 DÍAS, REALISTA)

**Filosofía: vende el resultado a mano antes de construir la máquina.** El MVP NO es una app. Es un **servicio concierge**.

### 6.1 Qué se construye en 30 días
- Una **landing** con la promesa, el caso 0 (tu manual) como prueba, y una lista de espera / botón de compra (Stripe + Typeform/Tally).
- Un **pipeline asistido interno** (no producto): carpeta de ingesta → scripts de transcripción/visión → un conjunto de *prompts maestros* (entrevista, 50 miradas, matriz de consenso, manual) ejecutados con Claude → plantilla de informe en PDF.
- Una **plantilla de informe** reutilizable y bonita.

### 6.2 Qué se valida sin código
- ¿La gente paga 300–500 € por un manual de usuario personal? (la única pregunta que importa)
- ¿El informe les parece *certero y útil*, no genérico? (NPS cualitativo, "¿pagarías de nuevo / lo recomendarías?")
- ¿Qué material aportan de forma natural y cuál les da reparo?

### 6.3 Qué vender manualmente
Informes individuales concierge. Tú (o un operador) conduces la entrevista, ejecutas el pipeline asistido, revisas a mano, entregas el PDF + una sesión de 45 min de devolución.

### 6.4 Qué automatizar primero (tras validar)
1. Transcripción e ingesta. 2. La entrevista conversacional. 3. La generación de las 50 miradas + matriz. La redacción final del manual se automatiza la última (es donde más se nota la mano humana).

### 6.5 Qué NO construir todavía
App móvil, login social, grafo en tiempo real, seguimiento semanal automatizado, módulo creator, B2B, marketplace de expertos, multi-idioma. Todo eso es post-validación.

### 6.6 Métricas e hipótesis

| Hipótesis | Métrica | Umbral de éxito |
|---|---|---|
| Hay disposición a pagar | Conversión visita→compra | ≥ 5 ventas reales en 30 días |
| El informe es valioso | "¿Recomendarías / repetirías?" | ≥ 70% sí |
| El informe es certero | "¿Te has sentido visto sin sentirte etiquetado?" | ≥ 8/10 medio |
| Es entregable con esfuerzo razonable | Horas/informe | ≤ 6 h al final del mes |

### 6.7 Precio piloto
**290–490 €** por informe (early-bird 290 €, completo 490 €). Sube el precio cada 3 ventas para encontrar el techo.

### 6.8 Primeros 10 usuarios
1. Tu red directa (técnicos/creativos que se sienten "raros"). 2. El vídeo de la IA presentándote (caso 0) en LinkedIn/IG. 3. Comunidades de neurodivergencia adulta, multipotenciales, IA. 4. Ofrecer 3 informes gratis a cambio de testimonio en vídeo (combustible de marketing).

---

## 7. ARQUITECTURA TÉCNICA

**Principio:** monolito modular pragmático, no microservicios. Toda la complejidad real está en el pipeline de IA, no en la infra.

### 7.1 Stack recomendado (decidido)

| Capa | Elección | Por qué |
|---|---|---|
| Frontend | **Next.js (React) + TypeScript + Tailwind** | SSR, buen DX, rápido para landing y app |
| Backend | **FastAPI (Python)** | El ecosistema de IA/ML/ingesta vive en Python |
| Cola/workers | **Celery o RQ + Redis** (o Dramatiq) | El análisis es asíncrono y largo |
| Base de datos | **PostgreSQL** | Relacional sólida, transaccional |
| Vectores | **pgvector** (en el mismo Postgres) | No metas otra DB hasta necesitarla |
| Cache/colas | **Redis** | Cola, locks, cache |
| Almacenamiento | **S3-compatible** (AWS S3 / Cloudflare R2 / MinIO) | Archivos del usuario; R2 = sin coste de egreso |
| Grafo | **Postgres (tablas de aristas) al principio; Neo4j sólo si el grafo se vuelve central** | Evita complejidad prematura |
| Modelo LLM | **Claude (Opus para razonamiento profundo: 50 miradas, matriz, manual; Haiku/Sonnet para tareas baratas: clasificación, extracción)** | Mejor razonamiento largo y matizado; arquitectura multi-tier por coste |
| Transcripción | **Whisper (self-host) o API de speech-to-text** | Audio→texto |
| Visión | **Modelo multimodal (Claude visión / equivalente)** | Descripción y temas de imágenes |
| Orquestación IA | **Capa propia ligera** (state machine + cola), no LangChain pesado | Control, trazabilidad, menos magia |
| PDF | **render desde HTML (Playwright / WeasyPrint)** | Informes con diseño |
| Observabilidad | **OpenTelemetry + Sentry + logs estructurados; tracing de prompts (Langfuse/Helicone)** | Hay que saber por qué la IA dijo X |
| Cifrado | **TLS en tránsito; cifrado en reposo (DB + S3); secrets gestionados** | Datos sensibles |
| Backups | **Backups cifrados de Postgres + versionado de S3** | Recuperación |
| Hosting | **Contenedores (Fly.io/Render al inicio; cloud mayor al escalar)** | Sencillez primero |

### 7.2 Pipeline de ingesta (flujo)

`Upload → almacenar en S3 + registrar Attachment → encolar job → detectar tipo → (texto: extraer | audio/vídeo: transcribir | imagen: describir) → trocear (chunk) → embeddings → guardar en pgvector → extraer señales → enlazar al grafo de identidad → marcar listo`

### 7.3 Costes (orden de magnitud)
El coste dominante es el LLM, no la infra. Un informe extremo con 50 perspectivas + matriz + síntesis puede costar **2–8 € en tokens** según modelo y longitud. Mitigaciones: modelo barato para extracción/clasificación, modelo caro sólo para razonamiento/síntesis; cache de prompts; reutilizar análisis intermedios. Infra base: decenas de €/mes hasta tener tracción.

### 7.4 Escalabilidad
El cuello de botella es coste/latencia de LLM y revisión humana, no CPU. Escala = más workers + colas con prioridad + degradación elegante (informe corto rápido, extremo en cola). No optimices para millones de usuarios antes de tener diez.

---

## 8. MODELO DE DATOS

Entidades principales, relaciones y campos clave.

```
User ──1:1── Profile
User ──1:N── Consent
User ──1:N── MemoryItem
User ──1:N── Observation
User ──1:N── Project
User ──1:N── Report
User ──1:N── AuditLog

MemoryItem ──1:N── Attachment
Attachment ──1:1── Transcript        (si es audio/vídeo)
MemoryItem/Observation ──N:M── Evidence
Evidence ──N:M── Pattern
Pattern ──N:M── Hypothesis
Pattern/Hypothesis ──N:M── Passion
Hypothesis ──N:M── FuturePath
Report ──1:N── ReportSection
Report ──1:N── JudgeAnalysis
JudgePersona ──1:N── JudgeAnalysis
Report ──1:1── ConsensusMatrix
FuturePath ──1:N── ActionPlan
```

| Entidad | Campos clave |
|---|---|
| **User** | id, email, estado, creado_en, locale |
| **Profile** | user_id, nombre, objetivo, frase_núcleo, resumen_vivo, versión |
| **MemoryItem** | id, user_id, tipo(texto/nota/diario/cv/convo), contenido, origen, sensibilidad, creado_en |
| **Observation** | id, user_id, attachment_id, qué_vio, emoción, patrón_percibido, "qué parte de mí mira esto", etiquetas |
| **Attachment** | id, memory_item_id, s3_key, mime, tamaño, hash, estado_proceso |
| **Transcript** | id, attachment_id, texto, segmentos[ts,hablante], idioma |
| **Project** | id, user_id, nombre, rol, periodo, descripción, energía(+/−) |
| **Passion** | id, user_id, nombre, visible/oculta, intensidad, evidencias[] |
| **Pattern** | id, user_id, descripción, fuerza(débil/fuerte), evidencias[] |
| **Hypothesis** | id, user_id, texto, tipo(no_clínica), confianza, evidencias[], **contraevidencia[]**, estado |
| **Evidence** | id, fuente_ref(memory/observation/transcript), cita, peso |
| **JudgePersona** | id, nombre, rol, lente, prompt_base |
| **JudgeAnalysis** | id, report_id, judge_id, patrón, riesgo, punto_ciego, pregunta, futuro, prueba_7d |
| **ConsensusMatrix** | id, report_id, señales_fuertes[], señales_débiles[], contradicciones[], hipótesis_nuevas[], descartados[], finalistas[], riesgos_críticos[] |
| **FuturePath** | id, user_id, título, encaje, evidencias[], riesgo, experimento_7d, ranking |
| **ActionPlan** | id, future_path_id, horizonte(30d), pasos[], experimentos[] |
| **Report** | id, user_id, versión, longitud(corta/media/extrema), estado, pdf_s3_key, disclaimer_versión |
| **ReportSection** | id, report_id, clave, título, contenido, nivel_evidencia |
| **Consent** | id, user_id, alcance, propósito, otorgado_en, revocado_en, retención |
| **AuditLog** | id, user_id, actor, acción, recurso, timestamp, metadatos |

**Campos transversales de gobernanza:** todo registro derivado guarda `evidencias[]` y `confianza`. Sin evidencia trazable, una afirmación no entra en el manual. Es la columna vertebral ética y de calidad.

---

## 9. ARQUITECTURA IA

Pipeline por capas. Cada capa produce artefactos trazables.

1. **Ingesta y normalización.** Extraer texto, transcribir, describir imágenes; trocear; normalizar a un formato común con metadatos de origen y sensibilidad.
2. **Extracción de señales.** Pasada barata (modelo pequeño) sobre cada fragmento: temas, emociones, intereses, tensiones, repeticiones, energía. Cada señal apunta a su fragmento de origen (evidencia).
3. **Clasificación y agregación.** Agrupar señales en candidatos a *patrón* y *pasión* (visible/oculta). Calcular fuerza por frecuencia + diversidad de fuentes + intensidad.
4. **Generación de hipótesis (no clínicas).** Modelo de razonamiento propone hipótesis de funcionamiento ("tiende al hiperfoco en X bajo condición Y"). **Obligatorio:** cada hipótesis lleva evidencia *y* contraevidencia, y una etiqueta explícita "hipótesis a explorar, no conclusión".
5. **Scoring de compatibilidad (no clínico).** Puntuar encaje entornos/futuros vs. patrones. Nunca puntuar "trastornos". El scoring mide *compatibilidad*, no *normalidad*.
6. **El Consejo (50 perspectivas).** Cada `JudgePersona` recibe un resumen estructurado del caso (no el dato crudo sensible completo) y produce su `JudgeAnalysis` con formato fijo (patrón/riesgo/punto ciego/pregunta/futuro/prueba 7d). Se ejecuta en paralelo por lotes para controlar coste/latencia.
7. **Matriz de consenso.** Una pasada de razonamiento cruza las 50 salidas: detecta repeticiones (señal fuerte), divergencias (contradicción), aportaciones únicas (hipótesis nueva), y consolida finalistas/descartados/riesgos. **Este es el cerebro del producto.**
8. **Generación del manual.** Redacta el informe desde patrones+hipótesis+matriz+futuros, citando evidencia. Tono y longitud según versión.
9. **Revisión de riesgos (guardrails).** Pasada final que: comprueba que no hay lenguaje diagnóstico, que toda afirmación fuerte tiene evidencia, que aparecen disclaimers, y que se detectan señales de crisis.
10. **Detección de crisis y derivación.** Clasificador que busca señales de riesgo grave (ideación, abuso, crisis aguda). Si aparece: el sistema NO interpreta ni "trata"; muestra recursos de ayuda profesional y de emergencia, y suaviza/pausa la generación. Documentado y auditado.
11. **Trazabilidad.** Toda afirmación del manual enlaza a sus evidencias y a la cadena de capas que la produjo ("por qué afirmo esto"). Es requisito de producto, no opcional.

**Guardrails permanentes (no negociables):**
- Prohibido afirmar diagnósticos ("tienes TDAH"). Permitido: "señales compatibles con X, a explorar con un profesional".
- Toda hipótesis fuerte exige contraevidencia visible.
- Nada de afirmaciones sobre terceros que aparezcan en el material como si fueran hechos.
- Crisis → recursos + freno, nunca consejo clínico.

---

## 10. EL INFORME

### 10.1 Índice maestro (versión extrema)
1. Resumen ejecutivo
2. Tesis central (una frase + un párrafo)
3. Patrón raíz
4. Mapa cognitivo (cómo piensas/aprendes/trabajas)
5. Hipótesis no clínicas (con evidencia y contraevidencia)
6. Pasiones visibles
7. Pasiones ocultas
8. Manual de usuario (instrucciones de uso de ti mismo: condiciones óptimas, antipatrones, cómo te "rompes", cómo te recuperas)
9. Riesgos
10. El Consejo — las 50 miradas (resumen por lente)
11. Matriz de consenso
12. Top 10 futuros compatibles
13. Top 3 finalistas (con experimento de 7 días cada uno)
14. Plan de 30 días
15. Preguntas para llevar a un profesional
16. Frase núcleo
17. Anexos: evidencias y trazabilidad
18. Disclaimer

### 10.2 Tres longitudes
- **Corta (≈10 pág.):** secciones 1, 2, 3, 8, 13, 14, 16, 18. Para decidir rápido.
- **Media (≈50 pág.):** todo menos el detalle exhaustivo de las 50 miradas y anexos largos.
- **Extrema (≈100+ pág.):** todo, con cada mirada desarrollada y anexo de evidencias completo.

### 10.3 Tono, evidencia, formato
- **Tono:** preciso, cálido, adulto. Ni horóscopo ni informe clínico. Habla "de tú".
- **Nivel de evidencia:** cada afirmación fuerte marca su nivel (observado / inferido / hipótesis). Sin evidencia, no se afirma.
- **Disclaimer (siempre, primera y última página):** *"Este documento no es un diagnóstico ni una evaluación clínica. Describe hipótesis de funcionamiento a partir del material que aportaste, para tu reflexión y para conversaciones con profesionales cualificados."*
- **Formato:** PDF diseñado (tipografía cuidada, jerarquía, citas de evidencia al margen). El diseño *es* parte del valor percibido.

---

## 11. MARCO ÉTICO Y LEGAL

Esto no es un anexo: es condición de existencia del producto.

| Tema | Postura / medida |
|---|---|
| **No-diagnóstico** | Núcleo. Nunca afirmar trastornos. Solo hipótesis a explorar. Guardrail técnico + revisión. |
| **Datos sensibles (GDPR art. 9)** | El material revela datos de salud, ideología, vida sexual, etc. Tratamiento basado en **consentimiento explícito, granular y revocable**. Minimización: pedir solo lo necesario. |
| **Salud mental / crisis** | Detección + derivación a recursos profesionales. No somos terapia y se dice claramente. |
| **Neurodivergencia** | Lenguaje afirmativo, no patologizante. "Mente no normativa", "funcionamiento", no "déficit". |
| **Consentimiento** | Capa de UI dedicada; registro `Consent` por propósito; renovable y revocable. |
| **Derecho al borrado** | Borrado real (DB + S3 + embeddings + backups en plazo). Botón visible. |
| **Datos de terceros** | El material menciona a otras personas. No se generan perfiles de terceros; se anonimiza su mención; se advierte al usuario de su responsabilidad. |
| **Uso de fotos** | Consentimiento específico; no entrenamiento con ellas; borrado garantizado; no reconocimiento facial de terceros. |
| **Menores** | **Fuera del alcance.** Verificación de edad adulta. |
| **Dependencia emocional** | Diseño anti-adicción: el producto entrega y se aparta; nada de engagement infinito ni gamificación de la introspección. |
| **Sesgos** | Las 50 lentes y la contraevidencia obligatoria mitigan sesgo único; auditar salidas; diversidad real de perspectivas. |
| **Transparencia y explicabilidad** | Trazabilidad de toda afirmación ("por qué digo esto"). |
| **GDPR** | Base legal clara, registro de tratamientos, DPA con proveedores, residencia de datos UE preferente, política de retención, derechos ARCO-POL. |
| **Riesgo regulatorio alto** | Si esto se usara en **empleo, educación reglada o salud**, entraría en zona de IA de alto riesgo (marco europeo de IA) y normativa sectorial. **Decisión: prohibir contractualmente el uso para selección/cribado de personas.** Es B2C de autoconocimiento, no una herramienta de evaluación de terceros. |

---

## 12. MODELO DE NEGOCIO

### 12.1 Líneas de ingreso (por fases)

| Línea | Qué es | Fase |
|---|---|---|
| **Informe premium concierge** | 1 manual hecho con curación humana + IA | **Ahora (MVP)** |
| **Informe individual self-serve** | El usuario lo genera en la app | Tras automatizar |
| **Suscripción** | Manual *vivo*: seguimiento, re-análisis, evolución mensual | Fase 2 |
| **Versión Creator** | Convierte tu manual en marca personal/contenido | Fase 2-3 |
| **Versión Pro / aliados** | Para coaches/consultores con sus clientes | Fase 3 |
| **B2B (con guardarraíles)** | Escuelas de negocio, universidades (adultos) | Fase 3+ |
| **Marketplace de expertos** | Conecta usuarios con profesionales para profundizar | Fase 4 |
| **Upsells** | Sesión de devolución, versión extrema, re-análisis | Desde MVP |

### 12.2 Pricing
- **Inicial (concierge):** 290–490 €/informe + 90 € sesión de devolución.
- **Futuro (self-serve):** informe 49–149 € según longitud; **suscripción 12–25 €/mes** (manual vivo); Pro 99–299 €/mes.
- **Márgenes:** self-serve con coste LLM de 2–8 €/informe → margen bruto >90% en software; concierge limitado por horas humanas (por eso urge automatizar tras validar).

### 12.3 Estrategia de validación
Vender concierge caro primero (valida valor y disposición a pagar con poquísimo desarrollo), luego bajar precio y subir volumen al automatizar. Nunca al revés.

---

## 13. EL PRIMER VÍDEO

**Premisa:** Antonio no aparece. La IA presenta a Antonio, el proyecto y el manual. Esto *es* la demostración del producto (la IA habla de una persona a partir de su material) y resuelve tu posible reticencia a exponerte.

- **Título:** *"Le pedí a una IA que escribiera mi manual de usuario. Esto es lo que vio."*
- **Duración:** 90–120 s.
- **Estructura (guion):**
  1. **Hook (0–8s):** voz IA, pantalla negra: *"Me han dado la vida de un hombre llamado Antonio. Textos, fotos, proyectos, frases. Y una pregunta: ¿cómo funciona?"*
  2. **Tensión (8–25s):** *"Antonio es informático. Y también fotógrafo. Construye sistemas y persigue la belleza. Lleva años intentando caber en una sola caja. No cabe. No porque le pase algo: porque es varias cosas a la vez."*
  3. **Qué hice (25–55s):** mostrar en pantalla el manual pasando páginas: patrón raíz, pasiones ocultas, las 50 miradas, la matriz, los futuros. *"No le hice un test. Leí su rastro. Y escribí cómo funciona."*
  4. **Aclaración ética (55–70s):** texto en pantalla + voz: *"Esto no es un diagnóstico. No digo lo que Antonio es. Describo cómo parece funcionar, con la evidencia delante."*
  5. **Promesa (70–95s):** *"Esto se llama Manual de Usuario. Tú también tienes uno. Solo que nadie lo ha escrito todavía."*
  6. **CTA (95–110s):** *"Sube tu vida. Recibe tu manual."* + enlace/lista de espera.
- **Tono visual:** sobrio, cinematográfico, mucho negro, tipografía elegante, el PDF como protagonista visual (scroll lento, zoom a frases). Cero stock cursi.
- **Voz en off:** voz IA serena, no robótica de parodia; calidez técnica.
- **Cómo mostrar el PDF:** capturas reales del informe (anonimiza lo íntimo), animación de páginas, resaltado de la "frase núcleo".
- **CTA:** lista de espera + 3 plazas de informe gratis a cambio de testimonio.

---

## 14. PITCH

- **1 frase:** *"Manual de Usuario convierte tu vida real en el manual de instrucciones de ti mismo."*
- **30 s:** *"La gente se conoce con tests de 16 preguntas o tras años de terapia. Manual de Usuario hace algo distinto: ingiere tu material real —lo que escribes, dices, miras y creas— y genera un manual de cómo funcionas: tus patrones, tus pasiones ocultas, los entornos que te encajan y los futuros compatibles. No te diagnostica. Te da el mapa para decidir."*
- **2 min:** *(30s) + categoría:* "Es una categoría nueva: Identity Intelligence. *(diferenciación)* No es journaling, no es terapia, no es un test. *(cómo)* Subes textos, audios, fotos, proyectos; nuestra IA construye un grafo de tu identidad, lo somete a un consejo de 50 perspectivas distintas, destila el consenso y escribe tu manual con la evidencia delante. *(ética)* Sin diagnóstico, con trazabilidad y borrado real. *(negocio)* Empezamos con informes premium hechos a mano a 300–500 €, validamos, y automatizamos hacia suscripción. *(por qué ahora)* La IA por fin razona sobre material cualitativo multimodal; antes esto era imposible."*
- **Inversor:** *"Categoría sin líder (Identity Intelligence), margen software >90%, ola de IA multimodal que lo hace posible justo ahora, foso = método + marca + disciplina ética. Validamos disposición a pagar con servicio concierge antes de gastar en producto. Riesgo gestionado: no tocamos empleo/salud regulados."*
- **Usuario:** *"¿Sientes que no cabes en una sola caja? No te falta nada. Te falta el manual. Te lo escribimos a partir de tu propia vida."*
- **Psicólogo/experto:** *"No sustituimos tu trabajo: te traemos un paciente que ya llega con un mapa estructurado de su funcionamiento e hipótesis a explorar contigo. Material de partida, no diagnóstico."*
- **Creador:** *"Tu manual es la base de tu marca personal: lo que te obsesiona, lo que solo tú ves, tu voz. Te damos el material crudo de tu identidad para crear."*

---

## 15. RIESGOS Y CONTRAARGUMENTOS (en duro)

| Riesgo | Por qué podría matar el proyecto | Mitigación concreta |
|---|---|---|
| **Exceso de ambición** | 50 miradas + grafo + observación + suscripción a la vez = nada terminado | MVP concierge de UN informe. Lo demás, prohibido hasta validar. |
| **Falta de foco** | Demasiados módulos y mensajes diluyen la promesa | Una promesa: "tu manual de usuario". Un ICP. Un entregable. |
| **Mercado que suena saturado** | "Otra app de autoconocimiento" | Categoría propia (Identity Intelligence) + material real + ética. No competir en "tests". |
| **Riesgo legal/sanitario** | Datos sensibles, salud mental, diagnóstico encubierto | No-diagnóstico como núcleo técnico; GDPR; prohibir uso en empleo/salud; derivación en crisis. |
| **Coste de IA** | Informes extremos caros | Multi-tier de modelos, cache, reutilización; cobrar acorde a longitud. |
| **Informes poco fiables / genéricos** | Si suena a horóscopo, muere | Trazabilidad de evidencia obligatoria; contraevidencia; revisión humana en concierge. |
| **Dependencia emocional** | Daño al usuario + reputación | Diseño anti-adicción; el producto entrega y se aparta. |
| **Privacidad** | Una filtración sería letal en estos datos | Cifrado, minimización, borrado real, residencia UE, auditoría. |
| **UX difícil** | Pedir "sube tu vida" da pereza/miedo | Entrevista conversacional guiada; empezar con poco; mostrar valor pronto. |
| **Falta de retención** | Es un "one-shot": te haces el manual y te vas | Manual *vivo* + seguimiento como suscripción; pero aceptar que el informe puntual ya es negocio. |
| **Big Tech** | Memoria personal con IA podría rozar esto | Foso en método, curación y marca, no en el modelo base. |
| **Sonar a autoayuda** | Pierde seriedad y precio | Tono técnico-clínico-cálido; evidencia; estética sobria. |
| **Diagnóstico encubierto** | Lo peor: parecer que diagnosticas sin licencia | Guardrails + lenguaje de hipótesis + disclaimers + derivación. |
| **Que nadie pague** | La hipótesis madre | Validar con concierge caro en 30 días antes de construir. |

---

## 16. DECISIONES FINALES

- **Nombre:** Marca madre **Manual**; producto **Manual de Usuario**; motor interno *Persona Técnica*; módulos *El Consejo* y *Aprendiendo a Observar*. (PersonaTécnica descartado como marca comercial.)
- **Categoría:** **Identity Intelligence**.
- **Producto principal:** generación de un manual de usuario personal a partir de material real, con las 50 perspectivas y la matriz de consenso como núcleo de valor.
- **MVP:** servicio **concierge** de un informe premium, sin app, en 30 días.
- **Usuario inicial:** multipotencial técnico-creativo, 28–45, usuario avanzado de IA, en inflexión vital, con renta.
- **Precio inicial:** 290–490 €/informe + 90 € devolución.
- **Stack:** Next.js + FastAPI + Postgres/pgvector + Redis + S3-compat + workers + Claude (multi-tier) + orquestación propia.
- **Primer entregable:** el manual "Este es Antonio Hermoso González" (caso 0).
- **Frase madre:** *"Descubre cómo funcionas antes de decidir quién deberías ser."*
- **Primer vídeo:** la IA presenta a Antonio y muestra el manual; Antonio no aparece.
- **Hoja de ruta 90 días:**
  - **Días 1–30:** caso 0 + landing + pipeline asistido + vídeo. Conseguir lista de espera.
  - **Días 31–60:** 10 informes concierge de pago. Medir certeza, disposición a pagar, horas/informe. Iterar plantilla y prompts.
  - **Días 61–90:** automatizar ingesta + entrevista + 50 miradas/matriz. Subir precio. Decidir si arranca suscripción (manual vivo).

---

## 17. DEFINICIÓN FINAL DEL PRODUCTO

> **Manual de Usuario — Identity Intelligence**

**Qué es.** Un sistema que toma el rastro real de una persona —lo que escribe, dice, mira, crea y repite— y genera el manual de instrucciones de sí misma: cómo piensa, cómo trabaja, qué se le repite, qué le bloquea, qué pasiones esconde, qué entornos le encajan y qué futuros son compatibles. No es un test, no es terapia, no es journaling, no es un diagnóstico.

**Para quién es.** Adultos multipotenciales, técnico-creativos, de mente no normativa, en un punto de inflexión, que sienten que "no caben en una sola caja" y quieren claridad sin reducirse. Usuarios avanzados de IA, con renta disponible.

**Qué problema resuelve.** La gente decide quién *debería* ser sin entender primero cómo *funciona*. Los tests etiquetan y la terapia es lenta y cara. Falta un mapa estructural, honesto y accionable de la propia identidad funcional.

**Cómo funciona.** El usuario aporta su material (texto, audio, imágenes, proyectos). La IA lo transcribe, lo describe, lo conecta en un grafo de identidad, extrae señales con evidencia, formula hipótesis no clínicas, somete el caso a un consejo de 50 perspectivas distintas, destila una matriz de consenso (señales fuertes, contradicciones, finalistas, riesgos) y redacta un manual con futuros compatibles y un plan — todo con trazabilidad de por qué afirma cada cosa.

**Qué lo diferencia.** Material real, no auto-reporte. Síntesis estructural, no entradas sueltas. Las 50 miradas + matriz de consenso como motor de objetividad. Disciplina ética anti-diagnóstico con trazabilidad y borrado real. Una categoría propia: Identity Intelligence.

**Cómo se construye.** Monolito modular: Next.js + FastAPI + Postgres/pgvector + Redis + S3 + workers, con Claude en arquitectura multi-tier y una capa de orquestación propia centrada en trazabilidad y guardrails. La complejidad vive en el pipeline de IA, no en la infra.

**Cómo se vende.** Primero servicio concierge premium (290–490 €/informe) para validar valor y disposición a pagar sin construir apenas. Después, automatización hacia self-serve (49–149 €) y suscripción (manual vivo). Aliados —psicólogos, coaches— como canal, nunca como sustituidos.

**Por qué puede ser grande.** Es una categoría sin líder, con margen de software, habilitada justo ahora por la IA multimodal que razona sobre material cualitativo. El foso es el método, la marca y la ética, no el modelo. Y toca un deseo universal y atemporal: entenderse de verdad.

**Primer paso concreto.** Construir el **caso 0** —el manual de Antonio Hermoso González— con el pipeline asistido, publicar la landing con ese caso como prueba y el vídeo de la IA presentándolo, y vender los primeros 10 informes concierge en 30 días.

---

### Nota final, sin suavizar

"PersonaTécnica" no es el mejor nombre y "app de autoconocimiento" no es la categoría correcta. El nombre amputa la mitad humana del proyecto y la categoría te entierra en un mercado saturado de tests baratos. **Decisión: producto "Manual de Usuario", categoría "Identity Intelligence".** Y el mayor riesgo del proyecto no es técnico ni de mercado: es tu tendencia —legítima, parte de tu funcionamiento— a construirlo todo a la vez. La disciplina del MVP concierge (un informe, a mano, vendido caro, validado en 30 días) es lo que separa esto de ser otra idea brillante sin terminar. Empieza por el caso 0. Vende diez. Después construye la máquina.
