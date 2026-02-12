"""
Ocean Salvage Platform (OSP) — Geometry Parameters
===================================================
All dimensions in METERS. CadQuery STEP output will be in meters.
Coordinate system:
  X = longitudinal (positive = forward, origin at midship)
  Y = transverse   (positive = port, origin at centreline)
  Z = vertical     (positive = up, origin at keel baseline)
"""

# ─── Principal dimensions ───────────────────────────────────────────
LOA = 275.0          # Length overall
BOA = 80.0           # Beam overall
DEPTH = 38.0         # Moulded depth (keel to main deck)
OP_DRAFT = 22.0      # Operating draft (waterline)
TRANSIT_DRAFT = 12.0 # Transit draft

# ─── Pontoons (×2) ─────────────────────────────────────────────────
PONT_LENGTH = 245.0
PONT_BEAM = 18.0
PONT_HEIGHT = 12.0
PONT_SHELL = 0.025   # 25 mm shell plate thickness
PONT_Y_PORT = 19.0   # Pontoon centre-to-centre half-spacing (10 m gap + 9 m half-beam)
PONT_Y_STBD = -19.0
PONT_X_OFFSET = 0.0  # Pontoons centred on midship

# ─── Columns (8 total, 4 per hull) ─────────────────────────────────
COL_SIZE = 18.0       # Square cross-section
COL_HEIGHT = 26.0     # From pontoon top (+12 m) to main deck (+38 m)
COL_Z_BASE = 12.0     # Bottom of columns at pontoon top
COL_SHELL = 0.025     # 25 mm shell (32 mm at ice belt)

# Column longitudinal positions (X from midship, positive = fwd)
COL_X_POSITIONS = [90.0, 30.0, -30.0, -90.0]  # Fwd to aft

# Column transverse positions (Y from centreline)
COL_Y_PORT = PONT_Y_PORT    # +19 m
COL_Y_STBD = PONT_Y_STBD   # -19 m

# ─── Channel / Moon Pool ───────────────────────────────────────────
CHANNEL_LENGTH = 135.0
CHANNEL_WIDTH = 20.0    # Clear opening between inner hull faces
CHANNEL_X_OFFSET = 0.0  # Centred on midship

# ─── Main Deck ─────────────────────────────────────────────────────
DECK_Z = 38.0         # Main deck elevation
DECK_PLATE = 0.020    # 20 mm deck plate
DECK_DEPTH = 3.0      # Deck girder depth (structural depth of main deck)

# Equipment deck
EQUIP_DECK_Z = 32.0   # Equipment/tween deck

# ─── Accommodation Block ───────────────────────────────────────────
ACCOM_LENGTH = 50.0
ACCOM_BEAM = 18.0
ACCOM_HEIGHT = 12.0     # 4 decks × 3 m
ACCOM_DECKS = 4
ACCOM_DECK_H = 3.0
ACCOM_X = 100.0         # Forward on stbd hull (centre of block from midship)
ACCOM_Y = PONT_Y_STBD   # On starboard hull → Y = -19 m
ACCOM_Z = DECK_Z        # Sits on main deck

# ─── Bridge / Wheelhouse ───────────────────────────────────────────
BRIDGE_LENGTH = 12.0
BRIDGE_BEAM = 12.0
BRIDGE_HEIGHT = 6.0     # 2 decks
BRIDGE_X = ACCOM_X + ACCOM_LENGTH / 2 - BRIDGE_LENGTH / 2  # Forward end of accom
BRIDGE_Z = ACCOM_Z + ACCOM_HEIGHT  # On top of accommodation

# ─── Reactor Handling Bay ───────────────────────────────────────────
REACTOR_LENGTH = 30.0
REACTOR_BEAM = 18.0
REACTOR_HEIGHT = 20.0
REACTOR_X = -95.0       # Aft on starboard hull
REACTOR_Y = PONT_Y_STBD
REACTOR_Z = DECK_Z
REACTOR_WALL = 0.750    # 250 mm lead + 500 mm concrete equivalent

# ─── Helideck ──────────────────────────────────────────────────────
HELI_DIAMETER = 28.0
HELI_X = -110.0         # Aft end, port side
HELI_Y = PONT_Y_PORT
HELI_Z = DECK_Z + 6.0   # Elevated on stanchions (+44 m)

# ─── Gantry System ─────────────────────────────────────────────────
GANTRY_BEAM_COUNT = 7   # 7 transverse beams spanning channel
GANTRY_SPAN = 28.0      # Beam span (channel + cantilevers each side)
GANTRY_DEPTH = 2.5      # I-beam depth
GANTRY_FLANGE_W = 1.2   # Flange width
GANTRY_WEB_T = 0.040    # Web thickness
GANTRY_FLANGE_T = 0.060 # Flange thickness
GANTRY_SPACING = 10.0   # Longitudinal spacing between beams
GANTRY_X_START = -30.0  # First beam (aftmost)

# Strand jacks (28 total, 4 per gantry beam)
SJ_COUNT = 28
SJ_PER_BEAM = 4
SJ_DIAMETER = 0.8       # Approximate external diameter
SJ_HEIGHT = 2.5         # Overall height of strand jack unit

# ─── Thrusters (10 units) ──────────────────────────────────────────
THRUSTER_DIAMETER = 5.0   # Propeller + nozzle OD
THRUSTER_HEIGHT = 4.0     # Thruster unit depth below keel
THRUSTER_NOZZLE_L = 3.0   # Nozzle length

# Thruster positions [name, x, y] — at keel level Z=0
THRUSTER_POS = [
    ("T1",   110.0, PONT_Y_STBD),   # Stbd fwd
    ("T2",    70.0, PONT_Y_STBD),   # Stbd fwd-mid
    ("T3",   110.0, PONT_Y_PORT),   # Port fwd
    ("T4",    30.0, PONT_Y_STBD),   # Stbd mid-fwd
    ("T5",    30.0, PONT_Y_PORT),   # Port mid-fwd
    ("T6",   -10.0, PONT_Y_PORT),   # Port midship
    ("T7",   -10.0, PONT_Y_STBD),   # Stbd midship
    ("T8",   -50.0, PONT_Y_PORT),   # Port mid-aft
    ("T9",  -110.0, PONT_Y_STBD),   # Stbd aft
    ("T10", -110.0, PONT_Y_PORT),   # Port aft
]

# ─── Cradle (inside channel) ───────────────────────────────────────
CRADLE_LENGTH = 125.0
CRADLE_BEAM = 14.0
CRADLE_HEIGHT = 6.0
CRADLE_SADDLE_PAIRS = 12
CRADLE_Z = PONT_HEIGHT  # Sits at pontoon-top level

# ─── Damping Plates (6 in channel at keel) ─────────────────────────
DAMP_PLATE_COUNT = 6
DAMP_PLATE_WIDTH = CHANNEL_WIDTH - 2.0  # 18 m
DAMP_PLATE_LENGTH = 8.0
DAMP_PLATE_THICK = 0.050  # 50 mm
DAMP_PLATE_Z = 0.5  # Just above keel

# ─── Engine rooms (for visual representation) ──────────────────────
ER_HEIGHT = 6.0  # Equipment deck height (+32 to +38)

# ─── Output directory ──────────────────────────────────────────────
import os
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "step_output")
os.makedirs(OUTPUT_DIR, exist_ok=True)
