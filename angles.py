import math

def error_check(test):
    # convert input to float, exit program if input is not a number
    try:
        tested = float(test)
        return tested
    except:
        print "Invalid input, please try again and enter a whole number"
        exit()

def rad_to_deg(rad):
    deg = rad * (180 / math.pi)
    return deg

def solve_angle_A(a, b, c):
    global rad_A
    cos_A = (a * a - b * b - c * c) / (-2 * b * c)
    rad_A = math.acos(cos_A)
    return rad_A

def solve_angle_B(a, b, c):
    global rad_B
    cos_B = (b * b - a * a - c * c) / (-2 * a * c)
    rad_B = math.acos(cos_B)
    return rad_B

def solve_angle_C(a, b, c):
    global rad_C
    cos_C = (c * c - a * a - b * b) / (-2 * a * b)
    rad_C = math.acos(cos_C)
    return rad_C


a = raw_input("Enter the length of first side of a triangle \n")
if len(a) > 0:
    side_a = error_check(a)
b = raw_input("Enter the length of second side of a triangle \n")
if len(b) > 0:
    side_b = error_check(b)
c = raw_input("Enter the length of third side of a triangle \n")
if len(c) > 0:
    side_c = error_check(c)

solve_angle_A(side_a, side_b, side_c)
solve_angle_B(side_a, side_b, side_c)
solve_angle_C(side_a, side_b, side_c)

deg_A = rad_to_deg(rad_A)
deg_B = rad_to_deg(rad_B)
deg_C = rad_to_deg(rad_C)

print deg_A, deg_B, deg_C