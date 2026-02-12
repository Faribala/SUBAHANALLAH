"""
OSP Reactor Handling Bay — Shielded enclosure on stbd hull aft.
30 × 18 × 20 m with 750 mm composite walls (lead + barite concrete).
Mass: ~6,500 t shielding.
"""
import cadquery as cq
from osp_parameters import *


def make_reactor_bay():
    """Shielded reactor bay enclosure — hollow box with thick walls."""
    wall = REACTOR_WALL  # 0.75 m total wall thickness
    
    # Outer shell
    outer = (
        cq.Workplane("XY")
        .box(REACTOR_LENGTH, REACTOR_BEAM, REACTOR_HEIGHT, centered=True)
    )
    # Inner void
    inner = (
        cq.Workplane("XY")
        .box(
            REACTOR_LENGTH - 2 * wall,
            REACTOR_BEAM - 2 * wall,
            REACTOR_HEIGHT - 2 * wall,
            centered=True,
        )
    )
    bay = outer.cut(inner)
    
    # Large access door opening (aft face, for submarine reactor section entry)
    door_w = 10.0
    door_h = 14.0
    door = (
        cq.Workplane("XY")
        .transformed(offset=(-REACTOR_LENGTH / 2, 0, -REACTOR_HEIGHT / 2 + door_h / 2 + wall))
        .box(wall + 0.1, door_w, door_h, centered=True)
    )
    bay = bay.cut(door)
    
    # Overhead crane rail (simplified beam inside bay)
    crane_rail = (
        cq.Workplane("XY")
        .box(REACTOR_LENGTH - 2 * wall - 1.0, 0.6, 0.8, centered=True)
        .translate((0, 0, REACTOR_HEIGHT / 2 - wall - 1.5))
    )
    bay = bay.union(crane_rail)
    
    # Position in global coordinates
    bay = bay.translate((REACTOR_X, REACTOR_Y, REACTOR_Z + REACTOR_HEIGHT / 2))
    return bay


if __name__ == "__main__":
    result = make_reactor_bay()
    cq.exporters.export(result, os.path.join(OUTPUT_DIR, "05_reactor_bay.step"))
    print("Exported 05_reactor_bay.step")
