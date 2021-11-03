#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This program will calculate area of decagon

from math import sqrt


def main():
    # main function
    print("We will be calculating the area of a decagon.")
    # input
    length = int(input("Enter the length of one side (mm): "))

    # process
    area = round((5 / 2) * pow(length, 2) * (sqrt(5 + 2 * sqrt(5))), 2)

    # output
    print(f"Area is {area} mm²")

    # output finished
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
