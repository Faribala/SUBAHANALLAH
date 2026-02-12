"""
OSP Full Assembly — Combines all sub-assemblies into one STEP model.
===============================================================

Usage:
    cd cad/
    python osp_assembly.py

Outputs:
    step_output/OSP_full_assembly.step   — Single combined STEP file (~275 m LOA)
    step_output/01_pontoons.step         — Pontoons only
    step_output/02_columns.step          — Columns only
    step_output/03_main_deck.step        — Deck structure only
    step_output/04_moon_pool.step        — Moon pool internals
    step_output/05_reactor_bay.step      — Reactor bay
    step_output/06_accommodation.step    — Accommodation + bridge
    step_output/07_gantry.step           — Gantry + strand jacks
    step_output/08_thrusters.step        — All 10 thrusters
    step_output/09_helideck.step         — Helideck + stanchions

Coordinate system (meters):
    X = longitudinal  (positive = forward, origin at midship)
    Y = transverse    (positive = port, origin at centreline)
    Z = vertical      (positive = up, origin at keel baseline)

Import into:
    - FreeCAD       → File > Import > STEP
    - Rhino         → File > Import > STEP
    - SOLIDWORKS    → File > Open > STEP
    - Fusion 360    → File > Open > Upload STEP
    - Blender       → Use FreeCAD STEP→STL, then import STL
"""
import os
import sys
import time
import cadquery as cq
from osp_parameters import OUTPUT_DIR

# ── Import sub-assembly builders ────────────────────────────────────
from osp_pontoons import make_pontoons
from osp_columns import make_all_columns
from osp_deck import make_full_deck
from osp_moon_pool import make_moon_pool
from osp_reactor_bay import make_reactor_bay
from osp_accommodation import make_accom_and_bridge
from osp_gantry import make_gantry_system
from osp_thrusters import make_all_thrusters
from osp_helideck import make_helideck


def build_and_export_sub(name, builder_fn, index):
    """Build one sub-assembly, export to STEP, and return the solid."""
    t0 = time.time()
    print(f"  [{index:02d}] Building {name}...", end="", flush=True)
    solid = builder_fn()
    fname = os.path.join(OUTPUT_DIR, f"{index:02d}_{name}.step")
    cq.exporters.export(solid, fname)
    dt = time.time() - t0
    print(f" done ({dt:.1f}s) → {fname}")
    return solid


def main():
    print("=" * 60)
    print("  Ocean Salvage Platform (OSP) — CadQuery CAD Generator")
    print("  275 m LOA × 80 m BOA × 38 m Depth")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    t_start = time.time()
    
    # Build each sub-assembly and export individually
    subs = [
        ("pontoons",       make_pontoons,        1),
        ("columns",        make_all_columns,     2),
        ("main_deck",      make_full_deck,       3),
        ("moon_pool",      make_moon_pool,       4),
        ("reactor_bay",    make_reactor_bay,     5),
        ("accommodation",  make_accom_and_bridge, 6),
        ("gantry",         make_gantry_system,   7),
        ("thrusters",      make_all_thrusters,   8),
        ("helideck",       make_helideck,        9),
    ]
    
    solids = {}
    for name, fn, idx in subs:
        solids[name] = build_and_export_sub(name, fn, idx)
    
    # ── Combine into full assembly ──────────────────────────────────
    print(f"\n  [10] Assembling full model...", end="", flush=True)
    t0 = time.time()
    
    assembly = solids["pontoons"]
    for name in ["columns", "main_deck", "moon_pool", "reactor_bay",
                  "accommodation", "gantry", "thrusters", "helideck"]:
        assembly = assembly.union(solids[name])
    
    full_path = os.path.join(OUTPUT_DIR, "OSP_full_assembly.step")
    cq.exporters.export(assembly, full_path)
    dt = time.time() - t0
    print(f" done ({dt:.1f}s) → {full_path}")
    
    # ── Summary ─────────────────────────────────────────────────────
    total = time.time() - t_start
    print(f"\n{'=' * 60}")
    print(f"  All exports complete in {total:.1f}s")
    print(f"  Files in: {os.path.abspath(OUTPUT_DIR)}")
    print(f"{'=' * 60}")
    
    # List output files
    print("\nGenerated STEP files:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        if f.endswith(".step"):
            fpath = os.path.join(OUTPUT_DIR, f)
            size_mb = os.path.getsize(fpath) / (1024 * 1024)
            print(f"  {f:40s}  {size_mb:6.1f} MB")


if __name__ == "__main__":
    main()
