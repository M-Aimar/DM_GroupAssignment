# Discrete Mathematics exercise 1

# Write a python programme to test if a given list of elements constitutes a set. It should take as its input a
# list of elements and should output a True or False value.
# If the truth value is False then it must also output the list converted to a set or to a list which
# represents the set.


# creating an empty list
my_list = []

# Asking number of elements as input
n = int(input("\nEnter the number of elements you want to input into your list: "))
print("Thank you!!! Please type your elements")

# Using a for loop for iterating till the range
for i in range(0, n):
    elements_list = input()  # Variable to store an element inputted by the user
    my_list.append(elements_list)  # Adding the element through each iteration of the for loop

# Creating a variable to convert the list to a set using the set() python function to convert from the list datatype
# to set datatype
my_list_set = set(my_list)
# Creating a variable to compare the lengths of the list and the set created from the list
# This is to know if it is True (or False) that a list is a set
truth_value = (len(my_list) == len(my_list_set))

# Printing the list of elements inputted by the user
print("\nThe inputted list is: " + str(my_list))

# print("\n" + str(truth_value)) will ask if this is necessary to output the truth value first
# before showing it in the result

# conditional if-else statement to print the truth value of the comparison of lengths
if truth_value:
    # print statement to be executed if the variable truth_value is True
    print("\n" + str(truth_value) + ", the list " + str(my_list) + " is a set")
else:
    # print statement to be executed if the variable truth_value is False
    # and prints the set which should come out from the list
    print("\n" + str(truth_value) + ", the set should be: " + str(sorted(list(my_list_set))))

# Don't forget the write up about the code to explain the concept used

# Lists have duplicates and sets don't
# For a list to be a set, we convert a list into a set (change the datatype)
# and compare the lengths of both i.e. compare the length of the list and the set
# the one with duplicate elements (the list) would always be longer than the set

# End of program
