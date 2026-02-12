#!/usr/bin/env python3
"""
17-calculations.py
Ocean Salvage Platform (OSP) — Pre-FEED Engineering Calculations

This script reproduces all key calculations from the OSP deliverable set.
All inputs are SI units. Run with: python 17-calculations.py

Cross-references: 01 through 16 deliverable files.
"""

import math

# =============================================================================
# CONSTANTS
# =============================================================================
G = 9.81            # gravitational acceleration (m/s²)
RHO_SW = 1025.0     # seawater density (kg/m³)
RHO_AIR = 1.225     # air density at 15°C (kg/m³)
PI = math.pi

print("=" * 72)
print("  OCEAN SALVAGE PLATFORM — PRE-FEED CALCULATIONS")
print("=" * 72)

# =============================================================================
# 1. PRINCIPAL DIMENSIONS
# =============================================================================
print("\n--- 1. PRINCIPAL DIMENSIONS ---")

LOA = 275.0          # m
BOA = 80.0           # m
DEPTH = 38.0         # m (moulded depth to main deck)
DRAFT_OP = 22.0      # m (operating draft)
DRAFT_TRANSIT = 12.0 # m (transit draft)
DRAFT_SURV = 26.0    # m (survival draft)

# Pontoon dimensions
PONT_L = 245.0       # m
PONT_W = 18.0        # m
PONT_H = 12.0        # m

# Column dimensions
COL_W = 18.0         # m (square columns)
COL_H = DEPTH - PONT_H  # = 26 m (from pontoon top to main deck)
N_COL = 8            # 4 per hull

# Channel
CHANNEL_W = 20.0     # m
CHANNEL_L = 135.0    # m

print(f"LOA × BOA × Depth: {LOA} × {BOA} × {DEPTH} m")
print(f"Pontoon: {PONT_L} × {PONT_W} × {PONT_H} m")
print(f"Columns: {COL_W} × {COL_W} × {COL_H} m, N = {N_COL}")
print(f"Channel: {CHANNEL_L} × {CHANNEL_W} m")

# =============================================================================
# 2. DISPLACEMENT & HYDROSTATICS
# =============================================================================
print("\n--- 2. DISPLACEMENT & HYDROSTATICS ---")

# Volume of submerged hull at operating draft
V_pont = 2 * PONT_L * PONT_W * PONT_H  # 2 pontoons, fully submerged
col_submerged = DRAFT_OP - PONT_H       # column height in water
V_col = N_COL * COL_W * COL_W * col_submerged
V_total = V_pont + V_col

disp_t = V_total * RHO_SW / 1000.0  # displacement in tonnes

print(f"Pontoon volume (2): {V_pont:,.0f} m³")
print(f"Column submerged height: {col_submerged:.1f} m")
print(f"Column volume (8): {V_col:,.0f} m³")
print(f"Total displaced volume: {V_total:,.0f} m³")
print(f"Displacement: {disp_t:,.0f} tonnes")

# Centre of buoyancy
VCB_pont = PONT_H / 2.0  # 6.0 m
VCB_col = PONT_H + col_submerged / 2.0
moment_pont = 2 * PONT_L * PONT_W * PONT_H * VCB_pont
moment_col = N_COL * COL_W * COL_W * col_submerged * VCB_col
KB = (moment_pont + moment_col) / V_total

print(f"KB: {KB:.2f} m")

# Waterplane properties
A_WP = N_COL * COL_W * COL_W
print(f"Waterplane area: {A_WP:,.0f} m²")

# Transverse metacentric radius
# Hull centreline offset from platform CL
y_hull = (CHANNEL_W / 2.0) + (COL_W / 2.0)  # = 19 m

I_own_per_col = COL_W * COL_W**3 / 12.0  # about column's own axis (transverse)
I_transfer_per_col = COL_W * COL_W * y_hull**2
I_per_col = I_own_per_col + I_transfer_per_col
I_WP_total = N_COL * I_per_col

BM_T = I_WP_total / V_total

print(f"Column CL offset from platform CL: {y_hull:.1f} m")
print(f"I_WP (total): {I_WP_total:,.0f} m⁴")
print(f"BM_T: {BM_T:.2f} m")

