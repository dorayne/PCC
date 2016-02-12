'''
Assignment: Get 3 triangle sides, return the 3 angles and the area of the triangle.
All error checking is done in loops such that the program will loop indefinitely
until a valid triangle is entered.
'''

import math

def float_test(test):
    # verify input is a number
    try:
        float(test)
        return True
    except:
        print "Invalid input, please try again and enter a number\n"
        return False

def positive_test(n):
    # verify input is a positive number
    if float(n) > 0:
        return True
    else:
        print "Invalid input, please try again and enter a positive number.\n"
        return False

def triangle_exist(a, b, c):
    # verifies if the given sides will form a triangle using the Triangle Inequality Theorem
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True
    else:
        print "The sides entered do not form a triangle. Please try again with different sides.\n"
        return False

def area_tri(a, b, c):
    # get the area of the triangle using Heron's formula
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - a) * (p - a)), 2
    return area

def rad_to_deg(rad):
    # convert radians to degrees
    deg = rad * (180 / math.pi)
    return deg

def solve_angle_A(a, b, c):
    # get angle A using the Law of Cosines
    rad_A = math.acos((a * a - b * b - c * c) / (-2 * b * c))
    return rad_A

def solve_angle_B(a, b, c):
    # get angle B using the Law of Cosines
    rad_B = math.acos((b * b - a * a - c * c) / (-2 * a * c))
    return rad_B

def solve_angle_C(a, b, c):
    # get angle C using the Law of Cosines
    rad_C = math.acos((c * c - a * a - b * b) / (-2 * a * b))
    return rad_C

def get_input():
    # get user input for the 3 sides
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
    side_a, side_b, side_c = get_input()
    if triangle_exist(side_a, side_b, side_c):
        break

area = round(area_tri(side_a, side_b, side_c), 2)

rad_A = solve_angle_A(side_a, side_b, side_c)
deg_A = round(rad_to_deg(rad_A), 2)

rad_B = solve_angle_B(side_a, side_b, side_c)
deg_B = round(rad_to_deg(rad_B), 2)

rad_C = solve_angle_C(side_a, side_b, side_c)
deg_C = round(rad_to_deg(rad_C), 2)

print "\nThe lengths of the sides of the triangle are %r, %r, and %r" % (side_a, side_b, side_c)
print "The area of the triangle is %r square units" % (area)
print "The angles of the triangle in degrees are %r, %r, and %r" %(deg_A, deg_B, deg_C)