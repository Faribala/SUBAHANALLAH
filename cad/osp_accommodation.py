"""
OSP Accommodation Block — 5-deck structure on stbd hull fwd.
50 × 18 × 12 m (4 living decks), plus bridge on top.
150 POB capacity.
"""
import cadquery as cq
from osp_parameters import *


def make_accommodation():
    """Multi-deck accommodation block with internal deck plates."""
    # Outer shell (hollow box)
    shell_t = 0.012  # 12 mm plate
    outer = (
        cq.Workplane("XY")
        .box(ACCOM_LENGTH, ACCOM_BEAM, ACCOM_HEIGHT, centered=True)
    )
    inner = (
        cq.Workplane("XY")
        .box(
            ACCOM_LENGTH - 2 * shell_t,
            ACCOM_BEAM - 2 * shell_t,
            ACCOM_HEIGHT - 2 * shell_t,
            centered=True,
        )
    )
    accom = outer.cut(inner)
    
    # Internal deck plates (3 intermediate decks, creating 4 levels)
    for deck_i in range(1, ACCOM_DECKS):
        z_offset = -ACCOM_HEIGHT / 2 + deck_i * ACCOM_DECK_H
        deck_plate = (
            cq.Workplane("XY")
            .box(
                ACCOM_LENGTH - 2 * shell_t,
                ACCOM_BEAM - 2 * shell_t,
                0.010,  # 10 mm deck plate
                centered=True,
            )
            .translate((0, 0, z_offset))
        )
        accom = accom.union(deck_plate)
    
    # Window openings (simplified: rows of rectangular cutouts on both long faces)
    window_h = 1.2
    window_w = 1.5
    window_spacing = 4.0
    for deck_i in range(ACCOM_DECKS):
        z_win = -ACCOM_HEIGHT / 2 + deck_i * ACCOM_DECK_H + ACCOM_DECK_H / 2
        n_windows = int(ACCOM_LENGTH / window_spacing) - 1
        for w in range(n_windows):
            x_win = -ACCOM_LENGTH / 2 + (w + 1) * window_spacing
            for y_face in [ACCOM_BEAM / 2, -ACCOM_BEAM / 2]:
                win = (
                    cq.Workplane("XY")
                    .transformed(offset=(x_win, y_face, z_win))
                    .box(window_w, shell_t + 0.1, window_h, centered=True)
                )
                accom = accom.cut(win)
    
    # Position in global coords
    accom = accom.translate((ACCOM_X, ACCOM_Y, ACCOM_Z + ACCOM_HEIGHT / 2))
    return accom


def make_bridge():
    """Bridge / wheelhouse on top of accommodation block."""
    bridge = (
        cq.Workplane("XY")
        .box(BRIDGE_LENGTH, BRIDGE_BEAM, BRIDGE_HEIGHT, centered=True)
    )
    # Angled windows (simplified: cut front face at angle)
    window_cut = (
        cq.Workplane("XY")
        .transformed(offset=(BRIDGE_LENGTH / 2, 0, BRIDGE_HEIGHT / 4))
        .box(2.0, BRIDGE_BEAM - 1.0, BRIDGE_HEIGHT / 2, centered=True)
    )
    bridge = bridge.cut(window_cut)
    
    bridge = bridge.translate((
        BRIDGE_X,
        ACCOM_Y,
        BRIDGE_Z + BRIDGE_HEIGHT / 2,
    ))
    return bridge


def make_accom_and_bridge():
    """Complete accommodation and bridge assembly."""
    return make_accommodation().union(make_bridge())


if __name__ == "__main__":
    result = make_accom_and_bridge()
    cq.exporters.export(result, os.path.join(OUTPUT_DIR, "06_accommodation.step"))
    print("Exported 06_accommodation.step")
