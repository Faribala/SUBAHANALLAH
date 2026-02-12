# 05 — Structural Design & Analysis

**Ocean Salvage Platform (OSP) — Pre-FEED Deliverable**
**Document:** 05-structural-design.md
**Date:** 12 February 2026

---

## 1. Introduction

This document defines the structural design for the OSP hybrid catamaran semi-submersible. All design is per DNV-OS-C101 (Design of Offshore Steel Structures), DNV-OS-C103 (Structural Design of Column Stabilised Units), and DNV-RP-C203 (Fatigue Design of Offshore Steel Structures).

---

## 2. Structural Configuration

### 2.1 Primary Structural Members

| Member | Dimensions | Function |
|--------|-----------|----------|
| Pontoons (×2) | 245 m × 18 m × 12 m | Buoyancy, ballast tanks, machinery |
| Columns (×8) | 18 m × 18 m × 16 m (submerged) | Waterplane, wave transparency |
| Upper hull / deck box | 275 m × 80 m × 6 m (depth) | Main deck, equipment, accommodation |
| Lower transverse bracing (×4) | 44 m × 8 m × 8 m | Connect port/stbd pontoons; shear transfer |
| Upper transverse box girders (×6) | 44 m × 12 m × 6 m | Connect hulls at deck level; primary bending |
| Moon pool interface structure | 135 m × 20 m opening perimeter | Edge reinforcement, strand jack rail support |

### 2.2 Structural Arrangement

```
        CROSS-SECTION AT MIDSHIPS
        
    ┌─────────────────────────────────────────────────────────┐
    │                 UPPER DECK BOX (6 m depth)             │ ← +38 m
    │   ┌────────┐                              ┌────────┐  │
    │   │DECK PL │   UPPER BOX GIRDERS (×6)     │DECK PL │  │
    │   │ 20 mm  │   12m W × 6m D               │ 20 mm  │  │ ← +32 m
    ├───┴────────┴───┐                      ┌───┴────────┴──┤
    │   COLUMN       │                      │   COLUMN      │
    │   18 × 18 m    │     OPEN MOON        │   18 × 18 m   │
    │   Plate: 22 mm │      POOL            │   Plate: 22mm │ 
    │   Frame: 800mm │     20 m CLEAR       │   Frame: 800mm│
~~~~│~~~~~~~~~~~~~~~~│~~~~~~~~~~~~~~~~~~~~~~│~~~~~~~~~~~~~~~│~~~~  ← WL +22m
    │                │                      │               │
    │   COLUMN       │                      │   COLUMN      │
    ├───┬────────┬───┘                      └───┬────────┬──┤
    │   │LOWER   │   LOWER BRACE (×4)          │LOWER   │  │ ← +12 m
    │   │BRACING │   44m × 8m × 8m             │BRACING │  │
    ├───┴────────┴──────────────────────────────┴────────┴──┤
    │   PONTOON (PORT)           │        PONTOON (STBD)    │
    │   245 × 18 × 12 m         │        245 × 18 × 12 m   │
    │   Shell: 25 mm             │        Shell: 25 mm      │
    │   Frames: 750 mm spacing   │        Frames: 750 mm    │
    │   Floors: 3600 mm spacing  │        Floors: 3600 mm   │
    └────────────────────────────┴──────────────────────────┘  ← 0 m (keel)
```

---

## 3. Global Load Analysis

### 3.1 Load Definitions

Per DNV-OS-C101:

| Load Category | Symbol | Description |
|--------------|--------|-------------|
| Permanent (G) | G | Lightship weight, permanent equipment |
| Variable (Q) | Q | Payload, consumables, ballast |
| Environmental (E) | E | Wave, wind, current, ice |
| Accidental (A) | A | Collision, dropped objects, fire/explosion |
| Deformation (D) | D | Temperature, fabrication tolerances |

### 3.2 Design Wave Methodology

Per DNV-OS-C103, design waves are selected to maximize specific structural responses:

**Governing environment: Norwegian Sea 100-year** (Hs = 15.0 m, Tp = 16.0 s)

