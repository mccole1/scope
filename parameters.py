TIP_PERCENTAGE = 18

def calculate_bill(original_bill_amount, split_number = 1):
	total_tip_amount = original_bill_amount * TIP_PERCENTAGE * .01
	total_bill_amount = total_tip_amount + original_bill_amount
	return total_bill_amount / split_number

print calculate_bill(100)
print calculate_bill(100, split_number = 2)
# OR print calculate_bill(100,2)