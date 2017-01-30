#Scope Exercise 1:

def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * tip_percentage * .01

#print calculate_tip(100, .20)


def total_bill(tip_amount, bill_amount):
    return tip_amount + bill_amount

#tip_amount = calculate_tip(100, .20)
#print total_bill(tip_amount, 100)


def split(bill_amount, num_people):
    return bill_amount / num_people

#bill_amount = total_bill(calculate_tip(100, .20), 100)
#print split(bill_amount, 4)


#Exercise 2:


def main():
    choice = raw_input("1 - calculate_tip" "\n" "2 - split the bill" "\n")
    if choice == "1":
        original_bill = float(raw_input("What was the original bill amount?: "))
        tip_percentage = float(raw_input("What tip percentage would you like to leave?: "))
        tip_amount = calculate_tip(original_bill, tip_percentage)
        bill_total = total_bill(tip_amount, original_bill)
        print "The tip amount is $%f." % tip_amount
        print "The bill amount is $%f." % bill_total
        split_choice = raw_input("Would you like to split the bill? Y/N: ")
        if split_choice == "Y":
            total = float(raw_input("What is the total bill amount?: "))
            num_people = float(raw_input("How many people are splitting the bill?: "))
            print split(total, num_people)
        else:
            print "Please enter 'Y' or 'N'"
    elif choice == "2":
        bill_total = float(raw_input("What is the total bill amount?: "))
        num_people = float(raw_input("How many people are splitting the bill?: "))
        print split(bill_total, num_people)
    else:
        print "Please enter '1' or '2'"
if __name__ == '__main__':
    main()


#Exercise 3


TIP_PERCENTAGE = .18


def calculate_bill(original_bill, num_people = 1):
    total_tip = TIP_PERCENTAGE * original_bill
    total_bill = total_tip + original_bill
    return total_bill / num_people

print calculate_bill(100, num_people = 2)


# Mega Challenge


def liters_to_gallons(liters):
    return liters / 3.785

def gallons_to_liters(gallons):
    return gallons * 3.785

def quarts_to_gallons(quarts):
    return quarts * 0.25

def quarts_to_liters(quarts):
    return quarts * 0.946353

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371


def main():
    choice = raw_input("What type of conversion would you like to do?:" "\n" "1. Liters to US Gallons" "\n" "2. US Gallons to Liters" "\n" "3. Quarts to US Gallons" "\n" "4. Quarts to Liters" "\n" "5. Miles to Kilometers" "\n" "6. Kilometers to Miles" "\n")
    if choice == "1":
        question1 = float(raw_input("How many liters?: "))
        answer1 = liters_to_gallons(question1)
        print "%f liters is equal to %f gallons." % (question1, answer1)
    elif choice == "2":
        question2 = float(raw_input("How many gallons? "))
        answer2 = gallons_to_liters(question2)
        print "%f gallons is equal to %f liters." % (question2, answer2)
    elif choice == "3":
        question3 = float(raw_input("How many quarts?: "))
        answer3 = quarts_to_gallons(question3)
        print "%f quarts is equal to %f gallons." % (question3, answer3)
    elif choice == "4":
        question4 = float(raw_input("How many quarts?: "))
        answer4 = quarts_to_liters(question4)
        print "%f quarts is equal to %f liters." % (question4, answer4)
    elif choice == "5":
        question5 = float(raw_input("How many miles?: "))
        answer5 = miles_to_kilometers(question5)
        print "%f miles is equal to %f kilometers." % (question5, answer5)
    elif choice == "6":
        question6 = float(raw_input("How many kilometers?: "))
        answer6 = kilometers_to_miles(question6)
        print "%f kilometers is equal to %f miles." % (question6, answer6)
    else:
        print "Please input '1', '2', '3', '4', '5', or '6'"
if __name__ == '__main__':
    main()
