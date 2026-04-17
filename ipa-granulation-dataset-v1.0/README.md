# Dry Granulation: Multi-Material Roll Compaction & Milling (Synthetic)

**Version:** 1.0
**Publisher:** [Innovative Process Applications (IPA)](https://www.innovativeprocess.com)
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Contact:** Crestwood, IL, USA

> ⚠️ **This dataset is 100% synthetic and intended for educational use only.**
> It was generated from published physical models and real compactor specifications —
> not measured on any real equipment, customer, or production batch. Do not use it for
> regulatory submissions, equipment validation, or commercial process design.

---

## What's in this dataset

720 simulated dry granulation runs across three pharmaceutical model materials,
three roll compactor geometries, two sealing systems, and two roll surfaces —
spanning the full multi-factor design space described in the granulation
literature.

### Process inputs (what you control)

| Column | Units | Description |
|---|---|---|
| `run_id` | — | Unique run identifier |
| `material` | — | Model material: MCC_101, Mannitol_SD, or MCC_Mannitol_Mix |
| `deformation_type` | — | Material deformation class: plastic, brittle, or mixed |
| `true_density_gcc` | g/cc | True (helium) density of the material |
| `compactor_config` | — | Machine geometry label (roll diameter × width) |
| `roll_diameter_mm` | mm | Roll diameter (120 or 250 mm — from published specs) |
| `roll_width_mm` | mm | Roll width (25 or 30 mm) |
| `sealing_system` | — | Side-sealing or rim-rolls |
| `roll_surface` | — | Smooth or knurled |
| `scf_kN_per_cm` | kN/cm | Specific compaction force |
| `gap_width_mm` | mm | Set gap width |
| `roll_speed_rpm` | rpm | Roll rotation speed |
| `feed_screw_rpm` | rpm | Feed screw speed |

### Intermediate physics (what the machine does)

| Column | Units | Description |
|---|---|---|
| `densification_factor` | — | DF = drawn-in width / gap width (scales with roll diameter) |
| `nip_angle_deg` | ° | Computed nip angle (depends on surface, friction, feed ratio) |
| `peak_pressure_MPa` | MPa | Estimated peak nip pressure |

### Quality responses (what you measure)

| Column | Units | Description |
|---|---|---|
| `ribbon_rel_density` | — | Relative density (fraction of true density) |
| `ribbon_density_gcc` | g/cc | Absolute ribbon density |
| `ribbon_porosity` | — | 1 − relative density |
| `density_CV_percent` | % | Across-width density coefficient of variation (uniformity) |
| `in_zinchuk_window` | Yes/No | Is ribbon RD in the 0.60–0.80 range for downstream tabletability? |
| `fines_fraction_pct` | % | Fraction of granules < 100 µm after milling (fines) |
| `granule_d50_um` | µm | Median granule size after oscillating mill |
| `throughput_kg_hr` | kg/hr | Mass throughput |

## Scientific basis

The physical model is grounded in the granulation fundamentals described in:

> Szappanos-Csordás, K. (2018). *Impact of material properties, process parameters
> and roll compactor design on roll compaction.* Doctoral dissertation,
> Heinrich-Heine-Universität Düsseldorf.

Key concepts from Chapter 1 modeled here:

1. **Three material deformation classes:** MCC 101 (plastic), spray-dried mannitol
   (brittle), and their 1:1 mixture — the same model materials used in the
   dissertation's experimental design.

2. **Densification factor (DF):** DF = DW/GW increases with roll diameter
   (Equations 1–3 in the dissertation). Larger rolls → wider drawn-in width →
   higher densification at the same gap setting.

3. **Nip angle dependency:** knurled roll surfaces and higher material friction
   coefficients produce larger nip angles and therefore higher densification.
   Smooth rolls and lubricants decrease the nip angle.

4. **Roll speed / dwell-time sensitivity:** Plastic materials (MCC) are highly
   sensitive to roll speed — fast rolls reduce dwell time and ribbon density.
   Brittle materials (mannitol) show negligible roll speed sensitivity because
   particle fragmentation is rapid.

5. **Sealing system effect:** Rim-roll sealing produces more uniform ribbon density
   (lower CV%) and fewer fines compared to side-sealing plates.

6. **Zinchuk tabletability criterion:** Ribbons with relative density between
   0.60–0.80 produce granules with appropriate characteristics for tableting.
   Below 0.60, ribbons are too weak; above 0.80, loss of compactibility occurs.

7. **Fines fraction:** Inversely related to ribbon density. Brittle materials
   produce more fines upon milling. Rim-roll sealing reduces bypass fines.

Machine specifications (roll diameters, widths, SCF ranges, sealing systems)
are drawn from Table 1 of the dissertation, which catalogs real laboratory-scale
roll compactors from multiple manufacturers.

The generator adds realistic measurement noise (±1.2% on ribbon density, ±0.5%
on CV, ±2% on fines, ±25 µm on d50). Full generator source is in
`generate_dataset.py` — reproducible with seed 2026.

## What you can teach with it

- **Multi-factor DOE:** analyze main effects and interactions of material type,
  machine design, and process parameters on ribbon and granule quality
- **Material science:** compare brittle vs. plastic deformation behavior and
  their consequences for compaction and milling
- **Machine design selection:** quantify the effect of roll diameter, sealing
  system, and roll surface on product quality
- **Quality-by-Design (QbD):** define a design space that meets the Zinchuk
  criterion while minimizing fines and maximizing throughput
- **Classification & clustering:** build classifiers for the Zinchuk window or
  cluster runs by quality profile
- **Scale-up reasoning:** use the densification factor relationship to reason
  about transferring processes between 120 mm and 250 mm roll compactors

## Cross-links (also published on)

- **Hugging Face Datasets:** https://huggingface.co/Innovative-Process-Applications
- **Zenodo (DOI):** https://zenodo.org/records/19636275
- **GitHub:** c
- **IPA website:** https://www.innovativeprocess.com
- **Kaggle:** https://www.kaggle.com/innovativeprocapps

## About IPA

Innovative Process Applications designs and manufactures twin-feed-screw roller
compactors, mills, and size-reduction equipment for the pharmaceutical,
nutraceutical, chemical, and food industries. Based in Crestwood, Illinois, IPA
is a direct OEM alternative to legacy Fitzpatrick Chilsonator and FitzMill
systems, with American manufacturing and direct engineer access. Learn more at
[innovativeprocess.com](https://www.innovativeprocess.com).

## Citation

If you use this dataset in teaching, a notebook, a paper, or a blog post, please cite:

> Innovative Process Applications (2026). *Dry Granulation: Multi-Material Roll
> Compaction & Milling (Synthetic), v1.0*. CC BY 4.0.
> https://www.innovativeprocess.com

Scientific basis:

> Szappanos-Csordás, K. (2018). *Impact of material properties, process
> parameters and roll compactor design on roll compaction.* Doctoral dissertation,
> Heinrich-Heine-Universität Düsseldorf.

## Version history

- **v1.0** (April 2026) — Initial release. 720 runs, 24 columns, 3 materials,
  3 compactor geometries, 2 sealing systems, 2 roll surfaces.
