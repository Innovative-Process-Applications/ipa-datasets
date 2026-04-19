"""
IPA Pharmaceutical Roller Compactor Platform: Scale-Up & Performance Dataset v1.0
==================================================================================
Synthetic dataset modeling the IPA CL-series pharmaceutical roller compactor
platform from R&D (CL25150) through full-scale production (CL100250), using
IPA's published specifications and Johanson/Heckel physical models.

Sources:
  - IPA Pharma RC Brochure (2026)
  - IPA Pharma Compactor Specifications page
  - IPA Roll Compactor page (industrial line dimensions)
  - IPA Products & Services PDF

Key IPA differentiators modeled:
  - Twin feed screw design (HFS + VFS independent control)
  - Scalable platform: consistent ribbon quality across CL sizes
  - Integrated milling (PM-series in-air impact mills)
  - Proprietary PLC controls with internal control loops
  - Low bulk density powder processing capability
  - Efficient changeover and simplified maintenance

THIS IS SYNTHETIC EDUCATIONAL DATA. NOT REAL CUSTOMER OR LAB DATA.
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=2026)

# =============================================================================
# IPA CL-SERIES PHARMA COMPACTOR SPECS (from published specifications)
# =============================================================================
CL_MODELS = [
    {"model": "CL25150",  "roll_dia_in": 1.0, "roll_width_in": 6,
     "roll_dia_cm": 2.5,  "roll_width_cm": 15,
     "max_pressure_lbs_in": 9900, "max_pressure_kn_cm": 17.5,
     "cap_light_lbs": (10, 23),   "cap_heavy_lbs": (25, 56),
     "mill_size": None, "total_hp": 5, "total_kw": 3.75,
     "weight_lbs": 1200, "scale": "R&D / Lab"},
    {"model": "CL30200",  "roll_dia_in": 1.0, "roll_width_in": 8,
     "roll_dia_cm": 3.0,  "roll_width_cm": 20,
     "max_pressure_lbs_in": 9900, "max_pressure_kn_cm": 17.5,
     "cap_light_lbs": (24, 54),   "cap_heavy_lbs": (64, 140),
     "mill_size": "PM3", "total_hp": 2.75, "total_kw": 2.0,
     "weight_lbs": 2100, "scale": "Pilot"},
    {"model": "CL50200",  "roll_dia_in": 2.0, "roll_width_in": 8,
     "roll_dia_cm": 5.0,  "roll_width_cm": 20,
     "max_pressure_lbs_in": 14800, "max_pressure_kn_cm": 26.0,
     "cap_light_lbs": (64, 140),  "cap_heavy_lbs": (120, 265),
     "mill_size": "PM6", "total_hp": 12, "total_kw": 9.0,
     "weight_lbs": 5000, "scale": "Pilot / Small Production"},
    {"model": "CL75200",  "roll_dia_in": 3.0, "roll_width_in": 8,
     "roll_dia_cm": 7.5,  "roll_width_cm": 20,
     "max_pressure_lbs_in": 8500, "max_pressure_kn_cm": 15.0,
     "cap_light_lbs": (95, 209),  "cap_heavy_lbs": (182, 400),
     "mill_size": "PM6", "total_hp": 20, "total_kw": 15.0,
     "weight_lbs": 6000, "scale": "Production"},
    {"model": "CL100250", "roll_dia_in": 4.0, "roll_width_in": 10,
     "roll_dia_cm": 10.0, "roll_width_cm": 25,
     "max_pressure_lbs_in": 9900, "max_pressure_kn_cm": 17.5,
     "cap_light_lbs": (200, 440), "cap_heavy_lbs": (425, 935),
     "mill_size": "PM8", "total_hp": 25, "total_kw": 19.0,
     "weight_lbs": 9500, "scale": "Full Production"},
]

# =============================================================================
# PHARMA MATERIALS (representative formulations)
# =============================================================================
MATERIALS = {
    "MCC_PH101": {
        "label": "MCC PH-101 (Low Density Filler)",
        "feed_density_gcc": 0.32, "compact_density_gcc": 1.20,
        "heckel_k": 0.020, "heckel_a": 0.55,
        "deformation": "plastic", "flow_index": 4,
        "moisture_pct": 4.5,
    },
    "lactose_DCL11": {
        "label": "Lactose DCL-11 (Direct Compression)",
        "feed_density_gcc": 0.62, "compact_density_gcc": 1.45,
        "heckel_k": 0.014, "heckel_a": 0.50,
        "deformation": "brittle", "flow_index": 7,
        "moisture_pct": 0.5,
    },
    "mannitol_SD200": {
        "label": "Mannitol SD-200 (Spray Dried)",
        "feed_density_gcc": 0.48, "compact_density_gcc": 1.49,
        "heckel_k": 0.012, "heckel_a": 0.48,
        "deformation": "brittle", "flow_index": 6,
        "moisture_pct": 0.3,
    },
    "API_blend_40pct": {
        "label": "API Blend 40% Drug Load",
        "feed_density_gcc": 0.38, "compact_density_gcc": 1.30,
        "heckel_k": 0.017, "heckel_a": 0.52,
        "deformation": "mixed", "flow_index": 3,
        "moisture_pct": 2.0,
    },
    "vitamin_premix": {
        "label": "Vitamin/Mineral Premix (Nutraceutical)",
        "feed_density_gcc": 0.45, "compact_density_gcc": 1.35,
        "heckel_k": 0.015, "heckel_a": 0.50,
        "deformation": "mixed", "flow_index": 5,
        "moisture_pct": 3.0,
    },
}

# =============================================================================
# PROCESS PARAMETERS
# =============================================================================
ROLL_PRESSURE_FRACTIONS = [0.3, 0.5, 0.7, 0.85, 1.0]  # fraction of max
ROLL_SPEED_RPM = [2, 4, 6, 8, 10]
HFS_SPEED_RPM = [15, 30, 50, 75, 100]  # horizontal feed screw
VFS_RATIO = [0.6, 0.8, 1.0, 1.2, 1.5]  # VFS/HFS ratio

N_REPLICATES = 3  # per condition

# =============================================================================
# PHYSICS
# =============================================================================

def compute_scf(pressure_lbs_in, roll_width_in):
    """Specific compaction force in kN/cm."""
    return (pressure_lbs_in * 0.00444822) / (roll_width_in * 2.54)

def ribbon_density(scf_kn_cm, roll_dia_cm, gap_mm, heckel_k, heckel_a,
                   vfs_ratio, hfs_rpm, roll_rpm, deformation):
    """Compute ribbon relative density using Heckel + IPA twin-screw model."""
    # Gap estimate based on roll geometry and pressure
    contact_len = np.sqrt(roll_dia_cm * 10 / 2 * 2.0 * gap_mm)
    pressure_mpa = (scf_kn_cm * 100) / max(contact_len, 3.0)

    # Heckel
    rd = 1.0 - np.exp(-(heckel_k * pressure_mpa + heckel_a))

    # Twin feed screw VFS ratio effect — optimal around 1.0
    vfs_optimality = np.exp(-((vfs_ratio - 1.0) ** 2) / (2 * 0.15 ** 2))
    rd *= (0.90 + 0.10 * vfs_optimality)

    # Roll speed / dwell time
    if deformation == "plastic":
        rd *= (1.0 - 0.006 * max(roll_rpm - 4, 0))
    elif deformation == "brittle":
        rd *= (1.0 - 0.001 * max(roll_rpm - 4, 0))
    else:
        rd *= (1.0 - 0.003 * max(roll_rpm - 4, 0))

    # HFS feed rate effect on pre-densification
    feed_ratio = hfs_rpm / max(roll_rpm, 1)
    feed_opt = np.exp(-((feed_ratio - 10) ** 2) / (2 * 5 ** 2))
    rd *= (0.95 + 0.05 * feed_opt)

    return np.clip(rd, 0.35, 0.92)

def compute_throughput(model, material, roll_rpm, hfs_rpm, rd):
    """Throughput in kg/hr based on capacity range and operating conditions."""
    if material["feed_density_gcc"] <= 0.5:
        cap_range = model["cap_light_lbs"]
    else:
        cap_range = model["cap_heavy_lbs"]

    # Scale within capacity range based on operating conditions
    rpm_frac = (roll_rpm - 2) / 8
    hfs_frac = (hfs_rpm - 15) / 85
    operating_frac = 0.5 * rpm_frac + 0.5 * hfs_frac

    throughput_lbs = cap_range[0] + (cap_range[1] - cap_range[0]) * np.clip(operating_frac, 0, 1)
    throughput_kg = throughput_lbs * 0.4536
    return throughput_lbs, throughput_kg

def density_uniformity_cv(vfs_ratio, hfs_rpm, roll_rpm, model_scale):
    """Across-ribbon density CV%. Twin feed screw advantage."""
    # Baseline: twin screw gives good uniformity
    base_cv = 2.5
    # VFS ratio: optimal around 1.0
    vfs_penalty = 2.0 * abs(vfs_ratio - 1.0)
    # Feed ratio
    ratio = hfs_rpm / max(roll_rpm, 1)
    ratio_penalty = 1.5 * abs(ratio - 10) / 10
    # Scale: larger machines slightly harder to keep uniform
    scale_factors = {"R&D / Lab": 0, "Pilot": 0.2, "Pilot / Small Production": 0.3,
                     "Production": 0.5, "Full Production": 0.7}
    scale_pen = scale_factors.get(model_scale, 0.3)
    return base_cv + vfs_penalty + ratio_penalty + scale_pen

def compute_granule_yield(rd, fines_pct):
    """Yield = 100% - fines% - oversize%."""
    oversize = max(0, 5 * (rd - 0.82))  # over-compacted ribbons resist milling
    return np.clip(100 - fines_pct - oversize, 40, 98)

def compute_fines(rd, deformation):
    """Fines fraction after integrated PM-series mill."""
    base = 55 * (1 - rd)
    if deformation == "brittle":
        base += 5
    return np.clip(base, 3, 50)

def compute_changeover_hr(model):
    """Changeover time — IPA advantage: efficient changeover design."""
    # Scales with machine size
    base = 1.0 + 0.5 * np.log2(model["weight_lbs"] / 1200)
    return round(base, 1)

# =============================================================================
# GENERATE DATASET
# =============================================================================
rows = []
run_id = 0

for model in CL_MODELS:
    for mat_key, mat in MATERIALS.items():
        for pf in ROLL_PRESSURE_FRACTIONS:
            for rs in ROLL_SPEED_RPM:
                for hfs in HFS_SPEED_RPM:
                    for vr in VFS_RATIO:
                        for rep in range(N_REPLICATES):
                            run_id += 1
                            pressure = model["max_pressure_lbs_in"] * pf
                            scf = compute_scf(pressure, model["roll_width_in"])
                            gap_mm = 1.5 + rng.uniform(-0.3, 0.3)

                            rd = ribbon_density(
                                scf, model["roll_dia_cm"], gap_mm,
                                mat["heckel_k"], mat["heckel_a"],
                                vr, hfs, rs, mat["deformation"])
                            rd += rng.normal(0, 0.010)
                            rd = np.clip(rd, 0.35, 0.92)

                            rib_density_gcc = rd * mat["compact_density_gcc"]
                            porosity = 1 - rd

                            cv = density_uniformity_cv(vr, hfs, rs, model["scale"])
                            cv += rng.normal(0, 0.3)
                            cv = np.clip(cv, 1.0, 12.0)

                            fines = compute_fines(rd, mat["deformation"])
                            fines += rng.normal(0, 1.5)
                            fines = np.clip(fines, 2, 55)

                            tp_lbs, tp_kg = compute_throughput(model, mat, rs, hfs, rd)
                            tp_kg += rng.normal(0, tp_kg * 0.03)
                            tp_kg = max(tp_kg, 1)
                            tp_lbs = tp_kg / 0.4536

                            granule_yield = compute_granule_yield(rd, fines)
                            granule_yield += rng.normal(0, 1.0)
                            granule_yield = np.clip(granule_yield, 35, 99)

                            zinchuk = "Yes" if 0.60 <= rd <= 0.80 else "No"
                            changeover = compute_changeover_hr(model)

                            # Specific energy
                            power_kw = model["total_kw"] * (0.4 + 0.6 * pf)
                            se = (power_kw / max(tp_kg, 1)) * 1000  # kWh/tonne

                            rows.append({
                                "run_id": run_id,
                                "compactor_model": model["model"],
                                "scale": model["scale"],
                                "roll_diameter_in": model["roll_dia_in"],
                                "roll_width_in": model["roll_width_in"],
                                "roll_diameter_cm": model["roll_dia_cm"],
                                "roll_width_cm": model["roll_width_cm"],
                                "max_roll_pressure_kn_cm": model["max_pressure_kn_cm"],
                                "integrated_mill": model["mill_size"] if model["mill_size"] else "None",
                                "total_power_kw": model["total_kw"],
                                "material": mat_key,
                                "feed_density_gcc": mat["feed_density_gcc"],
                                "deformation_type": mat["deformation"],
                                "roll_pressure_fraction": pf,
                                "scf_kn_cm": round(scf, 2),
                                "roll_speed_rpm": rs,
                                "hfs_speed_rpm": hfs,
                                "vfs_hfs_ratio": vr,
                                "gap_width_mm": round(gap_mm, 2),
                                "ribbon_rel_density": round(rd, 4),
                                "ribbon_density_gcc": round(rib_density_gcc, 4),
                                "ribbon_porosity": round(porosity, 4),
                                "density_cv_pct": round(cv, 2),
                                "fines_pct": round(fines, 2),
                                "granule_yield_pct": round(granule_yield, 2),
                                "in_zinchuk_window": zinchuk,
                                "throughput_kg_hr": round(tp_kg, 1),
                                "throughput_lbs_hr": round(tp_lbs, 1),
                                "specific_energy_kwh_tonne": round(se, 2),
                                "changeover_time_hr": changeover,
                                "replicate": rep + 1,
                            })

df = pd.DataFrame(rows)

# Subsample to manageable size (full factorial is huge)
# Keep ~3000 rows: stratified by model and material
samples = []
for _, group in df.groupby(["compactor_model", "material"]):
    samples.append(group.sample(min(120, len(group)), random_state=42))
df_sampled = pd.concat(samples, ignore_index=True)
df_sampled["run_id"] = range(1, len(df_sampled) + 1)
df_sampled.to_csv("ipa_pharma_compactor_v1.0.csv", index=False)

print(f"Wrote {len(df_sampled)} rows, {len(df_sampled.columns)} columns")
print(f"\n=== Model distribution ===")
print(df_sampled["compactor_model"].value_counts().sort_index())
print(f"\n=== Scale-up: mean throughput by model ===")
print(df_sampled.groupby("compactor_model")["throughput_kg_hr"].mean().round(1))
print(f"\n=== Zinchuk compliance ===")
print(df_sampled["in_zinchuk_window"].value_counts())
print(f"\n=== Mean density CV% by model ===")
print(df_sampled.groupby("compactor_model")["density_cv_pct"].mean().round(2))
print(f"\n=== Mean granule yield by model ===")
print(df_sampled.groupby("compactor_model")["granule_yield_pct"].mean().round(1))
