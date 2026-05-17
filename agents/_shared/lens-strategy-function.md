# LENTE DE ESTRATEGIA + FUNCIÓN — guía aplicada para sub-agentes

> Cómo cada sub-agente aplica las dos lentes obligatorias además del análisis técnico.

---

## POR QUÉ ESTAS DOS LENTES SON OBLIGATORIAS

El compliance técnico es necesario pero insuficiente. Un memo técnicamente
impecable que no aborda **(a) quién consume y para qué decisión** ni
**(b) cómo encaja en la estrategia del cliente** no sirve a un tax director
ni a un CFO. Las dos lentes elevan cada deliverable de "respuesta técnica"
a "input ejecutivo".

---

## LENTE DE FUNCIÓN FISCAL — preguntas obligatorias

### 1. ¿Quién consume?

Mapeo de stakeholders por tipo de output:

| Output | Consumidor primario | Consumidor secundario |
|---|---|---|
| Pillar Two calc por entidad | Controller | Tax director |
| Pillar Two consolidado | CFO + tax director | Audit committee · Treasury |
| TCF maturity scorecard | Tax director · Audit committee | CFO · CRO |
| TP local file | AEAT · external auditor | Controller · CFO |
| Master file | AEAT · external auditor · cliente legal department | CFO · CTO |
| CbCR público | Investor relations · sustainability · comms | Board · CFO |
| AIA | DPO · CIO · CTO · ético/AI committee | Legal · CFO |
| Memo opinion | Cliente (interlocutor concreto en matter.md) | Socio responsable |
| Memo board paper | Board · audit committee | CFO · GC |
| Defense pleading | AEAT/TEAR/TEAC · revisor sénior | Cliente legal department |
| Tax strategy paper | CFO · board · tax director · corporate development | Treasury · M&A team |

### 2. ¿Dónde encaja en el ciclo del tax function?

Cinco ciclos típicos:
- **Cierre mensual / trimestral**: provisión, retenciones, IVA, modelo 232
- **Cierre anual**: IS, BIN, ajustes BI, modelo 200
- **Provisión contable**: ETR forecast, deferred tax, uncertain tax positions
- **Planning trimestral**: ETR planning, restructuring, M&A, posturas nuevas
- **Response cycle**: requerimientos AEAT, inspección, MAP, APA

Cada deliverable identifica cuál de los cinco está apoyando.

### 3. ¿Qué KPI mueve?

KPIs típicos del tax function:
- **ETR consolidada** (objetivo · realizada · variación vs. presupuesto)
- **Cash tax** (vs. ETR contable; diferencias temporarias)
- **Días desde cierre hasta liquidación final** (efficiency)
- **Controversias abiertas** (número · cuantía · probabilidad de resolución)
- **Errores en autoliquidaciones** (autodescubiertos vs. AEAT-descubiertos)
- **Adherencia a CBPT** (sí/no · estado del reporting anual)
- **Cobertura TP doc** (% operaciones materiales documentadas)

### 4. ¿Qué cambio organizativo sugiere?

Si el deliverable revela problemas estructurales:
- Roles ausentes (¿hay regional tax lead para esta jurisdicción?)
- Tech stack insuficiente (¿el ERP soporta el data needed?)
- Reporting line incorrecto (¿controlling fiscal reporta a CFO o a contabilidad?)
- Skills gap (¿hay alguien que entienda Pilar Dos en el equipo?)

---

## LENTE DE ESTRATEGIA — preguntas obligatorias

### 1. ¿Cuál es la decisión estratégica que habilita o condiciona?

No "el cálculo es X". Sino: "el cálculo X habilita la decisión D" (ej:
"con top-up consolidado <2M€, mantener la estructura actual es viable;
con >2M€, abrir análisis de restructuring").

### 2. ¿Qué opciones existen?

Cada deliverable estratégico produce **opciones**, no recomendación única.
Opciones típicas:
- Hacer X · no hacer X · hacer X parcialmente · esperar
- Recurrir · firmar conformidad · acordar
- Solicitar consulta DGT · operar bajo riesgo silencioso · APA bilateral

Con trade-offs explícitos: ETR · cash tax · complexity · reputational ·
regulatory risk · timing · cost.

### 3. ¿Cuál es el segundo orden?

Efectos downstream:
- ¿Qué hace la AEAT si vemos esto?
- ¿Qué hacen los competidores si publicamos esto?
- ¿Qué pasa en N+1 ejercicios si esta postura se generaliza?
- ¿Crea precedente interno difícil de revertir?

### 4. ¿Cuándo cambia la respuesta por perfil de cliente?

| Cliente | Variación típica |
|---|---|
| Cotizada IBEX35 | Reputational risk alto · CbCR público obligatorio · SOX testing |
| Privada family-owned | Reputational risk medio · más tolerancia a complejidad |
| PE-owned | Horizonte exit-driven · estructura puede pivotar pre-IPO |
| Family office | Personal liability del propietario · más conservadora |
| Filial española de grupo extranjero | Subordinada a estrategia HQ · menos optionalidad |

---

## CÓMO REPORTAR LAS DOS LENTES

En el campo `strategy_angle` del output contract (SHAPE 1) y `function_lens`,
1-3 párrafos cada uno. NO checklists vacíos. Si la lente es genuinamente
no-aplicable (raro), justificarlo en una frase.
