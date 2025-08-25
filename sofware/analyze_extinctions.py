# software/analyze_extinctions.py
# Compute c from extinction RPMs using Fizeau relations.
# Examples:
#   python software/analyze_extinctions.py --L 1000 --N 300 --rpms 14980 15230 15510
#   python software/analyze_extinctions.py --L 1000 --N 300 --csv data/extinctions.csv

import argparse, sys, math, csv, statistics

def compute_c_from_first(L, N, f0):
    # c = 4 L N f0
    return 4.0 * L * N * f0

def compute_c_from_deltas(L, N, freqs):
    # consecutive differences should be constant: delta_f = c/(2 L N)
    # Use all consecutive pairs and average.
    deltas = [freqs[i+1]-freqs[i] for i in range(len(freqs)-1)]
    delta = statistics.mean(deltas)
    c_est = 2.0 * L * N * delta
    return c_est, deltas

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=float, required=True, help="One-way distance in meters")
    ap.add_argument("--N", type=int, required=True, help="Number of gaps (≈ teeth) in rotor")
    ap.add_argument("--rpms", type=float, nargs="*", help="Extinction RPM values (space-separated)")
    ap.add_argument("--csv", help="CSV file with RPM column named 'rpm' or 'RPM'")
    args = ap.parse_args()

    rpms = []
    if args.csv:
        with open(args.csv) as f:
            reader = csv.DictReader(f)
            for row in reader:
                for k in ("rpm","RPM","ext_rpm","extRPM"):
                    if k in row and row[k]:
                        rpms.append(float(row[k]))
                        break
    if args.rpms:
        rpms.extend(args.rpms)

    if not rpms:
        print("No RPM values given. Provide --rpms or --csv with a column named rpm/RPM.")
        sys.exit(1)

    # Convert RPM -> rev/s
    freqs = sorted([r/60.0 for r in rpms])
    f0 = freqs[0]

    c_first = compute_c_from_first(args.L, args.N, f0)
    c_delta, deltas = compute_c_from_deltas(args.L, args.N, freqs)

    print("Inputs: L = %.6f m, N = %d, extinctions = %s (RPM)" % (args.L, args.N, [round(r,2) for r in sorted(rpms)]))
    print("First-extinction estimate: c = %.6e m/s" % c_first)
    print("Delta-f method:           c = %.6e m/s" % c_delta)
    print("Consecutive Δf (Hz):", [round(d,4) for d in deltas])

    print("\nReference value: 2.99792458e8 m/s")
    print("Relative error (first): %.4f%%" % (100*(c_first/2.99792458e8 - 1.0)))
    print("Relative error (delta): %.4f%%" % (100*(c_delta/2.99792458e8 - 1.0)))

if __name__ == "__main__":
    main()
