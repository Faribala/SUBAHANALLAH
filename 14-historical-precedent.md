# 14 — Historical Precedent & Lessons Learned

**Ocean Salvage Platform (OSP) — Pre-FEED Deliverable**
**Document:** 14-historical-precedent.md
**Date:** 12 February 2026

---

## 1. Comparable Projects

### 1.1 Hughes Glomar Explorer (1974)

| Parameter | Glomar Explorer | OSP | Comparison |
|-----------|----------------|-----|------------|
| **Purpose** | Covert recovery of K-129 from 4,900 m | Recovery of 5+ nuclear submarines from 33–3,000 m | OSP is multi-target, declared programme |
| **Hull type** | Ship-shaped with split hull (Moon pool: 60 × 23 m) | Catamaran semi-submersible (Channel: 135 × 20 m) | OSP has 5× larger open area; better stability |
| **Displacement** | 63,000 t | 135,000 t | OSP is 2× larger |
| **Lift capacity** | ~4,000 t (pipe string + claw) | 12,000 t (strand jacks) | OSP has 3× capacity |
| **Depth achieved** | 4,900 m (partial recovery; hull broke during lift) | Design: 2,000 m | Glomar went deeper but with single-point failure |
| **Key failure** | Claw arm broke → recovered only forward third of K-129 | Distributed strand jack system; redundant rigging | OSP addresses Glomar's single-point failure |
| **DP** | None (moored) | DP3 | Major advancement |
| **Nuclear handling** | Rudimentary (1974 technology) | Full reactor handling bay with modern shielding | Vastly improved |
| **Cost** | ~$350M (1974) ≈ $2.1B (2024) | ~$2.9B (2026 estimate) | Comparable in adjusted terms |
| **Build time** | 4 years | 4 years (estimated) | Similar |

**Lessons for OSP:**
1. **Single-point failure in lifting mechanism is unacceptable.** The Glomar claw had no redundancy → catastrophic partial loss. OSP uses 28 distributed strand jacks; any 2 failures still allow completion.
2. **Ship-shaped hull has excessive roll motion.** Glomar needed ~3.0 m Hs limit for operations. Semi-submersible OSP operates to Hs 5.0 m.
3. **Moon pool wave amplification** was a major issue on Glomar. OSP's open channel design reduces piston resonance.
4. **Seabed breakout force** was underestimated on Glomar. OSP provides 140% of estimated breakout force as design margin.

### 1.2 Kursk Salvage (2001)

| Parameter | Kursk Salvage | OSP |
|-----------|--------------|-----|
| **Submarine** | K-141 Kursk (SSGN Oscar-II class) | Multiple targets |
| **Displacement (sub)** | 23,860 t (submerged) | ≤ 10,000 t (largest target K-278: ~8,500 t) |
| **Depth** | 107 m (Barents Sea) | 33–3,000 m |
| **Method** | 26 strand jacks on Giant 4 barge, cut bow section, lift main hull | Strand jacks + buoyancy pontoons |
| **Lift vessel** | Giant 4 (barge), purpose-converted | OSP (purpose-built) |
| **Lift capacity** | ~23,000 t (26 strand jacks × 900 t each) | 12,000 t (28 × 500 t) — sufficient for smaller targets |
| **DP** | None (barge anchored) | DP3 |
| **Duration** | 3 months (lift operation only) | 3–8 weeks per target |
| **Bow separated** | Yes — explosive-damaged bow cut off before lift | No — recovery of complete hull preferred |
| **Result** | Complete success (hull recovered minus bow) | — |
| **Cost** | ~$130M (2001) ≈ $220M (2024) | ~$325M–$1.22B per sub (campaign cost) |

**Lessons for OSP:**
1. **Strand jack technology proven at scale** for submarine recovery. 26 units worked reliably for Kursk. OSP uses similar technology.
2. **Rigging under hull is the critical path.** Kursk rigging (passing cables under hull in Barents Sea) took months. OSP ROV capability accelerates this.
3. **Ballast compensation during surfacing** was manually managed on Giant 4. OSP automates this with computerised ballast control.
4. **Weather window dependency.** Kursk lift waited weeks for acceptable weather in Barents Sea. OSP's semi-sub hull form extends the weather window.

