# Roller Compaction: Ribbon Density vs. Process Parameters (Synthetic)

**Version:** 1.0
**Publisher:** [Innovative Process Applications (IPA)](https://www.innovativeprocess.com)
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Contact:** Crestwood, IL, USA

> ⚠️ **This dataset is 100% synthetic and intended for educational use only.**
> It was generated from a published physical model (Johanson rolling theory + Heckel densification) — not measured on any real equipment, customer, or production batch. Do not use it for regulatory submissions, equipment validation, or commercial process design.

---

## What's in this dataset

600 simulated roller compaction runs on a representative pharmaceutical excipient blend (microcrystalline cellulose / lactose), spanning the operating envelope of a lab-to-pilot scale twin-feed-screw roller compactor.

| Column | Units | Description |
|---|---|---|
| `run_id` | — | Unique run identifier |
| `roll_force_kN_per_cm` | kN/cm | Specific roll force (normalized by roll width) |
| `roll_speed_rpm` | rpm | Roll rotation speed |
| `feed_screw_rpm` | rpm | Twin feed screw rotation speed |
| `roll_gap_mm` | mm | Target ribbon thickness / roll gap |
| `peak_pressure_MPa` | MPa | Computed peak nip pressure (Johanson) |
| `ribbon_rel_density` | — | Relative density (fraction of true density) |
| `ribbon_density_g_cc` | g/cc | Absolute ribbon density |
| `ribbon_porosity` | — | 1 − relative density |
| `density_CV_percent` | % | Across-width density coefficient of variation (uniformity) |
| `throughput_kg_hr` | kg/hr | Mass throughput |

## Realistic ranges (grounded in the literature)

The generator uses ranges consistent with published roller compaction studies on MCC/lactose blends:

- **Roll force:** 2–14 kN/cm (typical lab/pilot range)
- **Roll speed:** 1–12 rpm
- **Feed-to-roll speed ratio:** 3–30 (optimum ≈ 11 for twin feed screws on MCC)
- **Peak nip pressure:** ~30–200 MPa
- **Relative density:** 0.55–0.80 (ribbons below ~0.55 tend to crumble; above ~0.85 you over-compact and lose downstream granulation behavior)
- **Material:** true density 1.55 g/cc, bulk density 0.45 g/cc, Heckel K ≈ 0.018 MPa⁻¹

## Physical model

The synthetic data is generated from:

1. **Johanson rolling theory (1965)** — peak nip pressure as a function of roll force, gap, and roll geometry.
2. **Heckel equation** — relative density as a function of applied pressure: `ln(1/(1−D)) = K·P + A`.
3. **Twin feed screw effect** — a Gaussian optimality response centered on feed/roll ratio ≈ 11, penalizing both starved and over-fed nip conditions. This reflects IPA's twin-feed-screw design advantage for maintaining uniform nip feeding.
4. **Realistic measurement noise** (~1.5% on density, proportional noise on uniformity and throughput).

Full generator source is in `generate_dataset.py` — reproducible with seed 42.

## What you can teach with it

- **DOE / Response Surface Methodology:** fit a quadratic model to ribbon density as a function of roll force, roll speed, and feed screw speed.
- **Process optimization:** find the operating window that maximizes density while keeping CV% under a target (e.g., < 3%).
- **Regression & ML:** compare linear regression, random forests, and Gaussian processes on a small-but-physical dataset.
- **Quality-by-Design (QbD):** illustrate design space, critical process parameters (CPPs), and critical quality attributes (CQAs).

## Cross-links (other places to find this dataset)

- **Hugging Face Datasets:** https://huggingface.co/Innovative-Process-Applications
- **Zenodo (DOI):** https://zenodo.org/records/19636275
- **GitHub:** https://github.com/Innovative-Process-Applications
- **IPA website:** https://www.innovativeprocess.com
- **Kaggle:** https://www.kaggle.com/innovativeprocapps

## About IPA

Innovative Process Applications designs and manufactures twin-feed-screw roller compactors, mills, and size-reduction equipment for the pharmaceutical, nutraceutical, chemical, and food industries. Based in Crestwood, Illinois, IPA is a direct OEM alternative to legacy Fitzpatrick Chilsonator and FitzMill systems, with American manufacturing and direct engineer access. Learn more at [innovativeprocess.com](https://www.innovativeprocess.com).

## Citation

If you use this dataset in teaching, a notebook, a paper, or a blog post, please cite:

> Innovative Process Applications (2026). *Roller Compaction: Ribbon Density vs. Process Parameters (Synthetic), v1.0*. CC BY 4.0. https://www.innovativeprocess.com

## Version history

- **v1.0** (April 2026) — Initial release. 600 runs, 4 process parameters, 6 response variables.
