"""
Problem Statement:
A common task for many knowledge workers is to use a number, 
key, or ID to find information about a person. For example, 
a knowledge worker may use a phone number or e-mail address 
as a key to find (or look up) additional information about 
a customer. During this activity, your team will write a 
Python program that uses a student's I-Number to look up the 
student's name.

"""

"""
Instructions: 
Open the students.csv file for reading, skip the first line 
of text in the file because it contains only headings, and 
read the other lines of the file into a dictionary. The 
program must store each student I-Number as a key and each 
name as a value in the dictionary.
"""
import csv

def main():
    #call read_dict with i-number as the key
    inumber_dict = read_dict("students.csv", 0)
    #ask the user to input an i-number
    inumber = input("Enter an I-number (ex. 066588900): ")
    #if the i-number is in the dictionary, print the corresponding name
    if inumber in inumber_dict:
        print(inumber_dict[inumber])
    elif len(inumber) < 9:
        print("Invalid I-Number: too few digits ")
    elif len(inumber) > 9:
        print("Invalid I-Number: too many digits ")       
    else:
        print("No such student")
    


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    #create an empty dictionary
    my_dict = {}
    #open the file
    with open(filename, "rt") as text_file:
        reader = csv.reader(text_file)
        #skip the first line
        next(reader)
        #read into a dictionary
        for line in reader:
            my_dict[line[key_column_index]] = line[1]
    #return the dictionary
    return my_dict


"""
Stretch Challenge:
When a user enters an I-Number, your program should 
ensure it is a valid I-Number.
a) If there are too few digits in the I-Number, your 
program should print, "Invalid I-Number: too few 
digits" (without the quotes).
b) If there are too many digits in the I-Number, your 
program should print, "Invalid I-Number: too many 
digits" (without the quotes).
c) If the given I-Number contains any characters besides 
digits and dashes, your program should output "Invalid 
I-Number" (without the quotes).
"""

if __name__== "__main__":
    main()
import csv

# def main(): 
#     I_NUMBER_INDEX = 0
#     NAME_INDEX = 1

#     students_dict = read_dict("students.csv", I_NUMBER_INDEX)

#     i_number = input("Please enter an I-Number (xx-xx-xxxx): ")

#     i_number = i_number.replace("-","")

#     if not i_number.isdigit():
#         print("Invalid character in I-Number")
#     else:
#         if len(i_number) < 9:
#             print("Invalid I-Number: too few digits ")
#         elif len(i_number) > 9:
#             print("Invalid I-Number: too many digit")       
#         else:
#             print("No such student")

# def read_dict(filename, key_column_index):
#     """Read the contents of a CSV file into a compound
#     dictionary and return the dictionary.

#     Parameters
#         filename: the name of the CSV file to read.
#         key_column_index: the index of the column
#             to use as the keys in the dictionary.
#     Return: a compound dictionary that contains
#         the contents of the CSV file.
#     """
#     dictionary = {}
    
#     with open(filename, "rt") as csv_file:
#         reader = csv.reader(csv_file)
#         next(reader)
#         for row_list in reader:
#             key = row_list[key_column_index]
#             dictionary[key] = row_list
#     return dictionary

# if __name__ == "__main__":
#     main()