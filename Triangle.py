# get user input for 3 triangle sides
# print the area of the triangle as well as the 3 angles

import math

def error_check(test):
    # convert input to integer, exit program if input is not a number
    try:
        tested = float(test)
        return tested
    except:
        print "Invalid input, please try again and enter a whole number"
        exit()

def area_tri(x, y, z):
    # get the area of the triangle using Heron's formula
    global area
    perim = (x + y + z)
    p = float(perim/2)
    area = float(math.sqrt(p * (p - x) * (p - y) * (p - z)))
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

area_tri(side_a, side_b, side_c)

solve_angle_A(side_a, side_b, side_c)
deg_A = rad_to_deg(rad_A)

solve_angle_B(side_a, side_b, side_c)
deg_B = rad_to_deg(rad_B)

solve_angle_C(side_a, side_b, side_c)
deg_C = rad_to_deg(rad_C)


print "The lengths of the sides of the triangle are %d, %d, and %d" % (side_a, side_b, side_c)
print "The area of the triangle is %r" % (area)
print "The angles of the triangle in degrees are %r, %r, and %r" %(deg_A, deg_B, deg_C)