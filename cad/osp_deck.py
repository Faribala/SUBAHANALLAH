"""
OSP Main Deck — Transverse deck structure at +38 m with moon-pool cutout.
275 m × 80 m plate with channel opening (135 × 20 m).
Includes equipment deck at +32 m between and atop columns.
"""
import cadquery as cq
from osp_parameters import *


def make_main_deck():
    """Main deck plate with moon-pool opening."""
    # Full deck plate
    deck = (
        cq.Workplane("XY")
        .box(LOA, BOA, DECK_PLATE, centered=True)
    )
    
    # Cut the moon-pool / channel opening
    channel_cut = (
        cq.Workplane("XY")
        .box(CHANNEL_LENGTH, CHANNEL_WIDTH, DECK_PLATE + 1.0, centered=True)
    )
    deck = deck.cut(channel_cut)
    
    # Position at main deck elevation
    deck = deck.translate((0, 0, DECK_Z))
    return deck


def make_deck_girders():
    """Main structural girders under the deck (simplified as transverse beams)."""
    girders = None
    n_girders = 12
    spacing = LOA / (n_girders + 1)
    
    for i in range(1, n_girders + 1):
        x_pos = -LOA / 2 + i * spacing
        
        # Port-side girder
        girder_p = (
            cq.Workplane("XY")
            .box(1.0, PONT_BEAM, DECK_DEPTH, centered=True)
            .translate((x_pos, PONT_Y_PORT, DECK_Z - DECK_DEPTH / 2))
        )
        # Starboard-side girder
        girder_s = (
            cq.Workplane("XY")
            .box(1.0, PONT_BEAM, DECK_DEPTH, centered=True)
            .translate((x_pos, PONT_Y_STBD, DECK_Z - DECK_DEPTH / 2))
        )
        
        if girders is None:
            girders = girder_p.union(girder_s)
        else:
            girders = girders.union(girder_p).union(girder_s)
    
    return girders


def make_equipment_deck():
    """Equipment / tween deck at +32 m on both hull sides (not spanning channel)."""
    # Port-side equipment deck
    port_deck = (
        cq.Workplane("XY")
        .box(PONT_LENGTH, PONT_BEAM, DECK_PLATE, centered=True)
        .translate((0, PONT_Y_PORT, EQUIP_DECK_Z))
    )
    # Starboard-side equipment deck
    stbd_deck = (
        cq.Workplane("XY")
        .box(PONT_LENGTH, PONT_BEAM, DECK_PLATE, centered=True)
        .translate((0, PONT_Y_STBD, EQUIP_DECK_Z))
    )
    return port_deck.union(stbd_deck)


def make_full_deck():
    """Complete deck structure: main deck + girders + equipment deck."""
    return make_main_deck().union(make_deck_girders()).union(make_equipment_deck())


if __name__ == "__main__":
    result = make_full_deck()
    cq.exporters.export(result, os.path.join(OUTPUT_DIR, "03_main_deck.step"))
    print("Exported 03_main_deck.step")
