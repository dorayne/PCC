import math

def error_check(test):
    # convert input to float, exit program if input is not a number
    try:
        tested = float(test)
        return tested
    except:
        print "Invalid input, please try again and enter a number"
        exit()

def triangle_exist(a, b, c):
    # determines if the given sides will form a triangle using the Triangle Inequality Theorem
    # program will exit if the triangle does not exist
    if (a + b) > c and (b + c) > a and (a + c) > b:
        print "The sides entered form a triangle"
    else:
        print "The sides entered do not form a triangle. Please try again with different sides."
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