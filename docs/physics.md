# Physics Notes — Fizeau Method

Let the rotor have **N** equally spaced **gaps** (≈ number of teeth), and let its rotation frequency be **f** (rev/s). The angular pitch is \(2\pi/N\). A **gap-to-tooth** angular advance is **half a pitch**, i.e. \(\pi/N\).

If the beam passes through a gap at \(t=0\), travels a one‑way distance **L**, reflects, and returns after time \(t_{rt} = 2L/c\), the return will be blocked when the wheel has advanced by half a pitch:

\[
2L/c = \frac{1}{2Nf} \quad \Rightarrow \quad c = 4\,L\,N\,f.
\]

This is the **first extinction** (k=0). Adding integer multiples of a full pitch (2π/N) gives the general set of extinctions:

\[
2L/c = \frac{2k+1}{2Nf} \quad \Rightarrow \quad f_k = \frac{(2k+1)\,c}{4\,L\,N},\; k=0,1,2,\dots
\]

Therefore, consecutive extinctions are separated by a **constant** frequency step:

\[
\Delta f = f_{k+1}-f_k = \frac{c}{2\,L\,N}.
\]

**Practical implications**
- Increasing **N** (more gaps) or **L** (longer path) **reduces the required RPM**, improving safety and accuracy.
- Using the **difference method** (two extinctions) cancels some systematic errors (sensor lag, slight duty mismatch, etc.).
- Beam size slightly larger than the gap helps obtain deep minima without clipping.
