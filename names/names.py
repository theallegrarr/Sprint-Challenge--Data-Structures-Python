import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
duplicates = []
bst = BinarySearchTree('duplicate_names')

# insert the names into the tree
for name in names_1:
    bst.insert(name)
# check if names in names 2 are also inside names 1
for name in names_2:
    # if it is there, insert into the duplicates
    if bst.contains(name):
        duplicates.append(name)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
start_time_stretch = time.time()
duplicates = [name for name in names_1 if names_2.count(name)>=1]
end_time_stretch = time.time()
print (f"{len(duplicates)} duplicates: {end_time_stretch - start_time_stretch} seconds")