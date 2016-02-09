import math

def error_check(test):
    # convert input to integer, exit program if input is not a number
    try:
        tested = int(test)
        return tested
    except:
        print "Invalid input, please try again and enter a whole number"
        exit()

def area_tri(x, y, z):
    global area
    perim = float((x + y + z) / 2)
    area = float(math.sqrt(perim * (perim - x) * (perim - y) * (perim - z)))
    return area

def rad_deg(rad):
    global deg
    deg = rad * (180 / math.pi)
    return deg

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

area_tri(side_a, side_b, side_c)

#solve_angle_A(side_a, side_b, side_c)
#solve_angle_B(side_a, side_b, side_c)
#solve_angle_C(side_a, side_b, side_c)

#angle_A = rad_deg(rad_A)
#angle_B = rad_deg(rad_B)
#angle_C = rad_deg(rad_C)

print "The lengths of the sides of the triangle are %d, %d, and %d" % (side_a, side_b, side_c)
print "The area of the triangle with the given sides is %d" % (area)
#print "The angles of the triangle are %d, %d, and %d" %(angle_A, angle_B, angle_C)