# This is a program to test if the code in Question 4, saved in DMex4.py works well
# The program in DMex4.py is very chunky and working it here makes it easier and more readable

# Importing the contents of DMex4.py to be used in this file
import DMex4

# Initializing two finite sets A and A1 as well as two relations R and R1
A = {1, 4, 2, 5}
R = {(2, 2), (4, 4), (5, 5), (5, 2), (2, 4)}

A1 = {1, 2, 3, 4}
R1 = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 4), (4, 1), (4, 4)}


# Testing our program on A and R
print(DMex4.is_set(R))
print(DMex4.is_subset(R, A))
print(DMex4.is_relation(R, A))

if 'not' not in DMex4.is_relation(R, A):
    DMex4.is_reflexive(R, A)
    DMex4.is_transitive(R, A)
    DMex4.is_symmetric(R, A)

# Testing our program on A1 and R1
print(DMex4.is_set(R1))
print(DMex4.is_subset(R1, A1))
print(DMex4.is_relation(R1, A1))

if 'not' not in DMex4.is_relation(R1, A1):
    DMex4.is_reflexive(R1, A1)
    DMex4.is_transitive(R1, A1)
    DMex4.is_symmetric(R1, A1)

# Testing our program on A1 and R
print(DMex4.is_set(R))
print(DMex4.is_subset(R, A1))
print(DMex4.is_relation(R, A1))

if 'not' not in DMex4.is_relation(R, A1):
    DMex4.is_reflexive(R, A1)
    DMex4.is_transitive(R, A1)
    DMex4.is_symmetric(R, A1)

# Testing our program on R1 and A
print(DMex4.is_set(R1))
print(DMex4.is_subset(R1, A))
print(DMex4.is_relation(R1, A))

if 'not' not in DMex4.is_relation(R1, A):
    DMex4.is_reflexive(R1, A)
    DMex4.is_transitive(R1, A)
    DMex4.is_symmetric(R1, A)
