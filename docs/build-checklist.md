# Build & Test Checklist

## 0) Plan geometry
- Choose **N** (gaps) so the first extinction sits within your reachable RPM:
  - `f0 = c/(4 L N)` → `RPM0 = 60 f0`
  - Example: `L=1000 m`, `N=300` → `f0 ≈ 250 Hz`, `RPM0 ≈ 15,000`

## 1) Make rotor
- Open `hardware/openscad/rotor.scad`, set diameters/thickness and `N_teeth`.
- Export STL (3D‑print PETG/PLA, 2–3 mm thick) or DXF (laser‑cut).
- Deburr; balance with tiny tape dots.

## 2) Drive
- Mount on a collet or motor shaft with a printed hub.
- Full **clear acrylic shroud** around the disk.
- Slowly ramp speed; listen/feel for vibration.

## 3) Optics
- Laser pointer (≤5mW) and front‑surface mirror.
- Align so beam passes through a **gap**, travels distance **L**, and returns through the same angular slot position onto the **photodiode**.

## 4) Electronics
- Wire per `docs/wiring.md`.
- Flash Arduino with `firmware/arduino/FizeauLogger/FizeauLogger.ino`.
- Verify serial stream in Arduino Serial Monitor.

## 5) Run
- Start logging: `python software/log_serial.py --port COMx --out data/run1.csv`.
- Increase RPM slowly. At each deep minimum in the photodiode signal, press the **Mark** button and note the RPM displayed.
- Save the extinction RPMs into `data/extinctions.csv` or pass them on the command line.

## 6) Compute **c**
- `python software/analyze_extinctions.py --L <meters> --N <gaps> --csv data/extinctions.csv`
- Compare to `2.9979e8 m/s`. Use larger **L** and better balancing for accuracy.

## 7) Troubleshooting
- **No clear minima**: enlarge beam slightly; improve alignment; reduce ambient light; add smaller aperture before the photodiode.
- **Noisy tach**: move sensor closer; add Schmitt trigger; average over 0.2–0.5 s.
- **RPM too low**: increase **N**, increase **L**, or upgrade drive.