Design wave parameters for each structural response:

| Response | Wave Direction | Wave Height H (m) | Wave Period T (s) | Wave Length λ (m) |
|----------|---------------|-------------------|-------------------|-------------------|
| Vertical bending (sag) | Head (0°) | 27.9 | 14.9 | 346 |
| Vertical bending (hog) | Head (0°) | 27.9 | 14.9 | 346 |
| Transverse shear / split | Beam (90°) | 27.9 | 12.0 | 225 |
| Torsion | Quartering (45°) | 27.9 | 13.5 | 285 |
| Longitudinal shear | Quartering (30°) | 27.9 | 13.0 | 264 |

**Design wave height:** $H_d = 1.86 \times H_{s,100yr} = 1.86 \times 15.0 = 27.9$ m

### 3.3 Global Bending Moment

**Sagging (wave crest amidships):**

For a catamaran semi-submersible, the primary sagging loads come from:
- Wave crest amidships with troughs at bow/stern
- Buoyancy concentrated at columns amidships, weight distributed along length

$$M_{sag} = \frac{1}{8} \rho g B_e H_d L_{eff}^2 C_{response}$$

Where:
- $\rho g$ = 10,055 N/m³
- $B_e$ = effective waterplane beam ≈ 36 m (2 × 18 m column width)
- $H_d$ = 27.9 m
- $L_{eff}$ = 245 m (pontoon length)
- $C_{response}$ = 0.035 **[ASSUMPTION]** — response coefficient for semi-sub in head seas

$$M_{sag} = \frac{1}{8} \times 10{,}055 \times 36 \times 27.9 \times 245^2 \times 0.035$$

$$M_{sag} = \frac{1}{8} \times 10{,}055 \times 36 \times 27.9 \times 60{,}025 \times 0.035$$

$$M_{sag} = \frac{1}{8} \times 2.12 \times 10^{10} = 2.65 \times 10^9 \text{ N·m} = 2{,}650 \text{ MN·m}$$

**Hogging (wave trough amidships):**

$$M_{hog} \approx 0.85 \times M_{sag} = 2{,}253 \text{ MN·m}$$ **[ASSUMPTION]**

### 3.4 Transverse Split Force

The transverse split force tries to push the two hulls apart (or together) in beam seas:

$$F_{split} = \rho g A_{wp,one\_hull} \times \eta_{crest} \times C_{split}$$

Where $\eta_{crest}$ = 0.55 × $H_d$ = 15.3 m, $A_{wp,one\_hull}$ = 4 × 18 × 18 = 1,296 m², $C_{split}$ = 1.2 **[ASSUMPTION]**

$$F_{split} = 10{,}055 \times 1{,}296 \times 15.3 \times 1.2 = 239{,}000 \text{ kN} = 239 \text{ MN}$$

### 3.5 Torsional Moment

In quartering seas, the catamaran hull is subjected to torsion:

$$T_{torsion} \approx 0.5 \times F_{split} \times L_{eff} / 4 = 0.5 \times 239{,}000 \times 61.25 = 7{,}319 \text{ MN·m}$$

### 3.6 Global Shear Force

$$V_{max} = \frac{2 M_{sag}}{0.6 L_{eff}} = \frac{2 \times 2{,}650}{0.6 \times 245} = 36.1 \text{ MN}$$

### 3.7 Global Load Summary

| Load Component | Value | Unit | Governing Condition |
|----------------|-------|------|---------------------|
| Max sagging BM | 2,650 | MN·m | Head seas, 100-yr |
| Max hogging BM | 2,253 | MN·m | Head seas, 100-yr |
| Max shear force | 36.1 | MN | Head seas, 100-yr |
| Split force | 239 | MN | Beam seas, 100-yr |
| Torsional moment | 7,319 | MN·m | Quartering seas, 100-yr |

---

## 4. Local Loads

### 4.1 Slamming Pressures

Bottom slamming on pontoon (if exposed during large heave):

