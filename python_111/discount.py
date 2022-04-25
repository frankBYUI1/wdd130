'''
Write a Python program named discount.py that gets a customer's subtotal as 
input and gets the current day of the week from your computer's operating system. 
Your program must not ask the user to enter the day of the week. Instead, it must get 
the day of the week from your computer's operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must 
subtract 10% from the subtotal. Your program must then compute the total amount due by 
adding sales tax of 6% to the subtotal. Your program must print the discount amount if applicable, 
the sales tax amount, and the total amount due.

Core Requirements
Your program asks the user for the subtotal but does not ask the user for the day of the week. 
Your program gets the day of the week from your computer's operating system.
Your program correctly computes and prints the discount amount if applicable.
Your program correctly computes and prints the sales tax amount and the total amount due.
'''
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.
print(day_of_week)

subtotal =float(input("Please enter the subtotal: "))

# determine discount
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = subtotal * .1
    print(f"Discount amount: {discount:.2f}") 
    subtotal = subtotal - discount 

tax_amount = subtotal * .06
print(f"Tax amount: {tax_amount:.2f}")

total_amount = subtotal + tax_amount
print(f"Total amount: {total_amount:.2f}")
