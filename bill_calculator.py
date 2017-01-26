def calculate_tip(bill_amount, tip_percentage):
	return bill_amount * tip_percentage * .01


def calculate_total(tip_amount, bill_amount):
	return tip_amount + bill_amount


def split_bill(bill_total, num_people):
	return bill_total / num_people


def main():
	choice = raw_input("Choose an option:""\n""1 - calculate tip""\n""2 - split the bill""\n")


	if choice == "1":
		bill_amount = float(raw_input("What was the original bill amount?: "))
		tip_percentage = float(raw_input("What is the tip percentage?: "))
		tip_amount = calculate_tip(bill_amount, tip_percentage)
		print tip_amount
		print calculate_total(tip_amount, bill_amount)
		split_ask = raw_input("Would you like to split the bill?: ")
		if split_ask == "yes" or "Yes" or "Y" or "y":
			num_people = float(raw_input("How many ways?: "))
			bill_total = calculate_total(tip_amount, bill_amount)
			print split_bill(bill_total, num_people)
	elif choice == "2":
		bill_amount = float(raw_input("What was the original bill amount?: "))
		num_people = float(raw_input("How many ways?: "))
		split_again = split_bill(bill_amount, num_people)
		print "The cost per person is %f." % split_again
	else:
		print "Entry not valid! Please input '1' or '2'."


if __name__ == '__main__':
	main()











