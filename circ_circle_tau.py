#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Sep 28, 2023
# This program asks the user for the radius of
# a circle in mm. It then calculates and displays
# the circumference using tau.
import constants


def main():
    # get the radius from the user
    radius = float(input("Enter the radius (mm): "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("Circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()
