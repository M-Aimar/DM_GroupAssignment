# Discrete Mathematics exercise 2

# Write a programme that takes as input 2 finite SETS of any size, A;B, and outputs the following:
# a) the truth value of B "is a subset" A,
# b) the set A - B,
# c) the set A x B.


# Variables to create new empty sets A and B
A = set()
B = set()

# Small talk to interact with the user
print("Hello user. We want you to input elements into two empty sets A and B")

# Asking number of elements as input for the first set
n1 = int(input("\nPlease enter the number of elements you want to input into set A: "))
print("Thank you!!! Please enter your elements for set A")
for i in range(0, n1):
    elements_list1 = input()  # Variable to store an element inputted by the user
    A.add(elements_list1)  # Adding the element through each iteration of the for loop
# print functions to show the first set A
print("Thank you!!! You've entered all your elements for set A: ")
print(A)

# Asking number of elements as input for the second set
n2 = int(input("\nPlease enter the number of elements you want to input into set B: "))
print("Thank you!!! Please enter your elements for set B")
for i in range(0, n2):
    elements_list2 = input()  # Variable to store an element inputted by the user
    B.add(elements_list2)  # Adding the element through each iteration of the for loop
# print functions to show the second set B
print("Thank you!!! You've entered all your elements for set B: ")
print(B)

# print statement to show whether B is a subset of A using the builtin function issubset()
print("\nThe truth value of B 'is a subset of' A is " + str(B.issubset(A)))
# print statements to show the set A - B
print("\nThe set A - B is: ")
print(A - B)
# print statements to show the set or cartesian product A x B
print("\nThe set A x B is :")
print(sorted((i, j) for i in A for j in B))

# End of program
