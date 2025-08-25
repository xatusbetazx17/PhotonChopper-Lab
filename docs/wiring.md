# Wiring

## Tachometer (counts teeth)
- **Sensor**: TCRT5000 reflective IR sensor (or slotted opto)
- **Wiring (TCRT5000 module)**:
  - VCC → 5V
  - GND → GND
  - OUT → **D2** (Arduino external interrupt)
- Mount so each **tooth** edge produces one clean pulse per tooth. Adjust `PULSES_PER_REV` accordingly (usually = `N_GAPS`).

## Photodiode detector
- **Sensor**: BPW34 photodiode in reverse bias
- **Wiring**:
  - Photodiode anode → GND
  - Photodiode cathode → A0 through **100kΩ** to 5V (transimpedance‑style bias, simple version)
  - Read **A0** (0–1023). Higher = brighter.

> For best results build a proper transimpedance amplifier (OPA380 or LM358 single‑supply). Keep leads short; shield from ambient light.

## Optional: Mark button + LED
- Button between **D4** and **GND**; enable `INPUT_PULLUP` (active‑low).
- LED (with 220Ω) on **D13** to blink on extinction mark.

## Power
- Power the Arduino via USB.
- Power the BLDC/ESC from a battery or isolated supply.
- **Do not** power ESC from the Arduino’s 5V.
