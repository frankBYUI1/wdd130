'''
Full Name: Francesco Lezano
Teacher: Bro. Codling
Assignment: 10 Prove Assignment: Handling Exceptions

Problem Statement: A local grocery store subscribes to an online service that enables 
its customers to order groceries online. After a customer completes an order, the online 
service sends a CSV file that contains the customer's requests to the grocery store. 
The store needs you to write a program that reads the CSV file and prints to the terminal 
window a receipt that lists the purchased items and shows the subtotal, the sales tax 
amount, and the total.
'''

import csv

PRODUCT_ID = 0
REQUEST_QUANTITY = 1
PRODUCT_PRICE = 2
new_products = {}
new_request = []

def main():
    try:
        products = read_dict("products.csv", 0)
        with open("request.csv", "rt") as request:

            reader = csv.reader(request)
            next(reader)
            number = 0
            subtotal = 0

            for row in reader:
                name = row[PRODUCT_ID]
                new_products[name] = products[name]
                list = [name, row[REQUEST_QUANTITY]]
                new_request.append(list)

            print()
            print("Inkom Emporium")
            print()

            for row in new_request:
                print(f"{new_products[row[PRODUCT_ID]][REQUEST_QUANTITY]}: {row[REQUEST_QUANTITY]} @ {new_products[row[PRODUCT_ID]][PRODUCT_PRICE]}")
                number = number + int(row[REQUEST_QUANTITY])  
                subtotal += int(row[REQUEST_QUANTITY]) * float(new_products[row[PRODUCT_ID]][PRODUCT_PRICE])
                
        
        tax = subtotal * 0.0602
        total = subtotal + tax
        print()
        print(f"Number of Items: {number}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {tax:.2f}")
        print(f"Total: {total:.2f}")

        # Import the datetime class from the datetime
        # module so that it can be used in this program.
        from datetime import datetime

        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()

        # Print the current day of the week and the current time.
        print()
        print("Thank you for shopping at the Inkom Emporium.")
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

    except KeyError as error:
        print("Error: unknown product ID in the request.csv file")   
        print(error)

    except FileNotFoundError as error:
        print("Error: missing file")
        print(error)


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list

    return dictionary

if __name__ == "__main__":
    main()