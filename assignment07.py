# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with Pickling and Error Handling
# ChangeLog (Who,When,What):
# JLi,08.24.2020,Created started script
# JLi,08.24.2020,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Pickling module imported
import pickle

# input
make = input('Enter the make of the car: ')
model = input('Enter the model of the car: ')
list1 = [make, model]

# write
list_file = open('data.dat', 'wb')
pickle.dump(list1, list_file)
list_file.close()

# read
list_file = open('data.dat', 'rb')
list2 = pickle.load(list_file)
print('My Fav cars are:', list2)



# Error Handling

try:
    f = open("1.txt", "r")
    try:
        content = f.read()
        print(content)
        f.close()
    except NameError as error:
        print("Error:%s" % error)
except FileNotFoundError as error:
    print("Error:%s" % error)