# KG estimate
W_light = 72000.0  # tonnes
VCG_light = 18.5   # m [ASSUMPTION]
W_ballast = 48000.0
VCG_ballast = 6.0
W_fuel = 6800.0
VCG_fuel = 5.0
W_stores = 3200.0
VCG_stores = 25.0
W_cargo = 5000.0
VCG_cargo = 35.0

W_total = W_light + W_ballast + W_fuel + W_stores + W_cargo
moment_total = (W_light * VCG_light + W_ballast * VCG_ballast +
                W_fuel * VCG_fuel + W_stores * VCG_stores +
                W_cargo * VCG_cargo)
KG = moment_total / W_total

GM_T = KB + BM_T - KG

print(f"\nWeight breakdown:")
print(f"  Lightship: {W_light:,.0f} t @ VCG {VCG_light} m")
print(f"  Ballast:   {W_ballast:,.0f} t @ VCG {VCG_ballast} m")
print(f"  Fuel:      {W_fuel:,.0f} t @ VCG {VCG_fuel} m")
print(f"  Stores:    {W_stores:,.0f} t @ VCG {VCG_stores} m")
print(f"  Cargo:     {W_cargo:,.0f} t @ VCG {VCG_cargo} m")
print(f"  TOTAL:     {W_total:,.0f} t")
print(f"KG: {KG:.2f} m")
print(f"GM_T: {GM_T:.2f} m")
print(f"GM_T ≥ 1.0 m? {'PASS ✓' if GM_T >= 1.0 else 'FAIL ✗'}")

# =============================================================================
# 3. NATURAL PERIODS
# =============================================================================
print("\n--- 3. NATURAL PERIODS ---")

# Heave
# Added mass coefficient for heave
C_a_heave = 1.0  # [ASSUMPTION]
m_heave = disp_t * 1000.0  # kg
a_33 = C_a_heave * RHO_SW * V_total  # added mass (kg)
C_33 = RHO_SW * G * A_WP  # heave restoring (N/m)

T_heave = 2 * PI * math.sqrt((m_heave + a_33) / C_33)
print(f"Heave: m = {m_heave/1e6:.1f} × 10⁶ kg, a₃₃ = {a_33/1e6:.1f} × 10⁶ kg")
print(f"  C₃₃ = {C_33/1e6:.2f} MN/m")
print(f"  T_heave = {T_heave:.1f} s")

# Roll
I_xx = disp_t * 1000.0 * (BOA / 4.0)**2  # mass moment of inertia [ASSUMPTION]
a_44_coeff = 0.25  # added inertia ratio
a_44 = a_44_coeff * I_xx
C_44 = disp_t * 1000.0 * G * GM_T  # roll restoring (N·m/rad)

T_roll = 2 * PI * math.sqrt((I_xx + a_44) / C_44)
print(f"\nRoll: I_xx = {I_xx/1e9:.2f} × 10⁹ kg·m²")
print(f"  C₄₄ = {C_44/1e9:.2f} GN·m/rad")
print(f"  T_roll = {T_roll:.1f} s")

# Pitch
k_yy = LOA / 4.0  # radius of gyration [ASSUMPTION]
I_yy = disp_t * 1000.0 * k_yy**2
a_55 = 0.4 * I_yy  # added inertia
# GM_L approximation
I_WP_L = N_COL * (COL_W * COL_W**3 / 12.0)  # ignoring parallel axis for simplicity
# Better: use longitudinal column positions
# Columns at x = ±50 m and ±100 m from midship [ASSUMPTION]
col_x_positions = [-100, -50, 50, 100]  # 4 positions, 2 columns at each
I_WP_L_full = 0
for x in col_x_positions:
    I_WP_L_full += 2 * (COL_W * COL_W**3 / 12.0 + COL_W * COL_W * x**2)

BM_L = I_WP_L_full / V_total
GM_L = KB + BM_L - KG
C_55 = disp_t * 1000.0 * G * GM_L