$$p_{slam} = C_{slam} \times \frac{1}{2} \rho_w v_{rel}^2$$

Where:
- $C_{slam}$ = 5.0 (flat bottom) **[ASSUMPTION]**
- $v_{rel}$ = relative velocity between pontoon and wave = 3.0 m/s **[ASSUMPTION]**

$$p_{slam} = 5.0 \times 0.5 \times 1{,}025 \times 3.0^2 = 23.1 \text{ kPa}$$

**[ASSUMPTION]** Pontoons remain submerged in all conditions; slamming occurs only on column-to-pontoon transition zones.

### 4.2 Wave-in-Deck Impact

From `03-hydrodynamic-analysis.md`, wave-in-deck loading is possible during 100-year conditions:

$$p_{wid} = C_{wid} \times \frac{1}{2} \rho_w v_{deck}^2$$

Where $C_{wid}$ = 2.5, $v_{deck}$ = 4.0 m/s (estimated wave crest velocity at deck underside) **[ASSUMPTION]**

$$p_{wid} = 2.5 \times 0.5 \times 1{,}025 \times 4.0^2 = 20.5 \text{ kPa}$$

Applied to: transverse box girder undersides + deck structure between columns

### 4.3 Green Water Pressures

From `03-hydrodynamic-analysis.md`:

| Condition | Overtopping Height (m) | Pressure (kPa) |
|-----------|----------------------|----------------|
| Moderate | 1.0 | 15.1 |
| Severe | 3.0 | 45.3 |

### 4.4 Hydrostatic Collapse on Pontoons

External pressure on pontoon at maximum submergence:

In survival draft (26 m), pontoon bottom at 0 m → hydrostatic head = 26 m

$$p_{hydro} = \rho_w g d = 1{,}025 \times 9.81 \times 26 = 261 \text{ kPa}$$

Pontoon shell must resist this external pressure without buckling.

---

## 5. Material Selection

### 5.1 Steel Grade Selection Table

| Zone | Steel Grade | Min Yield (MPa) | Thickness Range (mm) | Rationale |
|------|------------|-----------------|---------------------|-----------|
| Pontoon shell, below WL | NV-EH36 | 355 | 22–30 | High strength for hydrostatic + ice loads |
| Pontoon internal structure | NV-DH36 | 355 | 14–22 | Good low-temp toughness for Arctic |
| Column shell (ice belt) | NV-EH36 | 355 | 25–35 | Ice impact + wave loads |
| Column shell (above ice belt) | NV-DH36 | 355 | 20–28 | Wave loading |
| Upper deck box | NV-DH36 | 355 | 16–24 | Primary global bending member |
| Transverse box girders | NV-EH36 | 355 | 20–30 | High split-force loads |
| Lower transverse bracing | NV-EH36 | 355 | 22–30 | Shear transfer, fatigue-critical |
| Moon pool edge structure | NV-EH40 | 390 | 25–40 | Stress concentration; fatigue-critical |
| Strand jack gantry | NV-EH36 | 355 | 25–50 | Heavy concentrated loads |
| Helideck | NV-A36 | 355 | 8–12 | Standard deck loads |

### 5.2 Low Temperature Requirements

Per DNV-OS-C101, design temperature for material selection:

| Region | WDLT (°C) | Charpy Test Temp (°C) |
|--------|----------|----------------------|
| Kara Sea | −40 | −40 (EH36/EH40 grade) |
| Barents Sea | −30 | −40 |
| Norwegian Sea | −15 | −20 (DH36 grade) |
| N. Atlantic | −5 | −20 |

**Governing:** Kara Sea at −40°C → EH36/EH40 grades required in primary structure. DH36 acceptable for internal/secondary structure.

---

## 6. Scantling Table

### 6.1 Key Structural Zones

