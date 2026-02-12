# Nuclear Submarine Salvage Operation Plan
## Comprehensive Operational Framework for Recovery of Sunken Nuclear Submarines

**Prepared:** 11 February 2026
**Classification:** UNCLASSIFIED — For Planning Purposes
**Reference Document:** sunken-nuclear-submarines-report.md

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Salvage Prioritization & Feasibility Matrix](#salvage-prioritization)
3. [Phase 1: Reconnaissance & Assessment](#phase-1)
4. [Phase 2: Engineering Design](#phase-2)
5. [Phase 3: Radiological & Environmental Safety](#phase-3)
6. [Phase 4: Operational Execution Plan](#phase-4)
7. [Phase 5: Transport & Disposition](#phase-5)
8. [Phase 6: Risk Management](#phase-6)
9. [Phase 7: Budget Estimate](#phase-7)
10. [Appendices](#appendices)

---

## Executive Summary

This document presents an implementable operational framework for the salvage of seven sunken nuclear submarines currently resting on the ocean floor. Two vessels — K-429 and K-141 Kursk — have already been successfully raised and are excluded from this plan.

### Submarines Requiring Salvage (Prioritized)

| Priority | Submarine | Depth (m) | Displacement (t) | Nuclear Hazards | Feasibility |
|---|---|---|---|---|---|
| **1 — CRITICAL** | K-27 | 33 | 4,380 | 2 liquid-metal reactors | HIGH |
| **2 — URGENT** | K-159 | 200 | 4,750 | 2 reactors (spent fuel) | HIGH |
| **3 — HIGH** | K-278 Komsomolets | 1,680 | 8,000 | 1 reactor + 2 nuclear torpedoes | MODERATE |
| **4 — MODERATE** | USS Thresher | 2,560 | 3,420 | 1 reactor | LOW-MODERATE |
| **5 — MODERATE** | USS Scorpion | 3,000 | 3,124 | 1 reactor + 2 nuclear torpedoes | LOW |
| **6 — LOW** | K-8 | 4,680 | 4,750 | 2 reactors + 4 nuclear torpedoes | VERY LOW |
| **7 — DEFERRED** | K-219 | 6,000 | 9,449 | 2 reactors + 16 nuclear missiles | IMPRACTICAL |

### Prioritization Rationale

- **K-27** is the highest priority because it sits in only 33 m of water in violation of IAEA guidelines (≥3,000 m), with exotic liquid-metal-cooled reactors whose fuel is fused to the coolant. Shallow depth makes it both the most accessible and the most vulnerable to disturbance.
- **K-159** is urgent because its hull had "the strength of foil" when it sank and contains ~800 kg of spent fuel (~5.3 GBq). At 200 m, it is technically recoverable.
- **K-278 Komsomolets** has active caesium-137 leakage (up to 800 Bq/L detected in 2019), two nuclear torpedoes with plutonium warheads, and sits at a challenging but achievable 1,680 m.
- **USS Thresher and USS Scorpion** are stable with no detected radiological release, but remain long-term liabilities at extreme depths.
- **K-8 and K-219** at 4,680 m and 6,000 m respectively are beyond practical salvage capability with current technology.

> **ASSUMPTION:** This plan focuses primary detailed planning on the three feasible candidates (K-27, K-159, K-278). Monitoring-only protocols are recommended for the four deep-water wrecks until technology advances.

---

## Salvage Prioritization & Feasibility Matrix

### Decision Tree: Salvage vs. Monitor-in-Place

```
                    ┌──────────────────────┐
                    │  Submarine Identified │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │  Depth < 2,000 m?    │
                    └──────────┬───────────┘
                          YES / \ NO
                         /       \
           ┌────────────▼┐    ┌───▼──────────────┐
           │ Active       │    │ Active            │
           │ radiological │    │ radiological      │
           │ release?     │    │ release?          │
           └──────┬───────┘    └───────┬──────────┘
              YES / \ NO          YES / \ NO
             /       \           /       \
    ┌───────▼──┐  ┌──▼───────┐ ┌▼───────┐ ┌▼──────────┐
    │SALVAGE   │  │SALVAGE   │ │CONTAIN │ │MONITOR    │
    │IMMEDIATE │  │PLANNED   │ │IN-SITU │ │ONLY       │
    └──────────┘  └──────────┘ └────────┘ └───────────┘
```

### Classification of Each Submarine

| Submarine | Depth Category | Active Release? | Decision |
|---|---|---|---|
| K-27 | Shallow (33 m) | Sealed but at risk | **SALVAGE IMMEDIATE** |
| K-159 | Shallow (200 m) | Deteriorating containment | **SALVAGE IMMEDIATE** |
| K-278 | Deep-recoverable (1,680 m) | Yes (Cs-137 detected) | **SALVAGE PLANNED** |
| USS Thresher | Ultra-deep (2,560 m) | No | **MONITOR → FUTURE SALVAGE** |
| USS Scorpion | Ultra-deep (3,000 m) | No | **MONITOR ONLY** |
| K-8 | Ultra-deep (4,680 m) | No data | **MONITOR ONLY** |
| K-219 | Abyssal (6,000 m) | Unknown | **MONITOR ONLY** |

---

## Phase 1: Reconnaissance & Assessment

### 1.1 Remote Survey Plan

#### ROV/AUV Selection Matrix

| Platform | Depth Rating | Application | Target Submarines |
|---|---|---|---|
| **Work-class ROV (e.g., Schilling UHD)** | 3,000 m | Hull inspection, sampling, tooling | K-27, K-159, K-278, Thresher |
| **Abyssal ROV (e.g., CURV-21 or Jason II)** | 6,500 m | Deep survey, photogrammetry | Scorpion, K-8, K-219 |
| **AUV (e.g., Kongsberg HUGIN 6000)** | 6,000 m | Bathymetric mapping, sidescan sonar | All submarines |
| **Micro-ROV (e.g., VideoRay Pro 5)** | 300 m | Internal hull penetration survey | K-27, K-159 |

#### Survey Protocol for Each Vessel

**K-27 (33 m) — Shallow Water**
1. Deploy multibeam echosounder (MBES) from survey vessel for full-coverage bathymetry (0.5 m resolution)
2. Sidescan sonar (100/400 kHz dual-frequency) mosaic of 500 m × 500 m area centered on wreck
3. Work-class ROV with HD/4K cameras + structured light scanner for full hull photogrammetry
4. Internal ROV inspection through any accessible hatches/hull openings — assess reactor compartment seal integrity
5. Magnetometer survey to map debris field
6. Sub-bottom profiler (Chirp 2–16 kHz) for sediment characterization beneath hull

> **ASSUMPTION:** K-27 is accessible by standard commercial diving and ROV operations. Water visibility in Kara Sea averages 5–15 m.

**K-159 (200 m) — Moderate Depth**
1. AUV bathymetric/sidescan survey of 1 km² area
2. Work-class ROV with 3D photogrammetry (Voyis laser scanner or equivalent)
3. Ultra-short baseline (USBL) acoustic positioning for centimeter-accuracy wreck mapping
4. Micro-ROV internal inspection via known hull fractures — assess fuel assembly condition
5. Visual and tactile assessment of hull plate thickness using ROV-mounted UT gauges
6. Current profiling (ADCP mooring for minimum 30 days)

**K-278 Komsomolets (1,680 m) — Deep Water**
1. AUV pre-survey: HUGIN 6000 with HISAS synthetic aperture sonar (2 cm resolution)
2. Deep-rated work-class ROV (3,000 m+) for visual survey of all hull fractures
3. Inspect 2019-era sealant condition on hull fractures
4. Map ventilation pipe where Cs-137 leakage was detected
5. Deploy seabed monitoring lander for 90-day data collection (current, temperature, turbidity, radiation)
6. 3D photogrammetric model of entire wreck for lift engineering

**Deep-Water Vessels (Thresher, Scorpion, K-8, K-219) — Monitoring Protocol**
1. Annual or biennial AUV survey missions
2. Water column sampling at 10 m, 50 m, 100 m above wreck for radiological analysis
3. Sediment grab samples at 5 points around wreck (cardinal directions + center)
4. Compare photogrammetry to previous surveys to measure corrosion progression
5. Deploy passive radiation monitoring plates on seabed near wreck

### 1.2 Radiological Survey Protocol

#### Water and Sediment Sampling Grid

For each submarine, a standardized sampling grid is deployed:

```
                    N
                    │
         NW ───────┼─────── NE
          │    250m │ 250m   │
          │         │        │
    W ────┼────── WRECK ─────┼──── E
          │         │        │
          │    250m │ 250m   │
         SW ───────┼─────── SE
                    │
                    S

    Sampling points: Center (directly above wreck) + 8 cardinal/ordinal points
    Additional: 4 points at 500m, 4 points at 1,000m (background reference)
```

**Water samples:** Collected at 5 depth intervals per station (surface, 25%, 50%, 75%, and seabed)
**Sediment samples:** Box-core samples (0–30 cm depth, sectioned at 5 cm intervals)

**Analytes:**
| Analyte | Method | Detection Limit |
|---|---|---|
| Cs-137 | Gamma spectrometry (HPGe) | 0.1 Bq/L (water), 1 Bq/kg (sediment) |
| Sr-90 | Radiochemical separation + LSC | 0.05 Bq/L |
| Pu-239/240 | Alpha spectrometry | 0.001 Bq/L |
| Co-60 | Gamma spectrometry | 0.1 Bq/L |
| Tritium (H-3) | Electrolytic enrichment + LSC | 1 Bq/L |
| Gross alpha/beta | Proportional counter | 0.05 Bq/L |

**Dosimetry Equipment (ROV-mounted):**
- NaI(Tl) scintillation detector for real-time gamma dose rate mapping
- Neutron detector (He-3 or BF-3) for criticality monitoring near reactor compartments
- Tissue-equivalent dosimeter for dose-rate profiling at hull surface

#### Submarine-Specific Radiological Concerns

| Submarine | Primary Radiological Hazard | Special Considerations |
|---|---|---|
| K-27 | Fused fuel/coolant mass (lead-bismuth eutectic with fuel fragments) | Po-210 production from Bi-209 activation; unique alpha hazard |
| K-159 | ~800 kg spent UO₂ fuel, ~5.3 GBq | Fuel assembly geometry may be compromised; risk of dispersal during lift |
| K-278 | Cs-137 leaking at ≤800 Bq/L; Pu in 2 torpedo warheads | Warhead integrity unknown; Pu in environment since 1994 |
| USS Thresher | Intact S5W reactor core (HEU fuel) | Weapons-grade uranium; criticality assessment required |
| USS Scorpion | S5W reactor + 2 Mk 45 torpedo warheads (Pu/U) | Warhead Pu likely corroded into insoluble form in sediment |

### 1.3 Structural Integrity Assessment Methodology

**Non-Destructive Examination (NDE) — ROV-Deployed Tools:**

1. **Ultrasonic thickness (UT) gauging** — Map remaining hull plate thickness at a minimum of 50 measurement points per hull section. Compare to original construction thickness (typically 25–50 mm HY-80/HY-100 steel for Western boats; AK-series steel for Soviet boats).

2. **Cathodic potential mapping** — Half-cell potential survey to assess active corrosion rate. Values more negative than −650 mV (Ag/AgCl) indicate active steel dissolution.

3. **Visual crack detection** — HD/4K video with structured lighting for crack/fracture identification. Map all visible hull openings, ruptures, and deformations.

4. **Acoustic emission monitoring** — Deploy contact sensors on hull during preliminary lift loading tests to detect crack propagation.

5. **Finite Element Analysis (FEA)** — Using photogrammetric 3D model and UT thickness data, construct FEA model of hull to determine:
   - Maximum safe lift loads at various attachment points
   - Residual crush depth capability
   - Predicted failure modes under lift loading

**Structural Classification:**

| Category | Criteria | Implication |
|---|---|---|
| **A — Intact** | >80% original wall thickness, no through-hull fractures | Standard lift rigging |
| **B — Degraded** | 50–80% wall thickness, localized fractures | Reinforced cradle, distributed loading |
| **C — Severely Compromised** | <50% wall thickness, major fractures/sections missing | Encapsulated lift or cut-and-raise |
| **D — Fragmented** | Multiple separated hull sections | Section-by-section recovery |

**Expected Classifications:**
- K-27: Category B–C (33 m, 44 years submerged, sealed reactor compartment)
- K-159: Category C–D (hull described as "strength of foil," 23 years submerged after 14 years rusting)
- K-278: Category B (titanium pressure hull, 37 years submerged, fractures sealed)

> **ASSUMPTION:** K-278's inner pressure hull was constructed of titanium alloy (reported for the Mike class), which has superior seawater corrosion resistance compared to the steel-hulled Soviet boats.

### 1.4 Seabed Geotechnical Survey

**Methods:**
1. **Gravity coring** — 3 m cores at 4 positions around hull footprint to determine:
   - Sediment type (clay/silt/sand/gravel)
   - Undrained shear strength (vane testing at 0.5 m intervals)
   - Consolidation properties
2. **Cone Penetration Testing (CPT)** — ROV-deployed seabed CPT (e.g., ROSON by A.P. van den Berg) for continuous strength profiling to 5 m depth
3. **Bearing capacity assessment** — Calculate ultimate bearing pressure under submarine hull and any temporary support structures (jack-up legs, mud mats)

**Site-Specific Conditions:**

| Submarine | Seabed Type | Bearing Concern |
|---|---|---|
| K-27 | Kara Sea — fine silt/clay, cold-water permafrost influence | Hull likely embedded 1–3 m into soft sediment. Suction breakout force required. |
| K-159 | Barents Sea — glacial till over bedrock, mixed sediments | Moderate bearing capacity; hull partially embedded |
| K-278 | Norwegian Sea — soft pelagic ooze/clay | Hull may have settled significantly (1–5 m). Major suction breakout force. |

**Suction Breakout Force Estimate:**
$$F_{breakout} = \gamma' \cdot A \cdot z + s_u \cdot A_{side}$$

Where:
- $\gamma'$ = effective unit weight of sediment (~5–8 kN/m³)
- $A$ = plan area of hull in contact with seabed
- $z$ = depth of embedment
- $s_u$ = undrained shear strength of sediment (typically 2–10 kPa for soft clay)
- $A_{side}$ = embedded hull surface area

For K-278 (estimated 60 m × 12 m footprint, 3 m embedment, su = 5 kPa):
$$F_{breakout} ≈ 6.5 \times 720 \times 3 + 5 \times (2 \times (60+12) \times 3) ≈ 14{,}040 + 2{,}160 = 16{,}200 \text{ kN} ≈ 1{,}650 \text{ tonnes}$$

This breakout force must be added to the lift weight.

### 1.5 Environmental Baseline Study

**Biological Survey:**
- Benthic ecology: Box-core sampling for macro/meiofauna species inventory and abundance
- Pelagic ecology: CTD casts + niskin bottle sampling for phytoplankton/zooplankton
- Megafauna: ROV video transects (minimum 4 × 500 m transects per site)
- Protected species assessment: Marine mammal observer during all vessel operations (particularly for Barents Sea sites — bowhead whales, polar bears, walrus)

**Oceanographic Baseline:**
- CTD profiling (temperature, salinity, dissolved oxygen, turbidity) on full water column
- Current meter moorings (ADCP) for minimum 30-day deployment at each site
- Tidal analysis (essential for K-27 at 33 m — shallow water is tide-sensitive)
- Wave climate analysis using satellite altimetry and hindcast data (ERA5)

**Environmental Sensitivity Mapping:**

| Site | Ecologically Sensitive Features | Seasonal Restrictions |
|---|---|---|
| K-27 (Kara Sea) | Arctic marine ecosystem; migratory bird routes; polar bear denning on Novaya Zemlya | Operations restricted to July–October (ice-free window) |
| K-159 (Barents Sea) | Cod spawning grounds; cold-water coral potential; Norwegian/Russian fisheries | Avoid March–June (spawning season) |
| K-278 (Norwegian Sea) | Deep-sea coral and sponge communities; whale migration routes | Year-round operations feasible; avoid whale calving season |

---

## Phase 2: Engineering Design

### 2.1 Lift System Architecture

#### Evaluation Matrix

| Criteria | Controlled Buoyancy | Mechanical Lift (Crane) | Hybrid (Selected for K-278) |
|---|---|---|---|
| Depth capability | Unlimited (pontoons can be deployed at any depth) | ≤3,000 m for wire rope; practical limit ~300 m for crane barges | Variable |
| Lift capacity | Up to 30,000+ tonnes (scalable with number of pontoons) | Up to ~14,200 tonnes (Heerema Sleipnir) | Combined capacity |
| Lift control | Moderate — ballast pumping rate controls ascent | Excellent — continuous winch control | Excellent |
| Risk of sudden ascent | HIGH if pontoon fails or over-blows | LOW | MODERATE |
| Historical precedent | Project Azorian (1974), Ehime Maru (2001) | Kursk (2001) — strand jack system | None at >500 m |
| Suitability for damaged hull | Good — distributed loading possible | Poor for fragile hulls — point loads | Good |

#### Selected Approach Per Submarine

**K-27 (33 m) — Mechanical Lift**
- **Rationale:** Shallow depth allows conventional crane barge operations. The Kursk precedent (108 m) used strand jacks; K-27 is shallower.
- **Equipment:** Semi-submersible heavy-lift vessel (HLV) with strand jack system (26 units × 900 t each = 23,400 t capacity), or floating crane barge (e.g., Saipem S7000: 14,000 t capacity).
- **Method:** Thread 26 steel strand cables through pre-cut holes in hull, anchor to lifting yoke on HLV platform. Lift using synchronized strand jacks. Transfer to submersible barge for transport.
- **Contingency:** If hull too fragile for strand jack penetrations, construct external steel cradle lowered around hull.

**K-159 (200 m) — Hybrid Approach**
- **Rationale:** Hull integrity is extremely poor ("strength of foil"). Cannot apply point loads. Needs distributed support.
- **Equipment:** Custom-built lifting cradle (steel frame with nylon slings) + controlled buoyancy pontoons + surface-vessel strand jacks.
- **Method:**
  1. ROV positions cradle sections around hull on seabed
  2. Connect cradle halves beneath hull (may require jetting/excavation of sediment under hull)
  3. Attach 4–8 syntactic foam buoyancy modules (rated to 300 m) to cradle — modules provide ~60% of lift force
  4. Surface vessel strand jacks provide remaining 40% + control
  5. Slow controlled ascent at ≤5 m/min
- **Contingency:** If hull disintegrates during rigging, switch to reactor compartment-only recovery (cut fore and aft, raise 40 m section containing reactors).

**K-278 Komsomolets (1,680 m) — Controlled Buoyancy (Primary) + Surface Tethered Control**
- **Rationale:** At 1,680 m, crane operations are impractical. The titanium hull is reasonably intact. Controlled buoyancy is the only viable primary lift method at this depth.
- **Equipment:** 
  - 12–16 deep-rated buoyancy pontoons (steel tanks, rated to 2,000 m, ~500 t buoyancy each)
  - Syntactic foam collar modules for additional distributed buoyancy
  - Surface Dynamic Positioning (DP) vessel with 2,000 m wire rope winch for ascent rate control and lateral positioning
- **Method:**
  1. ROV attaches steel rigging straps at 8 predetermined hard points along hull
  2. Pontoons lowered in flooded condition, attached to rigging
  3. Pontoons sequentially deballasted using compressed air via umbilical from surface
  4. Lift force applied gradually — begin with breakout from seabed at 110% of submerged weight + suction
  5. Ascent controlled at ≤2 m/min by metering air supply and using surface tether as brake
  6. At 100 m depth, transfer to HLV crane for final lift to surface
- **Contingency:** Emergency flood valves on every pontoon — can arrest ascent within 30 seconds. Ascent abort procedure at every 200 m depth interval.

### 2.2 Rigging & Attachment Point Design

**Hull Cradle Design — Universal Template**

```
    ┌──────────────────── LIFTING YOKE ────────────────────┐
    │    │    │    │    │    │    │    │    │    │    │      │
    │    ▼    ▼    ▼    ▼    ▼    ▼    ▼    ▼    ▼    ▼      │
    │  ┌────────────────────────────────────────────────┐  │
    │  │              SPREADER BEAM                     │  │
    │  └──┬──────┬──────┬──────┬──────┬──────┬────────┘  │
    │     │      │      │      │      │      │            │
    │     ▼      ▼      ▼      ▼      ▼      ▼            │
    │   ╔══════════════════════════════════════════╗       │
    │   ║           SUBMARINE HULL                ║       │
    │   ╚══════════════════════════════════════════╝       │
    │     ▲      ▲      ▲      ▲      ▲      ▲            │
    │     │      │      │      │      │      │            │
    │  ┌──┴──────┴──────┴──────┴──────┴──────┴────────┐  │
    │  │            BELLY CRADLE FRAME                 │  │
    │  └───────────────────────────────────────────────┘  │
    └──────────────────────────────────────────────────────┘
```

**Design Parameters:**

| Parameter | K-27 | K-159 | K-278 |
|---|---|---|---|
| Hull length | 109.8 m | ~107 m | 117.5 m |
| Hull beam (est.) | ~8 m | ~8 m | ~10 m |
| Cradle length | 100 m (excl. bow/stern) | 100 m | 110 m |
| Cradle material | S355 structural steel | S355 with HDPE padding | Titanium-compatible steel (cathodic protection required) |
| Number of sling loops | 12 (paired, 6 per side) | 16 (distributed for fragile hull) | 12 |
| Sling material | Dyneema SK-78 (290 t WLL per sling) | Nylon-polyester composite (200 t WLL, shock-absorbing) | Dyneema SK-78 |
| Safety factor | 3.0 | 4.0 (higher due to hull fragility) | 3.0 |

**Load Distribution Analysis:**

For a uniformly distributed load on a simply supported cradle, the bending moment diagram is parabolic:

$$M_{max} = \frac{wL^2}{8}$$

Where $w$ = distributed weight per meter of hull, $L$ = span between support points.

For K-278: $w = 8{,}000 \text{ t} / 117.5 \text{ m} ≈ 68 \text{ t/m}$, but weight is concentrated in reactor/weapons compartments. FEA model must account for actual weight distribution.

> **CRITICAL:** Rigging attachment MUST avoid the reactor compartment zone (typically frames 35–55 in Soviet submarines). All sling loads must pass around this area with spreader bars maintaining 3 m minimum clearance from reactor compartment hatches.

### 2.3 Structural Reinforcement Plan

**For K-159 (Category C–D hull):**

Since the hull lacks structural integrity for a conventional lift, the following reinforcement strategy is proposed:

1. **External steel strongback system:**
   - Pre-fabricated in 10 m sections, lowered to seabed, assembled around hull by ROV
   - I-beam longitudinal runners (HEM 600) welded to transverse ring frames at 5 m intervals
   - Ring frames clamp around hull circumference — bolted closure (not welded to hull)
   - System creates an exoskeleton transferring load from cradle to ring frames to hull

2. **Internal flooding control:**
   - Assume hull is fully flooded (adds ~2,000–3,000 m³ water = 2,000–3,000 t)
   - Net lift weight ≈ 4,750 t (submerged displacement) — hull is already at neutral buoyancy when flooded
   - Partial dewatering of non-reactor compartments possible via compressed air to reduce lift weight
   - **DO NOT dewater reactor compartment** — maintain water as radiation shielding and thermal buffer

3. **Hull consolidation at fracture points:**
   - Apply steel doubler plates over major fractures using ROV-operated hydraulic bolt guns
   - Inject marine-grade epoxy (e.g., Belzona 1111) into accessible cracks
   - Wrap critical hull sections with Kevlar composite belting

### 2.4 Reactor Compartment Containment Strategy

This is the single most critical engineering subsystem.

**Containment Philosophy:** The reactor compartment must be treated as a sealed unit. No breaching, cutting, or penetration of the reactor compartment is permitted during subsea operations. All radiological work occurs after the hull is in drydock.

**Containment Barriers:**

| Barrier | Description | Application |
|---|---|---|
| **Primary** | Existing reactor pressure vessel + fuel cladding | Already in place (unless breached) |
| **Secondary** | Reactor compartment bulkheads (hull structure) | Assessment required — reinforce if needed |
| **Tertiary** | Fabricated steel cofferdam — sealed enclosure welded/bolted over reactor compartment section | Installed subsea by ROV prior to lift |
| **Quaternary** | Containment barge — fully enclosed dry-transport compartment | Submarine placed inside for transit |

**Cofferdam Design (K-278 Example):**

A cofferdam is a watertight enclosure placed over the reactor compartment section of the hull to provide an additional containment barrier during lift and transport.

- **Dimensions:** 30 m (L) × 14 m (W) × 14 m (H) — sufficient to enclose reactor compartment with 2 m clearance all around
- **Material:** 12 mm marine-grade steel (Grade A shipbuilding steel)
- **Assembly:** Pre-fabricated in two halves (clamshell design), lowered to seabed, closed and sealed around hull section by ROV using hydraulic flange bolts and inflatable gaskets
- **Features:**
  - Pressure relief valve (prevents overpressure during ascent)
  - Sampling port (allows water sampling from inside cofferdam during ascent)
  - Drain valve (for controlled dewatering in drydock)
  - Sacrificial anodes for corrosion protection during transit

### 2.5 Load Path Analysis & Lift Dynamics

**Static Load Analysis:**

| Submarine | Submerged Weight (t) | Est. Suction Force (t) | Total Breakout Load (t) | Lift System Capacity Required (t) |
|---|---|---|---|---|
| K-27 | ~300 (net buoyancy after flooding) | 200–400 | 500–700 | 2,100 (3.0 SF) |
| K-159 | ~200 (net) | 300–600 | 500–800 | 3,200 (4.0 SF) |
| K-278 | ~500 (net, titanium hull — denser) | 1,500–2,000 | 2,000–2,500 | 7,500 (3.0 SF) |

> **NOTE:** Submerged weight is much less than displacement because the flooded hull is near neutral buoyancy. The primary forces are suction/adhesion to seabed and residual negative buoyancy from hull steel and machinery.

**Dynamic Load Factors:**

During lift, dynamic forces arise from:
1. **Wave-induced vessel motions** (heave, pitch, roll) — transmitted through lifting cables
2. **Current loading** on hull during ascent
3. **Vortex-induced vibrations** on cables

Dynamic Amplification Factor (DAF) per depth zone:

| Depth Zone | Wave Effect | Current Effect | DAF |
|---|---|---|---|
| 0–50 m | SEVERE | Moderate | 2.0 |
| 50–200 m | Moderate | Low | 1.5 |
| 200–500 m | Low | Low | 1.2 |
| >500 m | Negligible | Negligible | 1.1 |

**Maximum design load = Static breakout load × DAF × Safety Factor**

For K-278 at surface transition: $2{,}500 \times 2.0 \times 1.5 = 7{,}500 \text{ t}$

### 2.6 Contingency for Lift Abort

**Decision Gates During Ascent:**

| Depth (m) | Gate | Go/No-Go Criteria |
|---|---|---|
| Seabed | Breakout | Load cell readings within 120% of predicted. No asymmetric loading (>10% variation between attachment points). |
| 1,500 | Initial ascent | Ascent rate stable. No anomalous stresses on rigging. Radiological sensors nominal. |
| 1,000 | Mid-water | All systems nominal. Weather window confirmed >24 hr remaining. |
| 500 | Deep transition | Transfer from pontoon-only to hybrid control. All strand jacks engaged. |
| 200 | Pre-wave zone | Dynamic loading within design envelope. Hull acoustic emissions nominal. |
| 100 | Wave zone entry | Sea state ≤4 (Hs < 2.5 m). All vessel DP systems fully operational. |
| 50 | Near-surface | Final commitment point. Transfer to HLV crane if applicable. |
| 0 | Surface | Hull secured on transport vessel/barge. |

**Abort Procedure:**
1. **HOLD:** Arrest ascent. Maintain current depth. Assess situation.
2. **CONTROLLED DESCENT:** If abort required, re-flood pontoons at controlled rate. Return submarine to seabed.
3. **EMERGENCY DROP:** If catastrophic rigging failure — jettison controlled buoyancy. Submarine returns to seabed under gravity. Accept hull damage as preferable to uncontrolled surface broach.
4. **NEVER** allow uncontrolled free ascent — risk of hull implosion reversal (hull implodes on sinking, but rapid ascent can cause structural failure due to internal pressure exceeding external).

---

## Phase 3: Radiological & Environmental Safety

### 3.1 Radiological Characterization & Hazard Classification

**Source Term Estimates:**

| Submarine | Reactor Type | Fuel Type | Est. Activity (2026) | Dominant Isotopes |
|---|---|---|---|---|
| K-27 | 2 × VT-1 (Pb-Bi cooled) | UO₂ + metallic alloy, fused with Pb-Bi | ~100–500 GBq | Cs-137, Sr-90, Po-210 (from Bi activation), Pu isotopes |
| K-159 | 2 × VM-A (PWR) | Ceramic UO₂ pellets in Zr-alloy cladding | ~5.3 GBq (reported) | Cs-137, Sr-90, Co-60 (activation products) |
| K-278 | 1 × OK-650b-3 (PWR) | Ceramic UO₂, likely enriched | ~50–200 GBq (estimate) | Cs-137, Sr-90 + Pu-239 from warheads |
| USS Thresher | 1 × S5W (PWR) | Plate-type HEU (93% enriched) | ~10–100 GBq | Cs-137, Sr-90; HEU poses criticality concern |
| USS Scorpion | 1 × S5W (PWR) + 2 Mk 45 warheads | HEU plates + Pu pits | ~10–100 GBq + warhead materials | Cs-137, Sr-90, Pu-239/241, Am-241 |

**IAEA Hazard Classification:**

All submarines are classified as **Category 1 — Dangerous Sources** (capable of causing permanent injury or death from exposure) due to reactor fuel inventories.

K-27 is additionally classified as having **criticality risk** due to the unknown geometry of fuel/coolant mass.

> **CRITICAL SAFETY CONCERN:** K-27's liquid-metal-cooled reactors used lead-bismuth eutectic (LBE) as coolant. When the reactor overheated in 1968, ~20% of the fuel ruptured and mixed with the LBE coolant, creating a solidified fuel/metal matrix (corium analogue). This mass cannot be geometrically characterized without physical access. **Criticality analysis required before any operation that could alter the geometry of this mass** (e.g., tilting during lift, mechanical shock).

### 3.2 Containment Hierarchy

**Defense-in-Depth Model:**

```
    Level 5: ┌─────────────────────────────────────┐
    EMERGENCY│  Emergency response / evacuation     │
             └──────────────────┬──────────────────┘
    Level 4: ┌──────────────────▼──────────────────┐
    TRANSPORT│  Containment barge / shielded vessel │
             └──────────────────┬──────────────────┘
    Level 3: ┌──────────────────▼──────────────────┐
    COFFERDAM│  Fabricated steel cofferdam          │
             └──────────────────┬──────────────────┘
    Level 2: ┌──────────────────▼──────────────────┐
    HULL     │  Reactor compartment bulkheads       │
             └──────────────────┬──────────────────┘
    Level 1: ┌──────────────────▼──────────────────┐
    CORE     │  Reactor pressure vessel + fuel clad │
             └─────────────────────────────────────┘
```

For each submarine, the status of each barrier level is assessed:

| Barrier | K-27 | K-159 | K-278 |
|---|---|---|---|
| Level 1: RPV + fuel | COMPROMISED (fuel melted into coolant) | DEGRADED (23+ years deterioration) | LIKELY INTACT |
| Level 2: Compartment bulkheads | SEALED (bitumen/furfuryl alcohol, 1982) | COMPROMISED (hull "strength of foil") | DEGRADED (fractures, sealed 2019) |
| Level 3: Cofferdam | TO BE INSTALLED | TO BE INSTALLED | TO BE INSTALLED |
| Level 4: Transport containment | TO BE DESIGNED | TO BE DESIGNED | TO BE DESIGNED |
| Level 5: Emergency | TO BE PLANNED | TO BE PLANNED | TO BE PLANNED |

### 3.3 Personnel Dosimetry & ALARA Planning

**ALARA (As Low As Reasonably Achievable) — Dose Limits:**

| Personnel Category | Annual Dose Limit | Per-Operation Limit | Action Level |
|---|---|---|---|
| Radiation workers (Category A) | 20 mSv (IAEA BSS) | 5 mSv |2 mSv triggers review |
| Radiation workers (Category B) | 6 mSv | 1.5 mSv | 0.5 mSv triggers review |
| General crew (non-rad workers) | 1 mSv | 0.25 mSv | 0.1 mSv triggers review |
| Public (environmental) | 1 mSv/yr above background | N/A | Any measurable increase |

**ALARA Implementation:**

1. **Time:** Minimize personnel time near radiation sources. All subsea work performed by ROV. Surface operations near reactor compartment limited to ≤2 hours per worker per day.

2. **Distance:** Maintain exclusion zones around reactor compartment:
   - Red zone (0–5 m): No personnel except essential rad workers with full PPE
   - Orange zone (5–25 m): Supervised area, dosimetry required
   - Green zone (>25 m): Unrestricted

3. **Shielding:** 
   - Seawater provides excellent shielding during subsea phase (~7 cm of water = 1 TVL for Cs-137 gamma)
   - At surface: cofferdam + water flooding of cofferdam annulus maintained as shielding
   - Transport: lead/concrete shielding modules placed adjacent to reactor compartment on transport barge

4. **Monitoring:**
   - All personnel: Electronic personal dosimeter (EPD) + TLD badge
   - Continuous area monitoring: Fixed gamma/neutron detectors around work zones
   - Real-time telemetry to Radiation Protection Officer (RPO) on support vessel
   - Bioassay program: Urinalysis for tri-weekly for alpha-emitters (Pu, Am, Po)

### 3.4 Environmental Impact Assessment & Mitigation

**Potential Environmental Impacts:**

| Impact | Likelihood | Consequence | Mitigation |
|---|---|---|---|
| Sediment disturbance releasing contaminated particles | HIGH | MODERATE | Silt curtains around work area; real-time turbidity monitoring |
| Radiological release during lift | LOW-MODERATE | HIGH | Cofferdam containment; water sampling during ascent at 5-min intervals |
| Noise impact on marine mammals | MODERATE | LOW-MODERATE | Marine mammal observers; soft-start procedures; exclusion zone (500 m) |
| Fuel/oil spill from submarine systems | LOW | LOW | All fuel tanks likely empty (consumed or leaked post-sinking); containment boom standby |
| Anchor/mooring damage to seabed | LOW | LOW | DP vessels preferred; where anchoring required, pre-survey anchor corridor |

**Environmental Monitoring During Operations:**
- Continuous water sampling at 4 points around submarine during all lift operations
- Turbidity sensors (3 NTU trigger level for work stoppage)
- Sediment trap deployment 100 m downstream for post-event analysis
- Post-operation survey comparing to pre-operation baseline (re-survey same grid)

### 3.5 Emergency Response Procedures

**Scenario Matrix:**

| Emergency | Detection | Immediate Response | Escalation |
|---|---|---|---|
| **Radiological release detected during subsea ops** | ROV-mounted radiation sensors; water sample analysis | Suspend all subsea work. Pull ROVs to safe distance. Assess source. | Activate cofferdam pre-placement if not already installed. Notify IAEA. |
| **Cofferdam breach during lift** | Pressure sensors inside cofferdam; radiation monitors in surrounding water | Arrest ascent (HOLD). Sample water inside and outside cofferdam. | If release confirmed: controlled descent to seabed for repair. |
| **Rigging failure — partial** | Load cell on failed sling drops to zero; alarm on load monitoring system | Arrest ascent. Redistribute load. Assess remaining rigging capacity. | If >2 slings failed: controlled descent (abort). |
| **Rigging failure — catastrophic** | Sudden load drop on all sensors | Emergency: submarine falls. All vessels clear from overhead position. | Search and recovery of submarine on seabed. Reassess hull condition. |
| **Criticality event (K-27)** | Neutron detector spike; gamma dose rate increase | EVACUATE all personnel to >1 km distance. Notify flagstate + IAEA. | K-27 specific: if criticality detected at any phase — ABORT OPERATION. Re-characterize fuel geometry. |
| **Hull breakup during lift** | Acoustic emission sensors; visual (ROV camera); asymmetric load distribution | Arrest ascent. Assess damage. Decide: proceed cautiously or abort. | If reactor compartment separates: stabilize RC independently; lower remaining hull. |
| **Adverse weather** | Meteorological forecasting; vessel motion sensors | If sea state exceeds operational limit — execute weather abort procedure | If submarine mid-ascent: fast-track to surface if within 100 m; otherwise controlled descent. |

### 3.6 Waste Management & Disposal Pathway

**Waste Classification:**

| Waste Type | Source | Classification (IAEA) | Disposal Route |
|---|---|---|---|
| Spent nuclear fuel | Reactor cores | High-Level Waste (HLW) | National spent fuel reprocessing or deep geological repository |
| Activated reactor components | Pressure vessel, internals | Intermediate-Level Waste (ILW) | Engineered near-surface or intermediate-depth facility |
| Contaminated hull steel | Reactor compartment sections | Low-Level Waste (LLW) | Near-surface disposal or melt/decontamination for recycling |
| Contaminated seabed sediment | Beneath wreck footprint | Very Low-Level Waste (VLLW) or LLW | Landfill (VLLW) or near-surface disposal |
| Liquid effluent | Cofferdam drainage, decontamination water | Liquid LLW | Treatment, discharge within authorized limits |
| Nuclear weapons components | Torpedo warheads, missile warheads | Special Nuclear Material (SNM) | Warhead disassembly facility (military) |

**Disposal Facility Requirements:**

- Russian submarines (K-27, K-159, K-278): Sayda Bay or Murmansk NPO facilities (established infrastructure from Kursk decommissioning)
- American submarines (Thresher, Scorpion): Puget Sound Naval Shipyard or Hanford Site
- Warhead materials: Respective national weapons establishments

---

## Phase 4: Operational Execution Plan

### 4.1 Fleet Composition

**K-27 Salvage Fleet (Shallow — 33 m):**

| Vessel | Type | Role | Est. Charter Rate |
|---|---|---|---|
| **HLV (Heavy Lift Vessel)** | Semi-submersible crane vessel (e.g., Heerema Thialf) | Primary lift platform | $300,000–500,000/day |
| **DSV (Dive Support Vessel)** | DP2, with saturation diving system | Diver intervention at 33 m + ROV support | $150,000/day |
| **Survey Vessel** | DP1, with moon pool | Pre-operation survey; environmental monitoring | $50,000/day |
| **Tug × 2** | Ocean-going, 80+ t bollard pull | Tow management, standby | $25,000/day each |
| **Guard Vessel** | Patrol/supply vessel | Safety zone enforcement, personnel transfer | $15,000/day |
| **Transport Barge** | Submersible heavy transport barge (e.g., Boskalis Vanguard) | Receive and transport submarine | $200,000/day |
| **Nuclear Support Vessel** | Custom/chartered | Rad monitoring lab, waste storage, decontamination | $100,000/day |

**K-159 Salvage Fleet (200 m):**
Similar to K-27 but DSV replaced with dedicated ROV vessel (no divers at 200 m), and additional ROV spread for reinforcement work.

**K-278 Salvage Fleet (1,680 m):**
- No DSV (beyond diving depth)
- 2 × ROV support vessels (4–6 work-class ROVs total)
- Purpose-built or modified buoyancy control vessel
- Additional DP2 vessel for pontoon deployment
- All other support vessels as above

### 4.2 Personnel Requirements

**K-27 Operation (Representative):**

| Role | Number | Rotation | Certification Required |
|---|---|---|---|
| Project Manager | 1 | Shore-based + site visits | Naval engineering + salvage experience |
| Operations Manager (offshore) | 2 | 28/28 rotation | Master Mariner + salvage |
| Salvage Master | 2 | 28/28 | ISM salvage master certification |
| Radiation Protection Officer | 4 | 14/14 | IAEA-certified RPO; national dosimetry license |
| Health Physicist | 2 | 28/28 | M.Sc. health physics minimum |
| Nuclear Engineer | 4 | 28/28 | Reactor operations experience (naval preferred) |
| Crane operator / strand jack operator | 8 | 28/28 | LEEA-certified; strand jack competency |
| ROV pilots | 8 | 28/28 | IMCA R004/R005 competent |
| Commercial divers (K-27 only) | 12 | 28/28 | IMCA-certified; nuclear rad-worker training |
| Marine crew (per vessel) | 20–30 | 28/28 | STCW certified |
| Structural engineer | 2 | 28/28 | PE/CEng |
| Rigging superintendent | 2 | 28/28 | LEEA rigging |
| Environmental scientist | 2 | 28/28 | Marine ecology/chemistry |
| Medic | 2 | 28/28 | Offshore medic + rad exposure first response |
| Communications/logistics | 4 | 28/28 | — |
| **Total offshore personnel** | **~80–100** | | |

### 4.3 Operational Sequence with Decision Gates

**K-27 Operational Timeline:**

```
PHASE    TASK                                    DURATION    GATE
─────────────────────────────────────────────────────────────────
1.0      Mobilization & transit to site          14 days
                                                            ──► G1: Site confirmed accessible
1.1      Environmental baseline survey           14 days
1.2      Detailed hull survey (ROV + divers)     21 days
1.3      Radiological characterization           14 days
1.4      Geotechnical survey                     7 days
                                                            ──► G2: Proceed to engineering?
                                                                 - Hull classified (A/B/C/D)
                                                                 - Rad levels characterized
                                                                 - Lift method confirmed
─────────────────────────────────────────────────────────────────
2.0      Cofferdam fabrication (shore)           90 days     (parallel with Phase 1)
2.1      Cradle fabrication (shore)              90 days     (parallel with Phase 1)
2.2      Cofferdam installation (subsea)         21 days
2.3      Cradle/rigging installation             28 days
2.4      Reinforcement works (if Cat B/C hull)   21 days
                                                            ──► G3: Ready to lift?
                                                                 - All rigging installed & proof-loaded
                                                                 - Cofferdam sealed & tested
                                                                 - Transport barge on station
                                                                 - Weather window ≥72 hr confirmed
─────────────────────────────────────────────────────────────────
3.0      Breakout from seabed                    1 day
3.1      Lift to surface                         1 day
3.2      Transfer to transport barge             2 days
                                                            ──► G4: Transport?
                                                                 - Submarine secured on barge
                                                                 - Rad containment verified
                                                                 - Transit route & berth confirmed
─────────────────────────────────────────────────────────────────
4.0      Transit to disposal facility            7–14 days
4.1      Offload to drydock                      3 days
4.2      Reactor defueling & decommissioning     180–365 days
─────────────────────────────────────────────────────────────────
         TOTAL (excl. decommissioning):          ~6–8 months
         TOTAL (incl. decommissioning):          ~18–24 months
```

### 4.4 Weather Window Analysis

| Site | Operational Season | Sea State Limit | Wind Limit | Ice Considerations |
|---|---|---|---|---|
| K-27 (Kara Sea) | July–October | Hs ≤ 2.0 m for lift; ≤ 3.0 m for positioning | ≤ 25 kt sustained | Ice-free window limited; icebreaker escort may be required in transit |
| K-159 (Barents Sea) | May–October | Hs ≤ 2.5 m for lift; ≤ 4.0 m for positioning | ≤ 30 kt sustained | Generally ice-free; monitor polar lows |
| K-278 (Norwegian Sea) | April–September | Hs ≤ 2.0 m for near-surface phase | ≤ 25 kt sustained | No ice; North Atlantic storm systems are primary concern |

**Historical Weather Data (P50/P90):**

Using ERA5 reanalysis data for the Kara Sea (K-27 site):
- July: Hs(P50) = 0.8 m, Hs(P90) = 1.8 m — **OPTIMAL MONTH**
- August: Hs(P50) = 1.0 m, Hs(P90) = 2.2 m — Good
- September: Hs(P50) = 1.4 m, Hs(P90) = 3.0 m — Marginal
- October: Hs(P50) = 1.8 m, Hs(P90) = 4.0 m — Risky

**Recommendation:** Schedule K-27 lift for mid-July of the operational year.

### 4.5 Communications & Command Structure

```
                    ┌───────────────────────┐
                    │  NATIONAL AUTHORITY    │
                    │  (Rosatom / US Navy)   │
                    └───────────┬───────────┘
                                │
                    ┌───────────▼───────────┐
                    │  PROJECT DIRECTOR      │
                    │  (Shore HQ)            │
                    └───────────┬───────────┘
                                │
              ┌─────────────────┼──────────────────┐
              │                 │                  │
    ┌─────────▼───────┐ ┌──────▼──────┐ ┌────────▼────────┐
    │ SALVAGE MASTER  │ │ RADIATION   │ │ MARINE OPS      │
    │ (Offshore IC)   │ │ PROTECTION  │ │ COORDINATOR     │
    │                 │ │ OFFICER     │ │                 │
    └────────┬────────┘ └──────┬──────┘ └────────┬────────┘
             │                 │                  │
    ┌────────▼────────┐  ┌────▼─────┐   ┌───────▼────────┐
    │ Crane/Lift Ops  │  │ Rad Mon  │   │ Vessel Masters  │
    │ ROV Ops         │  │ Health   │   │ Tug Masters     │
    │ Rigging         │  │ Physics  │   │ DP Operators    │
    │ Dive Ops (K-27) │  │ Survey   │   │ Met Officer     │
    └─────────────────┘  └──────────┘   └────────────────┘
```

**Communications Plan:**
- Primary: VSAT broadband (Inmarsat Fleet Xpress) — data/voice/video
- Secondary: Iridium satellite phone — voice backup
- Emergency: VHF Channel 16 (distress), GMDSS EPIRB
- Internal: Encrypted digital UHF radio net (3 channels: Operations, Safety, General)
- ROV control: Fiber-optic umbilical (primary) + acoustic telemetry (backup)

**Reporting Schedule:**
- Daily progress report to Project Director
- Weekly report to National Authority
- Immediate reporting: Any radiological alarm, safety incident, or gate decision

---

## Phase 5: Transport & Disposition

### 5.1 Wet-Tow vs. Heavy-Lift Transport

**Decision Matrix:**

| Factor | Wet-Tow | Heavy-Lift Transport (Barge) | Recommended |
|---|---|---|---|
| K-27 (33 m depth, short transit to Sayda Bay) | Possible but hull too weak | **SELECTED** — load onto submersible barge | Barge |
| K-159 (200 m, transit to Sayda Bay/Murmansk) | Hull cannot survive tow | **SELECTED** | Barge |
| K-278 (1,680 m, transit to Norway/Russia) | Not feasible (no bow integrity) | **SELECTED** | Barge |
| Kursk (historical) | Hull towed at 2 kts below HLV Giant 4 | — | (Ref. only) |

**Selected Transport Method: Submersible Heavy Transport Barge**

The Kursk salvage used the Giant 4 barge with the hull suspended beneath the HLV. Given the fragile condition of these submarines, a submersible barge (e.g., Boskalis Vanguard or COSCO Xia Zhi Yuan 6) is preferred:

1. Barge ballasts down to submerge its deck
2. Submarine (in cradle) placed on deck while still at shallow submergence
3. Barge deballasts to raise deck and submarine above waterline
4. Transit at 4–8 knots under tug escort
5. At destination, barge enters drydock or berths alongside and cranes offload submarine

### 5.2 Receiving Facility Requirements

**Minimum Requirements for Drydock/Berth:**

| Requirement | Specification |
|---|---|
| Drydock length | ≥ 150 m (to accommodate barge + submarine) |
| Drydock width | ≥ 25 m |
| Crane capacity | ≥ 500 t (for reactor compartment handling) |
| Radiological lab | On-site or within 50 km; gamma spectrometry, alpha spectrometry |
| Spent fuel storage | Licensed wet or dry storage facility |
| Decontamination bay | Wash-down with filtered water capture; HEPA ventilation |
| Waste storage | Licensed ILW/LLW storage pads |
| Security | Restricted nuclear site; IAEA safeguards if weapons material present |

**Candidate Facilities:**

| Submarine | Recommended Facility | Backup | Distance |
|---|---|---|---|
| K-27 | Sayda Bay, Murmansk Oblast | Nerpa Shipyard, Snezhnogorsk | ~500 km from wreck |
| K-159 | Nerpa Shipyard (SRZ-10) | Sayda Bay | ~300 km from wreck |
| K-278 | Nerpa Shipyard or Norwegian facility (diplomatic negotiation req'd) | Arkhangelsk | ~1,200 km from wreck |
| USS Thresher | Puget Sound Naval Shipyard (Bremerton, WA) | Norfolk Naval Shipyard | ~5,000 km from wreck |
| USS Scorpion | Puget Sound Naval Shipyard | Norfolk Naval Shipyard | ~6,000 km from wreck |

### 5.3 Reactor Defueling & Decommissioning Sequence

**Standard Procedure (per reactor):**

```
Step 1:  Open reactor compartment access (drydock, full rad controls)
         ↓
Step 2:  Flood reactor compartment for shielding if not already flooded
         ↓
Step 3:  Remove reactor vessel head bolts (remotely operated tooling)
         ↓
Step 4:  Lift reactor vessel head using shielded crane
         ↓
Step 5:  Remove fuel assemblies using long-handled tools into shielded cask
         ↓
Step 6:  Transfer fuel to spent fuel storage pool
         ↓
Step 7:  Decontaminate reactor internals
         ↓
Step 8:  Section reactor compartment for disposal (ILW)
```

**K-27 Special Procedure:**

K-27's reactor cannot follow the standard procedure because the fuel is fused with the lead-bismuth coolant in a solidified mass. Alternative approach:

1. CT-scan the sealed reactor compartment using industrial radiography to map the fuel/coolant mass geometry
2. Perform criticality safety analysis based on actual geometry
3. If safe: cut the entire reactor/coolant/fuel block as a monolithic unit using underwater plasma cutting or diamond wire
4. Encapsulate the monolithic blocks in steel/concrete overpack
5. Transfer to deep geological repository or RADON-type engineered storage facility

> **HISTORICAL PRECEDENT:** Russia raised the Alfa-class submarine K-123 and dealt with a similar lead-bismuth-fused-fuel situation. The entire reactor compartment was sealed and stored at Sayda Bay.

### 5.4 Hull Dismantlement or Preservation Plan

After reactor compartment removal, the remaining hull can be:

| Option | Application | Process |
|---|---|---|
| **Radiological survey + free release** | Hull sections confirmed below clearance levels (<1 Bq/g for Cs-137) | Cut into sections, decontaminate, recycle as scrap steel |
| **Controlled disposal** | Hull sections above clearance but below LLW limits | Cut into sections, package, dispose at LLW facility |
| **Museum preservation** | Historically significant hulls (e.g., Komsomolets) | Full decontamination, preservation treatment, transport to museum site |

### 5.5 Final Waste Disposition & Site Remediation

**Post-Salvage Seabed Remediation:**

1. Re-survey wreck site using ROV/AUV — map any debris remaining
2. Collect all recoverable debris (hull fragments, equipment)
3. Sediment sampling on the wreck footprint: 1 m × 1 m grid, cores to 1 m depth
4. If contaminated sediment found: dredge and contain in sealed drums for shore disposal
5. If clean: leave seabed to natural recovery
6. 5-year post-remediation monitoring program (annual surveys)

---

## Phase 6: Risk Management

### 6.1 Risk Register

**Likelihood × Consequence Matrix:**

| | Negligible (1) | Minor (2) | Moderate (3) | Major (4) | Catastrophic (5) |
|---|---|---|---|---|---|
| **Almost Certain (5)** | 5 | 10 | 15 | 20 | **25** |
| **Likely (4)** | 4 | 8 | 12 | **16** | **20** |
| **Possible (3)** | 3 | 6 | 9 | **12** | **15** |
| **Unlikely (2)** | 2 | 4 | 6 | 8 | 10 |
| **Rare (1)** | 1 | 2 | 3 | 4 | 5 |

**Risk Score: ≥12 = HIGH (red), 6–11 = MEDIUM (amber), 1–5 = LOW (green)**

### 6.2 Top 10 Risks with Mitigation

| # | Risk | L | C | Score | Mitigation |
|---|---|---|---|---|---|
| R1 | Hull disintegrates during lift (K-159) | 4 | 4 | **16** | Pre-reinforce with exoskeleton; design cradle for full hull retention; reactor-compartment-only backup plan |
| R2 | Criticality event in K-27 fuel/coolant mass | 1 | 5 | **5** | Pre-lift criticality analysis; neutron monitoring; no operations that alter fuel geometry without prior analysis |
| R3 | Radiological release during lift | 3 | 4 | **12** | Cofferdam containment; continuous monitoring; abort procedure |
| R4 | Rigging failure — catastrophic drop | 2 | 5 | **10** | 3.0–4.0 safety factors; proof loading; redundant slings; regular inspection |
| R5 | Adverse weather during near-surface phase | 3 | 3 | **9** | Operational weather window; 72-hr forecast gate; fast transit through wave zone |
| R6 | Geopolitical/diplomatic obstruction | 3 | 4 | **12** | Early diplomatic engagement; IAEA mediation; bilateral agreements |
| R7 | Nuclear weapon warhead instability during handling | 2 | 5 | **10** | No direct warhead handling subsea; weapons recovery only in controlled drydock; military EOD team embedded |
| R8 | Vessel collision in operating area | 2 | 3 | **6** | Safety exclusion zone (NOTAM/NAVTEX); guard vessel; AIS monitoring |
| R9 | ROV entanglement in wreck | 4 | 2 | **8** | Debris survey pre-operation; cable management; backup ROV on standby |
| R10 | Cost overrun >50% of budget | 4 | 3 | **12** | Phase-gated funding approval; 30% contingency; fixed-price contracts where possible |

### 6.3 Insurance & Liability Framework

**Required Insurance Coverages:**

| Coverage | Application | Estimated Limit |
|---|---|---|
| P&I (Protection & Indemnity) | Third-party liability, pollution | $1 billion |
| Hull & machinery | Salvage fleet vessels | Per vessel valuation |
| Nuclear liability | Per Paris/Vienna Conventions | $700 million (operator) + state supplement |
| Environmental liability | Pollution remediation costs | $500 million |
| Workers' compensation | Radiation exposure claims | Per national regulation |
| Professional indemnity | Engineering/design errors | $100 million |

**Liability Regime:**
- Russian submarines: Russian Federation as flag state bears primary liability under the 1963 Vienna Convention on Civil Liability for Nuclear Damage (Russia acceded 2005)
- US submarines: US Government as sovereign operator — liability under the Price-Anderson Act for nuclear incidents
- International waters operations: Flag-state responsibility applies; UNCLOS Article 235 (responsibility for protection of marine environment)

### 6.4 Regulatory Approval Pathway

**K-27/K-159 (Russian-flag submarines):**

```
Step 1:  Rosatom proposal + safety case submission ───→ 6 months
Step 2:  Russian nuclear regulator (Rostechnadzor) review ───→ 12 months
Step 3:  Environmental Impact Assessment (EIA) per Russian law ───→ 6 months
Step 4:  IAEA notification (London Convention, OSPAR) ───→ 3 months
Step 5:  Norwegian consultation (Barents Sea / boundary areas) ───→ 6 months
Step 6:  Operational license granted ───→ Total ~24–30 months
```

**K-278 (Soviet/Russian-flag, Norwegian Sea):**
Additional: Norwegian Environmental Agency (Miljødirektoratet) approval; OSPAR Commission notification; potential Arctic Council consultation.

**USS Thresher / Scorpion (US-flag):**
- US Navy authorization (NAVSEA)
- NRC consultation (civilian nuclear regulatory oversight)
- EPA / NOAA environmental permits
- Congressional notification (significant budget)

---

## Phase 7: Budget Estimate

### 7.1 Cost Breakdown by Phase

**K-27 Estimated Cost (Shallow, 33 m):**

| Phase | Duration | Estimated Cost (USD) |
|---|---|---|
| Phase 1: Reconnaissance & Assessment | 3 months | $25–35 million |
| Phase 2: Engineering Design & Fabrication | 12 months | $60–80 million |
| Phase 3: Radiological Safety Preparation | 6 months (parallel) | $15–20 million |
| Phase 4: Offshore Operations (lift & transport) | 3 months | $80–120 million |
| Phase 5: Drydock Decommissioning | 12–24 months | $50–80 million |
| Phase 6: Risk/Insurance/Regulatory | Throughout | $20–30 million |
| **Subtotal** | | **$250–365 million** |
| Contingency (30%) | | $75–110 million |
| **TOTAL K-27** | | **$325–475 million** |

**K-159 Estimated Cost (200 m, fragile hull):**

| Phase | Estimated Cost (USD) |
|---|---|
| Phase 1 | $30–40 million |
| Phase 2 (incl. exoskeleton fabrication) | $80–120 million |
| Phase 3 | $15–20 million |
| Phase 4 (longer offshore campaign) | $100–150 million |
| Phase 5 | $50–80 million |
| Phase 6 | $20–30 million |
| **Subtotal** | **$295–440 million** |
| Contingency (35%) | $103–154 million |
| **TOTAL K-159** | **$398–594 million** |

**K-278 Komsomolets Estimated Cost (1,680 m):**

| Phase | Estimated Cost (USD) |
|---|---|
| Phase 1 | $40–60 million |
| Phase 2 (deep-sea pontoon system, custom fabrication) | $150–250 million |
| Phase 3 (incl. nuclear torpedo handling) | $25–40 million |
| Phase 4 (extended deep-water ops) | $200–350 million |
| Phase 5 (incl. weapons disposition) | $80–120 million |
| Phase 6 | $30–50 million |
| **Subtotal** | **$525–870 million** |
| Contingency (40%) | $210–348 million |
| **TOTAL K-278** | **$735 million – $1.22 billion** |

### 7.2 Cost Summary — All Feasible Submarines

| Submarine | Depth (m) | Estimated Total Cost (USD) |
|---|---|---|
| K-27 | 33 | $325–475 million |
| K-159 | 200 | $398–594 million |
| K-278 | 1,680 | $735 million – $1.22 billion |
| USS Thresher | 2,560 | $1.5–3.0 billion (rough order of magnitude) |
| USS Scorpion | 3,000 | $2.0–4.0 billion (rough order of magnitude) |
| **Combined (feasible 3)** | | **$1.46–2.29 billion** |
| **All 5 recoverable** | | **$4.5–8.3 billion** |

> K-8 (4,680 m) and K-219 (6,000 m) are not costed as salvage is beyond current technology.

### 7.3 Historical Cost Benchmarks

| Operation | Year | Depth | Cost (original) | Cost (2026 USD est.) |
|---|---|---|---|---|
| **Project Azorian** (CIA, K-129 partial recovery) | 1974 | 4,900 m | $800 million | ~$5 billion |
| **K-141 Kursk** (Smit/Mammoet) | 2001 | 108 m | $130 million (lift only) | ~$250 million |
| **Ehime Maru** (US Navy) | 2001 | 610 m → 35 m (relocated, not surfaced) | $60 million | ~$115 million |
| **K-27 + K-159 planned** (Russian decree) | 2020 | 33 + 200 m | $330 million (announced) | $330–400 million |
| **Costa Concordia** (non-nuclear, reference) | 2013–2014 | 30 m (listing) | $2 billion (total project) | ~$2.6 billion |

**Observations:**
- The Russian government's announced $330 million budget for K-27 + K-159 combined is at the low end of this estimate. Historically, nuclear salvage projects overrun estimates by 50–200%.
- The Kursk operation cost ~$130 million for the lift alone at only 108 m depth. K-278 at 1,680 m can be expected to cost 5–10× more.
- Project Azorian demonstrated that deep-ocean nuclear submarine recovery is technically possible but extraordinarily expensive, even with 1970s-era technology.

### 7.4 Major Cost Drivers & Sensitivity

| Cost Driver | % of Total | Sensitivity | Notes |
|---|---|---|---|
| Vessel charter costs | 30–40% | HIGH — every day of weather delay costs $500K–1M | Schedule compression reduces cost |
| Custom fabrication (cradles, pontoons, cofferdams) | 20–25% | MODERATE — design-dependent | K-278 pontoon system is largest single cost |
| Nuclear safety & regulatory compliance | 10–15% | LOW — non-negotiable | Cost of not complying is catastrophically higher |
| Decommissioning & waste disposal | 10–15% | MODERATE | Depends on fuel condition upon recovery |
| Engineering & project management | 8–10% | LOW | Fixed-price design contracts recommended |
| Insurance | 3–5% | MODERATE | Nuclear liability premiums are expensive |
| Contingency consumed | 15–25% | HIGH | Historical data shows >80% of contingency is typically consumed |

---

## Appendices

### Appendix A: Key Assumptions

1. All submarine locations are known to sufficient accuracy for survey vessel positioning (±500 m).
2. No military classification restrictions prevent access to hull design drawings for lift engineering.
3. Russia cooperates on salvage of Soviet/Russian submarines (K-27, K-159, K-278).
4. The United States authorizes salvage of USS Thresher and USS Scorpion if technically feasible.
5. No ongoing armed conflict prevents access to any wreck site.
6. Technology available in 2026 is sufficient for operations to 2,000 m depth. Operations beyond 3,000 m require significant technology development.
7. Nuclear fuel in all reactors has remained subcritical since the time of loss.
8. K-278's titanium pressure hull retains >50% structural integrity.
9. K-159's hull will require full exoskeleton reinforcement — zero load-bearing capability assumed.
10. K-27's reactor compartment seal (bitumen/furfuryl alcohol applied in 1982) is degraded but not fully compromised.

### Appendix B: Applicable Standards & Regulations

| Standard | Application |
|---|---|
| IAEA GSR Part 3 (Radiation Protection) | All operations |
| IAEA SSR-5 (Disposal of Radioactive Waste) | Fuel and component disposal |
| IAEA Safety Guide RS-G-1.7 (Occupational Radiation Protection) | Personnel dosimetry |
| UNCLOS Articles 192, 235 | Environmental protection obligation |
| London Convention / London Protocol | Prohibition on sea dumping; relevant to any material left on seabed |
| OSPAR Convention | NE Atlantic environmental protection (K-278, K-159) |
| IMO International Salvage Convention 1989 | Salvage rights and responsibilities |
| IMCA Guidelines (D 024, R 004) | ROV operations, diving operations |
| DNV-OS-H101/H201 | Marine operations, heavy lift |
| API RP 2A / DNV-OS-C101 | Structural design of lifting systems |

### Appendix C: Key Contacts and Stakeholders

| Organization | Role | Involvement |
|---|---|---|
| Rosatom (Russia) | State nuclear corporation | Lead authority for Russian submarine salvage |
| US Navy (NAVSEA) | US naval authority | Lead authority for USS Thresher/Scorpion |
| IAEA | International nuclear regulator | Oversight, safety review, safeguards (weapons material) |
| Norwegian Radiation & Nuclear Safety Authority (DSA) | Regional regulator | Barents/Norwegian Sea operations |
| Smit Salvage (Netherlands) | Salvage contractor | Kursk experience; potential prime contractor |
| Mammoet (Netherlands) | Heavy lift contractor | Kursk experience; strand jack systems |
| EPRON / Russian Navy Salvage Service | Russian military salvage | Direct involvement in Russian operations |

### Appendix D: Decision Tree — Which Submarines to Salvage

```
START: Should this submarine be salvaged?
│
├─ Depth > 4,000 m? ──── YES ──→ MONITOR ONLY (K-8, K-219)
│                                  Review every 10 years as
│                                  technology advances.
│     NO
│     ↓
├─ Active radiological release? ── YES ──→ Is salvage feasible?
│                                           ├─ YES → SALVAGE (K-278)
│                                           └─ NO  → CONTAIN IN-SITU
│     NO
│     ↓
├─ Depth < 500 m? ──── YES ──→ SALVAGE (K-27, K-159)
│                                High accessibility + high risk
│                                from shallow depth.
│     NO
│     ↓
├─ Depth 500–4,000 m? ── YES ──→ Is contamination risk 
│                                  increasing? 
│                                  ├─ YES → PLAN SALVAGE (Thresher, Scorpion)
│                                  └─ NO  → MONITOR (reassess in 10 yr)
│
└─ END
```

---

*End of Nuclear Submarine Salvage Operation Plan*
*Document Version 1.0 — 11 February 2026*
*Compiled using data from sunken-nuclear-submarines-report.md*
