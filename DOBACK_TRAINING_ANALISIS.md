# DOBACK / Training — Análisis estratégico duro (sobre la realidad, no sobre suposiciones)

> Para Antonio Hermoso. Análisis fundado en: tus repos reales, el informe maestro, y la investigación de mercado del nicho (seguridad y formación de conductores de flotas críticas / vehículos de emergencia sobre telemetría).
> Tono: criterio, no suavidad.

---

## Hechos de mercado que enmarcan todo (verificados, jun 2026)

- **Vuelcos = 66% de accidentes mortales de camiones de bomberos.** Accidentes de vehículo = 2ª causa de muerte en acto de servicio (~25% de LODD). 70% ocurren en emergencia. Conductores de emergencias: 12x más riesgo que policía. → **Problema de vida, no de coste.**
- **Driver safety market: 1,5B$ (2024) → 2,5B$ (2032), 11% CAGR.** Líderes (Lytx, Samsara, Geotab, Motive) = **flotas comerciales**, no emergencias. Valor migrando de hardware (comodity) a **software de coaching + formación**.
- **Webfleet/Bridgestone = ecosistema abierto de apps sectoriales de terceros.** Integración, no competencia.
- **ROI probado:** coaching+telemetría → 52–94% menos eventos, 22% menos costes, menos primas.

---

## 17.1 Diagnóstico brutal

**Qué estás construyendo realmente:** una **capa especializada de seguridad operacional y formación para flotas críticas de emergencia, sobre telemetría real (Webfleet), con Bomberos Madrid como cliente faro.** Eso es Training/DobackSoft. Es lo único de todo tu ecosistema que tiene a la vez: cliente real, datos reales, dolor cuantificado y mercado.

**Qué crees que estás construyendo pero quizá no:** "DOBACK, la plataforma universal de telemetría + IA + inclinación + auditoría + formación + mundos". Eso no es un producto; es un paraguas que esconde dispersión. Nadie compra un paraguas.

**Dónde hay producto real:** Training (capa de safety/formación). 

**Dónde hay fantasía técnica (valiosa pero no negocio ahora):** Artificial World, Prisma, MobiAI, ContextOS, IncliSafe-como-hardware. `dobacksoft-audit` es una herramienta interna excelente, no producto.

**Dónde hay oportunidad comercial:** emergencias/flotas críticas, empezando por Bomberos Madrid → otras emergencias del sector público.

**Dónde hay dispersión:** en que tienes 8 universos abiertos. Tu patrón de siempre. Esta vez tienes que cerrar 7.

---

## 17.2 Ranking de proyectos (frío)

| Proyecto | Madurez | Cliente | Ingreso | Diferenciación | Riesgo | Escala | Vendible 90d | Veredicto |
|---|---|---|---|---|---|---|---|---|
| **Training / DobackSoft** | Alta | **Real (Bomberos)** | Alto | Alta (vertical+datos) | Medio (IP) | Sí | **Sí** | **FOCO** |
| DOBACK (paraguas) | — | — | — | Confusa | Alto | — | No | Reformular, no es producto |
| IncliSafe (módulo) | Media | vía Training | Medio | Alta pero arriesgada | **Alto (certificación)** | Sí | No | Módulo futuro, no claim de seguridad |
| ContextOS (servicio) | Baja | 0 | Medio | Media | Bajo | Servicio | Sí pero | **Congelar** (compite por foco) |
| Prisma | Media | 0 (B2C) | Bajo | Media | Alto (privacy) | Difícil | No | **Congelar** |
| MobiAI | Media | 0 | Bajo | Media | Alto (devtools) | Difícil | No | **Congelar** (útil interno) |
| Artificial World | Media | 0 | Bajo | Conceptual | Alto | Difícil | No | **Congelar** (laboratorio) |
| Portfolio/marca | — | — | Indirecto | — | Bajo | — | No | Mantener mínimo (reputación) |

**Conclusión del ranking:** una sola fila merece tu energía 90 días. Las demás se congelan, no se matan.

---

## 17.3 Training / DobackSoft