### 1.3 K-429 Recovery (1983)

| Parameter | K-429 Salvage | OSP |
|-----------|--------------|-----|
| **Submarine** | K-429 (Charlie-I class SSGN) | Multiple |
| **Depth** | 39 m | 33–3,000 m |
| **Method** | Pontoon lift by Soviet Navy salvage vessels | Strand jacks + buoyancy |
| **Result** | Successful; submarine returned to service | — |
| **Duration** | 5 months (total) | — |

**Lesson:** Shallow-water pontoon lifts are established practice. OSP Mode A (strand jacks) is more controlled and faster for similar depths.

### 1.4 Heerema Sleipnir (2019)

| Parameter | Sleipnir | OSP |
|-----------|---------|-----|
| **Type** | Semi-submersible crane vessel | Semi-submersible salvage platform |
| **LOA × BOA** | 220 m × 102 m | 275 m × 80 m |
| **Displacement** | ~275,000 t (full load) | ~135,000 t |
| **DP** | DP3 (12 thrusters) | DP3 (10 thrusters) |
| **Crane capacity** | 2 × 10,000 t | 12,000 t (strand jacks, not cranes) |
| **Power** | 86 MW (LNG + diesel) | 111.6 MW (diesel) |
| **Build time** | ~4 years (2015–2019) | ~4 years (estimated) |
| **Cost** | ~$2.5B | ~$2.9B |

**Lessons for OSP:**
1. **DP3 proven on semi-submersible at this scale.** Sleipnir operates DP3 routinely in North Sea.
2. **12 thrusters provides good redundancy** — OSP uses 10 (marginal but acceptable with mooring backup for shallow sites).
3. **Power plant sizing** — Sleipnir at 86 MW with 12 thrusters; OSP at 111.6 MW with 10 thrusters → adequate margin.
4. **Construction schedule** of 4 years at Korean yard is realistic for this vessel class.

---

## 2. Submarine-Specific Precedents

### 2.1 Nuclear Submarine Recovery — Key Differences from Past Operations

| Factor | Previous Operations | OSP Design Response |
|--------|-------------------|-------------------|
| Depth range | 39–4,900 m (Glomar only >200 m) | Dual-mode system (strand jack + buoyancy) covers full range |
| Nuclear safety standards | 1974–2001 standards; relatively lax | Full IAEA compliance; reactor handling bay; criticality prevention |
| DP technology | Unavailable or primitive | DP3 (DYNPOS-3 AUTRO) — state of art |
| ROV capability | Minimal (1974); improved (2001) | 4 × work-class ROVs to 3,000 m; modern tooling |
| Rigging technology | Wire rope; manual tensioning | High-strength synthetic + wire; AHC; computerised load monitoring |
| Environmental standards | Minimal | Full EIA; MARPOL; contaminated water treatment |

### 2.2 Summary of All Nuclear Submarine Sinkings

| # | Submarine | Nation | Year Sunk | Depth (m) | Cause | Status | Recovery Feasibility |
|---|-----------|--------|-----------|-----------|-------|--------|---------------------|
| 1 | USS Thresher (SSN-593) | US | 1963 | 2,560 | Pipe failure; collapse | Debris field | ★★ (scattered wreckage) |
| 2 | USS Scorpion (SSN-589) | US | 1968 | 3,000 | Unknown; torpedo? | Collapsed hull | ★ (extreme depth + fragmented) |
| 3 | K-8 | USSR | 1970 | 4,680 | Fire; scuttled | Intact on seabed | ★ (extreme depth) |
| 4 | K-27 | USSR | 1981 | 33 | Reactor accident (1968); dumped | Intact, sealed | ★★★★★ (shallow, intact) |
| 5 | K-429 | USSR | 1983 | 39 | Flooding | **Recovered 1983** | N/A |
| 6 | K-219 | USSR | 1986 | 5,500 | Missile silo explosion | Intact on seabed | ★ (extreme depth) |
| 7 | K-278 Komsomolets | USSR | 1989 | 1,680 | Fire | Intact, some damage | ★★★★ (within OSP range) |
| 8 | K-141 Kursk | Russia | 2000 | 107 | Torpedo explosion | **Recovered 2001** | N/A |
| 9 | K-159 | Russia | 2003 | 200 | Hull flooding (tow) | Intact on seabed | ★★★★★ (shallow, intact) |

