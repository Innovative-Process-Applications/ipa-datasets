# IPA Pharmaceutical Roller Compactor Platform: Scale-Up & Performance (Synthetic)

**Version:** 1.0
**Publisher:** [Innovative Process Applications (IPA)](https://www.innovativeprocess.com)
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

> ⚠️ **This dataset is 100% synthetic and intended for educational use only.**
> Generated from IPA's published CL-series specifications and standard
> compaction physics — not real production or clinical batch data.

---

## What's in this dataset

3,000 simulated pharmaceutical roller compaction runs spanning IPA's complete
CL-series platform — from R&D lab (CL25150, 5 HP) through full production
(CL100250, 25 HP) — across 5 pharma/nutraceutical materials and the full
operating envelope of twin-feed-screw process parameters.

### Equipment specifications (from IPA published data)

| Model | Roll Size | Max Pressure | Integrated Mill | Power | Scale |
|---|---|---|---|---|---|
| CL25150 | 1"×6" (2.5×15 cm) | 17.5 kN/cm | None | 5 HP | R&D / Lab |
| CL30200 | 1"×8" (3×20 cm) | 17.5 kN/cm | PM3 | 2.75 HP | Pilot |
| CL50200 | 2"×8" (5×20 cm) | 26.0 kN/cm | PM6 | 12 HP | Pilot / Small Prod |
| CL75200 | 3"×8" (7.5×20 cm) | 15.0 kN/cm | PM6 | 20 HP | Production |
| CL100250 | 4"×10" (10×25 cm) | 17.5 kN/cm | PM8 | 25 HP | Full Production |

### Column descriptions

| Column | Units | Description |
|---|---|---|
| `compactor_model` | — | IPA CL-series model |
| `scale` | — | R&D / Lab, Pilot, Production, Full Production |
| `roll_diameter_in` / `_cm` | in / cm | Roll diameter |
| `roll_width_in` / `_cm` | in / cm | Roll width |
| `max_roll_pressure_kn_cm` | kN/cm | Maximum specific compaction force |
| `integrated_mill` | — | PM-series in-air impact mill (or None) |
| `total_power_kw` | kW | Total system power |
| `material` | — | Pharma material identifier |
| `feed_density_gcc` | g/cc | Feed powder bulk density |
| `deformation_type` | — | Plastic, brittle, or mixed |
| `roll_pressure_fraction` | — | Fraction of max pressure applied (0.3–1.0) |
| `scf_kn_cm` | kN/cm | Actual specific compaction force |
| `roll_speed_rpm` | rpm | Roll rotation speed |
| `hfs_speed_rpm` | rpm | Horizontal feed screw speed (controls throughput) |
| `vfs_hfs_ratio` | — | Vertical/horizontal feed screw speed ratio (controls pre-compression) |
| `gap_width_mm` | mm | Roll gap |
| `ribbon_rel_density` | — | Relative density (fraction of true density) |
| `ribbon_density_gcc` | g/cc | Absolute ribbon density |
| `ribbon_porosity` | — | 1 − relative density |
| `density_cv_pct` | % | Across-ribbon density uniformity |
| `fines_pct` | % | Fines fraction after milling |
| `granule_yield_pct` | % | Usable granule yield |
| `in_zinchuk_window` | Yes/No | Ribbon RD in 0.60–0.80 tabletability range |
| `throughput_kg_hr` / `_lbs_hr` | kg/hr / lbs/hr | Mass throughput |
| `specific_energy_kwh_tonne` | kWh/tonne | Energy efficiency |
| `changeover_time_hr` | hours | Estimated changeover time |

## IPA platform advantages demonstrated in the data

1. **Twin feed screw (HFS + VFS):** Independent control of throughput (HFS)
   and pre-compression (VFS) produces a uniquely tunable operating space.
   The VFS/HFS ratio is a key process parameter not available on single-screw
   compactors.

2. **Scalable platform:** Consistent ribbon quality (CV%, yield) across the
   CL25150 → CL100250 range, enabling direct R&D-to-production scale-up.

3. **Integrated in-air impact milling:** PM-series mills minimize heat
   generation and maximize granule yield with precise PSD control.

4. **Efficient changeover:** Modular design enables fast product changeover,
   critical for multi-product pharma facilities.

5. **Low bulk density capability:** Twin screw design is proven efficient
   with light powders (feed density 0.3–0.5 g/cc) containing high air content.

## Cross-links

- **Kaggle:** https://www.kaggle.com/innovativeprocapps
- **Hugging Face:** https://huggingface.co/datasets/Innovative-Process-Applications/ipa-pharma-compactor-platform
- **Zenodo:** https://zenodo.org/records/19646708
- **GitHub:** https://huggingface.co/datasets/Innovative-Process-Applications/ipa-pharma-compactor-platform
- **IPA website:** https://ipaapplications.com/

## Citation

> Innovative Process Applications (2026). *IPA Pharmaceutical Roller Compactor
> Platform: Scale-Up & Performance (Synthetic), v1.0*. CC BY 4.0.
> https://www.innovativeprocess.com
