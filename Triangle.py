'''
Assignment: Get 3 triangle sides, return the 3 angles and the area of the triangle.
All error checking is done in loops such that the program will loop indefinitely
until a valid triangle is entered.
'''

import math

def error_change_float(test):
    # convert input to float
    try:
        tested = float(test)
        return tested
    except:
        print "Invalid input, please try again and enter a number\n"
        return False

def error_pos_num(num):
    # verify that input is a positive number
    if num > 0:
        return num
    else:
        print "Invalid input, please try again and enter a positive number.\n"
        return False

def error_triangle_exist(a, b, c):
    # determines if the given sides will form a triangle using the Triangle Inequality Theorem
    global exists
    if (a + b) > c and (b + c) > a and (a + c) > b:
        exists = True
        return a, b, c, exists
    else:
        print "The sides entered do not form a triangle. Please try again with different sides.\n"
        exists = False
        get_input()
        return exists

def area_tri(x, y, z):
    # get the area of the triangle using Heron's formula
    global area
    perim = x + y + z
    p = perim/2
    area = round(math.sqrt(p * (p - x) * (p - y) * (p - z)), 2)
    return area
    
def rad_to_deg(rad):
    # convert radians to degrees
    deg = rad * (180 / math.pi)
    return deg

def solve_angle_A(a, b, c):
    # get angle A using the Law of Cosines
    global rad_A
    rad_A = math.acos((a * a - b * b - c * c) / (-2 * b * c))
    return rad_A

def solve_angle_B(a, b, c):
    # get angle B using the Law of Cosines
    global rad_B
    rad_B = math.acos((b * b - a * a - c * c) / (-2 * a * c))
    return rad_B

def solve_angle_C(a, b, c):
    # get angle C using the Law of Cosines
    global rad_C
    rad_C = math.acos((c * c - a * a - b * b) / (-2 * a * b))
    return rad_C
    
def get_input():
    # get user input for the 3 sides
    global side_a, side_b, side_c
    while True:
        raw_a = raw_input("Enter the length of first side of a triangle \n")
        side_a = error_pos_num(error_change_float(raw_a))
        if side_a:
            break

    while True:
        raw_b = raw_input("Enter the length of second side of a triangle \n")
        side_b = error_pos_num(error_change_float(raw_b))
        if side_b:
            break

    while True:
        raw_c = raw_input("Enter the length of third side of a triangle \n")
        side_c = error_pos_num(error_change_float(raw_c))
        if side_c:
            break

get_input()

while True:
    error_triangle_exist(side_a, side_b, side_c)
    if exists:
        break

area_tri(side_a, side_b, side_c)

solve_angle_A(side_a, side_b, side_c)
deg_A = round(rad_to_deg(rad_A), 2)

solve_angle_B(side_a, side_b, side_c)
deg_B = round(rad_to_deg(rad_B), 2)

solve_angle_C(side_a, side_b, side_c)
deg_C = round(rad_to_deg(rad_C), 2)


print "The lengths of the sides of the triangle are %d, %d, and %d" % (side_a, side_b, side_c)
print "The area of the triangle is %r square units" % (area)
print "The angles of the triangle in degrees are %r, %r, and %r" %(deg_A, deg_B, deg_C)