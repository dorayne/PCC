import math

def error_check(test):
    # convert input to float, exit program if input is not a number
    try:
        tested = float(test)
        return tested
    except:
        print "Invalid input, please try again and enter a whole number"
        exit()

def area_tri(x, y, z):
    global area
    perim = (x + y + z)
    print perim
    p = float(perim/2)
    print p
    area = float(math.sqrt(p * (p - x) * (p - y) * (p - z)))
    return area

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

print "The area of the triangle is %r" % (area)