| Zone | Plate Thick. (mm) | Stiffener Type | Stiffener Spacing (mm) | Frame/Floor Spacing (mm) |
|------|--------------------|---------------|----------------------|------------------------|
| Pontoon bottom | 25 | HP 300×12 | 650 | 3,600 |
| Pontoon sides | 22 | HP 260×10 | 700 | 3,600 |
| Pontoon top (inner bottom) | 22 | HP 280×11 | 700 | 3,600 |
| Pontoon inner sides (tanks) | 16 | HP 220×10 | 750 | 3,600 |
| Column shell (ice belt) | 32 | FB 350×25 | 400 | 800 |
| Column shell (general) | 25 | HP 300×12 | 600 | 800 |
| Column internal decks | 16 | HP 220×10 | 750 | — |
| Deck box plating, top | 20 | HP 280×11 | 700 | 3,600 |
| Deck box plating, bottom | 22 | HP 300×12 | 650 | 3,600 |
| Transverse box girder web | 25 | HP 320×12 | 600 | 2,400 |
| Transverse box girder flanges | 30 | — | — | — |
| Moon pool edge plates | 35 | HP 400×16 | 500 | 600 |
| Strand jack foundation | 50 | Built-up girders | N/A | 1,200 |

### 6.2 Stiffener Definitions

| Designation | Type | Depth (mm) | Flange/Bulb (mm) | Web Thick. (mm) |
|-------------|------|-----------|------------------|----------------|
| HP 300×12 | Bulb flat | 300 | Bulb | 12 |
| HP 280×11 | Bulb flat | 280 | Bulb | 11 |
| HP 260×10 | Bulb flat | 260 | Bulb | 10 |
| HP 220×10 | Bulb flat | 220 | Bulb | 10 |
| HP 320×12 | Bulb flat | 320 | Bulb | 12 |
| HP 400×16 | Bulb flat | 400 | Bulb | 16 |
| FB 350×25 | Flat bar | 350 | — | 25 |

---

## 7. Fatigue Assessment

### 7.1 Methodology

Per DNV-RP-C203:
- **S-N curve approach** with Palmgren–Miner cumulative damage rule
- **Design fatigue life** = Design life × DFF = 25 years × DFF
- **Design Fatigue Factor (DFF):** depends on inspectability and consequence of failure

### 7.2 DFF Assignment

| Location | Inspectable? | DFF | Design Fatigue Life (years) |
|----------|-------------|-----|---------------------------|
| Pontoon/column connections | Yes (internal) | 3.0 | 75 |
| Transverse brace connections | Yes (external) | 2.0 | 50 |
| Moon pool corner brackets | Yes (internal) but critical | 10.0 | 250 |
| Upper deck girder connections | Yes | 2.0 | 50 |
| Strand jack foundations | Yes | 3.0 | 75 |
| Lower brace tubular joints | Difficult (subsea in survival) | 3.0 | 75 |

### 7.3 Fatigue-Critical Detail Catalog

| Detail # | Location | S-N Curve | Detail Class | DFF | Notes |
|----------|----------|-----------|-------------|-----|-------|
| FD-01 | Column-to-pontoon bracket toe | D (DNV-RP-C203) | D | 3.0 | Geometric stress concentration; grind weld toe |
| FD-02 | Moon pool corner radius | C1 | C1 | 10.0 | Critical for structural integrity; radiused corner with full-pen weld |
| FD-03 | Transverse brace tubular joint | T (tubular joint) | T | 3.0 | Hot-spot stress approach; SCF per Efthymiou |
| FD-04 | Column-to-deck bracket | D | D | 2.0 | Standard bracket with soft toe |
| FD-05 | Pontoon longitudinal butt weld | C2 | C2 | 2.0 | Full-penetration butt weld, ground flush |
| FD-06 | Strand jack foundation stiffener heel | E | E | 3.0 | High cyclic loading from lift operations |

### 7.4 Fatigue Damage Calculation (Example: FD-01)

**Location:** Column-to-pontoon bracket toe (Port hull, column 2)

Using S-N curve D: $\log N = 12.164 - 3 \log \Delta\sigma$ for N < 10⁷; $\log N = 15.606 - 5 \log \Delta\sigma$ for N > 10⁷

**[ASSUMPTION]** Stress range histogram from spectral fatigue analysis (simplified):

