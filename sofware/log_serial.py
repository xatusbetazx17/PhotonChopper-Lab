# software/log_serial.py
# Read Arduino serial stream and save to CSV.
# Usage: python software/log_serial.py --port COM5 --baud 115200 --out data/run1.csv

import argparse, sys, time, csv
import serial

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", required=True, help="Serial port, e.g. COM5 or /dev/ttyUSB0")
    ap.add_argument("--baud", type=int, default=115200)
    ap.add_argument("--out", required=True, help="Output CSV path")
    args = ap.parse_args()

    ser = serial.Serial(args.port, args.baud, timeout=1)
    # wait for header
    print("Waiting for header...")
    header = ser.readline().decode(errors="ignore").strip()
    while "time_ms" not in header:
        if header:
            print(header)
        header = ser.readline().decode(errors="ignore").strip()
    print("Header:", header)

    with open(args.out, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header.split(","))
        print("Logging to", args.out)
        try:
            while True:
                line = ser.readline().decode(errors="ignore").strip()
                if not line:
                    continue
                writer.writerow(line.split(","))
        except KeyboardInterrupt:
            print("\nStopped.")

if __name__ == "__main__":
    main()
