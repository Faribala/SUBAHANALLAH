# 02 — Environmental & Metocean Design Basis

**Ocean Salvage Platform (OSP) — Pre-FEED Deliverable**
**Document:** 02-environmental-design-basis.md
**Date:** 12 February 2026

---

## 1. Introduction

This document defines the environmental and metocean design basis for the OSP across all four operating regions. These data drive structural loads, hydrodynamic analysis, station-keeping design, and operational weather windows.

**Operating regions:**
1. **Kara Sea** — K-27 (33 m depth), 71°N, 55°E
2. **Barents Sea** — K-159 (200 m depth), 69°N, 37°E
3. **Norwegian Sea** — K-278 Komsomolets (1,680 m depth), 73°N, 13°E
4. **North Atlantic** — USS Thresher/Scorpion (2,560–3,000 m depth), 41°N–33°N, 65°W–33°W

---

## 2. Data Sources

| Source | Dataset | Application |
|--------|---------|-------------|
| ECMWF ERA5 | Global reanalysis, 0.25° resolution, 1940–present | Wave climate, wind, surface currents |
| NORA10 | 10 km hindcast, Norwegian/Barents/Nordic Seas | High-resolution regional wave/wind statistics |
| NDBC | Buoy observations, N. Atlantic | Validation of hindcast data |
| DNV-RP-C205 | Environmental conditions and loads | Design methodology |
| DNV-OS-E301 | Position mooring | Mooring design environmental loads |
| ISO 19901-1 | Metocean conditions | Offshore structural design basis |
| AARI (Arctic & Antarctic Research Institute) | Russian Arctic ice/metocean data | Kara Sea ice conditions |
| Norwegian Meteorological Institute | Operational forecasting data | Barents/Norwegian Sea validation |

**[ASSUMPTION]** Where exact site-specific measurements are unavailable, ERA5 reanalysis data supplemented by NORA10 hindcast statistics are used. Values represent the best available characterization at pre-FEED stage. Site-specific metocean campaigns are recommended for FEED.

---

## 3. Design Sea States

### 3.1 Metocean Design Parameters

| Condition | Parameter | Kara Sea (K-27) | Barents Sea (K-159) | Norwegian Sea (K-278) | N. Atlantic (Thresher/Scorpion) |
|-----------|-----------|-----------------|---------------------|----------------------|-------------------------------|
| **Operational limit** | Hs (m) | 4.0 | 5.0 | 5.0 | 5.5 |
| | Tp (s) | 9.0 | 10.5 | 11.0 | 12.0 |
| **Operational (lifting)** | Hs (m) | 2.0 | 2.5 | 2.5 | 3.0 |
| | Tp (s) | 7.0 | 8.0 | 8.5 | 9.0 |
| **Survival (100-yr)** | Hs (m) | 8.5 | 13.5 | 15.0 | 16.5 |
| | Tp (s) | 12.5 | 15.0 | 16.0 | 17.0 |
| **Survival (10,000-yr)** | Hs (m) | 11.0 | 17.0 | 19.5 | 21.5 |
| **Extreme individual wave** | Hmax (m) | 15.8 | 25.1 | 27.9 | 30.7 |
| **Surface current** | Vc (m/s) | 0.5 | 0.8 | 1.0 | 1.5 |
| **Wind (10-min mean, 100-yr)** | Vw (m/s) | 28 | 36 | 38 | 42 |
| **Wind (1-min gust, 100-yr)** | Vg (m/s) | 35 | 45 | 48 | 53 |

**Derivation of Hmax from Hs (100-year):**

Using the Forristall (2000) crest distribution for 3-hour storm duration:

$$H_{max} = H_s \times 1.86$$

**[ASSUMPTION]** Factor of 1.86 applied per DNV-RP-C205 for 1000 wave cycles in a 3-hour storm.

| Region | Hs,100yr (m) | Hmax (m) |
|--------|-------------|----------|
| Kara Sea | 8.5 | 15.8 |
| Barents Sea | 13.5 | 25.1 |
| Norwegian Sea | 15.0 | 27.9 |
| N. Atlantic | 16.5 | 30.7 |

### 3.2 Seasonal Variation

**Kara Sea (K-27):**

