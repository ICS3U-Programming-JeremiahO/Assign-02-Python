#!/usr/bin/env python3
# Created by: Jeremiah omoike
# Created on: October 2 2022
# This program asks the user for the length,
# width and height of the rectangular prism in cm. It then
# calculates and displays the surface area and
# Volume .
from cmath import sqrt
import math
from re import A
from tokenize import Exponent


def main():
    # input
    # User inputed the length, width and height
    print("Today we will calculate the surface area and")
    print("volume of a rectangular prism")
    length = int(input("Enter the length (cm): "))
    width = int(input("Enter the width (cm): "))
    height = int(input("Enter the height (cm): "))
    surface_area_part_A = length * width + length * math.sqrt(
        (width / 2) * (width / 2) + height * height
    )
    surface_area_part_B = width * math.sqrt(
        (length / 2) * (length / 2) + height * height
    )
    # process
    # calculate the surface area and volume
    Surfacearea = surface_area_part_A + surface_area_part_B

    volume = length * width * height / 3

    # output
    # display the Surface area and volume 
    print("")
    print("Surfacearea = {} cm^2".format(Surfacearea))
    print("Volume = {} cm^3".format(volume))


if __name__ == "__main__":
    main()
