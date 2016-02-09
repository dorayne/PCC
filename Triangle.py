import math

def error_check(test):
    # convert input to integer, exit program if input is not a number
    try:
        tested = int(test)
        return tested
    except:
        print "Invalid input, please try again and enter a whole number"
        exit()

a = raw_input("Enter the length of first side of a triangle \n")
if len(a) > 0:
    side_a = error_check(a)
b = raw_input("Enter the length of second side of a triangle \n")
if len(b) > 0:
    side_b = error_check(b)
c = raw_input("Enter the length of third side of a triangle \n")
if len(c) > 0:
    side_c = error_check(c)

print "The lengths of the sides of the triangle are %s, %s, %s" % a, b, c