| Stress Range Δσ (MPa) | Number of Cycles n (25 yr) | N (from D-curve) | Damage (n/N) |
|----------------------|-------------------------|-------------------|-------------|
| 120 | 1.0 × 10⁴ | 8.47 × 10⁵ | 0.0118 |
| 100 | 5.0 × 10⁴ | 1.46 × 10⁶ | 0.0342 |
| 80 | 2.0 × 10⁵ | 2.85 × 10⁶ | 0.0702 |
| 60 | 1.0 × 10⁶ | 6.76 × 10⁶ | 0.1479 |
| 40 | 5.0 × 10⁶ | 2.28 × 10⁷ | 0.2193 |
| 20 | 3.0 × 10⁷ | 4.65 × 10⁸ | 0.0645 |
| 10 | 6.0 × 10⁷ | 1.49 × 10¹⁰ | 0.0040 |
| **Total** | | | **D = 0.552** |

Allowable damage: $D_{allow} = 1.0 / DFF = 1.0 / 3.0 = 0.333$

⚠️ **D = 0.552 > 0.333 — FAILS DFF = 3.0 requirement**

**Remediation:**
1. Upgrade detail class from D to C1 by grinding weld toe to radius ≥ 3 mm → reduces stress by ~20%
2. Apply post-weld treatment (TIG dressing or ultrasonic peening) → gains 2 detail classes
3. After remediation, estimated D reduces to ~0.22 < 0.333 ✓

---

## 8. Corrosion Protection

### 8.1 Corrosion Allowances

| Zone | Corrosion Allowance (mm) | Basis |
|------|------------------------|-------|
| Pontoon shell (external, below WL) | 3.0 | DNV-OS-C101 + ice-class addition |
| Column shell (splash zone) | 4.0 | Enhanced for Arctic splash zone |
| Column shell (below splash) | 2.5 | Submerged; CP protected |
| Internal structure (ballast tanks) | 2.0 | Coating + CP |
| Internal structure (dry spaces) | 1.0 | Coating only |
| Main deck (exposed) | 1.5 | Coating |
| Moon pool area | 3.5 | Intermittent wetting; contaminated water exposure |

### 8.2 Coating Specification

| Zone | Coating System | DFT (μm) | Type |
|------|---------------|-----------|------|
| External hull (below WL) | Epoxy primer + anti-fouling | 350 + 250 | Jotamastic 80 + SeaQuantum X200 |
| Splash zone | Glass-flake epoxy | 500 | Jotamastic 80 GF |
| Internal ballast tanks | Epoxy + polyurethane | 320 | Per PSPC (IMO MSC.215(82)) |
| Main deck | Epoxy + polyurethane topcoat | 250 | Standard deck coating |
| Moon pool (internal) | Epoxy + nuclear-grade decontaminable overcoat | 400 | Strippable coating for decontamination |
| Ice belt | Glass-flake epoxy, reinforced | 600 | Abrasion-resistant |

### 8.3 Cathodic Protection

| Zone | System | Anode Type | Design Life |
|------|--------|-----------|-------------|
| Submerged hull (pontoon) | Sacrificial anodes | Al-Zn-In alloy (DNV RP-B401) | 25 years |
| Column (below WL) | Sacrificial anodes | Al-Zn-In alloy | 25 years |
| Ballast tanks | Sacrificial anodes | Zn block type | 5 years (replace at drydock) |
| Moon pool structure | ICCP (impressed current) | Platinized titanium anodes | 25 years (replaceable anodes) |

**Total sacrificial anode mass (estimated):** 450 t (Al-Zn-In alloy)

---

## 9. FEA Methodology Specification

### 9.1 Global FEA Model

| Parameter | Specification |
|-----------|--------------|
| Software | ANSYS Mechanical / Sesam GeniE + Sestra |
| Element type | 4-node shell (QUAD4) for plating; beam (BEAM2) for stiffeners |
| Mesh size (global) | 1.0–1.5 × frame spacing (800–1,200 mm) |
| Mesh size (fine, at hot spots) | t × t (plate thickness, ~25 mm) |
| Boundary conditions | Inertia relief (free-floating); no rigid supports |
| Mass modelling | Distributed mass elements; point masses for equipment |
| Load cases | 12 design wave cases + still-water + ballast variations |