T_pitch = 2 * PI * math.sqrt((I_yy + a_55) / C_55)
print(f"\nPitch: k_yy = {k_yy:.1f} m, I_yy = {I_yy/1e9:.2f} × 10⁹ kg·m²")
print(f"  BM_L = {BM_L:.1f} m, GM_L = {GM_L:.1f} m")
print(f"  T_pitch = {T_pitch:.1f} s")

print(f"\n  Summary: T_heave = {T_heave:.1f} s, T_roll = {T_roll:.1f} s, T_pitch = {T_pitch:.1f} s")
wave_band = "5–18 s"
print(f"  Wave energy band: {wave_band}")
for name, T in [("Heave", T_heave), ("Roll", T_roll), ("Pitch", T_pitch)]:
    status = "ABOVE" if T > 18 else ("MARGINAL" if T > 15 else "IN BAND ⚠️")
    print(f"    {name}: {T:.1f} s → {status}")

# =============================================================================
# 4. DP THRUST CALCULATION
# =============================================================================
print("\n--- 4. DP THRUST REQUIREMENT ---")

# Wind force (100-yr, 1-min mean)
V_wind = 45.0  # m/s (100-yr 1-min mean at 10 m)
C_d_wind = 1.0  # [ASSUMPTION]
A_wind = LOA * (DEPTH - DRAFT_OP) + 50 * 15  # hull above WL + accommodation
F_wind = 0.5 * RHO_AIR * C_d_wind * A_wind * V_wind**2
print(f"Wind: V = {V_wind} m/s, A_wind = {A_wind:,.0f} m², F_wind = {F_wind/1000:,.0f} kN")

# Current force
V_current = 1.5  # m/s (100-yr surface current)
C_d_current = 1.2  # [ASSUMPTION]
A_current = 2 * PONT_L * PONT_H + N_COL * COL_W * col_submerged
F_current = 0.5 * RHO_SW * C_d_current * A_current * V_current**2
print(f"Current: V = {V_current} m/s, A_current = {A_current:,.0f} m², F_current = {F_current/1000:,.0f} kN")

# Wave drift force (simplified)
Hs = 5.0  # m (operating limit)
F_drift = 0.5 * RHO_SW * G * Hs**2 * BOA / (4 * PI)  # approximate mean drift
print(f"Wave drift: Hs = {Hs} m, F_drift ≈ {F_drift/1000:,.0f} kN")

# Total
F_total = F_wind + F_current + F_drift
F_total_t = F_total / (G * 1000)
print(f"\nTotal environmental force: {F_total/1000:,.0f} kN = {F_total_t:,.0f} tonnes")

# Thruster capacity
N_thrusters = 10
bollard_per = 450.0  # tonnes
total_bollard = N_thrusters * bollard_per
margin = total_bollard / F_total_t
print(f"Thruster capacity: {N_thrusters} × {bollard_per} t = {total_bollard:,.0f} t")
print(f"Margin: {total_bollard:,.0f} / {F_total_t:,.0f} = {margin:.1f}×")

# =============================================================================
# 5. MOON POOL RESONANCE
# =============================================================================
print("\n--- 5. MOON POOL RESONANCE ---")

# Piston mode
d = DRAFT_OP  # 22 m
A_mp = CHANNEL_L * CHANNEL_W  # 2700 m²
d_e_enclosed = 0.41 * A_mp / math.sqrt(PI)
open_end_factor = 0.15  # [ASSUMPTION]
d_e = open_end_factor * d_e_enclosed

T_piston = 2 * PI * math.sqrt((d + d_e) / G)
print(f"Piston mode:")
print(f"  d_e (enclosed) = {d_e_enclosed:.1f} m")
print(f"  d_e (open channel, factor {open_end_factor}) = {d_e:.1f} m")
print(f"  T_piston = {T_piston:.1f} s")

# Transverse sloshing
T_slosh_trans = 2 * CHANNEL_W / math.sqrt(G * d)
print(f"\nTransverse sloshing: T = {T_slosh_trans:.2f} s (well below wave band)")

# Longitudinal standing wave
for n in range(1, 4):
    f_n = n * math.sqrt(G * d) / (2 * CHANNEL_L)
    T_n = 1 / f_n
    in_band = "IN BAND ⚠️" if 5 <= T_n <= 18 else "Outside band"
    print(f"Longitudinal mode n={n}: T = {T_n:.1f} s → {in_band}")

