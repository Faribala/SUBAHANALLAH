"""
OSP Gantry & Strand Jack System — 7 transverse gantry beams + 28 strand jacks.
Beams span 28 m across channel at 10 m spacing.
4 strand jacks per beam (2 per hull side).
"""
import cadquery as cq
from osp_parameters import *


def make_gantry_beam():
    """Single I-beam cross-section gantry beam."""
    # Simplified as a solid rectangular beam (I-section detail too fine for this scale)
    beam = (
        cq.Workplane("XY")
        .box(1.5, GANTRY_SPAN, GANTRY_DEPTH, centered=True)
    )
    return beam


def make_strand_jack():
    """Single strand jack unit (simplified as cylinder)."""
    sj = (
        cq.Workplane("XY")
        .cylinder(SJ_HEIGHT, SJ_DIAMETER / 2, centered=True)
    )
    return sj


def make_gantry_system():
    """All 7 gantry beams plus 28 strand jacks."""
    assembly = None
    gantry_z = DECK_Z + GANTRY_DEPTH / 2  # Beams sit on main deck
    
    for i in range(GANTRY_BEAM_COUNT):
        x_pos = GANTRY_X_START + i * GANTRY_SPACING
        
        # Gantry beam
        beam = make_gantry_beam().translate((x_pos, 0, gantry_z))
        
        if assembly is None:
            assembly = beam
        else:
            assembly = assembly.union(beam)
        
        # 4 strand jacks per beam: 2 on port side, 2 on starboard
        sj_y_positions = [
            PONT_Y_PORT - COL_SIZE / 4,   # Port outer
            PONT_Y_PORT + COL_SIZE / 4,   # Port inner (toward channel)
            PONT_Y_STBD - COL_SIZE / 4,   # Stbd inner (toward channel)
            PONT_Y_STBD + COL_SIZE / 4,   # Stbd outer
        ]
        
        for y_pos in sj_y_positions:
            sj = make_strand_jack().translate((
                x_pos,
                y_pos,
                gantry_z + GANTRY_DEPTH / 2 + SJ_HEIGHT / 2,
            ))
            assembly = assembly.union(sj)
    
    return assembly


if __name__ == "__main__":
    result = make_gantry_system()
    cq.exporters.export(result, os.path.join(OUTPUT_DIR, "07_gantry.step"))
    print("Exported 07_gantry.step")
