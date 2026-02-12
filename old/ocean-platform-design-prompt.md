# Design of an Ocean Salvage Platform (OSP) for Nuclear Submarine Recovery

---

**Role:** You are a world-class multidisciplinary engineer with expertise in naval architecture, offshore platform design, hydrodynamics, structural engineering, dynamic positioning, heavy-lift offshore engineering, nuclear safety engineering, marine operations, FEA/CFD, and classification society rules (DNV, Lloyd's, ABS).

---

## Objective

Design a purpose-built **Ocean Salvage Platform (OSP)** to recover sunken nuclear-powered submarines from 30–2,000 m depth. Requirements:

- Sustained heavy-lift operations in open ocean (operational up to Sea State 6: Hs = 4–6 m)
- Survival in 100-year return period storms (rogue waves up to 2× Hs)
- Integrated nuclear-safe containment, heavy-lift, ROV/AUV deployment, and crew habitability
- 90+ continuous days on station without critical resupply

**Reference documents:** `sunken-nuclear-submarines-report.md`, `nuclear-submarine-salvage-operation-plan.md`

---

## Target Submarines

| Submarine | Depth (m) | Displacement (t) | Length (m) | Nuclear Hazards | Location / Seabed |
|---|---|---|---|---|---|
| K-27 | 33 | 4,380 | 109.8 | 2 Pb-Bi liquid-metal reactors; fused fuel/coolant | Kara Sea — silt/clay, permafrost |
| K-159 | 200 | 4,750 | ~107 | 2 PWRs, ~800 kg spent fuel (~5.3 GBq) | Barents Sea — glacial till/bedrock |
| K-278 Komsomolets | 1,680 | 8,000 | 117.5 | 1 PWR + 2 Pu torpedo warheads | Norwegian Sea — pelagic ooze/clay |
| USS Thresher | 2,560 | 3,420 | 85 | 1 S5W PWR (HEU) | N. Atlantic — abyssal clay |
| USS Scorpion | 3,000 | 3,124 | 76.7 | 1 S5W PWR + 2 Mk 45 nuclear warheads | N. Atlantic — abyssal sediment |

**Design Envelope:**
- Lift capacity: ≥ 10,000 t (K-278 at 8,000 t + ~2,000 t suction breakout + safety factor)
- Operational depth: up to 2,000 m
- Max submarine dimensions: 120 m × 12 m
- Environments: Arctic (Kara/Barents Sea), Sub-Arctic (Norwegian Sea), North Atlantic

---

## Design Requirements

Produce each section in full engineering detail with calculations, equations, assumptions (flagged **[ASSUMPTION]**), and units.

### 1. Hull Form & Platform Type Selection

Evaluate these candidates via quantitative scoring matrix:

| Candidate | Key Trait |
|---|---|
| Semi-submersible | Reduced waterplane, wave transparency |
| SPAR-type | Deep-draft, excellent heave, limited deck area |
| Barge / ship-shaped | Large deck area, high wave response |
| Catamaran / SWATH | Small waterplane, structural complexity |
| Jack-up (shallow only) | Zero motion, limited to ≤150 m |
| Hybrid / novel | Optimal combination |

**Evaluation criteria:** (1) Wave response RAOs at SS6–7, (2) Station-keeping (DP/mooring), (3) Moon pool feasibility (≥15 m × 130 m), (4) Deck area & payload, (5) Transit speed & self-propulsion, (6) Cost & schedule, (7) Depth adaptability (33–2,000 m).

**Deliverable:** Select one type with full justification and textual/ASCII general arrangement drawings.

### 2. Wave Resistance & Survivability

#### 2.1 Design Sea States

Populate using ERA5, NORA10, NDBC or equivalent (cite sources):

| Condition | Parameter | Kara Sea | Barents Sea | Norwegian Sea | N. Atlantic |
|---|---|---|---|---|---|
| Operational limit | Hs (m), Tp (s) | — | — | — | — |
| Survival (100-yr) | Hs (m), Tp (s) | — | — | — | — |
| Survival (10,000-yr) | Hs (m) | — | — | — | — |
| Extreme individual wave | Hmax (m) | — | — | — | — |
| Surface current | Vc (m/s) | — | — | — | — |
| Wind (10-min mean) | Vw (m/s) | — | — | — | — |

#### 2.2 Hydrodynamic Design

1. **Motion minimization:** Estimated RAOs (heave, pitch, roll) for T = 5–25 s; natural heave period tuning to avoid resonance at all sites
2. **Extreme wave survival:**
   - Air gap calculation: $\text{Air gap} \geq \eta_{max,100yr} + \text{crest allowance} + \text{settlement/squat}$ (use Forristall distribution for $\eta_{max}$)
   - Green water design: scuppers, drainage, structural reinforcement
   - Parametric rolling mitigation
3. **Dynamic positioning:**
   - DP3 preferred (DP2 minimum); thruster type, number, arrangement, total bollard pull
   - Station-keeping envelope and watch circle radius during lift
   - Thruster ventilation in large waves; DP power budget in survival conditions
4. **Mooring (if applicable for shallow ops):**
   - Configuration, line composition, pretension, breakload, safety factors per DNV-OS-E301
   - Response to 100-year collinear and non-collinear environmental loads
5. **Roll damping:**
   - Bilge keels, passive/active anti-roll tanks (sized for SS5–6), gyroscopic stabilizers if applicable

#### 2.3 Structural Design for Wave Loads

1. **Global loads:** Max bending moment (sag/hog), shear, torsion in 100-year sea state; fatigue accumulation (Palmgren–Miner, DNV-RP-C203 S-N curves, 25-year design life)
2. **Local loads:** Slamming, wave-in-deck impact, green water pressures, hydrostatic collapse on submerged members
3. **Materials & scantlings:** Steel grades (DH36/EH36/NV), plate thickness, stiffener/frame spacing, fatigue-critical details (bracket toes, tubular joints, moon pool corners), corrosion allowance, cathodic protection
4. **Analysis methodology:** Global FEA (element types, mesh, BCs), wave load application (design wave / spectral / time-domain), ULS/ALS/FLS/SLS checks per DNV-OS-C101/C103

### 3. Moon Pool & Heavy-Lift System

#### 3.1 Moon Pool

- Dimensions: ≥130 m × 18 m clear opening
- Structural integrity impact; water column oscillation and piston-mode resonance; damping devices (perforated plates, cofferdams, flaps)
- Alternative if through-hull impractical: open stern / split-hull (cf. Glomar Explorer) or deck-edge gantry
- Natural period of water column: $T_n = 2\pi \sqrt{(d + d_e)/g}$ — must avoid 5–15 s wave period range; specify damping if resonance unavoidable

#### 3.2 Heavy-Lift Systems

Three operational modes:

**Mode A — Strand Jack (0–200 m):**
Capacity per unit, strand specs, ≤5 mm sync tolerance, AHC specs, lift/descent speed, dynamic load amplification attenuation

**Mode B — Controlled Buoyancy (200–2,000 m):**
Pontoon deployment, umbilical/compressed air management, winch system for ascent control, handover to strand jacks at 100–200 m

**Mode C — Hybrid:** Mode A + B integration, load-sharing protocol, control architecture (auto/semi-auto/manual override)

#### 3.3 Active Heave Compensation (AHC)

- AHC specs: stroke, velocity, force capacity
- Max allowable dynamic load variation: ±X% of static load
- Sea state at which tolerance is exceeded (operational lift limit)
- AHC sizing calculations; performance envelope and saturation point
- Failure consequence analysis; passive backup redundancy
- Emergency load-set-down procedure

### 4. Nuclear Safety & Containment

#### 4.1 Radiation Shielding

1. **Moon pool / landing area shielding:**
   - Materials: steel, lead, polyethylene (neutron), concrete
   - Gamma shielding (Cs-137 @ 662 keV, Co-60 @ 1.17/1.33 MeV) + neutron shielding (K-27)
   - Target: ≤ 2.5 μSv/hr at nearest occupied area
   - TVL approach: $n = \log_{10}(D_0 / D_{target}) / \text{TVL}$ — provide TVL values per material/isotope

2. **Reactor handling bay:**
   Enclosed, HEPA-filtered negative-pressure (≥10 ACH), containment sump (100% cofferdam water volume), airlock with contamination monitors, remote handling (cranes/manipulators)

3. **Monitoring network:**
   ≥20 fixed gamma monitors, continuous airborne samplers (particulate + iodine + tritium), stack monitors, seawater discharge monitors, neutron detectors around moon pool (K-27 criticality surveillance)

#### 4.2 Criticality Prevention (K-27)

K-27's fuel is fused with Pb-Bi coolant in uncharacterized geometry — tilting/shock could increase reactivity.

1. Maintain submarine level ±1° throughout lift via mechanical restraint/gimbal cradle
2. Neutron absorber provisions (borated water, cadmium sheets) around reactor area
3. Emergency procedures for rising neutron count rate

#### 4.3 Contaminated Water Management

- Drainage capacity: 1,000–5,000 m³
- Treatment: filtration, ion exchange, evaporation to meet discharge limits (Cs-137 < 10 Bq/L per IAEA)
- Holding tanks for untreatable water; continuous discharge monitoring

### 5. Power Generation & Distribution

1. **Demand estimate:** DP thrusters, strand jacks/winches, AHC hydraulics, HVAC/life support, radiological systems, hotel load
2. **Plant:** Generator type/number (diesel/LNG/hybrid); redundancy N+1 (DP), N+2 (nuclear safety); emergency power (UPS for rad monitoring, EDG for DP); blackout recovery
3. **Distribution:** HV switchboard, redundant split-bus (DP), PMS with load shedding — nuclear safety systems are NEVER shed

### 6. Stability & Ballast

1. **Intact stability:** GZ curves for all loading conditions (lightship, operating, survival, max deck load); IMO MODU Code 2009; moon pool free-surface effect on GM
2. **Damage stability:** Two-compartment flooding survival; positive stability after worst-case flooding; progressive flooding during lift
3. **Ballast:** Active system for trim/heel compensation during asymmetric loading; transfer rate matched to strand jack load rate; auto-controlled anti-heeling tanks
4. **Lift-through-moon-pool stability:** Model progressive buoyancy-to-structure load transfer; demonstrate stable equilibrium at all stages; max list/trim ≤2°

### 7. Accommodation & Life Safety

1. **150–200 personnel:** 1/2-person cabins (key staff), 4-person (crew); mess, recreation, medical bay; SOLAS lifeboats/rafts (200% capacity)
2. **Helideck:** S-92 capable (≥22.8 m D-value), positioned upwind and max distance from reactor handling area
3. **Radiological zoning:** Accommodation = GREEN zone (<1 μSv/hr); HVAC intakes upwind of rad work areas with auto-damper closure on contamination alarm

### 8. Operational Modes

| Mode | Description | Key Systems |
|---|---|---|
| Transit | Self-propelled ≥8 kn | Propulsion, navigation, hotel |
| Station-keeping | Survey & rigging | DP, ROV, cranes |
| Shallow lift (≤200 m) | Strand jack through moon pool | Strand jacks, AHC, ballast, containment |
| Deep lift (200–2,000 m) | Buoyancy-assisted + winch; handover to strand jacks | Winches, pontoons, AHC, containment |
| Submarine on deck | Secured, in transit to port | Reactor bay containment, shielding |
| Survival | 100-year storm, no operations | DP/mooring, structural endurance, containment |

For each: active systems & power demand, max sea state, mode transitions, abort/emergency procedures.

### 9. Construction Specification

1. Overall dimensions (L × B × D × draft for operating and survival)
2. Lightship and max operating displacement
3. Structural steel weight and major material quantities
4. Yard requirements (dock size, crane capacity)
5. Construction schedule (months, steel cutting to delivery)
6. Classification notation (e.g., DNV +1A1 Column Stabilised Unit, DYNPOS-3, CRANE, HELDK-SH, Clean Design, ICE-C)
7. CAPEX estimate (±30%, benchmarked against Sleipnir, Pioneering Spirit, etc.)

### 10. Historical Precedent Analysis

Extract transferable design features, limitations to overcome, and operational lessons from:

| Vessel | Relevance |
|---|---|
| Hughes Glomar Explorer (1974) | Submarine lift from 4,900 m; moon pool design |
| Heerema Sleipnir (2019) | 2 × 10,000 t cranes; DP3; capability benchmark |
| Allseas Pioneering Spirit | 48,000 t topside lift; catamaran; through-hull concepts |
| Giant 4 / Mammoet–Smit (Kursk, 2001) | 26 strand jacks; barge-based submarine lift |
| Boskalis Vanguard / Blue Marlin | Semi-submersible heavy transport; unconventional naval loads |

---

## Constraints

1. **Nuclear safety is the paramount design driver** — overrides cost, schedule, and convenience
2. IAEA safety standards (GSR Part 3, SSR-5, SSG-47)
3. Structural: DNV-OS-C101, C103, C301
4. Marine operations: DNV-OS-H101, H201
5. Stability: IMO MODU Code 2009
6. All systems TRL ≥ 6 (demonstrated in relevant environment)
7. Design life ≥ 25 years
8. Ice Class capable (min. DNV ICE-C) for Arctic operations
9. MARPOL Annex I–VI; Polar Code
10. No military classification restrictions assumed

---

## Output Format — Deliverable File Set

You must produce your design as a set of **separate, named files** written to disk. Each file must be self-contained, properly formatted, and production-quality. Use Markdown (`.md`) for narrative/calculations, CSV (`.csv`) for tabular data, Mermaid diagrams (embedded in Markdown via ` ```mermaid ` blocks) for schematics, and Python (`.py`) for executable analysis scripts.

### Formatting Rules (apply to every file)

- Hierarchically numbered sections (1, 1.1, 1.1.1)
- All calculations with LaTeX equations, **[ASSUMPTION]** tags, and SI units
- Tables for all trade studies, comparisons, and parametric data
- Cite precedents throughout: Project Azorian, Kursk salvage, Sleipnir, Pioneering Spirit
- Cross-reference other deliverable files by filename where relevant

---

### Deliverable Files

Produce **all** of the following files. Use the exact filenames specified.

#### File 1 — `01-hull-form-selection.md`
**Hull Form & Platform Type Trade Study**
- Quantitative scoring matrix (weighted, all 7 criteria)
- RAO comparison charts (text/ASCII) for all candidates at SS6–7
- Decision tree for hull type selection with branch rationale
- Selected hull form: full justification with numerical evidence
- ASCII General Arrangement drawing: plan view, profile view, and midship cross-section
- Mermaid diagram: platform zoning layout (deck plan)
- Principal dimensions table (L × B × D × draft for each mode)

#### File 2 — `02-environmental-design-basis.md`
**Environmental & Metocean Design Basis**
- Completed metocean table (Section 2.1) for all four operating regions
- Data sources cited (ERA5 / NORA10 / NDBC / equivalent)
- Wave spectra selection (JONSWAP / Pierson–Moskowitz) with justification and γ values
- Wind profiles and current profiles by depth
- Ice loading criteria for Arctic sites (Kara/Barents)
- Design environmental load combinations (ULS, ALS, FLS)

#### File 3 — `03-hydrodynamic-analysis.md`
**Hydrodynamic Design & Motion Analysis**
- RAO calculations/estimates (heave, pitch, roll) for T = 5–25 s wave period range
- Natural period tuning analysis (heave, roll, pitch) — demonstrate avoidance of wave energy band
- Parametric roll assessment
- Roll damping system design: bilge keel sizing, anti-roll tank volume/location/performance
- Air gap calculation (Forristall crest distribution)
- Green water analysis and drainage design
- Mermaid diagram: RAO response envelope (simplified bar chart or qualitative)

#### File 4 — `04-dynamic-positioning.md`
**Dynamic Positioning & Station-Keeping System**
- DP class selection justification (DP2 vs DP3)
- Thruster arrangement: type, number, thrust per unit, total bollard pull
- Station-keeping capability analysis: watch circle radius vs. sea state
- DP power budget (transit, station-keeping, lifting, survival)
- Thruster ventilation analysis in large waves
- Mooring system for shallow operations (≤200 m): configuration, line composition, pretension, safety factors per DNV-OS-E301
- Mermaid diagram: thruster layout (plan view)
- Mermaid diagram: DP redundancy architecture (power/control split)

#### File 5 — `05-structural-design.md`
**Structural Design & Analysis**
- Global load calculations: max bending moment (sag/hog), shear force, torsion in 100-year sea state
- Fatigue assessment: Palmgren–Miner, S-N curves (DNV-RP-C203), design fatigue factors, 25-year life
- Local loads: slamming pressures, wave-in-deck impact, hydrostatic collapse on submerged members
- Material selection table: steel grades (DH36/EH36/NV), yield strengths, application zones
- Scantling table: plate thickness, stiffener spacing/size, frame spacing for key structural zones
- Fatigue-critical detail catalog: bracket toes, tubular joints, moon pool corners — detail class and DFF
- Corrosion protection: allowances, coating specs, cathodic protection design
- FEA methodology specification: element types, mesh density, boundary conditions, load cases
- ULS / ALS / FLS / SLS check summary table per DNV-OS-C101/C103

#### File 6 — `06-moon-pool-design.md`
**Moon Pool & Through-Hull Design**
- Moon pool dimensions and structural arrangement
- Water column resonance analysis: natural period calculation, resonance avoidance strategy
- Damping system design: perforated plates, cofferdams, or flaps — sizing and performance
- Structural reinforcement around moon pool opening: stress concentration analysis
- Alternative assessment: split-hull / open-stern / deck-edge gantry comparison
- ASCII cross-section drawing of moon pool with dimensions
- Mermaid diagram: moon pool operational sequence (submarine entry to secured)

#### File 7 — `07-heavy-lift-system.md`
**Heavy-Lift System Design**
- **Mode A (Strand Jack, 0–200 m):** capacity per unit, strand specs, synchronization tolerance (≤5 mm), AHC integration, lift/descent speed, dynamic load amplification
- **Mode B (Controlled Buoyancy, 200–2,000 m):** pontoon design, umbilical/air management, winch specs, ascent rate control, handover protocol
- **Mode C (Hybrid):** integration architecture, load-sharing protocol, control system (auto/semi-auto/manual)
- AHC detailed design: stroke, velocity, force capacity, performance envelope, saturation point
- Max dynamic load variation: ±X% of static load with calculation
- Failure mode analysis: AHC failure consequences, passive backup, emergency load-set-down
- Mermaid diagram: lift system control architecture
- Mermaid diagram: Mode A/B/C decision tree

#### File 8 — `08-nuclear-safety-containment.md`
**Nuclear Safety & Containment Systems**
- Radiation shielding design: TVL calculations for each isotope (Cs-137, Co-60, neutrons)
- Shielding material specifications and thicknesses by zone
- Reactor handling bay design: HEPA filtration, negative pressure (≥10 ACH), containment sump, airlocks
- Criticality prevention protocol for K-27: gimbal cradle specs, tilt tolerance (±1°), neutron absorber provisions
- Radiation monitoring network: detector types, locations (≥20 gamma, airborne samplers, stack/seawater monitors)
- Contaminated water management: capacity, treatment process (filtration → ion exchange → evaporation), discharge limits
- Radiological zoning map with dose rate targets per zone
- Mermaid diagram: radiological zone layout (plan view)
- Mermaid diagram: contaminated water treatment flowchart
- Mermaid diagram: criticality emergency response decision tree

#### File 9 — `09-power-generation.md`
**Power Generation & Electrical Distribution**
- Total power demand estimate broken down by system and operational mode (table)
- Generator plant: type, number, rated power, fuel type, redundancy level (N+1 DP, N+2 nuclear safety)
- Emergency power: UPS for rad monitoring, EDG for DP — sizing and autonomy
- Blackout recovery sequence and timing
- HV switchboard single-line diagram (Mermaid)
- Load shedding priority table — nuclear safety systems marked as NON-SHEDDABLE
- Fuel storage capacity and endurance (90+ days at max operational demand)
- Mermaid diagram: power distribution single-line diagram
- Mermaid diagram: load shedding priority hierarchy

#### File 10 — `10-stability-ballast.md`
**Stability & Ballast System Design**
- GZ curves for all loading conditions (lightship, operating, survival, max deck load) — tabulated data + ASCII plot
- IMO MODU Code 2009 compliance check table
- Moon pool free-surface correction on GM
- Damage stability: two-compartment flooding survival demonstration
- Progressive flooding analysis during lift operations
- Ballast system: tank arrangement, transfer rates, auto-controlled anti-heeling
- Lift-through-moon-pool stability: progressive buoyancy-to-structure load transfer model
- Max list/trim ≤2° demonstration at all lift stages

#### File 11 — `11-accommodation-life-safety.md`
**Accommodation, Life Safety & Helideck**
- Accommodation layout: 150–200 personnel, cabin types and allocation
- SOLAS life-saving appliances: lifeboats, rafts (200% capacity), muster stations
- Helideck design: S-92 capable (≥22.8 m D-value), positioning rationale
- Radiological zoning of accommodation: GREEN zone (<1 μSv/hr)
- HVAC design: intake positioning relative to rad work areas, auto-damper closure on contamination alarm
- Medical bay specifications (including radiation injury treatment capability)
- Mermaid diagram: accommodation deck layout
- Mermaid diagram: emergency evacuation routes

#### File 12 — `12-operational-modes.md`
**Operational Modes & Procedures**
- Detailed description of each operational mode (Transit, Station-keeping, Shallow Lift, Deep Lift, Submarine on Deck, Survival)
- Active systems and power demand per mode (table)
- Max sea state per mode
- Mode transition procedures and criteria
- Abort and emergency procedures for each mode
- Mermaid diagram: mode transition state machine
- Mermaid diagram: abort/emergency decision flowchart

#### File 13 — `13-construction-specification.md`
**Construction Specification & Cost Estimate**
- Principal dimensions summary table
- Lightship and max operating displacement
- Structural steel weight and major material quantities
- Yard requirements: dock size, crane capacity, facilities
- Construction schedule: Gantt chart (Mermaid) from steel cutting to delivery
- Classification notation (DNV notation string with all class descriptors)
- CAPEX estimate (±30%) with line-item breakdown, benchmarked against Sleipnir, Pioneering Spirit, Glomar Explorer (inflation-adjusted)

#### File 14 — `14-historical-precedent-analysis.md`
**Historical Precedent Analysis**
- For each reference vessel (Glomar Explorer, Sleipnir, Pioneering Spirit, Giant 4/Kursk, Vanguard/Blue Marlin):
  - Design features extracted and adapted for OSP
  - Limitations identified and how OSP design overcomes them
  - Operational lessons incorporated
- Comparison table: OSP vs. all precedent vessels across key parameters

#### File 15 — `15-risk-register.csv`
**Risk Register** (CSV format with headers)
- Columns: `Risk_ID, Category, Description, Likelihood (1-5), Consequence (1-5), Risk_Score, Mitigation_Measure, Residual_Risk_Score, Owner`
- Categories: Structural, Hydrodynamic, Nuclear Safety, Operational, Environmental, Schedule, Cost
- Minimum 40 identified risks

#### File 16 — `16-bill-of-materials.csv`
**Pre-FEED Bill of Materials** (CSV format)
- Columns: `Item_ID, System, Component, Specification, Quantity, Unit, Unit_Weight_t, Total_Weight_t, Estimated_Cost_USD, Lead_Time_Months, Supplier_Type`
- Cover all major systems: hull steel, propulsion, DP thrusters, strand jacks, winches, AHC, generators, shielding materials, HVAC, cranes, ROVs, mooring, lifeboats

#### File 17 — `17-design-calculations.py`
**Executable Design Calculations** (Python script)
- Hydrostatic calculations (displacement, waterplane area, BM, GM, GZ)
- Wave load estimation (Morison equation for submerged members; strip theory approximation)
- Moon pool resonance period calculation with damping assessment
- AHC sizing calculations (stroke, velocity, force vs. sea state)
- Shielding thickness calculations (TVL method for gamma and neutron)
- Strand jack capacity and dynamic amplification factor
- Stability check (IMO MODU Code criteria)
- Power demand summation by mode
- All inputs clearly defined as variables at the top; all outputs printed with units
- Use only standard libraries: `math`, `numpy` (if available), `csv` for output
- Include docstrings and inline comments explaining every equation

#### File 18 — `18-design-data-tables.csv`
**Consolidated Design Data Tables** (CSV format)
- Principal dimensions and hydrostatics
- Metocean design parameters (combined for all sites)
- Weight breakdown by system
- Power demand by mode
- Stability criteria compliance checklist
- One sheet/section per topic, separated by a header row

#### File 19 — `19-general-arrangement-drawings.md`
**General Arrangement Drawings** (ASCII/text art)
- Profile view (side elevation) with major dimensions, waterlines, key equipment
- Plan view: main deck, lower deck, pontoon/column level
- Midship cross-section with scantling annotations
- Moon pool detail (plan + section)
- Thruster arrangement (plan view)
- Radiological zone overlay on plan view
- All drawings to include dimension lines, labels, and scale references

#### File 20 — `20-design-summary.md`
**Executive Design Summary**
- One-page key parameters table (dimensions, displacement, lift capacity, endurance, speed, crew, DP class, classification)
- Design philosophy statement
- Top 10 design innovations/features
- Top 10 risks and mitigations
- Compliance matrix: all constraints (Section "Constraints" above) with status and evidence reference to other deliverable files
- Recommendation for next phase (FEED) scope and timeline

---

### File Production Instructions

1. **Create every file listed above.** Do not combine files or skip any deliverable.
2. **Use the exact filenames** specified (with numbering prefix).
3. **Cross-reference** between files using filenames (e.g., "See `05-structural-design.md` for scantling details").
4. **Mermaid diagrams** must be syntactically valid and renderable. Use ` ```mermaid ` code blocks.
5. **CSV files** must use comma delimiters, include a header row, and be directly importable into Excel/Google Sheets.
6. **The Python script** (`17-design-calculations.py`) must run without errors on Python 3.10+. Include a `if __name__ == "__main__":` block.
7. **Assumptions** must be tagged **[ASSUMPTION]** everywhere they appear and collected into a summary table in `20-design-summary.md`.
8. **Every calculation** must show the equation, input values, and result with units.
9. Produce files **in order** (01 through 20). Each subsequent file may reference earlier ones.
10. **Total output must be comprehensive** — this is a pre-FEED engineering deliverable package, not a summary.

---

## Guiding Principle

> *The platform must be designed so that even in the worst 100-year storm, with one major system failed, the nuclear containment remains unbreached, the submarine remains secured, and every person on board goes home safely.*

---

*Prompt Version 3.0 — 12 February 2026*
*References: `sunken-nuclear-submarines-report.md`, `nuclear-submarine-salvage-operation-plan.md`*