Feasibility: ★ = Extremely difficult → ★★★★★ = Most feasible

### 2.3 OSP Priority Targets (from `nuclear-submarine-salvage-operation-plan.md`)

1. **K-27** (★★★★★) — Shallowest (33 m); highest criticality risk; international pressure
2. **K-159** (★★★★★) — 200 m; intact; conventional PWR
3. **K-278** (★★★★) — 1,680 m; within depth capability; nuclear torpedoes add complexity
4. **USS Thresher** (★★) — 2,560 m; scattered debris field; partial recovery only
5. **USS Scorpion** (★) — 3,000 m; beyond OSP depth rating; would require enhanced buoyancy

---

## 3. Technology Readiness Assessment

| Technology | TRL | Basis | Risk |
|-----------|-----|-------|------|
| Semi-submersible hull design | 9 | Hundreds built and operating | LOW |
| DP3 system | 9 | Standard on modern offshore vessels | LOW |
| Large strand jacks (500 t each) | 8 | Enerpac/Mammoet units to 650 t proven | LOW |
| AHC on strand jacks | 7 | Proven on offshore cranes; novel applied to strand jacks | MODERATE |
| Buoyancy pontoon controlled ascent | 6 | Concept proven (Glomar Explorer); full system demonstration needed | MODERATE |
| ROV rigging at 1,680 m | 7 | Deep-water ROV tooling proven; rigging at this depth is novel | MODERATE |
| Nuclear reactor handling bay (afloat) | 5 | No offshore precedent; land-based reactor handling well established | HIGH |
| Gimbal cradle for criticality control | 5 | Concept only; requires engineering development | HIGH |
| Contaminated water treatment (offshore) | 7 | Land-based IX/RO proven; offshore deployment needs marinisation | MODERATE |
| Catamaran semi-submersible (this size) | 6 | Smaller catamaran semi-subs exist; 275 m is unprecedented | MODERATE |

**Average TRL: 6.9** — generally mature technologies with key novel integrations.

---

## 4. Key Risk Areas from Precedent

| # | Risk from Precedent | Historical Example | OSP Mitigation |
|---|--------------------|--------------------|----------------|
| 1 | Lifting mechanism failure | Glomar Explorer claw breakage | 28 distributed strand jacks; no single point of failure |
| 2 | Weather delays | Kursk waited weeks | Semi-sub hull → wider weather window (Hs 5 m vs 2–3 m) |
| 3 | Rigging difficulty at depth | Kursk: months of preparation at 107 m | 4 work-class ROVs; practice at shallower targets first |
| 4 | Nuclear contamination spread | K-27 dumped with minimal containment | Reactor bay + water treatment + IAEA oversight |
| 5 | Criticality accident | K-27 unique risk (Pb-Bi reactor) | Gimbal cradle; neutron monitoring; boron injection |
| 6 | Schedule overrun | Glomar Explorer: 4 years planned → 4 years actual (unusual) | Conservative 4-year schedule with 6-month float |
| 7 | Cost escalation | All large marine projects | 20% contingency; AACE Class 4 estimate |
| 8 | Hull structural failure during lift | Glomar Explorer K-129 hull broke | Distributed sling loading; thorough pre-lift survey |

---

*Cross-references: `01-hull-form-selection.md`, `07-heavy-lift-system.md`, `08-nuclear-safety-containment.md`, `12-operational-modes.md`, `15-risk-register.csv`*
