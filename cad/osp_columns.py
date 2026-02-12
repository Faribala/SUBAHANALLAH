"""
OSP Columns — 8 square columns (18 × 18 m), 4 per hull.
Hollow with 25 mm shell, extending from pontoon top (+12 m) to main deck (+38 m).
"""
import cadquery as cq
from osp_parameters import *


def make_single_column(size, height, shell_t):
    """Single hollow square column."""
    outer = cq.Workplane("XY").box(size, size, height, centered=True)
    inner = cq.Workplane("XY").box(
        size - 2 * shell_t, size - 2 * shell_t, height - 2 * shell_t, centered=True
    )
    return outer.cut(inner)


def make_all_columns():
    """Create all 8 columns positioned in global coordinates."""
    assembly = None
    col_z_centre = COL_Z_BASE + COL_HEIGHT / 2  # Centre of column in Z
    
    for i, x_pos in enumerate(COL_X_POSITIONS):
        for y_pos in [COL_Y_PORT, COL_Y_STBD]:
            col = make_single_column(COL_SIZE, COL_HEIGHT, COL_SHELL)
            col = col.translate((x_pos, y_pos, col_z_centre))
            if assembly is None:
                assembly = col
            else:
                assembly = assembly.union(col)
    return assembly


if __name__ == "__main__":
    result = make_all_columns()
    cq.exporters.export(result, os.path.join(OUTPUT_DIR, "02_columns.step"))
    print("Exported 02_columns.step")
