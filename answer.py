
'''
This is a program that calculates the tip and the bill total.
The bill can also be split.
'''
g_tip_amount = 0
g_total_bill = 0
g_split_amount = 0


#Old Part 3, the all in one.
def calculate_bill_globals(original_bill_amount, tip_percentage=18, split_number=1):
    global g_tip_amount
    global g_total_bill
    global g_split_amount
    g_tip_amount = calculate_tip(original_bill_amount, tip_percentage)
    g_total_bill = calculate_bill_total(original_bill_amount, g_tip_amount)
    g_split_amount = split_bill(g_total_bill, split_number)


def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * tip_percentage * .01


def calculate_bill_total(tip, bill_amount):
    return tip + bill_amount


def split_bill(bill_total, split_number):
    return bill_total/split_number


def main():
    print "Please choose one of the following."
    print "1 - Calculate Tip"
    print "2 - Split Bill"
    print "3 - Default Tip Amount"
    choice = int(raw_input())

    if choice == 1:
        bill = float(raw_input("How much was your bill?"))
        tip_percentage = float(raw_input("What percentage tip?"))
        tip = calculate_tip(bill, tip_percentage)
        bill_total = calculate_bill_total(tip, bill)
        print "The tip is %f." % tip
        print "The bill total is %f." % bill_total
        is_split = raw_input("Would you like the bill split, Y/N?")
        if (is_split.upper() == "Y"):
            split_number = int(raw_input("How many ways would you like to split the check?"))
            split_amount = split_bill(bill_total, split_number)
            print "The bill is %f for each person." % (split_amount)
    elif choice == 2:
        bill = float(raw_input("How much was your bill?"))
        split_number = int(raw_input("How many ways would you like to split the check?"))
        split_amount = split_bill(bill, split_number)
        print "The bill is %f for each person." % (split_amount)
    elif choice == 3:
        bill = float(raw_input("How much was your bill?"))
        calculate_bill_globals(bill)
        print "The tip is %f." % g_tip_amount
        print "The bill total is %f." % g_total_bill
        print "The bill is %f for each person." % (g_split_amount)


if __name__ == '__main__':
    print __name__
    main()
