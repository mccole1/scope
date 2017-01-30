# num = 8
# def double():
#     doubled = num * 2
#     return doubled

# print double()


# score = 0

# def increase_score(points):
#     new_score = score + points
#     return new_score

# print score
# print increase_score(10) # Returns 0 10


# score = 0

# def increase_score(points):
#     new_score = score + points
#     return new_score

# print new_score # This produces an error because new_score isn't defined globally


# score = 0

# def increase_score(points):
#     new_score = score + points
#     return new_score

# print score
# print increase_score(10)
# print score # Returns 0 10 0 (resets to 0)


# score = 0

# def increase_score(points):
#     new_score = score + points
#     return new_score

# print score
# score = increase_score(10)
# print score


# PI = 3.14159265359
# RADIUS = 15

# def circle_area():
#     area = PI * (RADIUS ** 2)
#     return area

# def circle_diameter():
#     diameter = RADIUS * 2
#     return diameter

# def circle_circumference():
#     circumference = 2 * PI * RADIUS
#     return circumference

# print "For Radius: ", RADIUS
# print "The area is: ", circle_area()
# print "The diameter is: ", circle_diameter()
# print "The circumference is: ", circle_circumference()

# global_variable = 13.4

# def function_one():
#     do_something

# def function_two():
#     do_something

# def main():
#     if (condition == true):
#         function_one()
#     else:
#         function_two()

# if __name__ == '__main__'
#     main()

# # call functions after all the functions have been defined
# function_one()
# function_two()


# def do_something(param1, param2 = 14, param3 = 0):
#     return param1 + param2 + param3

# print do_something(4, param3 = 10)
# print do_something(param3 = 1, param1 = 10, param2 = 4)


def calculate_sales_tax(bill_amount, tax_percentage = 10.0):
    return bill_amount * tax_percentage * .01

print calculate_sales_tax(200)
print calculate_sales_tax(200, 20)
print calculate_sales_tax(200, tax_percentage = 15)
print calculate_sales_tax(tax_percentage = 15, bill_amount = 200)