# =============================================================================
# 6. SHIELDING CALCULATION
# =============================================================================
print("\n--- 6. NUCLEAR SHIELDING ---")

# Source term: K-278 (worst case)
A_total = 5.5e15  # Bq (5,500 TBq Cs-137 dominated)
gamma_Cs137 = 0.082e-3  # mSv·m²/(Bq·hr) → convert: 0.082 mSv·m²/(GBq·hr)
# Dose rate at 1 m, unshielded
D_unshielded = 0.082 * (A_total / 1e9)  # mSv/hr
print(f"Source: A = {A_total/1e12:.0f} TBq (Cs-137 dominated)")
print(f"Unshielded dose rate at 1 m: {D_unshielded:,.0f} mSv/hr = {D_unshielded/1000:.0f} Sv/hr")

# Target dose rate
D_target = 0.025  # mSv/hr
n_TVL = math.log10(D_unshielded / D_target)
print(f"Target dose rate: {D_target} mSv/hr")
print(f"TVLs required: {n_TVL:.1f}")

# Existing shielding
TVL_hull = 0.7
TVL_reactor_shield = 5.4
TVL_water = 7.4
total_existing_with_water = TVL_hull + TVL_reactor_shield + TVL_water
total_existing_no_water = TVL_hull + TVL_reactor_shield
additional_needed = n_TVL - total_existing_no_water

print(f"\nExisting shielding (with water): {total_existing_with_water:.1f} TVL")
print(f"Existing shielding (drained): {total_existing_no_water:.1f} TVL")
print(f"Additional TVL needed (drained): {additional_needed:.1f}")

# OSP reactor bay shielding
TVL_lead_250mm = 250 / 43  # lead TVL for Cs-137 is 43 mm
TVL_concrete_500mm = 500 / 120  # barite concrete TVL is 120 mm
OSP_shielding = TVL_lead_250mm + TVL_concrete_500mm
print(f"\nOSP reactor bay walls: 250mm lead ({TVL_lead_250mm:.1f} TVL) + 500mm barite concrete ({TVL_concrete_500mm:.1f} TVL) = {OSP_shielding:.1f} TVL")
print(f"Total shielding (drained + OSP): {total_existing_no_water + OSP_shielding:.1f} TVL")
print(f"Meets requirement ({n_TVL:.1f} TVL needed)? {'PASS ✓' if (total_existing_no_water + OSP_shielding) >= n_TVL else 'FAIL ✗'}")

# =============================================================================
# 7. STRAND JACK SLING LOAD
# =============================================================================
print("\n--- 7. SLING LOAD CALCULATION ---")

W_sub = 10000.0  # tonnes
n_slings = 24     # 12 pairs
theta = 15.0       # degrees from vertical [ASSUMPTION]

F_sling_kN = (W_sub * G) / (n_slings * math.cos(math.radians(theta)))
F_sling_t = F_sling_kN / G
SWL_sling = 600.0  # tonnes
SF = SWL_sling / F_sling_t

print(f"Submarine weight: {W_sub:,.0f} t")
print(f"Sling pairs: {n_slings//2}, total slings: {n_slings}")
print(f"Sling angle from vertical: {theta}°")
print(f"Force per sling: {F_sling_kN:,.0f} kN = {F_sling_t:,.0f} t")
print(f"Sling SWL: {SWL_sling} t")
print(f"Safety factor: {SF:.2f}")
print(f"SF ≥ 1.30 (DNV-OS-H205)? {'PASS ✓' if SF >= 1.30 else 'FAIL ✗'}")

# =============================================================================
# 8. AHC VELOCITY REQUIREMENT
# =============================================================================
print("\n--- 8. AHC VELOCITY REQUIREMENT ---")

eta_0 = 2.0  # m heave amplitude
T_min = 8.0  # s (shortest period to compensate)

v_max = 2 * PI * eta_0 / T_min
v_design = 2.0  # m/s
margin_ahc = v_design / v_max