- **¿Oportunidad real?** Sí. Es la única con cliente, datos y dolor de vida-o-muerte.
- **Producto mínimo vendible:** un **informe/dashboard de seguridad y formación por conductor y por parque**, alimentado por Webfleet, que un **instructor/jefe de parque** usa para coaching no punitivo: eventos críticos (velocidad, aceleración lateral/longitudinal, frenadas, riesgo de maniobra), evolución antes/después de la formación, y un informe que se entrega y se firma. Nada más en el MVP.
- **Comprador (quien firma):** el responsable de formación / jefe de flota / dirección del cuerpo (sector público). 
- **Usuario (quien lo usa a diario):** el **instructor** y el jefe de parque. Diseña PARA el instructor: ese es tu usuario y tu foso de workflow.
- **Problema concreto que se paga:** "no puedo demostrar que mi formación reduce accidentes ni dirigir el coaching con datos; dependo de percepción." Tú lo conviertes en **mejora medible de seguridad.**
- **Métrica que demuestra valor:** reducción de eventos críticos por conductor antes/después de la formación. Esa curva ES tu venta.
- **Qué NO construir todavía:** hardware, IncliSafe sensórico, IA/RAG conversacional, multi-OEM, módulos de mundos, app de consumo. 
- **Qué cerrar técnicamente primero:** el pipeline Webfleet→normalización multi-org→informe de conductor/parque estable en producción, con auth de manager y un informe que venda. Cierra los pendientes (Celery/timer FTP, smoke real con MANAGER, Driver Report). Deja de abrir; cierra.
- **Demo que vende:** la pantalla **antes/después de un conductor real de Bomberos Madrid** tras formación. Una curva bajando. Eso emociona a un jefe de bomberos más que mil features.
- **De Bomberos Madrid a otros:** el sector público compra **lo que usan sus iguales.** Bomberos Madrid como faro → otros cuerpos de bomberos autonómicos/municipales, SAMUR/112, protección civil. La referencia es el motor de ventas, no el marketing.

---

## 17.4 DOBACK / IncliSafe — decisiones firmes

- **¿Hardware o software?** **Software**, encima de telemetría existente. El hardware (sensores, instalación, homologación, responsabilidad) es un agujero negro para un fundador. No ahora.
- **¿DOBACK es producto?** No. **DOBACK es marca paraguas; el producto es Training.** Reduce DOBACK a marca, no a "plataforma universal".
- **¿IncliSafe?** Es el ángulo más emocional (66% de muertes son vuelcos) y por eso el más **peligroso legalmente**. Vender un "sistema antivuelco" sin certificación = responsabilidad enorme si alguien vuelca igualmente.
- **Cómo posicionar IncliSafe sin claims arriesgados:** como **módulo de análisis y formación de riesgo**, no como dispositivo de seguridad activa. "Detectamos maniobras de **alto riesgo de inclinación** para entrenarlas", no "evitamos vuelcos". Advisory, no actuación. Sin certificación, **cero claims de seguridad activa.**
- **Qué pruebas faltan:** correlación real entre tus métricas y riesgo de vuelco, con datos suficientes y validación de instructores. Hasta tenerla, IncliSafe es módulo de scoring para formación, no producto de seguridad.

---

## 17.5 Mercado — qué vertical primero

**Primero: bomberos (España), desde Bomberos Madrid.** Por qué: ya tienes el pie dentro, el dolor es máximo (vuelcos), y el sector público compra por referencia entre iguales. Luego, en orden:
1. Otros cuerpos de bomberos (autonómicos/municipales).
2. SAMUR / ambulancias / 112 / protección civil (EMS: 12x más riesgo).
3. Vehículos militares / defensa (conecta con Cosigein; cuidado confidencialidad).
4. Después: flotas críticas privadas (residuos, grúas, transporte especial).

No empieces por flotas comerciales genéricas: ahí están Lytx/Samsara y pierdes.

---

## 17.6 Competencia — dónde te diferencias de verdad

- **Webfleet/Geotab/Samsara/Lytx:** genéricos, comerciales, sin workflow de emergencias ni de instructor. **Tú: integras con ellos (Webfleet) y especializas donde no llegan.** No compitas en telemetría; compite en **la capa de formación y seguridad de emergencias.**
- **OEM / ESP / Roll Stability Control (Bosch, ZF/WABCO, Knorr-Bremse):** actúan sobre el vehículo, homologados. **No compitas ahí.** Tú usas el dato para **formar y prevenir**, no para actuar.
- **Formación vial / EVOC (cursos, simuladores):** desconectados del dato real. **Tu diferencia: unir telemetría real + formación medible + workflow de instructor.** Eso hoy no lo hace nadie bien para emergencias.

Tu foso real, en una línea: **datos de conducción de emergencias reales + workflow del instructor + referencia de Bomberos Madrid.** Eso no lo tiene ni un gigante ni un recién llegado.

---

## 17.7 Modelo de negocio

- **Fase 1 (ahora):** proyecto/servicio con Bomberos Madrid (integración + despliegue + módulo de formación + soporte). Es lo que ya hay. **Úsalo para generar el caso y los datos.**
- **Fase 2 (productizar):** licencia anual por organización/parque + por vehículo/conductor. El sector público prefiere **licencia enterprise anual** (a veces on-premise por sensibilidad de datos) a SaaS puro. Banda orientativa: licencia anual por cuerpo + precio por vehículo/conductor activo.
- **Transición servicio→producto:** cada despliegue deja módulos reutilizables (Fleet Data Core, Training, Safety Intelligence). Cuando 2-3 cuerpos repitan, el producto existe.
- **Hardware:** solo si IncliSafe madura con certificación y un socio industrial. No en el horizonte de 90 días.

---

## 17.8 Riesgos legales / IP — LO MÁS URGENTE (léelo dos veces)

