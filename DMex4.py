# This program checks if R is a relation on A and what properties the relation satisfies
"""
This program takes in a finite set/list A and a relation written mathematically R
The program will output whether R is a set and a subset of AxA to decide if R is a relation on A
After this it will check for three properties, namely; Reflexivity, Transitivity, Symmetry
If R doesnt fit a property among the three, the program will let us know which elements R has/lacks to fit the property
If R is not a relation A, the program will not go on to check the properties.
However, we will be told why R is not a relation on A
"""

# Library that allows us to compute the cartesian product, used to find AxA
from itertools import product


# Function that checks whether R is a set, A condition R has to meet in order to be a relation on A
def is_set(r):
    if isinstance(r, set):
        return 'R is a set'
    else:
        return 'R is not a set'


# Function that check whether R is a subset of A, A condition R has to meet in order to be a relation on A
def is_subset(r, a):
    unique_elements = []  # Variable that stores elements that may be in R and not in AxA if R is not a subset of AxA
    axa = product(a, a)  # Calculating AxA from the itertools library

    # Checking if each element in R is also in AxA
    for i in list(r):
        if i not in a:
            unique_elements.append(i)

    # Checking whether or not R is a subset of AxA
    if r.issubset(axa):
        return 'R is a subset of AxA'

    # If R is not a subset of AxA, the we let the user know what elements of R are not in AxA
    # We use two conditions to get the grammar correct when we have multiple or a single element unique to R
    else:
        if len(unique_elements) > 1:
            return f'R is not a subset of AxA because the following elements are in R but not in AxA: {unique_elements}'

        else:
            return f'R is not a subset of AxA because the following element is in R but not in AxA: {unique_elements}'


# Checking if R is a relation on A
def is_relation(r, a):
    set_status = is_set(r)  # Checking whether R is a set
    subset_status = is_subset(r, a)  # checking whether R is a subset of AxA

    # Letting the user know whether or not R is a relation on AxA
    if 'not' in set_status:
        return 'R is not a relation on A'
    elif 'not' in subset_status:
        return 'R is not a relation on A'
    else:
        return 'R is a relation on A'


# Checking whether R is Reflexive
def is_reflexive(r, a):
    not_reflexive = []  # Variable that stores the elements that dont fit the property in case R is not Reflexive

    # Checking for the reflexive property
    # If an element doesnt fit/is missing from R to satisfy reflexivity we add it to not_reflexive list
    for i in a:
        if (i, i) not in r:
            not_reflexive.append(i)

    # If the list is empty the R is reflexive otherwise R is not reflexive
    if len(not_reflexive) == 0:
        print('R is reflexive')

    else:
        print(f'R is not reflexive: {not_reflexive}')


# Checking whether R is Transitive
def is_transitive(r, a):
    not_transitive = []  # Stores elements that dont fit the property in case R is not Transitive

    # Checking for transitivity on each possible element pair in set A
    # Adding the pair to the not_transitive list if they make our relation not transitive
    for x in a:
        for y in a:
            if (x, y) in r:
                for z in a:
                    if (y, z) in r and (x, z) not in r:
                        not_transitive.append((x, y))

    # If the list is empty the R is transitive otherwise R is not transitive
    if len(not_transitive) == 0:
        print('R is transitive')

    else:
        print(f'R is not transitive: {not_transitive}')


# Checking whether R is Symmetric
def is_symmetric(r, a):
    not_symmetric = []  # Variable that stores the elements that dont fit the property in case R is not Symmetric

    # Checking for the Symmetric property
    # If an element doesnt fit/is missing from R to satisfy Symmetric we add it to not_symmetric list
    for i in r:
        if i[0] in a and i[1] in a and i[::-1] not in r:
            not_symmetric.append(i)

    # If the list is empty the R is symmetric otherwise R is not symmetric
    if len(not_symmetric) == 0:
        print('R is symmetric')

    else:
        print(f'R is not symmetric: {not_symmetric}')
