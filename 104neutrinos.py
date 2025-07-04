#!/usr/bin/env python3
import sys
from math import sqrt

def update_number_of_values(current_count):
    return current_count + 1

def update_arithmetic_mean(old_mean, old_count, new_value):
    new_mean = (old_mean * old_count + new_value) / (old_count + 1)
    return new_mean

def update_harmonic_mean(old_mean, old_count, new_value):
    new_harmonic = old_count / old_mean + 1 / new_value
    new_harmonic = (old_count + 1) / new_harmonic
    return new_harmonic

def update_standard_deviation(old_mean, old_count, old_sd, new_value):
    sum_of_squares = (old_sd**2 * old_count) + (old_mean**2 * old_count)
    sum_of_squares += new_value**2
    new_mean = update_arithmetic_mean(old_mean, old_count, new_value)
    new_sum_of_squares = sum_of_squares - (new_mean**2 * (old_count + 1))
    new_sd = (new_sum_of_squares / (old_count + 1))**0.5
    return new_sd

def update_rms(old_rms, old_count, new_value):
    sum_of_squares = (old_rms ** 2) * old_count
    sum_of_squares += new_value ** 2
    mean_of_squares = sum_of_squares / (old_count + 1)
    new_rms = sqrt(mean_of_squares)
    return new_rms

def main():
    if len(sys.argv) != 5:
        print("USAGE")
        print("    ./104neutrinos n a h sd")
        print("\n")
        print("DESCRIPTION")
        print("    n       number of values")
        print("    a       arithmetic mean")
        print("    h       harmonic mean")
        print("    sd      standard deviation")
        sys.exit(84)

    try:
        # Initial values from command line arguments
        n = int(sys.argv[1])
        a = float(sys.argv[2])
        h = float(sys.argv[3])
        sd = float(sys.argv[4])
    except ValueError:
        print("Error: Invalid input values.")
        sys.exit(84)

    while True:
        user_input = input("Enter next value: ").strip()
        if user_input == "END":
            break

        try:
            new_value = float(user_input)
        except ValueError:
            print("Error: Invalid value. Please enter a number or 'END' to exit.")
            continue

        # Update values
        n = update_number_of_values(n)
        a = update_arithmetic_mean(a, n - 1, new_value)
        h = update_harmonic_mean(h, n - 1, new_value)
        sd = update_standard_deviation(a, n - 1, sd, new_value)
        rms = update_rms(h, n - 1, new_value)

        # Display updated values
        print(f"    Number of values:   {n}")
        print(f"    Standard deviation: {sd:.2f}")
        print(f"    Arithmetic mean:    {a:.2f}")
        print(f"    Root mean square:   {rms:.2f}")
        print(f"    Harmonic mean:      {h:.2f}")
        print("\n")

if __name__ == "__main__":
    main()