Esto es lo más importante que te voy a decir, y es incómodo:

1. **El producto probablemente NO es tuyo, es de Cosigein.** Lo desarrollas como empleado, para un cliente de la empresa (Bomberos Madrid/CMadrid), con datos e infraestructura de la empresa. Salvo pacto escrito, **la propiedad intelectual es del empleador.** Antes de soñar con comercializarlo como "tu" producto, **necesitas una conversación formal con Cosigein** sobre titularidad, tu rol y tu participación (¿empleado?, ¿socio?, ¿% / royalties?, ¿spin-off?). No construyas un año sobre algo que no sabes de quién es.
2. **Repos personales públicos con sistema de un cliente real = problema.** `dobacksoft-audit`, `dobacksoft-app`, `IncliSafeV2` están **públicos** bajo tu cuenta personal y referencian un sistema real con multi-tenant, credenciales, organizaciones (CMadrid), Webfleet. Eso es **riesgo de confidencialidad y de seguridad.** Acción inmediata: **ponlos privados y barre cualquier secreto/credencial/dato de cliente** del histórico. Hoy, no la semana que viene.
3. **Datos de Bomberos Madrid:** no son tuyos para reutilizar comercialmente sin permiso contractual. Para que los datos sean un activo, necesitas **cláusula de uso/derivados, anonimización y consentimiento.** Pregúntalo antes de basar el negocio en ello.
4. **IA/agentes sobre código y credenciales:** cuidado con pasar credenciales o datos de cliente por herramientas de terceros. En sector público/defensa esto puede ser grave.

**Resumen:** la oportunidad es real, pero **la base legal está sin resolver, y eso es el riesgo número uno**, por encima de cualquier tema técnico o de mercado.

---

## 17.9 Plan de 90 días (realista)

**Semanas 1-2 — Suelo legal y seguridad (antes de nada más):**
- Pon privados los repos del cliente; barre secretos.
- Prepara y ten **la conversación con Cosigein** sobre titularidad, tu rol y tu participación. Deja por escrito qué es de la empresa y qué (si algo) es tuyo.
- Confirma con el cliente qué datos puedes usar y para qué.

**Semanas 3-6 — Cerrar el MVP vendible:**
- Estabiliza Webfleet→informe de conductor/parque en producción (cierra los pendientes técnicos).
- Construye **la pantalla antes/después** de formación de un conductor real.
- Congela TODO lo demás (Artificial World, Prisma, MobiAI, ContextOS, IncliSafe-hardware).

**Semanas 7-10 — Demostrar valor:**
- Mide la reducción de eventos críticos tras una acción de formación con datos reales de Bomberos Madrid.
- Empaqueta un **informe ejecutivo** que enseñar a dirección.

**Semanas 11-13 — Preparar la expansión:**
- Con el caso de Bomberos Madrid (con permiso), prepara la presentación para **un segundo cuerpo** de bomberos/emergencias.
- Define la oferta: licencia anual + por vehículo. Plan de transición servicio→producto.

**Qué medir todo el tiempo:** una métrica — **reducción de eventos críticos por conductor tras formación.** Es tu prueba y tu venta.

---

## 17.10 Conclusión (sin suavidad)

> **Antonio: el producto no es DOBACK, es Training. Y no es hardware, es safety/training intelligence.** Sigue por ahí — es lo único con cliente, datos y dolor real — pero con tres condiciones innegociables: (1) **resuelve la IP con Cosigein y la seguridad de los repos ANTES de seguir**, porque hoy estás construyendo sobre arena legal; (2) **congela los otros 7 universos** 90 días; (3) **no toques claims de seguridad/antivuelco sin certificación.**

Tu hipótesis (§18) es correcta. La valido: capa especializada de formación y seguridad operacional para flotas críticas, desde Bomberos Madrid, sobre Webfleet, con IncliSafe solo como módulo de análisis cuando haya datos. La única corrección es de prioridad: **lo legal va primero, no el código.**

---

## Frase de producto (la mejor de tus candidatas, afinada)

De tus opciones, la nº1 es la más fuerte. Afinada:

> **"DOBACK convierte la telemetría de los vehículos de emergencia en formación medible y prevención de accidentes."**

Para vender a un jefe de bomberos, aún más directo:
> **"Menos accidentes de tus vehículos, demostrado con datos."**

---

## Fuentes
- Bomberos/accidentes: Fire Engineering, Fire Apparatus Magazine, CDC/NIOSH, Lexipol, NSC.
- Mercado driver safety: ABI Research 2026, GlobeNewswire (Driver Safety Outlook), Mordor Intelligence.
- EVOC / emergencias: EMS1 Academy, OnQ Safety, NSC.
- Webfleet/Bridgestone ecosistema: webfleet.com, Bridgestone Data Solutions, press.bridgestone-emea.
- ROI: Element Fleet, Samsara, SureCam, ZenduIT, FleetShield.
