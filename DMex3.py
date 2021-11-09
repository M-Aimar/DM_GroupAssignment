# Discrete Mathematics exercise 3

# Write a programme that takes as input 2 finite LISTS of any size, A;B, and outputs the following:
# a) the truth value of B "is a subset" A,
# b) the set A - B,
# c) the set A x B.

# This is the same question as Question 2 except you are not allowed to use the set environment in
# Python nor are you allowed to use in-built or package Python functions specific to sets which output
# the required sets immediately. You must use lists, for loops, if statements, and other basic Python commands.

# Variables to create new empty lists A and B
A = []
B = []

# Small talk to interact with the user
print("Hello user. We want you to input items into two empty lists A and B")

# Asking number of items as input for the first list
n1 = int(input("\nPlease enter the number of items you want to input into list A: "))
print("Thank you!!! Please enter your items for list A")
for i in range(0, n1):
    items_list1 = input()  # Variable to store an item inputted by the user
    A.append(items_list1)  # Adding the item through each iteration of the for loop
# print functions to show the first list A
print("Thank you!!! You've entered all your items for list A: ")
print(A)

# Asking number of items as input for the second list
n2 = int(input("\nPlease enter the number of items you want to input into list B: "))
print("Thank you!!! Please enter your items for list B")
for i in range(0, n2):
    items_list2 = input()  # Variable to store an element inputted by the user
    B.append(items_list2)  # Adding the item through each iteration of the for loop
# print functions to show the second list B
print("Thank you!!! You've entered all your items for list B: ")
print(B)


# To obtain the desired results for the three questions a, b and c, three functions will be created
# and called to show the desired results

# Creating a sublist function to check if list B is a sublist of list A
def sublist(list1, list2):
    # Using a variable sublist_check to iterate between all the items in the first and second lists
    sublist_check = (x in list1 for x in list2)

    # Assigning a variable sublist_confirmation to confirm that after iterating through the lists
    # list B is a subset of list A (1 is used to represent the value true)
    sublist_confirmation = 1

    # An iteration is performed using a boolean variable 'answer'
    # to check is the items of list B are a sublist of list A
    for answer in sublist_check:
        if not answer:  # If the items of list B are not a sublist of list A,
            sublist_confirmation = 0  # then the sublist_confirmation equals 0 (or false)

    # If-else statements are then used to print or output if list B is a sublist of list A
    if sublist_confirmation == 1:
        print("B ⊆ A.")
    else:
        print("B ⊈ A.")

    # End of function


# Creating a function to perform a list difference operation i.e. output all the items in A that are not in B
def list_difference(list1, list2):
    # Create a list called list_diff to store the result of the operation A - B
    list_diff = []
    # The function uses the variable 'item' to iterate through items of the first list using a for loop
    for item in list1 + list2:  # Iterate through items of the first list and store in 'item' after each iteration
        if item in list1 and item not in list2:  # If an item is in the first list and is not found in the second list,
            list_diff.append(item)  # Add that item to the variable list_diff
        else:
            pass
    print("A - B = " + str(list_diff))  # Print the result
    # li_diff = [item for item in list1 + list2 if item in list1 and item not in list2]
    # would be an alternative to the lines of code used in the function list_difference

    # End of function


# Creating a function to print the cartesian product of two lists A x B
def cartesian(list1, list2):
    # Create a list called cartesian_product to store the result of the operation
    # Two for loops are used (one nested into another) to iterate through each item of lists A and B
    # and the product is arranged in the form (item1, item2) for each iterations performed
    cartesian_product = [(item1, item2) for item1 in list1 for item2 in list2]
    print("A x B = " + str(cartesian_product))  # This prints the result A x B represented by cartesian_product

    # End of function


print("\n")
sublist(A, B)  # Function call for the result "B is a subset of A"
list_difference(A, B)  # Function call for the result A - B
cartesian(A, B)  # Function call for the result A x B

# End of program
