# Brushless Variant (Optional Roadmap)

If you want to turn the aesthetic into an actual **BLDC motor** (educational project):

## Rotor
- Use the scalloped **outer rim** from `rotor.scad` purely as a cosmetic shroud.
- Real rotor: steel sleeve or 3D‑printed carrier with **NdFeB magnets** (e.g., 14‑pole, 12‑slot stator).
- Epoxy magnets with proper indexing; add a carbon/Kevlar wrap for retention.

## Stator
- Re‑use a COTS stator (from an RC outrunner) **or** wind your own (12‑slot, 3‑phase ABCABC).
- Drive with a hobby **ESC** for first spins.

## Control
- Start sensorless (ESC). For custom control, add 3 Hall sensors or back‑EMF observer.

## Safety
- Magnet retention and clearances are critical. Always shroud the rotor.

This path is completely **optional** for the Fizeau experiment (which only needs a driver to spin the chopper).