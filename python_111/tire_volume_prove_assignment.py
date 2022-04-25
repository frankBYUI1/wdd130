'''
Full Name: Francesco Lezano
Teacher: Bro. Codling
Title: 02 Prove Assignment 

Many companies wish to understand the needs and wants of their customers more deeply so the company can create 
products that fill those needs and wants. One way to understand customers more deeply is to record the values 
entered by customers while they are using a program and then to analyze those values. One common way to record 
values is for a program to store them in a file.
'''
import math 
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

w=float(input("Enter the width of the tire in mm (ex 205): ")) 
a=float(input("Enter the aspect ratio of the tire (ex 60): "))
d=float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = math.pi * w ** 2 * a * (w * a + 2540 * d) / 10000000000
print(f"The approximate volume is {v:.2f} liters")
# Using different prices founded in the internet depends on the values the user wrote. 
if (v > 0 and v < 10):
    print("It is going to cost you $80")
elif (v > 10 and v < 50):
    print("It is going to cost you $220")
else:    
    print("It is going to cost you $850")

answer = input("Do you still want to buy it? ")
# No matter if the user writes YES or NO in uppercase the program will compute it as a normal yes or no
answer = answer.lower()

if answer == "yes":
    phone_number = input("Please, write down your phone number: ")
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()
    print(f"Today's date: {current_date_and_time:%Y-%m-%d}")
    # I'm the function open so I can be able to open a text file named volumes.txt
    with open("volumes.txt", "at") as tire_file: 
        # Just print all values I want to copy on the volumes.txt file
        print(f"{current_date_and_time:%Y-%m-%d} {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number}", file=tire_file) 
# Make the user feel that he always can choose if yes or no buy a product
elif answer == "no":
    print("Thank you for coming, come back soon.")
else: 
    print("Only yes or no answers, please.")




