# Write a program that asks the user to input the radius and height of two cylinders. Calculate and compare their volumes (use the formula `Volume = π * radius^2 * height`), and inform the user which cylinder has a larger volume, or if they are equal

import math

def calculate_volume(radius, height):
    return math.pi * radius**2 * height

def compare_volumes(radius1, height1, radius2, height2):
    volume1 = calculate_volume(radius1, height1)
    volume2 = calculate_volume(radius2, height2)

    if volume1 > volume2:
        print("Cylinder 1 has a larger volume.")
    elif volume1 < volume2:
        print("Cylinder 2 has a larger volume.")
    else:
        print("Both cylinders have equal volume.")

radius1 = float(input("Enter radius of cylinder 1: "))
height1 = float(input("Enter height of cylinder 1: "))
radius2 = float(input("Enter radius of cylinder 2: "))
height2 = float(input("Enter height of cylinder 2: "))

compare_volumes(radius1, height1, radius2, height2)