| Month | Hs,P50 (m) | Hs,P90 (m) | Ice Cover (%) | Operational? |
|-------|-----------|-----------|---------------|-------------|
| Jan–May | N/A | N/A | 80–100% | NO — ice-covered |
| June | 0.6 | 1.4 | 20–50% | Marginal |
| July | 0.8 | 1.8 | 0–10% | **YES — optimal** |
| August | 1.0 | 2.2 | 0–5% | **YES — good** |
| September | 1.4 | 3.0 | 0–10% | YES — marginal for lift |
| October | 1.8 | 4.0 | 10–30% | NO — too rough / ice forming |
| Nov–Dec | N/A | N/A | 50–90% | NO — ice-covered |

**[ASSUMPTION]** Sea ice data from AARI and NSIDC satellite records (1979–2025). Arctic sea ice extent continues to decline per observed trends.

**Barents Sea (K-159):**

| Month | Hs,P50 (m) | Hs,P90 (m) | Operational? |
|-------|-----------|-----------|-------------|
| Jan–Mar | 3.5 | 6.5 | NO |
| Apr | 2.5 | 5.0 | Marginal |
| May | 1.8 | 3.5 | YES |
| Jun–Aug | 1.2 | 2.8 | **YES — optimal** |
| Sep | 1.5 | 3.2 | YES |
| Oct | 2.5 | 5.0 | Marginal |
| Nov–Dec | 3.5 | 7.0 | NO |

**Norwegian Sea (K-278):**

| Month | Hs,P50 (m) | Hs,P90 (m) | Operational? |
|-------|-----------|-----------|-------------|
| Jan–Mar | 4.0 | 8.0 | NO |
| Apr | 2.8 | 5.5 | Marginal |
| May–Aug | 1.5 | 3.5 | **YES — optimal** |
| Sep | 2.0 | 4.5 | YES |
| Oct | 3.0 | 6.0 | Marginal |
| Nov–Dec | 4.5 | 9.0 | NO |

**North Atlantic (Thresher/Scorpion):**

| Month | Hs,P50 (m) | Hs,P90 (m) | Operational? |
|-------|-----------|-----------|-------------|
| Jan–Mar | 4.5 | 8.5 | NO |
| Apr | 3.0 | 6.0 | Marginal |
| May–Sep | 1.8 | 4.0 | **YES — optimal (Jun–Aug)** |
| Oct | 3.0 | 6.5 | Marginal |
| Nov–Dec | 4.5 | 9.5 | NO |

---

## 4. Wave Spectra Selection

### 4.1 Spectrum Type

| Region | Spectrum | Justification |
|--------|----------|--------------|
| Kara Sea | JONSWAP (γ = 2.0–3.3) | Fetch-limited enclosed sea; developing sea states |
| Barents Sea | JONSWAP (γ = 2.5–3.3) | Fetch-limited but larger than Kara; swell component present |
| Norwegian Sea | JONSWAP (γ = 1.0–2.5) + Torsethaugen double-peak | Mix of wind-sea and North Atlantic swell; double-peak spectrum required for survival |
| N. Atlantic | Pierson–Moskowitz (γ = 1.0) for swell; JONSWAP for wind-sea | Fully developed open-ocean sea; swell dominates |

### 4.2 JONSWAP Spectrum Formulation

$$S(\omega) = \frac{\alpha g^2}{\omega^5} \exp\left[-\frac{5}{4}\left(\frac{\omega_p}{\omega}\right)^4\right] \gamma^{\exp\left[-\frac{(\omega - \omega_p)^2}{2\sigma^2\omega_p^2}\right]}$$

Where:
- $\alpha$ = Phillips parameter (spectral energy level)
- $\omega_p = 2\pi / T_p$ = peak angular frequency (rad/s)
- $\gamma$ = peak enhancement factor
- $\sigma$ = spectral width parameter ($\sigma_a = 0.07$ for $\omega \leq \omega_p$; $\sigma_b = 0.09$ for $\omega > \omega_p$)

### 4.3 Design Wave Periods

For structural design, the response must be evaluated across a range of wave periods:

| Region | Tp range (s) | Dominant Tp (operational) | Dominant Tp (survival) |
|--------|-------------|--------------------------|----------------------|
| Kara Sea | 4–13 | 7–9 | 11–13 |
| Barents Sea | 5–16 | 8–11 | 14–16 |
| Norwegian Sea | 5–18 | 9–12 | 15–17 |
| N. Atlantic | 6–20 | 10–13 | 16–18 |

---

## 5. Wind Design Data

### 5.1 Wind Speed Profiles

Wind speed varies with height above sea level per the power law (DNV-RP-C205):

$$V(z) = V_{ref} \left(\frac{z}{z_{ref}}\right)^{\alpha}$$

