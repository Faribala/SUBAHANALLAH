# 13 — Construction Specification

**Ocean Salvage Platform (OSP) — Pre-FEED Deliverable**
**Document:** 13-construction-specification.md
**Date:** 12 February 2026

---

## 1. Build Strategy

### 1.1 Modular Construction Approach

The OSP is too large and complex for single-location construction. A distributed modular build is recommended:

```mermaid
graph TD
    subgraph "MODULE FABRICATION (Multiple Yards)"
        M1[Module 1: Port Pontoon<br>245 × 18 × 12 m<br>~12,000 t steel]
        M2[Module 2: Stbd Pontoon<br>245 × 18 × 12 m<br>~12,000 t steel]
        M3[Module 3: Port Columns ×4<br>18 × 18 × 26 m each<br>~4,500 t steel]
        M4[Module 4: Stbd Columns ×4<br>18 × 18 × 26 m each<br>~4,500 t steel]
        M5[Module 5: Upper Hull / Deck Box<br>275 × 80 m deck structure<br>~9,000 t steel]
    end
    
    subgraph "TOPSIDE MODULES"
        T1[Module 6: Accommodation<br>50 × 18 × 15 m<br>~2,500 t]
        T2[Module 7: Reactor Bay<br>30 × 18 × 20 m<br>~6,500 t (shielding)]
        T3[Module 8: Engine Rooms ×4<br>18 × 30 × 8 m each<br>~3,000 t total]
        T4[Module 9: Lift System<br>Gantry beams + strand jacks<br>~5,150 t]
    end
    
    subgraph "INTEGRATION (Drydock)"
        I1[Float out pontoons]
        I2[Install columns on pontoons]
        I3[Float-on deck box]
        I4[Install topsides modules by crane]
    end
    
    M1 --> I1
    M2 --> I1
    M3 --> I2
    M4 --> I2
    M5 --> I3
    T1 --> I4
    T2 --> I4
    T3 --> I4
    T4 --> I4
    
    I1 --> I2 --> I3 --> I4
    I4 --> COM[Commissioning<br>& Sea Trials]
```

### 1.2 Construction Facilities Required

| Facility | Requirement |
|----------|-------------|
| Drydock | ≥ 300 m × 90 m × 14 m (depth) |
| Cranage | ≥ 3,000 t lift capacity for topside module installation |
| Steel fabrication halls | ≥ 50,000 m² covered area |
| Quayside | ≥ 400 m with 15 m water depth |
| Candidate yards | Samsung Heavy Industries (KR), DSME (KR), Hyundai HI (KR), Keppel (SG), Sembcorp (SG), Severodvinsk (RU) |

---

## 2. Construction Schedule

| WBS | Activity | Duration (months) | Start (Month) | End (Month) |
|-----|----------|-------------------|---------------|-------------|
| 1.0 | Detail Engineering | 18 | M0 | M18 |
| 2.0 | Material Procurement (long lead) | 24 | M6 | M30 |
| 2.1 | — Steel plate procurement | 12 | M6 | M18 |
| 2.2 | — Main engines procurement | 18 | M8 | M26 |
| 2.3 | — Azimuth thrusters procurement | 20 | M8 | M28 |
| 2.4 | — Strand jacks / AHC | 18 | M10 | M28 |
| 2.5 | — Lead shielding / nuclear equipment | 16 | M12 | M28 |
| 3.0 | Pontoon fabrication (2 hulls) | 18 | M12 | M30 |
| 4.0 | Column fabrication (8 units) | 14 | M16 | M30 |
| 5.0 | Deck box fabrication | 16 | M14 | M30 |
| 6.0 | Topside modules fabrication | 14 | M18 | M32 |
| 7.0 | Integration in drydock | 8 | M30 | M38 |
| 8.0 | Outfitting (mechanical/electrical) | 12 | M30 | M42 |
| 9.0 | Commissioning | 6 | M38 | M44 |
| 10.0 | Sea trials | 3 | M44 | M47 |
| 11.0 | Classification & certification | 2 | M46 | M48 |
| **TOTAL** | | | | **48 months (4 years)** |

