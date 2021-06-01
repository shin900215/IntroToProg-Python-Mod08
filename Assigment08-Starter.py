# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# CShin,5.30.2021,Modified code to complete assignment 8
    # Product, FileProcessor, and IO Classes were created to be used
    # Properties, methods, and definitions are used in the Main Body of the script
    # Classes were used to read, print, and save data for the user.
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
class Product:
    """Stores data about a product:
    properties: product_name & product_price
    methods: print current data
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Charles Shin,5.30.2021,Modified code to complete assignment 8
    """
        # -- properties -- #
    @property
    def product_name(self):
        return str(self.__product_name).title()
    @product_name.setter
    def product_name(self, value: str):
        try:
            self.__product_name = str(value)  # cast to string
        except ValueError:
            raise Exception("Names cannot be numbers")
    @property
    def product_price(self):
        return float(self.__product_price)
    @product_price.setter
    def product_price(self, value: float):
        try:
            self.__product_price = float(value)  # cast to float
        except ValueError:
            raise Exception("Prices must be numbers")
        # -- Methods -- #
    def print_current_Items_in_list(list_of_rows):
        print("******* The current Tasks ToDo are: *******")
        for row in products.txt:
            print(str(row["Name"]) + str(row["Price"]))
            print("*******************************************")
            print()  # Add an extra line for looks
    pass
# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Charles Shin,5.30.2021,Modified code to complete assignment 8
    """
    # ------------- read current data ----------------------#
    def read_data_from_file():
        list_of_rows = []
        file = open("products.txt", "r")
        for line in file:
            data = line.split(",")
            row = {"Name": data[0].strip(), "Price": data[1].strip()}
            list_of_rows.append(row)
            file.close()
        return list_of_rows
    # ------------- read current data ----------------------#

    # ------------- save data ----------------------#
    def write_data_to_file():
        file = open(products.txt, "w")
        for row in list_of_rows:
            file.write(str(row["Name"]) + ',' + str(row["Price"] + '\n'))
        file.close()
        print("DATA IN FILE")
        return list_of_rows, 'Success'
    # ------------- save data ----------------------#
    pass
# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # --- For DocString --- #
    """Please select from the menu option choice.
    1. Show current data
    2. Add a new data (name and price)
    """
    # --- For DocString --- #

    # ------------- getting new data ----------------------#
    def input_new_name_and_price():
        product_name = str(input("What is the name of the item? -")).strip()
        product_price = str(input("What is the price of the item? - ")).strip()
        return product_name, product_price
    # ------------- getting new data ----------------------#

    pass
# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# --- Showing current data and ask for input ---#
Product.print_current_Items_in_list(products.txt)
lstTable = Processor.read_data_from_file("products.txt")  # read file data
print(IO.__doc__)
# --- Showing current data and ask for input ---#

# --- User Choice and program reaction ---#
while(True):
    Choice = str(input("Which option would you like to perform? [1 or 2] - ")).strip()
    print()  # Add an extra line for looks
    if  strChoice.strip() == '1':  # Add a new Data
        tplData = IO.input_new_name_and_price()
        FileProcessor.write_data_to_file()
        continue  # to show the menu
    elif strChoice.strip() == '2':  # show current data
            lstTable.clear()
            lstTable = Processor.read_data_from_file(strFileName)
            Product.print_current_Tasks_in_list(lstTable)
        continue  # to show the menu
break
# --- User Choice and program reaction ---#
# Main Body of Script  ---------------------------------------------------- #

