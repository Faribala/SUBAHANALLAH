# Ocean Salvage Platform (OSP) — Pre-FEED Design Package

A comprehensive Pre-FEED engineering design for a purpose-built hybrid catamaran semi-submersible vessel capable of recovering sunken nuclear submarines from depths up to 2,000 m.

## Overview

The Ocean Salvage Platform addresses the radiological, environmental, and geopolitical risks posed by at least nine sunken nuclear submarines worldwide. Priority recovery targets include K-27 (Kara Sea, 33 m), K-159 (Barents Sea, 200 m), and K-278 *Komsomolets* (Norwegian Sea, 1,680 m).

### Key Specifications

| Parameter | Value |
|-----------|-------|
| Hull type | Hybrid catamaran semi-submersible |
| LOA × BOA | 275 m × 80 m |
| Operating displacement | 135,000 t |
| Moon pool | 135 m × 20 m open channel |
| Lift capacity | 14,000 t (strand jacks) / 9,720 t (buoyancy) |
| Operating depth | 0–2,000 m |
| Station-keeping | DP3 (10 × 6,000 kW azimuth thrusters) |
| Installed power | 6 × 18.6 MW = 111.6 MW |
| Accommodation | 150 persons |
| Ice class | ICE-1A (Arctic-rated) |
| Estimated cost | $2.9 billion (AACE Class 4, ±30%) |
| Build duration | 48 months |

## Repository Structure

### Design Documents

| # | File | Description |
|---|------|-------------|
| 01 | `01-hull-form-selection.md` | Trade study, hull selection, principal dimensions |
| 02 | `02-environmental-design-basis.md` | Metocean data, load combinations |
| 03 | `03-hydrodynamic-analysis.md` | Motion analysis, RAOs, natural periods |
| 04 | `04-dynamic-positioning.md` | DP3 system design, thruster layout |
| 05 | `05-structural-design.md` | Global loads, scantlings, fatigue |
| 06 | `06-moon-pool-design.md` | Channel resonance, cradle system |
| 07 | `07-heavy-lift-system.md` | Strand jacks, buoyancy, AHC |
| 08 | `08-nuclear-safety-containment.md` | Shielding, criticality, waste treatment |
| 09 | `09-power-generation.md` | Diesel-electric, distribution, fuel |
| 10 | `10-stability-ballast.md` | Intact/damaged stability, ballast system |
| 11 | `11-accommodation-systems.md` | Living quarters, LSA, helideck |
| 12 | `12-operational-modes.md` | 8 operational modes, campaign timelines |
| 13 | `13-construction-specification.md` | Build strategy, schedule, materials |
| 14 | `14-historical-precedent.md` | Glomar Explorer, Kursk, comparisons |
| 15 | `15-risk-register.csv` | 42 risks with mitigations |
| 16 | `16-bill-of-materials.csv` | 76 BOM line items |
| 17 | `17-calculations.py` | Python verification calculations |
| 18 | `18-data-tables.csv` | ~100 key design parameters |
| 19 | `19-general-arrangement.md` | ASCII art GA drawings, fire zones |
| 20 | `20-design-summary.md` | Executive design summary |

### CAD Models (`cad/`)

Parametric 3D CAD models built with FreeCAD / CadQuery, with STEP file exports:

- `osp_parameters.py` — Central parameter definitions
- `osp_pontoons.py` — Twin pontoon hulls
- `osp_columns.py` — Support columns
- `osp_deck.py` — Main deck structure
- `osp_moon_pool.py` — Moon pool channel
- `osp_reactor_bay.py` — Nuclear reactor handling bay
- `osp_accommodation.py` — Accommodation block
- `osp_gantry.py` — Heavy-lift gantry
- `osp_thrusters.py` — Azimuth thruster units
- `osp_helideck.py` — Helideck
- `osp_assembly.py` — Full platform assembly
- `step_output/` — Exported STEP files for each component and full assembly

## Applicable Standards

- **DNV-OS-C101/C103/C301** — Offshore structural design
- **DNV-RP-C203/C205** — Fatigue and environmental loads
- **DNV DYNPOS-3 AUTRO** — DP Class 3
- **IMO MODU Code 2009** — Mobile offshore unit requirements
- **IAEA GSR Part 3 / SSR-5** — Radiation protection and radioactive waste
- **IMO Polar Code** — Arctic operations
- **SOLAS** — Life safety and communications
- **MARPOL 73/78** — Marine pollution prevention

## Running Calculations

The verification calculations require Python 3:

```bash
python 17-calculations.py
```

## License

This design package is provided for any purpose.