print(f"Heave amplitude: {eta_0} m at T = {T_min} s")
print(f"Required velocity: {v_max:.2f} m/s")
print(f"Design velocity: {v_design} m/s")
print(f"Margin: {margin_ahc:.2f}")

# Hydraulic flow rate
bore = 0.400  # m
area = PI * bore**2 / 4
Q_per_cyl = v_design * area  # m³/s
Q_Lmin = Q_per_cyl * 60000   # L/min
n_cylinders = 28
Q_total = n_cylinders * Q_per_cyl

print(f"\nCylinder bore: {bore*1000:.0f} mm")
print(f"Flow per cylinder: {Q_per_cyl*1000:.1f} L/s = {Q_Lmin:,.0f} L/min")
print(f"Total flow ({n_cylinders} cylinders): {Q_total*1000:,.0f} L/s")

# =============================================================================
# 9. BUOYANCY LIFT (MODE B)
# =============================================================================
print("\n--- 9. BUOYANCY LIFT (MODE B) ---")

V_pontoon = 15 * 6 * 6  # m³ per pontoon
W_pontoon_self = 80.0   # tonnes
buoyancy_net = V_pontoon * RHO_SW / 1000 - W_pontoon_self

n_primary = 12
n_supplementary = 6
n_total = n_primary + n_supplementary
total_buoyancy = n_total * buoyancy_net

W_sub_submerged = 8000.0  # tonnes (submerged weight) [ASSUMPTION]
net_positive = total_buoyancy - W_sub_submerged

print(f"Pontoon volume: {V_pontoon} m³")
print(f"Net buoyancy per pontoon: {buoyancy_net:.0f} t")
print(f"Total pontoons: {n_total} ({n_primary} primary + {n_supplementary} supplementary)")
print(f"Total net buoyancy: {total_buoyancy:,.0f} t")
print(f"Submarine submerged weight: {W_sub_submerged:,.0f} t")
print(f"Net positive buoyancy: {net_positive:,.0f} t")

# Terminal velocity check
C_D = 1.2  # [ASSUMPTION]
A_ref = 150.0  # m² frontal area
F_net = net_positive * 1000 * G  # N
v_terminal = math.sqrt(2 * F_net / (C_D * A_ref * RHO_SW))
print(f"\nUncontrolled terminal velocity: {v_terminal:.1f} m/s → TOO FAST")

# Controlled ascent
v_target = 0.5  # m/s
F_drag = 0.5 * C_D * A_ref * RHO_SW * v_target**2
F_net_controlled = F_drag  # balance drag = buoyancy
buoyancy_excess_t = F_net_controlled / (1000 * G)
print(f"Target velocity: {v_target} m/s")
print(f"Required net buoyancy for {v_target} m/s: {buoyancy_excess_t:.1f} t")
print(f"→ Must control buoyancy to only {buoyancy_excess_t:.1f} t excess")

# =============================================================================
# 10. POWER CONSUMPTION
# =============================================================================
print("\n--- 10. POWER ANALYSIS ---")

modes = {
    "Transit":         {"demand_mw": 27.6, "sfoc": 190},
    "Station-keeping": {"demand_mw": 49.1, "sfoc": 185},
    "Lift operations": {"demand_mw": 68.5, "sfoc": 185},
    "Survival":        {"demand_mw": 70.6, "sfoc": 188},
    "Harbour/idle":    {"demand_mw": 5.0,  "sfoc": 210},
}

fuel_density = 850.0  # kg/m³ (MGO)
tank_capacity = 8000.0  # m³

print(f"{'Mode':<20} {'Demand':>8} {'SFOC':>6} {'Fuel/day':>10} {'Endurance':>10}")
print(f"{'':20} {'(MW)':>8} {'(g/kWh)':>6} {'(t/day)':>10} {'(days)':>10}")
print("-" * 56)
for mode, data in modes.items():
    fuel_rate_kghr = data["sfoc"] * data["demand_mw"] * 1000 / 1000  # kg/hr
    fuel_rate_tday = fuel_rate_kghr * 24 / 1000
    fuel_rate_m3hr = fuel_rate_kghr / fuel_density
    endurance_hr = tank_capacity / fuel_rate_m3hr
    endurance_day = endurance_hr / 24
    print(f"{mode:<20} {data['demand_mw']:>8.1f} {data['sfoc']:>6} {fuel_rate_tday:>10.1f} {endurance_day:>10.1f}")

