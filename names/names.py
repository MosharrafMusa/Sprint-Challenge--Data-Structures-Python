import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

all_names = names_1 + names_2

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# It takes 7.56818 seconds
'''
for name_1 in names_1: 
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)'''

# Implement a BST and the time will be reduced (It takes only 0.11911 seconds).
'''
bst = BSTNode(names_1[0])
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)'''

# Using sets and the built-in python function `intersection`(It only takes 0.00698 seconds)

duplicates = set.intersection(
    set(names_1), set(names_2))  # Reached STRETCH Goal


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
