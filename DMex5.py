X = []  # Empty list X
Y = []  # Empty list Y

# Function that takes in both lists: X and Y and checks the validity of the statement
def factor(X,Y):
    # Loops through each element in list Y
    for i in Y:
        # Initialize an empty list called result
        result = []
        # Loop through each element in list X
        for j in X:
            # Divides each element of X by an element of Y
            if j%i == 0:
                # If j|i and gives an integer, then append the result list with 'True'
                result.append(True)

        # At the end of the for loop, check if the length of X and result lists are equal
        if len(result) == len(X):
            # If that is true, then the true value of the statement is True
            print("The truth value for the expression ∀x ∈ X, ∃y ∈ Y such that y | x is:",True)
            exit()

    # Else, the truth value is False
    print("The truth value for the expression ∀x ∈ X, ∃y ∈ Y such that y | x is:", False)

# Small talk to interact with the user
print("Hello user. We want you to input items into two empty lists X and Y")

# Asking number of items as input for the first list
n1 = int(input("\nPlease enter the number of items you want to input into list X: "))
print("Thank you!!! Please enter your items for list X"
      "(Only integers or whole numbers)")
for i in range(0, n1):
    items_list1 = int(input())  # Variable to store an item inputted by the user
    X.append(items_list1)  # Adding the item through each iteration of the for loop
# print function to show the first list X
print("Thank you!!! You've entered all your items for list X: " + str(X))

# Asking number of items as input for the second list
n2 = int(input("\nPlease enter the number of items you want to input into list Y: "))
print("Thank you!!! Please enter your items for list Y"
      "(Only integers or whole numbers)")
for i in range(0, n2):
    items_list2 = int(input())  # Variable to store an element inputted by the user
    Y.append(items_list2)  # Adding the item through each iteration of the for loop
# print functions to show the second list Y
print("Thank you!!! You've entered all your items for list Y: " + str(Y))

factor(X, Y)