**[ASSUMPTION]** Schedule based on comparable semi-submersible construction projects (e.g., Heerema Sleipnir: ~4 years).

---

## 3. Steel Specification

### 3.1 Steel Grades (per `05-structural-design.md`)

| Grade | Standard | Yield (MPa) | UTS (MPa) | Application |
|-------|----------|-------------|-----------|-------------|
| NV-DH36 | DNV Rules Pt.2 Ch.2 | 355 | 490–630 | General hull plating, internal structure |
| NV-EH36 | DNV Rules Pt.2 Ch.2 | 355 | 490–630 | Primary strength members, Arctic service |
| NV-EH40 | DNV Rules Pt.2 Ch.2 | 390 | 510–660 | Highly stressed joints, gantry beams |
| NV-EH47 | DNV Rules Pt.2 Ch.2 | 460 | 570–720 | Column-pontoon connections (critical nodes) |

### 3.2 Steel Quantities

| Component | Grade | Plate Thickness Range (mm) | Weight (t) |
|-----------|-------|---------------------------|-----------|
| Pontoons (2) | DH36 / EH36 | 16–30 | 18,000 |
| Columns (8) | EH36 / EH40 | 20–35 | 8,000 |
| Deck box (transverse + longitudinal) | DH36 | 14–25 | 7,000 |
| Gantry beams | EH40 / EH47 | 30–50 | 1,500 |
| Accommodation structure | DH36 | 8–14 | 1,800 |
| Reactor bay structure | EH36 | 20–35 | 1,200 |
| Miscellaneous (brackets, stiffeners) | DH36 | 10–20 | 4,500 |
| **TOTAL** | | | **42,000** |

### 3.3 Welding Requirements

| Parameter | Specification |
|-----------|---------------|
| Process | FCAW (primary), SAW (butt joints in flat position) |
| Pre-qualification | All WPSs to AWS D1.1 or DNV Rules |
| Welder qualification | DNV/AWS certified; re-tested every 6 months |
| Full penetration butt welds | All primary structural joints |
| Fillet welds | Secondary attachments; minimum throat = 0.7 × thinner plate |
| NDT (primary joints) | 100% UT + 100% visual; 20% TOFD |
| NDT (secondary joints) | 20% UT + 100% visual |
| Acceptance criteria | DNV-OS-C401, Quality level B (ISO 5817) |
| PWHT | Required for thickness ≥ 50 mm; EH47 joints |

---

## 4. Coating Specification

| Zone | System | DFT (µm) | Expected Life |
|------|--------|----------|---------------|
| Underwater (below LWL) | Epoxy anti-corrosion (2 coats) + anti-fouling TBT-free | 350 + 250 | 5 years (AF); 15 years (AC) |
| Splash zone (LWL ± 5 m) | Epoxy glass flake (3 coats) | 1,000 | 15 years |
| Topsides | Epoxy primer + polyurethane topcoat | 320 | 15 years |
| Ballast tanks | Epoxy (2 coats) per PSPC | 320 | 15 years |
| Moon pool / channel | Epoxy glass flake + sacrificial anodes | 1,000 | 10 years |
| Reactor bay interior | Decontaminable epoxy (smooth, non-porous) | 500 | 15 years |
| Accommodation | Epoxy primer + Chlorinated rubber topcoat | 250 | 15 years |

---

## 5. Key Equipment Specifications

### 5.1 Main Engines

| Parameter | Specification |
|-----------|---------------|
| Make/Model | Wärtsilä 16V46F or equivalent |
| Number | 6 |
| Power each | 18.6 MW at 514 rpm |
| Configuration | V-16 cylinder, medium-speed diesel |
| Fuel | MGO (DMA grade, ISO 8217) |
| SFOC | ≤ 185 g/kWh at 85% MCR |
| Emissions | IMO Tier III (NOx); 0.10% S (ECA compliant) |
| SCR | Required for Tier III compliance |
| Weight per engine | ~190 t (dry) |
| Dimensions | ~15 m L × 5.5 m W × 7 m H |

### 5.2 Azimuth Thrusters