### 9.2 Sub-Model Requirements

| Area | Mesh Size | Purpose |
|------|-----------|---------|
| Column-pontoon connection | 25 mm (t × t) | Hot-spot stress for fatigue |
| Moon pool corners | 15 mm | Stress concentration; crack initiation |
| Transverse brace joints | 20 mm | Tubular joint fatigue per Efthymiou |
| Strand jack foundations | 30 mm | Concentrated load distribution |

### 9.3 Load Application

| Method | Application |
|--------|------------|
| Design wave (deterministic) | ULS global strength check |
| Spectral (frequency domain) | FLS fatigue screening |
| Time-domain (stochastic) | FLS detailed fatigue at critical joints + ALS |

---

## 10. Limit State Check Summary

### 10.1 ULS (Ultimate Limit State)

| Check | Load Combination | Criterion | Method |
|-------|-----------------|-----------|--------|
| Yielding | 1.3G + 1.3Q + 1.0E | $\sigma_{vM} \leq f_y / \gamma_M$ | FEA global model |
| Buckling (plate) | 1.3G + 1.3Q + 1.0E | Per DNV-OS-C101 Ch.6 | Johnson-Ostenfeld / Perry-Robertson |
| Buckling (stiffened panel) | 1.3G + 1.3Q + 1.0E | Per DNV-RP-C201 | Effective width approach |
| Column hydrostatic | External pressure at max draft | Collapse check per DNV | Ring stiffener design |

### 10.2 ALS (Accidental Limit State)

| Check | Scenario | Criterion |
|-------|----------|-----------|
| Progressive collapse | 2-compartment flooding | Residual stability + structural integrity |
| Collision | 5,000 t vessel at 2 m/s | Energy absorption; no breach to nuclear spaces |
| Dropped object | 100 t from 30 m onto main deck | Local rupture acceptable; no breach to nuclear spaces |
| Fire | Machinery space fire | A-60 divisions maintain structural integrity |

### 10.3 FLS (Fatigue Limit State)

| Check | Method | Criterion |
|-------|--------|-----------|
| Screening | Spectral analysis, simplified | D < 1.0/DFF |
| Detailed | Stochastic time-domain, rainflow counting | D < 1.0/DFF |
| Inspection planning | Based on calculated fatigue lives | Interval = 0.5 × calculated fatigue life |

### 10.4 SLS (Serviceability Limit State)

| Check | Limit | Basis |
|-------|-------|-------|
| Deck deflection | L/500 of span | Strand jack rail alignment |
| Global elastic deflection | L/1000 of overall length | Equipment alignment |
| Vibration | f₁ > 2 Hz for deck | Human comfort; equipment sensitivity |

---

## 11. Structural Weight Estimate

| Component | Weight (t) | % of Total |
|-----------|-----------|-----------|
| Pontoons (×2, hull steel) | 15,200 | 36% |
| Columns (×8) | 6,400 | 15% |
| Upper deck box structure | 8,500 | 20% |
| Transverse box girders (×6) | 3,200 | 8% |
| Lower transverse bracing (×4) | 2,800 | 7% |
| Moon pool edge structure | 1,400 | 3% |
| Strand jack gantry structure | 2,000 | 5% |
| Miscellaneous (brackets, doublers, etc.) | 2,500 | 6% |
| **Total structural steel** | **42,000** | **100%** |

**[ASSUMPTION]** Steel weight estimated using specific steel weight of 0.20–0.25 t/m³ enclosed volume, benchmarked against Pioneering Spirit (~52,000 t steel for 382 m vessel).

---

*Cross-references: `01-hull-form-selection.md`, `02-environmental-design-basis.md`, `03-hydrodynamic-analysis.md`, `06-moon-pool-design.md`*
