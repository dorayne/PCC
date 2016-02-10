# get user input for 3 triangle sides
# print the area of the triangle as well as the 3 angles

import math

def error_check(test):
    # convert input to float, exit program if input is not a number
    try:
        tested = float(test)
        return tested
    except:
        print "Invalid input, please try again and enter a whole number"
        exit()

def triangle_exist(a, b, c):
    # determines if the given sides will form a triangle using the Triangle Inequality Theorem
    # program will exit if the triangle does not exist
    if (a + b) > c and (b + c) > a and (a + c) > b:
        print "The sides entered form a triangle"
    else:
        print "The sides entered do not form a triangle. Please try again with different sides."
        exit()

def area_tri(x, y, z):
    # get the area of the triangle using Heron's formula
    global area
    perim = (x + y + z)
    p = perim/2
    area = round(math.sqrt(p * (p - x) * (p - y) * (p - z)), 2)
    return area
    
def rad_to_deg(rad):
    # conver radians to degrees
    deg = rad * (180 / math.pi)
    return deg

def solve_angle_A(a, b, c):
    # get angle A using the Law of Cosines
    global rad_A
    cos_A = (a * a - b * b - c * c) / (-2 * b * c)
    rad_A = math.acos(cos_A)
    return rad_A

def solve_angle_B(a, b, c):
    # get angle B using the Law of Cosines
    global rad_B
    cos_B = (b * b - a * a - c * c) / (-2 * a * c)
    rad_B = math.acos(cos_B)
    return rad_B

def solve_angle_C(a, b, c):
    # get angle C using the Law of Cosines
    global rad_C
    cos_C = (c * c - a * a - b * b) / (-2 * a * b)
    rad_C = math.acos(cos_C)
    return rad_C

# get user input for the 3 sides
a = raw_input("Enter the length of first side of a triangle \n")
if len(a) > 0:
    side_a = error_check(a)
b = raw_input("Enter the length of second side of a triangle \n")
if len(b) > 0:
    side_b = error_check(b)
c = raw_input("Enter the length of third side of a triangle \n")
if len(c) > 0:
    side_c = error_check(c)

triangle_exist(side_a, side_b, side_c)

area_tri(side_a, side_b, side_c)

solve_angle_A(side_a, side_b, side_c)
deg_A = round(rad_to_deg(rad_A), 2)

solve_angle_B(side_a, side_b, side_c)
deg_B = round(rad_to_deg(rad_B), 2)

solve_angle_C(side_a, side_b, side_c)
deg_C = round(rad_to_deg(rad_C), 2)


print "The lengths of the sides of the triangle are %d, %d, and %d" % (side_a, side_b, side_c)
print "The area of the triangle is %r" % (area)
print "The angles of the triangle in degrees are %r, %r, and %r" %(deg_A, deg_B, deg_C)