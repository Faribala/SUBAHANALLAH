"""
OSP Helideck — 28 m diameter circular helideck at +44 m, aft port side.
Supported by stanchions from main deck.
"""
import cadquery as cq
from osp_parameters import *


def make_helideck():
    """Helideck: circular platform with H-mark + support stanchions."""
    # Main circular platform (plate + edge lip)
    plate_t = 0.012  # 12 mm plate
    lip_h = 0.2
    
    deck = (
        cq.Workplane("XY")
        .cylinder(plate_t, HELI_DIAMETER / 2, centered=True)
    )
    # Edge lip
    lip_outer = (
        cq.Workplane("XY")
        .cylinder(lip_h, HELI_DIAMETER / 2, centered=True)
        .translate((0, 0, plate_t / 2 + lip_h / 2))
    )
    lip_inner = (
        cq.Workplane("XY")
        .cylinder(lip_h + 0.1, HELI_DIAMETER / 2 - 0.15, centered=True)
        .translate((0, 0, plate_t / 2 + lip_h / 2))
    )
    lip = lip_outer.cut(lip_inner)
    helideck = deck.union(lip)
    
    # H marking (raised strips)
    bar_w = 1.0
    bar_h = 8.0
    bar_t = 0.005  # Paint thickness, just for visual
    
    # Left vertical of H
    h_left = (
        cq.Workplane("XY")
        .box(bar_w, bar_h, bar_t, centered=True)
        .translate((-2.5, 0, plate_t / 2 + bar_t / 2))
    )
    # Right vertical of H
    h_right = (
        cq.Workplane("XY")
        .box(bar_w, bar_h, bar_t, centered=True)
        .translate((2.5, 0, plate_t / 2 + bar_t / 2))
    )
    # Crossbar of H
    h_cross = (
        cq.Workplane("XY")
        .box(5.0, bar_w, bar_t, centered=True)
        .translate((0, 0, plate_t / 2 + bar_t / 2))
    )
    helideck = helideck.union(h_left).union(h_right).union(h_cross)
    
    # Support stanchions (4 legs from main deck to helideck)
    stanchion_r = 0.4
    stanchion_h = HELI_Z - DECK_Z  # 6 m
    offsets = [
        (-8, -8), (-8, 8), (8, -8), (8, 8),
    ]
    for dx, dy in offsets:
        leg = (
            cq.Workplane("XY")
            .cylinder(stanchion_h, stanchion_r, centered=True)
            .translate((dx, dy, -stanchion_h / 2))
        )
        helideck = helideck.union(leg)
    
    # Position in global coords
    helideck = helideck.translate((HELI_X, HELI_Y, HELI_Z))
    return helideck


if __name__ == "__main__":
    result = make_helideck()
    cq.exporters.export(result, os.path.join(OUTPUT_DIR, "09_helideck.step"))
    print("Exported 09_helideck.step")
