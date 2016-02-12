"""
Assignment: Get 3 triangle sides, return the 3 angles and the area of the triangle.
All error checking is done in loops such that the program will loop indefinitely
until a valid triangle is entered.
"""

import math

def float_test(test):
    """verify input is a number"""
#    try:
    float(test)
    return True
#    except:
    print "Invalid input, please try again and enter a number\n"
    return False

def positive_test(num):
    """verify input is a positive number"""
    if float(num) > 0:
        return True
    else:
        print "Invalid input, please try again and enter a positive number.\n"
        return False

def triangle_exist(side_a, side_b, side_c):
    """verify if the given sides will form a triangle using the Triangle Inequality Theorem"""
    if (side_a + side_b) > side_c and (side_b + side_c) > side_a and (side_a + side_c) > side_b:
        return True
    else:
        print "The sides entered do not form a triangle. Please try again with different sides.\n"
        return False

def area_tri(side_a, side_b, side_c):
    """get the area of the triangle using Heron's formula"""
    hlf_perim = (side_a + side_b + side_c) / 2
    area = math.sqrt(hlf_perim * (hlf_perim - side_a) * (hlf_perim - side_b) * (hlf_perim - side_c))
    return area

def rad_to_deg(rad):
    """convert radians to degrees"""
    deg = rad * (180 / math.pi)
    return deg

def solve_angle_1(side_a, side_b, side_c):
    """get angle A using the Law of Cosines"""
    rad_1 = math.acos((side_a ** 2 - side_b ** 2 - side_c ** 2) / (-2 * side_b * side_c))
    return rad_1

def solve_angle_2(side_a, side_b, side_c):
    """get angle B using the Law of Cosines"""
    rad_2 = math.acos((side_b ** 2 - side_a ** 2 - side_c ** 2) / (-2 * side_a * side_c))
    return rad_2

def solve_angle_3(side_a, side_b, side_c):
    """get angle C using the Law of Cosines"""
    rad_3 = math.acos((side_c ** 2 - side_a ** 2 - side_b ** 2) / (-2 * side_a * side_b))
    return rad_3

def get_input():
    """get user input for the 3 sides"""
    while True:
        raw_a = raw_input("Enter the length of first side of a triangle \n")
        if float_test(raw_a):
            if positive_test(raw_a):
                break
    while True:
        raw_b = raw_input("Enter the length of second side of a triangle \n")
        if float_test(raw_b):
            if positive_test(raw_b):
                break
    while True:
        raw_c = raw_input("Enter the length of third side of a triangle \n")
        if float_test(raw_c):
            if positive_test(raw_c):
                break
    return (float(raw_a), float(raw_b), float(raw_c))

while True:
    SIDE_A, SIDE_B, SIDE_C = get_input()
    if triangle_exist(SIDE_A, SIDE_B, SIDE_C):
        break

AREA = round(area_tri(SIDE_A, SIDE_B, SIDE_C), 2)

RAD_1 = solve_angle_1(SIDE_A, SIDE_B, SIDE_C)
DEG_1 = round(rad_to_deg(RAD_1), 2)

RAD_2 = solve_angle_2(SIDE_A, SIDE_B, SIDE_C)
DEG_2 = round(rad_to_deg(RAD_2), 2)

RAD_3 = solve_angle_3(SIDE_A, SIDE_B, SIDE_C)
DEG_3 = round(rad_to_deg(RAD_3), 2)

print "\nThe lengths of the sides of the triangle are %r, %r, and %r" % (SIDE_A, SIDE_B, SIDE_C)
print "The area of the triangle is %r square units" % (AREA)
print "The angles of the triangle in degrees are %r, %r, and %r" %(DEG_1, DEG_2, DEG_3)