Where:
- $V_{ref}$ = reference wind speed at $z_{ref}$ = 10 m
- $\alpha$ = power law exponent = 0.12 (offshore, neutral stability) **[ASSUMPTION]**

**Wind speeds at key platform heights:**

| Height (m) | Kara Sea (m/s) | Barents Sea (m/s) | Norwegian Sea (m/s) | N. Atlantic (m/s) |
|-----------|---------------|-------------------|---------------------|-------------------|
| 10 (reference) | 28.0 | 36.0 | 38.0 | 42.0 |
| 22 (operating WL) | 30.2 | 38.8 | 41.0 | 45.3 |
| 38 (main deck) | 32.1 | 41.2 | 43.5 | 48.1 |
| 55 (top of crane) | 33.5 | 43.0 | 45.4 | 50.2 |
| 65 (helideck top) | 34.2 | 43.9 | 46.4 | 51.2 |

**[ASSUMPTION]** 100-year return period, 10-minute mean wind speeds. Gust factors applied per DNV-RP-C205 Table 2-1.

### 5.2 Wind Force on Platform

**[ASSUMPTION]** Projected wind area estimated from `01-hull-form-selection.md` dimensions:

| Component | Projected Area (m²) | Cs (shape coeff.) |
|-----------|--------------------|--------------------|
| Accommodation block | 2,400 | 1.0 |
| Strand jack gantry | 1,800 | 1.3 |
| Columns (8 total, above WL) | 2,880 | 0.65 |
| Cranes (2) | 800 | 1.2 |
| Helideck structure | 600 | 1.0 |
| **Total effective** | **~6,200** | **1.0 (weighted)** |

Wind force:

$$F_w = \frac{1}{2} \rho_a C_s A V^2$$

At 100-year (Norwegian Sea): $F_w = 0.5 \times 1.225 \times 1.0 \times 6{,}200 \times 38^2 = 5{,}490 \text{ kN} \approx 560 \text{ t}$

---

## 6. Current Profiles

### 6.1 Surface Current Design Values

| Region | 1-year (m/s) | 10-year (m/s) | 100-year (m/s) |
|--------|-------------|---------------|----------------|
| Kara Sea | 0.3 | 0.4 | 0.5 |
| Barents Sea | 0.5 | 0.7 | 0.8 |
| Norwegian Sea | 0.6 | 0.8 | 1.0 |
| N. Atlantic | 0.8 | 1.2 | 1.5 |

### 6.2 Current Profile with Depth

Per DNV-RP-C205, current velocity profile:

$$V_c(z) = V_{c,0} \left(\frac{d + z}{d}\right)^{1/7}$$

Where:
- $V_{c,0}$ = surface current velocity
- $d$ = water depth
- $z$ = depth below surface (negative downward)

**Current velocities at pontoon depth (22 m below surface) for OSP:**

| Region | Surface Vc (m/s) | At 22 m depth (m/s) |
|--------|-----------------|---------------------|
| Kara Sea (d=33 m) | 0.5 | 0.35 |
| Barents Sea (d=200 m) | 0.8 | 0.71 |
| Norwegian Sea (d=1,680 m) | 1.0 | 0.98 |
| N. Atlantic (d=2,560 m) | 1.5 | 1.48 |

### 6.3 Current Force on Submerged Hull

$$F_c = \frac{1}{2} \rho_w C_D A_{sub} V_c^2$$

Where:
- $\rho_w$ = 1,025 kg/m³ (seawater)
- $C_D$ = drag coefficient (0.6 for rounded pontoon, 1.2 for columns) **[ASSUMPTION]**
- $A_{sub}$ = projected submerged area

**Submerged projected area:**

| Component | Frontal Area (m²) | Cd |
|-----------|-------------------|----|
| 2 pontoons (beam × depth) | 2 × 18 × 12 = 432 | 0.6 |
| 8 columns (below WL, transverse) | 8 × 18 × 10 = 1,440 | 1.0 |
| **Total** | **~1,872** | **0.85 (weighted)** |

100-year current force (N. Atlantic): $F_c = 0.5 \times 1{,}025 \times 0.85 \times 1{,}872 \times 1.5^2 = 1{,}836 \text{ kN} \approx 187 \text{ t}$

---

## 7. Ice Loading Criteria

### 7.1 Ice Conditions

| Parameter | Kara Sea | Barents Sea |
|-----------|----------|-------------|
| Ice type | First-year level ice | Ice edge/drift ice |
| Max ice thickness (operational) | 0.5 m | 0.3 m |
| Max ice thickness (survival) | 1.5 m (multi-year drift) | 0.8 m |
| Ice drift speed | 0.3–0.5 m/s | 0.2–0.5 m/s |
| Icing (atmospheric) | Severe (spray + sub-zero temps) | Moderate |
| Ice-free season | July–September | May–November |

