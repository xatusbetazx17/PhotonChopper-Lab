# software/plot_log.py
# Plot RPM and photodiode signal from a log CSV.
# Usage: python software/plot_log.py data/run1.csv

import sys, pandas as pd, matplotlib.pyplot as plt

def main():
    if len(sys.argv) < 2:
        print("Usage: python software/plot_log.py data/run1.csv")
        sys.exit(1)
    df = pd.read_csv(sys.argv[1])
    # basic cleanup
    df['time_s'] = df['time_ms'] / 1000.0
    fig1 = plt.figure()
    plt.plot(df['time_s'], df['photo'])
    plt.xlabel("Time (s)")
    plt.ylabel("Photodiode level (A0)")
    plt.title("Beam intensity")
    fig2 = plt.figure()
    plt.plot(df['time_s'], df['rpm'])
    plt.xlabel("Time (s)")
    plt.ylabel("RPM")
    plt.title("Rotor speed")
    plt.show()

if __name__ == "__main__":
    main()
