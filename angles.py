import math

def error_check(test):
    # convert input to integer, exit program if input is not a number
    try:
        tested = float(test)
        return tested
    except:
        print "Invalid input, please try again and enter a whole number"
        exit()

def solve_angle_A(a, b, c):
    global rad_A
    rad_A = float(math.acos((a * a - b * b - c * c) /  (-2 * b * c)))
    return rad_A

def solve_angle_B(a, b, c):
    global rad_B
    rad_B = float(math.acos((b * b - a * a - c * c) /  (-2 * a * c)))
    return rad_B

def solve_angle_C(a, b, c):
    global rad_C
    rad_C = float(math.acos((c * c - a * a - b * b) /  (-2 * a * b)))
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
solve_angle_A(side_a, side_b, side_c)
solve_angle_A(side_a, side_b, side_c)

print "The angles of the triangle in radians are %r, %r, and %r" % (rad_A, rad_B, rad_C)

