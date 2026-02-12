"""
OSP Pontoons — Two parallel pontoons forming the lower hull.
Each pontoon: 245 m × 18 m × 12 m, hollow with 25 mm shell.
"""
import cadquery as cq
from osp_parameters import *


def make_pontoon_shell(length, beam, height, shell_t):
    """Create a single hollow pontoon (box minus inner void)."""
    outer = (
        cq.Workplane("XY")
        .box(length, beam, height, centered=True)
    )
    inner = (
        cq.Workplane("XY")
        .box(length - 2 * shell_t, beam - 2 * shell_t, height - 2 * shell_t, centered=True)
    )
    return outer.cut(inner)


def make_pontoon_with_bulkheads(length, beam, height, shell_t, n_compartments=8):
    """Pontoon shell plus transverse watertight bulkheads."""
    pontoon = make_pontoon_shell(length, beam, height, shell_t)
    
    # Transverse bulkheads dividing into n_compartments
    bhd_spacing = length / n_compartments
    for i in range(1, n_compartments):
        x_pos = -length / 2 + i * bhd_spacing
        bhd = (
            cq.Workplane("XY")
            .transformed(offset=(x_pos, 0, 0))
            .box(shell_t, beam - 2 * shell_t, height - 2 * shell_t, centered=True)
        )
        pontoon = pontoon.union(bhd)
    return pontoon


def make_pontoons():
    """Create both port and starboard pontoons, positioned in global coords."""
    port = make_pontoon_with_bulkheads(
        PONT_LENGTH, PONT_BEAM, PONT_HEIGHT, PONT_SHELL
    )
    # Translate: centre of pontoon at (0, +19, 6) — Z centre at half pontoon height
    port = port.translate((PONT_X_OFFSET, PONT_Y_PORT, PONT_HEIGHT / 2))
    
    stbd = make_pontoon_with_bulkheads(
        PONT_LENGTH, PONT_BEAM, PONT_HEIGHT, PONT_SHELL
    )
    stbd = stbd.translate((PONT_X_OFFSET, PONT_Y_STBD, PONT_HEIGHT / 2))
    
    return port.union(stbd)


if __name__ == "__main__":
    result = make_pontoons()
    cq.exporters.export(result, os.path.join(OUTPUT_DIR, "01_pontoons.step"))
    print("Exported 01_pontoons.step")