### 7.2 Ice Force Estimation

Per DNV-OS-C101 and ISO 19906 (Arctic offshore structures):

**Global ice force (level ice):**

$$F_{ice} = p \times D \times h$$

Where:
- $p$ = ice crushing pressure = 1.5 MPa **[ASSUMPTION]** (first-year ice, DNV-OS-C101)
- $D$ = structure width at waterline (column width = 18 m, or pontoon if surfaced)
- $h$ = ice thickness

For one column, 0.5 m ice: $F_{ice} = 1.5 \times 10^6 \times 18 \times 0.5 = 13.5 \text{ MN} \approx 1{,}376 \text{ t}$

**[ASSUMPTION]** For 8 columns simultaneously contacting ice, consider shielding effects. Approximate total ice force = 4 × individual column force (front 4 columns; rear shielded):

$$F_{ice,total} = 4 \times 13.5 = 54 \text{ MN} \approx 5{,}500 \text{ t}$$

### 7.3 Ice Class Requirements

| Feature | Requirement per DNV ICE-C |
|---------|--------------------------|
| Hull plating (ice belt) | Increased thickness in CL 100 region (±0.3 m from WL) |
| Frame spacing | Reduced in ice belt zone |
| Stem/bow shape | Ice-breaking profile on forward columns |
| Propeller | Ice-class propeller (Pb rating) or ducted |
| Heating | Ballast tank heating in exposed areas |
| De-icing | Spray/icing protection for deck equipment |

### 7.4 Atmospheric Icing

**[ASSUMPTION]** Spray icing rate per ISO 19906 for Arctic operations:

| Condition | Icing rate (mm/hr) | Mitigation |
|-----------|-------------------|------------|
| Air temp < −2°C, wind > 8 m/s, waves > 2 m | 10–30 | De-icing systems on critical equipment |
| Severe (−15°C, 15 m/s, Hs > 4 m) | 30–50 | Suspend deck operations; shelter equipment |

Design ice accumulation for stability: 30 mm on all exposed surfaces above 22 m elevation **[ASSUMPTION]**

$$W_{ice} = \rho_{ice} \times t_{ice} \times A_{exposed}$$

Where $\rho_{ice}$ = 900 kg/m³, $t_{ice}$ = 0.03 m, $A_{exposed}$ ≈ 20,000 m²:

$$W_{ice} = 900 \times 0.03 \times 20{,}000 = 540 \text{ t}$$

This mass is included in stability calculations (see `10-stability-ballast.md`).

---

## 8. Design Environmental Load Combinations

Per DNV-OS-C101 and DNV-OS-C103:

### 8.1 ULS (Ultimate Limit State)

| Load Case | Wave | Wind | Current | Ice | Notes |
|-----------|------|------|---------|-----|-------|
| ULS-1 (collinear) | 100-yr Hs | 100-yr V10m | 10-yr Vc | — | All loads from same direction |
| ULS-2 (non-collinear) | 100-yr Hs | 100-yr V10m (0°) | 10-yr Vc (+30°) | — | Current misaligned 30° |
| ULS-3 (ice + wave) | 10-yr Hs | 100-yr V10m | — | 100-yr ice | Kara/Barents only |
| ULS-4 (cross sea) | 100-yr Hs from 0° and 90° | 100-yr V10m | 10-yr Vc | — | Two wave systems |

### 8.2 ALS (Accidental Limit State)

| Load Case | Description |
|-----------|-------------|
| ALS-1 | 10,000-yr wave (Hs) + 100-yr wind + 10-yr current |
| ALS-2 | Collision (supply vessel, 5,000 t at 2 m/s) |
| ALS-3 | Fire/explosion in machinery spaces |
| ALS-4 | Loss of one DP thruster during 100-yr storm |
| ALS-5 | Dropped object (strand jack component, 100 t from 30 m) |
| ALS-6 | Progressive flooding (2-compartment damage) |

### 8.3 FLS (Fatigue Limit State)

| Parameter | Value |
|-----------|-------|
| Design life | 25 years |
| Fatigue damage ratio limit | D ≤ 1.0 / DFF |
| Design Fatigue Factor (DFF) | 2.0 (inspectable joints), 3.0 (non-inspectable), 10.0 (critical non-inspectable joints in way of moon pool) |
| Wave scatter diagram | Combined for all sites, weighted by operational time at each |
| Number of wave cycles | ~10⁸ over 25 years |

