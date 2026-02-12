"""
OSP Moon Pool — Channel between hulls with damping plates and submarine cradle.
Channel: 135 × 20 m open waterway between pontoons.
Cradle: 125 × 14 m, 12 saddle pairs.
6 perforated damping plates at keel level.
"""
import cadquery as cq
import math
from osp_parameters import *


def make_damping_plates():
    """Six perforated damping plates at keel level inside channel."""
    plates = None
    plate_spacing = CHANNEL_LENGTH / (DAMP_PLATE_COUNT + 1)
    
    for i in range(1, DAMP_PLATE_COUNT + 1):
        x_pos = -CHANNEL_LENGTH / 2 + i * plate_spacing
        
        # Solid plate
        plate = (
            cq.Workplane("XY")
            .box(DAMP_PLATE_LENGTH, DAMP_PLATE_WIDTH, DAMP_PLATE_THICK, centered=True)
        )
        
        # Perforate with circular holes (simplified: 5×3 grid)
        for row in range(5):
            for col in range(3):
                hx = -DAMP_PLATE_LENGTH / 2 + (row + 1) * DAMP_PLATE_LENGTH / 6
                hy = -DAMP_PLATE_WIDTH / 2 + (col + 1) * DAMP_PLATE_WIDTH / 4
                hole = (
                    cq.Workplane("XY")
                    .transformed(offset=(hx, hy, 0))
                    .cylinder(DAMP_PLATE_THICK + 0.1, 0.8, centered=True)
                )
                plate = plate.cut(hole)
        
        plate = plate.translate((x_pos, 0, DAMP_PLATE_Z))
        
        if plates is None:
            plates = plate
        else:
            plates = plates.union(plate)
    
    return plates


def make_cradle():
    """Submarine cradle with saddle supports inside channel."""
    # Base frame (longitudinal rails)
    rail_w = 0.6
    rail_h = 1.5
    
    rail_port = (
        cq.Workplane("XY")
        .box(CRADLE_LENGTH, rail_w, rail_h, centered=True)
        .translate((0, CRADLE_BEAM / 2, CRADLE_Z + rail_h / 2))
    )
    rail_stbd = (
        cq.Workplane("XY")
        .box(CRADLE_LENGTH, rail_w, rail_h, centered=True)
        .translate((0, -CRADLE_BEAM / 2, CRADLE_Z + rail_h / 2))
    )
    cradle = rail_port.union(rail_stbd)
    
    # Saddle supports (12 pairs — V-shaped simplified as blocks)
    saddle_spacing = CRADLE_LENGTH / (CRADLE_SADDLE_PAIRS + 1)
    saddle_w = 2.0
    saddle_h = CRADLE_HEIGHT - rail_h
    
    for i in range(1, CRADLE_SADDLE_PAIRS + 1):
        x_pos = -CRADLE_LENGTH / 2 + i * saddle_spacing
        for y_sign in [1, -1]:
            y_pos = y_sign * CRADLE_BEAM / 3
            saddle = (
                cq.Workplane("XY")
                .box(saddle_w, 1.0, saddle_h, centered=True)
                .translate((x_pos, y_pos, CRADLE_Z + rail_h + saddle_h / 2))
            )
            cradle = cradle.union(saddle)
    
    # Cross-beams connecting rails
    for i in range(0, CRADLE_SADDLE_PAIRS + 2, 3):
        x_pos = -CRADLE_LENGTH / 2 + i * saddle_spacing
        xbeam = (
            cq.Workplane("XY")
            .box(0.5, CRADLE_BEAM, rail_h, centered=True)
            .translate((x_pos, 0, CRADLE_Z + rail_h / 2))
        )
        cradle = cradle.union(xbeam)
    
    return cradle


def make_moon_pool():
    """Complete moon pool assembly: damping plates + cradle."""
    return make_damping_plates().union(make_cradle())


if __name__ == "__main__":
    result = make_moon_pool()
    cq.exporters.export(result, os.path.join(OUTPUT_DIR, "04_moon_pool.step"))
    print("Exported 04_moon_pool.step")
