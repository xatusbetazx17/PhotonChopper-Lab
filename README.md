# PhotonChopper‑Lab
Measure the speed of light **c** using a rotating chopper ring (Fizeau method) built around a rigid version of Marcelo’s corrugated‑ring shape.

> ⚠️ **Safety first**: Spinning rotors and laser beams can injure. Use an acrylic guard, keep hands away, wear wavelength‑rated laser goggles, and secure all parts before spin‑up.

---

## What this repo gives you
- **Hardware**: Parametric OpenSCAD model of a scalloped/slotted rotor based on the corrugated ring shape, ready for 3D‑printing or laser cutting.
- **Electronics**: Minimal, breadboard‑friendly schematic and wiring table for an RPM sensor and a photodiode detector.
- **Firmware (Arduino)**: Logs RPM and photodiode intensity to serial; optional button to mark an extinction.
- **Software (Python)**:
  - `log_serial.py` – save Arduino serial data to CSV.
  - `analyze_extinctions.py` – compute **c** from recorded extinction RPMs and your geometry.
  - `plot_log.py` – plot RPM vs. photodiode level to visualize extinctions.
- **Docs**: Bill of materials, assembly steps, and physics notes.
- **License**: MIT.

This project implements the classic **Fizeau** rotating‑wheel measurement: a beam passes through a gap in a rotating ring, travels to a distant mirror, returns, and is blocked when the ring advances by half a pitch during the round‑trip time.

### Core equations
With **N** gaps (≈ number of teeth) and rotation frequency **f** (rev/s), the first extinction occurs when
\(
\displaystyle c = 4\,L\,N\,f
\)
where **L** is the one‑way distance (meters).

More generally, extinctions occur at
\(
\displaystyle f_k = \frac{(2k+1)\,c}{4\,L\,N},\;\;k=0,1,2,\dots
\)
so the **difference** between consecutive extinctions is constant:
\(
\displaystyle \Delta f = f_{k+1}-f_k = \frac{c}{2\,L\,N}.
\)

Use either the **first extinction** or the **difference method** to estimate **c**.

---

## Quick start

### 1) Build the rotor (your corrugated‑ring aesthetic, but rigid)
- Open `hardware/openscad/rotor.scad` in **OpenSCAD**.
- Set parameters: outer/inner diameter, thickness, number of **teeth** (gaps), hub size.
- `F6` to render, then **Export as STL** (3D print) or **DXF** (laser‑cut).

### 2) Wire electronics
See `docs/wiring.md` for a clear diagram and table. You’ll connect:
- **IR/optical sensor** → tachometer input (counts teeth).
- **Photodiode + resistor** → analog input (beam intensity).
- **Optional button** → mark an extinction when you observe a deep minimum.
- **Brushless motor/ESC** or a variable‑speed drill press/lathe as the driver (guard it!).

### 3) Flash the Arduino
- Open `firmware/arduino/FizeauLogger/FizeauLogger.ino` in Arduino IDE.
- Set `PULSES_PER_REV` and `N_GAPS` in the top defines to match your rotor and sensor.
- Upload; open Serial Monitor to verify streaming RPM and photodiode values.

### 4) Log and analyze
- Install Python requirements: `pip install -r software/requirements.txt`
- Run the logger: `python software/log_serial.py --port COM5 --baud 115200 --out data/run1.csv`
- Spin the rotor slowly upward. Each time you see a deep minimum in the photodiode trace (or hear the buzzer/LED cue), press the **Mark** button or note the RPM.
- Compute **c** using:  
  `python software/analyze_extinctions.py --L 1000 --N 300 --rpms 14980 15230`  
  or with a CSV of marked events:
  `python software/analyze_extinctions.py --L 1000 --N 300 --csv data/extinctions.csv`

### 5) Plot (optional)
`python software/plot_log.py data/run1.csv`

---

## Why your original foil ring can’t be a motor (but works as a *shape*)
Motors need a rigid rotor, stator coils, bearings, and balanced geometry. Your crimped foil ring is a **great aesthetic** for a **scalloped/slotted rotor** used as an **optical chopper**. Here we upgrade it into a precise, safe, balanced disk you can actually spin and measure with.

If you prefer to build a true **brushless motor** with this aesthetic, see `docs/brushless‑variant.md` for a roadmap (stator, magnets, controller). That path is optional—**the Fizeau measurement doesn’t require it**.

---

## Legal & safety
- MIT License. Build/use at your own risk.
- Follow your local laser regulations. Use rated eyewear.
- Guard the rotor completely; stand clear on first spin‑ups; ramp speed slowly.

---

## Credits
- Project concept & structure: based on discussions with **Marcelo Collado** (corrugated ring → rigid scalloped rotor for Fizeau measurement).
- Classical method credited to Hippolyte Fizeau (1849); modernized here for maker‑grade tools.
