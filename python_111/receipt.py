import csv

PRODUCT_NUM_INDEX = 0

def main():
    products_dict = read_dict("products.csv", 0)
    print()
    print("All Products")
    print(products_dict)
    


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