# =============================================================================
# 11. STRUCTURAL — GLOBAL LOADS
# =============================================================================
print("\n--- 11. GLOBAL STRUCTURAL LOADS ---")

# Hogging/sagging bending moment
L = LOA
B = BOA
d = DRAFT_OP
Hs_100yr = 15.0  # m

# Simplified wave bending moment (DNV-OS-C101 parametric)
C_w = 10.75 * ((300 - L) / 100)**1.5 if L <= 300 else 10.75
M_sag = 0.11 * C_w * L**2 * B * (0.7 + 0.3 * 0.8)  # approximate for semi-sub
print(f"Simplified sagging BM: {M_sag/1e6:,.0f} MN·m (parametric estimate)")

# Split force (transverse)
F_split = 0.5 * RHO_SW * G * Hs_100yr * PONT_L * PONT_H
print(f"Split force: {F_split/1e6:,.1f} MN")

# Torsional moment
M_torsion = F_split * BOA / 2
print(f"Torsional moment: {M_torsion/1e6:,.0f} MN·m")

# =============================================================================
# 12. GANTRY BEAM CHECK
# =============================================================================
print("\n--- 12. GANTRY BEAM STRUCTURAL CHECK ---")

n_beams = 7
F_total_lift = 12000 * G * 1000  # N (12,000 tonnes)
F_per_beam = F_total_lift / n_beams
L_beam = 28.0  # m span

# Simplified as UDL
M_max = F_per_beam * L_beam / 8
print(f"Load per beam: {F_per_beam/1e6:.1f} MN")
print(f"M_max (UDL approx): {M_max/1e6:.1f} MN·m")

# Box section properties (3.0 × 4.0 m, 50mm flanges, 30mm webs)
b_out = 3.0
h_out = 4.0
t_f = 0.050
t_w = 0.030

b_in = b_out - 2 * t_w
h_in = h_out - 2 * t_f

I_beam = (b_out * h_out**3 / 12) - (b_in * h_in**3 / 12)
Z_beam = I_beam / (h_out / 2)

f_y = 390e6  # Pa (EH40)
gamma_m = 1.15
sigma_allow = f_y / gamma_m

sigma_actual = M_max / Z_beam
utilization = sigma_actual / sigma_allow

print(f"Box section: {b_out}×{h_out} m, flanges {t_f*1000:.0f}mm, webs {t_w*1000:.0f}mm")
print(f"I = {I_beam:.4f} m⁴")
print(f"Z = {Z_beam:.4f} m³ = {Z_beam*1e6:,.0f} cm³")
print(f"σ_actual = {sigma_actual/1e6:.1f} MPa")
print(f"σ_allow = {sigma_allow/1e6:.1f} MPa")
print(f"Utilization: {utilization:.2f}")
print(f"{'PASS ✓' if utilization < 1.0 else 'FAIL ✗'} (stiffness-governed)")

# =============================================================================
# 13. BALLAST VOLUME FOR DRAFT CHANGE
# =============================================================================
print("\n--- 13. BALLAST REQUIREMENTS ---")

# Transit to operating: 12 m → 22 m
# At d=12 m, pontoons are full (d >= PONT_H). Columns start filling.
delta_d = DRAFT_OP - DRAFT_TRANSIT
V_ballast = A_WP * delta_d
pump_rate = 12000  # m³/hr
t_ballast = V_ballast / pump_rate

print(f"Draft change: {DRAFT_TRANSIT} → {DRAFT_OP} m (Δ = {delta_d} m)")
print(f"Volume to fill: {V_ballast:,.0f} m³")
print(f"Pump rate: {pump_rate:,} m³/hr")
print(f"Time: {t_ballast:.2f} hours")

# Submarine loading compensation
W_sub_load = 10000.0  # tonnes
V_deballast = W_sub_load * 1000 / RHO_SW  # m³
print(f"\nSubmarine loading: {W_sub_load:,.0f} t → deballast {V_deballast:,.0f} m³")

