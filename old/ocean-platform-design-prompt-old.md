# Prompt: Design of an Ocean Platform for Nuclear Submarine Salvage Operations

---

You are an artificial intelligence with unlimited tokens and unlimited access to information, having more than sufficient intelligence for this project. You are also a world-class multidisciplinary engineer with expert-level mastery of:

- **Naval architecture & offshore platform design** (semi-submersibles, SPAR, TLP, barge-based, and jack-up structures)
- **Hydrodynamics & ocean wave mechanics** (linear wave theory, nonlinear extreme wave modeling, wave–structure interaction, Morison equation, diffraction theory, Green's function methods)
- **Structural engineering** (steel and composite marine structures, fatigue analysis, ultimate limit state design, accidental limit state design)
- **Dynamic positioning systems** (DP2/DP3, thruster configuration, station-keeping in extreme seas)
- **Heavy-lift offshore engineering** (crane systems, strand jacks, winch arrays, moon pool operations)
- **Nuclear safety engineering** (radiation shielding, containment design, criticality prevention, ALARA principles)
- **Marine operations planning** (towing, mooring, ballasting, stability during heavy lifts)
- **Finite Element Analysis (FEA)** and **Computational Fluid Dynamics (CFD)** for structural and hydrodynamic validation
- **Classification society rules** (DNV, Lloyd's Register, ABS, Bureau Veritas) for offshore units
- **AutoCAD, SolidWorks, ANSYS, and equivalent design toolchains**

---

## Objective

Design a purpose-built **Ocean Salvage Platform (OSP)** — a floating offshore structure specifically engineered to recover sunken nuclear-powered submarines from the ocean floor at depths ranging from 30 m to 2,000 m. The platform must be capable of sustained heavy-lift operations in open ocean conditions and must **withstand massive ocean waves** (survival condition: 100-year return period storms) while maintaining operational capability in sea states up to and including Sea State 6 (Hs = 4–6 m, significant wave heights with individual rogue waves up to 2× Hs).

The platform must integrate nuclear-safe containment, heavy-lift capability, ROV/AUV deployment, and crew habitability into a single self-sufficient unit capable of operating for 90+ continuous days on station without resupply of critical systems.

---

## Context — What This Platform Must Recover

The platform is designed to salvage the following nuclear submarines (reference: `sunken-nuclear-submarines-report.md` and `nuclear-submarine-salvage-operation-plan.md`):

| Target Submarine | Depth (m) | Submerged Displacement (t) | Hull Length (m) | Nuclear Hazards | Seabed Type |
|---|---|---|---|---|---|
| K-27 | 33 | 4,380 | 109.8 | 2 liquid-metal reactors (Pb-Bi); fused fuel/coolant mass | Kara Sea — fine silt/clay, permafrost influence |
| K-159 | 200 | 4,750 | ~107 | 2 PWR reactors with ~800 kg spent fuel (~5.3 GBq) | Barents Sea — glacial till over bedrock |
| K-278 Komsomolets | 1,680 | 8,000 | 117.5 | 1 PWR reactor + 2 nuclear torpedo warheads (Pu) | Norwegian Sea — soft pelagic ooze/clay |
| USS Thresher | 2,560 | 3,420 | 85 | 1 S5W PWR (HEU fuel — weapons-grade uranium) | North Atlantic — abyssal clay |
| USS Scorpion | 3,000 | 3,124 | 76.7 | 1 S5W PWR + 2 Mk 45 nuclear torpedo warheads | North Atlantic — abyssal sediment |

**Design Envelope:**
- **Maximum lift capacity required:** ≥ 10,000 tonnes (to lift K-278 at 8,000 t displacement + ~2,000 t suction breakout force, with safety factor)
- **Maximum operational depth for lift systems:** 2,000 m (wire rope / pontoon deployment)
- **Maximum submarine length to handle:** 120 m
- **Maximum submarine beam:** ~12 m
- **Operating environments:** Arctic (Kara Sea, Barents Sea), Sub-Arctic (Norwegian Sea), North Atlantic

---

## Design Requirements — Produce Each Section in Full Engineering Detail

### 1. Hull Form & Platform Type Selection

Evaluate and select the optimal platform configuration from the following candidates. Provide a rigorous comparison matrix with quantitative scoring:

| Candidate | Description |
|---|---|
| **Semi-submersible** | Twin or multi-column hull with pontoon base; reduced waterplane area for wave transparency |
| **SPAR-type** | Deep-draft cylindrical hull; excellent heave response but limited deck area |
| **Barge / ship-shaped** | Large deck area and cargo capacity; high wave response (heave, pitch, roll) |
| **Catamaran / SWATH** | Small waterplane area twin hull; excellent stability but structural complexity |
| **Jack-up (for shallow operations only)** | Bottom-founded; zero wave-induced motion but limited to ≤150 m depth |
| **Hybrid / novel configuration** | Any combination or novel design that optimally addresses the requirements |

For each, evaluate against:
1. Wave response characteristics (heave, pitch, roll RAOs) in Sea State 6–7
2. Station-keeping capability (DP and/or mooring)
3. Moon pool feasibility (size sufficient for submarine passage: ≥15 m × 130 m)
4. Deck area and payload capacity
5. Transit speed and self-propulsion capability
6. Construction cost and schedule
7. Adaptability across the depth range (33 m to 2,000 m)

**Deliverable:** Select one platform type (or hybrid) with full justification. Provide preliminary general arrangement (GA) drawings described textually or in ASCII/diagram form.

### 2. Wave Resistance & Survivability Engineering

This is the **most critical design challenge.** The platform must operate in some of the most hostile ocean environments on Earth (Barents Sea, Norwegian Sea, North Atlantic) while performing precision heavy-lift operations with nuclear-hazardous loads.

#### 2.1 Design Sea States

Define the following environmental design conditions using site-specific metocean data:

| Condition | Parameter | Kara Sea (K-27) | Barents Sea (K-159) | Norwegian Sea (K-278) | North Atlantic (Thresher/Scorpion) |
|---|---|---|---|---|---|
| **Operational limit** | Hs (m) | — | — | — | — |
| **Operational limit** | Tp (s) | — | — | — | — |
| **Survival (100-year)** | Hs (m) | — | — | — | — |
| **Survival (100-year)** | Tp (s) | — | — | — | — |
| **Survival (10,000-year)** | Hs (m) | — | — | — | — |
| **Extreme individual wave** | Hmax (m) | — | — | — | — |
| **Current (surface)** | Vc (m/s) | — | — | — | — |
| **Wind (10-min mean)** | Vw (m/s) | — | — | — | — |

Fill in all values using best available metocean databases (ERA5, NORA10, NDBC, or equivalent). Cite sources.

#### 2.2 Hydrodynamic Design Philosophy

Address each of the following in detail:

1. **Wave transparency / motion minimization:**
   - How does the selected hull form minimize heave, pitch, and roll response in beam, head, and quartering seas?
   - Provide estimated Response Amplitude Operators (RAOs) for heave, pitch, and roll across wave periods of 5–25 seconds
   - What is the natural period of heave for this platform, and how is it tuned to avoid resonance with dominant wave period ranges at all operating sites?

2. **Extreme wave survival (rogue waves, breaking waves):**
   - Design for wave impact pressures from breaking/slamming waves on the platform underside (air gap design)
   - Calculate minimum air gap between still water level and underside of deck using the formula:

     $$\text{Air gap} \geq \eta_{max,100yr} + \text{wave crest allowance} + \text{settlement/squat}$$

     Where $\eta_{max}$ is the 100-year maximum crest elevation (use a second-order Stokes or Forristall distribution).
   - Design for green water on deck: scupper capacity, deck drainage, and structural reinforcement for deck wetness events
   - Address the phenomenon of **parametric rolling** and how the hull form avoids or mitigates it

3. **Dynamic positioning in extreme seas:**
   - Specify the DP class (DP2 minimum, DP3 preferred for nuclear operations)
   - Thruster type, number, arrangement, and total bollard pull
   - Station-keeping capability envelope: at what sea state does the platform lose position? What is the watch circle radius during lift operations?
   - Thruster–wave interaction and ventilation in large waves
   - Power budget for DP in survival conditions

4. **Mooring system (if applicable for shallow-water operations):**
   - Spread mooring vs. turret mooring vs. DP-only
   - Mooring line composition (chain, wire, synthetic fiber) and pretension
   - Mooring line breakload and safety factors per DNV-OS-E301
   - Mooring system response to 100-year environmental loads (wind + wave + current collinear and non-collinear cases)

5. **Bilge keels, anti-roll tanks, and active stabilization:**
   - Specify all roll damping systems
   - Passive vs. active anti-roll tanks — sizing and performance in Sea State 5–6
   - Gyroscopic stabilizers (if applicable for the platform size)

#### 2.3 Structural Design for Wave Loads

1. **Global wave loads:**
   - Maximum longitudinal bending moment (sagging and hogging) in 100-year sea state
   - Maximum shear force at critical cross-sections
   - Torsional loads from quartering/oblique seas
   - Fatigue damage accumulation over design life (25-year minimum) using Palmgren–Miner rule and DNV-RP-C203 S-N curves

2. **Local wave loads:**
   - Slamming pressures on pontoon/hull undersides (if semi-submersible)
   - Wave-in-deck impact pressures (if deck is within wave reach in extreme conditions)
   - Green water pressures on exposed deck equipment
   - Hydrostatic collapse pressure on any submerged structural members

3. **Structural materials and scantlings:**
   - Primary structure: material grade (e.g., DH36, EH36, NV-steel grades)
   - Plate thickness, stiffener spacing, and frame spacing for all primary members
   - Fatigue-critical details: bracket toes, tubular joints, moon pool corners
   - Corrosion allowance and cathodic protection design

4. **Structural analysis methodology:**
   - Global FEA model description (element types, mesh density, boundary conditions)
   - Wave load application method (design wave approach, stochastic spectral analysis, or time-domain simulation)
   - ULS, ALS, FLS, and SLS checks per DNV-OS-C101 / DNV-OS-C103

### 3. Moon Pool & Heavy-Lift System Design

The platform must be capable of lowering equipment to the seabed and raising an entire nuclear submarine (up to 120 m long and 10,000 t) from depths up to 2,000 m.

#### 3.1 Moon Pool Design

1. **Dimensions:** 
   - Length: sufficient to pass the longest submarine hull (≥130 m clear, accounting for cradle overhang)
   - Width: sufficient for cradle + clearance (≥18 m clear)
   - Describe how a moon pool of this scale affects hull structural integrity and wave response (water column oscillation, sloshing, and piston-mode resonance in the moon pool)
   - Moon pool damping devices (perforated plates, cofferdams, spring-loaded flaps)
   - Alternative: If a through-hull moon pool of this size is impractical, design an **open stern / split-hull** configuration (similar to the Hughes Glomar Explorer / Azorian) or a **deck-edge gantry** system

2. **Moon pool hydrodynamics:**
   - Calculate the natural period of the water column oscillation in the moon pool:
   
     $$T_n = 2\pi \sqrt{\frac{d + d_e}{g}}$$
   
     Where $d$ = draft of moon pool and $d_e$ = added mass correction for the water column.
   - Ensure this natural period does not coincide with operational wave periods (5–15 s range)
   - If resonance is unavoidable, specify damping measures

#### 3.2 Heavy-Lift Systems

Design a multi-mode lift system capable of all three operational scenarios:

**Mode A — Strand Jack Lift (0–200 m depth)**
- Number of strand jack units, capacity per unit, and arrangement on platform
- Strand specifications (diameter, grade, breaking strength)
- Synchronization system for ≤5 mm differential lift between jacks
- Heave compensation during lift through wave zone (active heave compensator specifications)
- Maximum lift speed and descent speed
- Wave-induced dynamic load amplification — how does the heave compensator attenuate this?

**Mode B — Controlled Buoyancy with Tethered Ascent Control (200–2,000 m)**
- Pontoon/buoyancy module deployment from platform
- Umbilical management for compressed air supply to pontoons at depth
- Wire rope winch system for ascent speed control and lateral positioning
- Handover procedure from buoyancy-controlled ascent to strand jack lift at 100–200 m depth

**Mode C — Combined (Hybrid)**
- Integration of Mode A and Mode B for the deepest and heaviest lifts
- Load-sharing protocol between buoyancy forces and mechanical lift forces
- Control system architecture (automated, semi-automated, manual override)

**Heave compensation (critical for nuclear-safe operations):**
- Active heave compensator (AHC) specifications: stroke length, velocity, force capacity
- Performance envelope: at what sea state does the AHC saturate?
- Consequence analysis: what happens to the suspended load if the AHC fails?
- Redundancy: is there a passive backup?

#### 3.3 Active Heave Compensation Under Extreme Waves

Because the platform must handle nuclear materials, uncontrolled dynamic loading on the suspended submarine is unacceptable. Provide:

1. Maximum allowable dynamic load variation on the submarine during lift: ±X% of static load
2. Sea state at which this tolerance is exceeded (operational limit for lift)
3. AHC sizing calculations showing stroke, velocity, and power requirements to maintain tolerance up to the operational limit
4. Emergency load-set-down procedure if AHC limits are exceeded mid-lift

### 4. Nuclear Safety & Radiological Containment Integration

The platform is not merely a crane — it must function as a **mobile nuclear facility** during and after retrieval of a submarine. Design the following:

#### 4.1 Radiation Shielding

1. **Shielding around moon pool / landing area:**
   - Material (steel, lead, polyethylene for neutron moderation, concrete)
   - Thickness calculations for gamma shielding (Cs-137 at 662 keV, Co-60 at 1.17/1.33 MeV) and neutron shielding (for K-27 criticality concern)
   - Target: reduce dose rates at nearest occupied area to ≤ 2.5 μSv/hr (annual limit consistent with 5 mSv to Category A workers at 2,000 hrs/yr)
   - Use the tenth-value layer (TVL) approach:

     $$n = \frac{\log_{10}(D_0 / D_{target})}{\text{TVL}}$$

     Where $n$ = number of TVLs required, $D_0$ = unshielded dose rate, $D_{target}$ = target dose rate
   - Provide TVL values for each shielding material and each isotope

2. **Reactor compartment handling bay:**
   - Enclosed, ventilated bay where the submarine's reactor compartment section is positioned on deck
   - HEPA-filtered negative-pressure ventilation (min. 10 air changes/hour)
   - Containment sump with capacity for 100% of water volume in cofferdam
   - Airlock entry/exit with personnel contamination monitors
   - Remote handling capability (cranes, manipulators) to avoid personnel entry

3. **Radiological monitoring network:**
   - Fixed gamma area monitors at ≥20 locations across the platform
   - Airborne contamination samplers (continuous particulate + iodine + tritium)
   - Stack monitors on all ventilation exhaust points
   - Seawater discharge monitors (continuous flow-through sampling)
   - Neutron detectors around moon pool (for criticality surveillance during K-27 operations)

#### 4.2 Nuclear Criticality Prevention (K-27 Specific)

K-27's fuel is fused with the lead-bismuth coolant in an uncharacterized geometry. During lift, tilting or mechanical shock could theoretically rearrange this mass into a more reactive configuration.

1. How does the platform design ensure the submarine remains level (±1°) during the entire lift through the moon pool?
2. Mechanical restraint and gimbal/cradle system to prevent tilting during wave-induced platform motions
3. Neutron absorber provisions: can borated water or cadmium sheets be deployed around the reactor area during lift as an additional criticality margin?
4. Emergency procedures if neutron count rate rises above alarm threshold during lift

#### 4.3 Contaminated Water Management

During the lift, large volumes of seawater will drain from the submarine and cofferdam. This water may be radiologically contaminated.

1. Drip tray and drainage system capacity (estimate volume: 1,000–5,000 m³)
2. Water treatment system: filtration, ion exchange, evaporation — capable of reducing activity to discharge limits
3. Holding tank capacity for water that cannot be immediately treated
4. Discharge monitoring and authorized discharge limits (Cs-137 < 10 Bq/L, per IAEA discharge guidelines)

### 5. Power Generation & Distribution

1. **Total power demand estimate:**
   - DP thrusters (account for maximum bollard pull in survival sea state)
   - Strand jack / winch systems during lift
   - Heave compensator hydraulic power units
   - HVAC and life support
   - Radiological monitoring and containment systems
   - Lighting, communications, hotel load
2. **Power plant configuration:**
   - Number and type of generators (diesel, LNG, or hybrid)
   - Redundancy requirements (N+1 minimum for DP; N+2 for nuclear safety systems)
   - Emergency power (UPS for radiation monitoring; emergency diesel generator for DP)
   - Blackout recovery time and procedure
3. **Electrical distribution:**
   - HV switchboard configuration
   - Redundant bus arrangement (split bus for DP)
   - Power management system (PMS) with automatic load shedding priority: nuclear safety systems are NEVER shed

### 6. Stability & Ballast System

1. **Intact stability analysis:**
   - GZ curve for all loading conditions (lightship, operating, survival, maximum lift load on deck)
   - Compliance with IMO MODU Code (2009) stability criteria
   - Effect of free-surface in moon pool on GM — is there a risk of negative GM during any phase?

2. **Damage stability:**
   - Two-compartment flooding survival (minimum)
   - Demonstrate positive stability after worst-case flooding (collision, grounding)
   - Progressive flooding scenarios during lift operations

3. **Ballast system:**
   - Active ballast system to maintain trim and heel during asymmetric lift loading
   - Ballast transfer rate sufficient to compensate for the load transfer rate of strand jacks (i.e., as the submarine weight comes onto the platform, ballast water is simultaneously pumped to maintain even keel)
   - Anti-heeling tanks with automatic control

4. **Stability during submarine lift-through-moon-pool sequence:**
   - As the submarine enters the moon pool from below, its weight transfers from water buoyancy to the platform structure. Model this progressive load transfer and demonstrate stable equilibrium at all stages.
   - Maximum list/trim at any stage: ≤2° (for nuclear safety — prevent tilting the submarine)

### 7. Accommodation & Life Safety

1. **Accommodation for 150–200 personnel** (crew + salvage team + nuclear specialists):
   - Cabin layout (1- and 2-person cabins for key staff; 4-person for general crew)
   - Mess, recreation, medical bay, helipad
   - Emergency mustering and lifeboat/liferaft capacity (SOLAS compliant, 100% + 100%)
2. **Helideck:**
   - Sized for Sikorsky S-92 or equivalent (Category A, ≥22.8 m diameter 'D' value)
   - Position relative to moon pool and radiological zones (upwind, maximum distance from reactor handling area)
   - Helicopter operations limitations in extreme weather
3. **Radiological zoning for accommodation:**
   - Accommodation block classified as GREEN zone (unrestricted, <1 μSv/hr)
   - Distance and shielding between accommodation and moon pool/reactor handling bay
   - Ensure HVAC intakes for accommodation are upwind of any radiological work areas; automatic damper closure on airborne contamination alarm

### 8. Operational Modes & Configuration

The platform must be adaptable. Define distinct operational configurations:

| Mode | Description | Key Systems Active |
|---|---|---|
| **Transit** | Self-propelled at ≥8 knots to operating site | Propulsion, navigation, hotel |
| **Station-keeping** | On-station, pre-lift survey and rigging work | DP, ROV systems, cranes |
| **Shallow lift (≤200 m)** | Strand jack lift through moon pool | Strand jacks, AHC, ballast compensation, nuclear containment |
| **Deep lift (200–2,000 m)** | Buoyancy-assisted lift with winch control; handover to strand jacks at depth | Winch array, pontoon control, AHC, nuclear containment |
| **Submarine on deck** | Post-lift, submarine secured, in transit to receiving facility | Reactor bay containment, transport stability, shielding |
| **Survival** | 100-year storm, no operations, submarine either below or secured on deck | DP (survival mode) or mooring, structural endurance, nuclear containment integrity |

For each mode, specify:
- Active systems and power demand
- Maximum sea state for that mode
- Transition procedure between modes
- Abort/emergency procedure specific to that mode

### 9. Construction Specification

1. **Overall dimensions:** Provide estimated length, beam, depth, draft (operating and survival)
2. **Lightship displacement and maximum operating displacement**
3. **Structural steel weight and major material quantities**
4. **Construction yard requirements** (dock size, crane capacity, special facilities)
5. **Estimated construction schedule** (months from steel cutting to delivery)
6. **Classification:** Which class society and notation (e.g., DNV +1A1 Column Stabilised Unit, DYNPOS-3, CRANE, HELDK-SH, Clean Design, NAUT-OSV(A))
7. **Estimated construction cost** (provide range with justification, benchmarking against comparable offshore units such as Heerema Sleipnir, Allseas Pioneering Spirit, etc.)

### 10. Historical Precedent Analysis

Analyze the following historical platforms/vessels and extract design lessons applicable to this project:

| Vessel/Platform | Relevance |
|---|---|
| **Hughes Glomar Explorer** (Project Azorian, 1974) | Purpose-built to lift a submarine (K-129) from 4,900 m. Moon pool design, capture vehicle, cover story. |
| **Heerema Sleipnir** (2019) | World's largest semi-submersible crane vessel. 2 × 10,000 t cranes. DP3. Benchmark for capability. |
| **Allseas Pioneering Spirit** | World's largest construction vessel. Can lift 48,000 t topsides. Catamaran hull. Relevant for through-hull lift concepts. |
| **Giant 4 / Mammoet–Smit consortium** (Kursk, 2001) | Modified barge for lifting Kursk hull using 26 strand jacks through hull-mounted grippers. |
| **Boskalis Vanguard** | Semi-submersible heavy transport vessel. Relevant for submarine transport after recovery. |
| **Blue Marlin / Dockwise (now Boskalis)** | Heavy transport semi-submersible. Precedent for carrying unconventional naval loads. |

For each, identify:
- What design features are directly transferable to the OSP?
- What limitations of that platform would the OSP need to overcome?
- What lessons learned from operations should inform the OSP design?

---

## Constraints

1. **Nuclear safety is the paramount design driver** — it overrides cost, schedule, and operational convenience at all decision points.
2. Comply with **IAEA safety standards** (GSR Part 3, SSR-5, SSG-47 for decommissioning).
3. Structural design per **DNV Offshore Standards** (OS-C101, OS-C103, OS-C301 for column-stabilised units).
4. Marine operations per **DNV-OS-H101** (Marine Operations, General) and **DNV-OS-H201** (Load Transfer Operations).
5. Stability per **IMO MODU Code 2009** as amended.
6. **Technology Readiness Level (TRL) ≥ 6** for all systems — no speculative technology. All proposed systems must have been demonstrated in a relevant environment.
7. Design life: **25 years** minimum (accounting for fatigue, corrosion, and obsolescence).
8. The platform must be **Ice Class** capable (minimum DNV ICE-C or equivalent) for Kara Sea and Barents Sea operations.
9. Environmental compliance: **MARPOL Annex I–VI**, **Polar Code** (for Arctic operations).
10. Assume no military classification restrictions unless stated — hull design parameters of target submarines may be used for engineering.

---

## Output Format

- Use clear hierarchically numbered sections (1, 1.1, 1.1.1, etc.)
- Include engineering diagrams described textually or in ASCII/diagram form where they add clarity
- Include tables for all parametric comparisons and trade studies
- Show all critical calculations with equations, assumptions, and units
- Flag all assumptions explicitly with **[ASSUMPTION]** tags
- Cite historical precedents (Project Azorian, Kursk salvage, Sleipnir, Pioneering Spirit)
- Provide decision trees for critical design branch points
- Include a risk register specific to the platform design (structural, hydrodynamic, nuclear safety)
- Provide a bill of materials for major systems at a pre-FEED (Front End Engineering Design) level of detail
- Include a CAPEX estimate with ±30% accuracy and a benchmarked justification

---

## Guiding Principle

> *The ocean will try to destroy this platform with 25-meter waves, hurricane-force winds, and relentless fatigue loading. The submarine resting on its deck will contain enough radioactive material to contaminate an entire sea. The platform must be designed so that even in the worst 100-year storm, with one major system failed, the nuclear containment remains unbreached, the submarine remains secured, and every person on board goes home safely.*

---

*Prompt Version 1.0 — 12 February 2026*
*Reference Documents: `sunken-nuclear-submarines-report.md`, `nuclear-submarine-salvage-operation-plan.md`*
