"""
OSP Thrusters — 10 × 360° azimuth thrusters at keel level.
5.0 m propeller diameter in nozzle, 6,000 kW each.
"""
import cadquery as cq
from osp_parameters import *


def make_single_thruster():
    """Single azimuth thruster: nozzle ring + propeller disk + steering column."""
    # Nozzle (hollow cylinder)
    nozzle_or = THRUSTER_DIAMETER / 2 + 0.3
    nozzle_ir = THRUSTER_DIAMETER / 2
    nozzle = (
        cq.Workplane("XY")
        .cylinder(THRUSTER_NOZZLE_L, nozzle_or, centered=True)
    )
    nozzle_hole = (
        cq.Workplane("XY")
        .cylinder(THRUSTER_NOZZLE_L + 0.1, nozzle_ir, centered=True)
    )
    nozzle = nozzle.cut(nozzle_hole)
    
    # Propeller disk (simplified)
    prop = (
        cq.Workplane("XY")
        .cylinder(0.2, THRUSTER_DIAMETER / 2 - 0.1, centered=True)
    )
    
    # Steering column (connects to hull)
    column = (
        cq.Workplane("XY")
        .cylinder(THRUSTER_HEIGHT, 0.8, centered=True)
        .translate((0, 0, THRUSTER_NOZZLE_L / 2 + THRUSTER_HEIGHT / 2))
    )
    
    return nozzle.union(prop).union(column)


def make_all_thrusters():
    """All 10 thrusters positioned at keel level."""
    assembly = None
    
    for name, x, y in THRUSTER_POS:
        thruster = make_single_thruster()
        # Thrusters hang below keel (Z=0 is keel baseline)
        thruster = thruster.translate((x, y, -THRUSTER_NOZZLE_L / 2))
        
        if assembly is None:
            assembly = thruster
        else:
            assembly = assembly.union(thruster)
    
    return assembly


if __name__ == "__main__":
    result = make_all_thrusters()
    cq.exporters.export(result, os.path.join(OUTPUT_DIR, "08_thrusters.step"))
    print("Exported 08_thrusters.step")
