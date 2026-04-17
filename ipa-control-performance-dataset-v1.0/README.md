# Roll Compactor Control Performance: PID Tuning & Process Stability (Synthetic)

**Version:** 1.0
**Publisher:** [Innovative Process Applications (IPA)](https://www.innovativeprocess.com)
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Contact:** Crestwood, IL, USA

> **This dataset is 100% synthetic and intended for educational use only.**
> It was generated from PID control theory applied to roll compaction process
> dynamics — not measured on any real equipment, customer, or production batch.

---

## What's in this dataset

Two linked files containing synthetic roll compaction process control data:

### 1. Summary file: `control_performance_summary_v1.0.csv` (96 runs × 22 columns)

Each row is one 3-minute compaction run with computed control metrics.

| Column | Description |
|---|---|
| `run_id` | Unique run identifier |
| `control_architecture` | Control strategy identifier |
| `control_label` | Human-readable control description |
| `feed_type` | Single screw or twin screw |
| `has_scf_pid` / `has_gw_pid` | Whether PID control is active for SCF / gap width |
| `material` | Model material (MCC_101, Mannitol_SD, MCC_Mannitol_Mix) |
| `scenario` | Setpoint change scenario (step up, step down, simultaneous, etc.) |
| `scf_setpoint_kN_per_cm` | Target specific compaction force |
| `gw_setpoint_mm` | Target gap width |
| `scf_ss_mean` / `scf_ss_std` / `scf_ss_cv_pct` | Steady-state SCF statistics |
| `scf_deviation_from_setpoint_pct` | Steady-state deviation from target (%) |
| `scf_settling_time_s` | Time to reach ±2% of setpoint after change |
| `scf_overshoot_pct` | Peak overshoot above setpoint (%) |
| `gw_ss_mean_mm` / `gw_ss_std_mm` / `gw_ss_cv_pct` | Steady-state gap width statistics |
| `gw_deviation_from_setpoint_pct` | Gap width deviation from target (%) |
| `gw_settling_time_s` | Gap width settling time |
| `control_quality_grade` | Overall grade: Excellent / Good / Acceptable / Poor |

### 2. Time-series file: `control_performance_timeseries_v1.0.csv` (8,640 rows × 8 columns)

Actual process data sampled every 2 seconds for each run (90 timepoints × 96 runs).

| Column | Description |
|---|---|
| `run_id` | Links to summary table |
| `time_s` | Timestamp in seconds (0–180) |
| `scf_setpoint_kN_per_cm` | Current SCF setpoint (changes at t=30s) |
| `scf_actual_kN_per_cm` | Measured SCF value |
| `gw_setpoint_mm` | Current gap width setpoint |
| `gw_actual_mm` | Measured gap width |
| `roll_speed_rpm` | Roll rotation speed |
| `screw_speed_rpm` | Feed screw speed (adapts if GW PID is active) |

## Scientific basis

The dataset models PID control behavior as described in:

> Szappanos-Csordás, K. (2018). *Impact of material properties, process parameters
> and roll compactor design on roll compaction.* Chapter 3.1: Control performance
> of the different types of roll compactors. Heinrich-Heine-Universität Düsseldorf.

Key concepts from Section 3.1 modeled here:

1. **Four control architectures** of increasing sophistication:
   - No gap control (hydraulic pressure setpoint only) — highest variability
   - PID with gap width + screw speed control — moderate performance
   - PID with SCF + gap width control — good performance
   - PID with SCF + gap width + twin feed screw — best performance

2. **PID controller dynamics:** Proportional, Integral, and Derivative terms
   producing characteristic overshoot, oscillation, and settling behavior.
   Without PID (no gap control), the system shows steady-state offset because
   there is no integral term to eliminate it.

3. **Settling time:** Time required after a setpoint change for the process to
   stabilize within ±2% of the new setpoint. Varies by control architecture,
   material properties, and magnitude of the setpoint change.

4. **Coefficient of variation (CV%):** Ratio of standard deviation to mean during
   steady-state production. Lower CV indicates more robust process control.
   The dissertation reports CV values from ~0.8% (best) to ~3.6% (no control).

5. **Material-dependent control difficulty:** Brittle materials (mannitol)
   produce more erratic force signals due to particle fragmentation, making
   control harder. Plastic materials (MCC) compact more smoothly.

6. **Twin feed screw advantage:** Reduces feed rate fluctuations, lowering both
   SCF and gap width variability — a key differentiator in IPA's CL-series
   compactor design.

7. **Setpoint change scenarios:** Step increases, step decreases, and simultaneous
   changes in SCF and gap width — mirroring the experimental protocol in the
   dissertation's Tables 2–3.

## What you can teach with it

- **PID controller tuning:** Examine overshoot, settling time, and steady-state
  error across different control architectures
- **Statistical Process Control (SPC):** Build control charts, calculate Cp/Cpk,
  identify out-of-control conditions
- **Time-series analysis:** Apply filtering, spectral analysis, or change-point
  detection to the process signals
- **Control architecture comparison:** Quantify the value of closed-loop PID
  control vs. open-loop hydraulic setpoint
- **Material effects on controllability:** Compare control performance across
  plastic, brittle, and mixed deformation materials
- **Classification:** Train models to predict control quality grade from
  time-series features

## Cross-links (also published on)

- **Hugging Face Datasets:** https://huggingface.co/Innovative-Process-Applications
- **Zenodo (DOI):** https://zenodo.org/records/19636275
- **GitHub:** https://github.com/Innovative-Process-Applications
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

> Innovative Process Applications (2026). *Roll Compactor Control Performance:
> PID Tuning & Process Stability (Synthetic), v1.0*. CC BY 4.0.
> https://www.innovativeprocess.com

Scientific basis:

> Szappanos-Csordás, K. (2018). *Impact of material properties, process
> parameters and roll compactor design on roll compaction.* Doctoral dissertation,
> Heinrich-Heine-Universität Düsseldorf.

## Version history

- **v1.0** (April 2026) — Initial release. 96 runs, 4 control architectures,
  3 materials, 8 scenarios. Summary + time-series files.