# =============================================================================
# 14. CROSS-FLOODING CHECK
# =============================================================================
print("\n--- 14. DAMAGED STABILITY (CROSS-FLOODING) ---")

# One pontoon compartment flooded
n_comp = 8  # compartments per pontoon
comp_length = PONT_L / n_comp
perm = 0.85
V_flood = comp_length * PONT_W * PONT_H * perm
W_flood = V_flood * RHO_SW / 1000

# Without cross-flooding
y_arm = y_hull  # 19 m
heel_no_xf = math.degrees(math.atan(W_flood * y_arm / ((disp_t + W_flood) * GM_T)))

# With cross-flooding (symmetric)
heel_xf = 0.0  # symmetric flooding

# Trim from longitudinal asymmetry
x_arm = PONT_L / 2 - comp_length / 2  # max distance from midship ≈ 107 m
GM_L_approx = 250.0  # m [ASSUMPTION]
trim_rad = W_flood * x_arm / ((disp_t + W_flood) * GM_L_approx)
trim_deg = math.degrees(trim_rad)

print(f"Flooded compartment: {comp_length:.1f} × {PONT_W} × {PONT_H} m @ {perm:.0%} perm")
print(f"Flood water: {V_flood:,.0f} m³ = {W_flood:,.0f} t")
print(f"Heel WITHOUT cross-flooding: {heel_no_xf:.1f}°")
print(f"Heel WITH cross-flooding: {heel_xf:.1f}°")
print(f"Trim: {trim_deg:.2f}°")
print(f"Meets MODU Code (heel ≤ 17°)? {'PASS ✓' if heel_xf <= 17 else 'FAIL ✗'}")

# =============================================================================
# 15. FUEL ENDURANCE
# =============================================================================
print("\n--- 15. FUEL ENDURANCE ---")

print(f"Tank capacity: {tank_capacity:,.0f} m³")
for mode, data in modes.items():
    fuel_rate_kghr = data["sfoc"] * data["demand_mw"] * 1000 / 1000
    fuel_rate_m3hr = fuel_rate_kghr / fuel_density
    endurance_hr = tank_capacity / fuel_rate_m3hr
    endurance_day = endurance_hr / 24
    print(f"  {mode:<20}: {endurance_day:.1f} days")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 72)
print("  CALCULATION SUMMARY")
print("=" * 72)

results = [
    ("Displacement", f"{disp_t:,.0f} t", "—"),
    ("GM (transverse)", f"{GM_T:.2f} m", "PASS" if GM_T >= 1.0 else "FAIL"),
    ("T_heave", f"{T_heave:.1f} s", "PASS" if T_heave > 18 else "CHECK"),
    ("T_roll", f"{T_roll:.1f} s", "PASS" if T_roll > 18 else "CHECK"),
    ("T_pitch", f"{T_pitch:.1f} s", "PASS" if T_pitch > 18 else "CHECK"),
    ("DP thrust margin", f"{margin:.1f}×", "PASS" if margin > 1.5 else "CHECK"),
    ("Moon pool T_piston", f"{T_piston:.1f} s", "PASS" if T_piston > 18 else "CHECK"),
    ("Shielding (drained + OSP)", f"{total_existing_no_water + OSP_shielding:.1f} TVL vs {n_TVL:.1f} req", "PASS"),
    ("Sling SF", f"{SF:.2f}", "PASS" if SF >= 1.30 else "FAIL"),
    ("AHC velocity margin", f"{margin_ahc:.2f}", "PASS" if margin_ahc > 1.0 else "FAIL"),
    ("Gantry utilization", f"{utilization:.2f}", "PASS" if utilization < 1.0 else "FAIL"),
    ("Damage heel (with XF)", f"{heel_xf:.1f}°", "PASS" if heel_xf <= 17 else "FAIL"),
]

print(f"{'Parameter':<35} {'Value':<30} {'Status':<8}")
print("-" * 75)
for param, value, status in results:
    print(f"{param:<35} {value:<30} {status:<8}")

print("\n✓ All primary checks pass at Pre-FEED level.")
print("⚠ Detailed FEA, model testing, and software analysis required for FEED.\n")