| Parameter | Specification |
|-----------|---------------|
| Make/Model | Rolls-Royce (Kongsberg) AZP150 or equivalent |
| Number | 10 |
| Power each | 6,000 kW |
| Bollard pull each | 450 t (forward); 400 t (reverse) |
| Propeller diameter | 5.0 m |
| Type | Fixed-pitch with nozzle |
| Ice class | ICE-1A (for Kara Sea operations) |
| Rotation | 360° continuous |
| Weight per unit | ~120 t (including motor) |

---

## 6. Outfitting and Commissioning

### 6.1 Outfitting Sequence

| Phase | Activities |
|-------|-----------|
| Mechanical outfitting | Piping (ballast, fuel, FW, SW, steam, hydraulic); HVAC ducting; crane installation |
| Electrical outfitting | Cable pull (~500 km of cable); switchgear; transformers; MCC; lighting |
| Instrument & control | SCADA; DP system; navigation; communication; radiation monitoring |
| Nuclear systems | Lead shielding installation; ventilation system; water treatment plant |
| Heavy lift system | Gantry beam installation; strand jack mounting; AHC system; hydraulic piping |
| Accommodation | Cabin finishing; galley equipment; furniture; fire/safety systems |

### 6.2 Commissioning Phases

| Phase | Duration (weeks) | Activities |
|-------|------------------|-----------|
| Pre-commissioning | 8 | Flushing piping; megger testing cables; cold checks of systems |
| Mechanical completion | 4 | Punch-list closure; documentation review |
| Energisation | 2 | Generator first run; switchboard energisation; UPS |
| Systems commissioning | 8 | Each system tested individually (ballast, DP, HVAC, fire, etc.) |
| Integrated testing | 4 | DP FMEA proving trials; power management; emergency systems |
| **Total** | **26 weeks** | |

### 6.3 Sea Trials

| Test | Duration | Acceptance Criteria |
|------|----------|---------------------|
| Speed trials | 2 days | ≥ 10 kn at 80% MCR |
| Manoeuvring trials | 1 day | Turning circle; stopping distance; crash stop |
| DP trials (FMEA proving) | 5 days | Worst-case single-failure: maintain position per DNV-RP-E306 |
| Ballast system test | 2 days | Full draft change 12→26→12 m; all pumps; remote control |
| Lift system test (no load) | 3 days | Strand jack operation; AHC response; control system |
| Navigation & communication | 1 day | All nav aids; GMDSS; VSAT |
| Life-saving equipment | 1 day | Lifeboat launch; FRC; fire drills |
| **Total sea trials** | **15 days** | |

---

## 7. Estimated Construction Cost

| Item | Cost (USD million) | % of Total |
|------|--------------------|-----------|
| Detail engineering | 150 | 5.0% |
| Steel procurement (42,000 t × $1,500/t) | 63 | 2.1% |
| Steel fabrication & assembly | 800 | 26.7% |
| Main engines (6 × $15M) | 90 | 3.0% |
| Thrusters (10 × $8M) | 80 | 2.7% |
| DP system | 40 | 1.3% |
| Heavy lift system (strand jacks, AHC, yoke) | 200 | 6.7% |
| Nuclear containment systems | 180 | 6.0% |
| Electrical systems (cable, switchgear, VFD) | 120 | 4.0% |
| Piping & mechanical | 150 | 5.0% |
| Accommodation outfitting | 80 | 2.7% |
| Coatings | 40 | 1.3% |
| Commissioning & sea trials | 60 | 2.0% |
| Class & certification | 20 | 0.7% |
| Project management & insurance | 180 | 6.0% |
| ROV systems (4 units) | 50 | 1.7% |
| Buoyancy pontoons (18 units) | 90 | 3.0% |
| Contingency (20%) | 479 | 16.0% |
| **TOTAL** | **~2,872** | **~$2.9 billion** |

**[ASSUMPTION]** Cost estimates at ±30% accuracy (Pre-FEED level, AACE Class 4 estimate).

---

*Cross-references: `01-hull-form-selection.md`, `05-structural-design.md`, `07-heavy-lift-system.md`, `08-nuclear-safety-containment.md`, `09-power-generation.md`, `16-bill-of-materials.csv`*