**[ASSUMPTION]** Operational time split: 30% Kara/Barents, 40% Norwegian Sea, 20% N. Atlantic, 10% transit/port.

### 8.4 SLS (Serviceability Limit State)

| Parameter | Limit | Application |
|-----------|-------|-------------|
| Heave amplitude | ≤ 1.5 m | During lifting operations |
| Roll angle | ≤ 2° single amplitude | During lifting operations |
| Pitch angle | ≤ 1° single amplitude | During lifting operations |
| Horizontal offset (DP) | ≤ 5 m from target | During lifting operations |
| Structural deflection | L/500 for deck structure | Strand jack rail alignment |

---

## 9. Wave Directionality

### 9.1 Wave Rose Data

**[ASSUMPTION]** Dominant wave directions from ERA5:

| Region | Dominant Direction | Secondary Direction | Spread (°) |
|--------|-------------------|---------------------|------------|
| Kara Sea | NW (315°) | W (270°) | ±30 |
| Barents Sea | W–SW (225–270°) | N (0°) | ±45 |
| Norwegian Sea | SW (225°) | W (270°) | ±45 |
| N. Atlantic | W (270°) | SW–NW (225–315°) | ±60 |

### 9.2 Platform Heading Strategy

The OSP should be oriented with the bow into the dominant wave direction for:
- Minimum roll response
- Optimal DP performance
- Weather-vaning capability via DP

**[ASSUMPTION]** DP system capable of maintaining heading within ±10° of desired orientation up to operational sea state limits.

---

## 10. Design Wave Selection for Structural Analysis

Per DNV-OS-C103, design waves are selected for specific structural responses:

| Response | Design Wave Direction | Design Wave Tp (s) | Design Wave H (m) | Basis |
|----------|----------------------|--------------------|--------------------|----|
| Midship sag bending | Head seas (0°) | 0.8 × L_pp / sqrt(g) ≈ 14.9 s | 100-yr Hs × 1.86 = 27.9 m | Norwegian Sea governs |
| Midship hog bending | Head seas (0°) | ~15 s | 27.9 m | Norwegian Sea governs |
| Transverse shear | Beam seas (90°) | ~12 s | 27.9 m | Norwegian Sea governs |
| Torsion | Quartering seas (45°) | ~13 s | 27.9 m | Norwegian Sea governs |
| Split force (transverse) | Beam seas (90°) | ~12 s | 27.9 m | Catamaran hull split force |

**[ASSUMPTION]** The Norwegian Sea 100-year conditions govern structural design as the most severe environment among operational sites. The N. Atlantic values are more extreme but the OSP would operate there only for monitoring, not lifting.

---

## 11. Environmental Data Uncertainty

| Parameter | Estimated Uncertainty | Impact |
|-----------|----------------------|--------|
| Hs (100-yr) | ±15% | Direct impact on structural loads; addressed by safety factors |
| Tp range | ±1 s | Affects resonance analysis; conservative range used |
| Wind speed (100-yr) | ±10% | Affects DP sizing; addressed by thrust margin |
| Current speed | ±20% | Affects station-keeping; addressed by DP margin |
| Ice thickness | ±30% | High uncertainty in Kara Sea; use 1.5× design value for ALS |
| Wave direction | ±15° | Addressed by multi-directional structural analysis |

**Recommendation for FEED phase:** Deploy metocean buoys at K-27 and K-159 sites for minimum 12 months of in-situ measurements before finalizing structural design.

---

## 12. Summary of Governing Design Conditions

| Design Condition | Governing Region | Governing Value |
|------------------|-----------------|-----------------|
| Max operational Hs | N. Atlantic | 5.5 m |
| Max survival Hs (100-yr) | N. Atlantic | 16.5 m |
| Max Hmax | N. Atlantic | 30.7 m |
| Max wind speed | N. Atlantic | 42 m/s (10-min mean) |
| Max current | N. Atlantic | 1.5 m/s |
| Ice loading | Kara Sea | 1.5 m multi-year ice |
| Most restrictive operational window | Kara Sea | July–August only (2 months) |
| Longest operational season | N. Atlantic | May–September (5 months) |

The **North Atlantic** governs for wave, wind, and current. The **Kara Sea** governs for ice and operational window restrictions.

---

*Cross-references: `01-hull-form-selection.md`, `03-hydrodynamic-analysis.md`, `04-dynamic-positioning.md`, `05-structural-design.md`*
