# Discount Eligibility Program

# ask user for input of their bill 
# and if the user is a member or not
# initialize discount
# check conditions
# calculate final amount
# print final result

total_bill = float(input("Enter total bill amount: "))
is_member = input("Are you a member? (yes/no): ")


discount = 0


if total_bill >= 1000 and is_member == "yes":
    discount = 0.10  # 10% discount
    print("You got 10% discount")

elif total_bill >= 1000 and is_member == "no":
    discount = 0.05  # 5% discount
    print("You got 5% discount")

else:
    print("No discount applied")


final_amount = total_bill - (total_bill * discount)


print("Final amount to pay:", final_amount)
