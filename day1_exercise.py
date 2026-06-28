print (f"Hello World! I'm starting my AI journey today!")

# Virtual environment ek isolated Python environment hai. Har project ka apna alag environment hota hai, jiski apni libraries aur Python version hoti hai. Isse projects aapas mein interfere nahi karte.

#  python -m venv venv
# venv\Scripts\activate
# deactivate
# pip list (to check installed packages)
'''pip freeze > requirements.txt	(Requirements file banao)
pip install -r requirements.txt	 (Requirements se install karo)'''

name :str = "Haider Abbas"
roll_Number : str= "F23-0632"
age : int = 21
cgpa : float = 3.0
single : bool = True # 😓

"""
Quick cheat table

Type        Example         Mutable?   Ordered?   Duplicates?
List        [1, 2, 3]       Yes        Yes        Yes
Tuple       (1, 2, 3)       No         Yes        Yes
Set         {1, 2, 3}       Yes        No         No
Dict        {"a": 1}        Yes        Yes        Keys unique

Use:
- List -> for ordered items
- Tuple -> for fixed data
- Set -> for unique values
- Dict -> for key-value data
"""
 # All About List
L1= list(range(1,11))
print(L1)
# adding methods in List
L1.append(11)
L1.insert(0,0)

#removing methods in List
L1.remove(5) # removes first occurrence of 5
L1.pop(0) # removes first element   
L1.pop() # removes last element

# accessing or searching methods in List
L1[0] # returns first element
L1[-1] # returns last element
L1.index(3) # returns index of first occurrence of 3
L1.count(3) # returns count of 3 in list
L1.sort() # sorts the list in ascending order
L1.reverse() # reverses the list
"x in L1" # returns True if x is in list, else False

# merging or extending methods in List
L2= [12, 13, 14]
"L1 + L2" # returns a new list with elements of L1 and L2 
L1.extend(L2) # extends L1 with elements of L2
L1.copy() # returns a shallow copy of L1
L1.clear() # removes all elements from L1
L1.len() # returns the number of elements in L1
len(L1) # returns the number of elements in L1
# ______________________________________________________________

# All About Tuple
T1=tuple(range(1,11))
 # adding methods in tuple
"T1.add(11)" # ❌ Can't add
"T1.remove(5)" # ❌ Can't remove
x = T1[0] # returns first element
y = T1[-1] # returns last element
T1.index(3) # returns index of first occurrence of 3
T1.count(3) # returns count of 3 in tuple
 T2= (12, 13, 14)
 T3=T1 + T2 # returns a new tuple with elements of T1 and T2
T3.sort() # ❌ Can't sort
T3.reverse() # ❌ Can't reverse
sorted(T3) # returns a new sorted list of T3
len(T3) # returns the number of elements in T3


# -------------------------
# All About Set
# -------------------------
# Sets store unique items and are unordered. Fast membership checks (avg O(1)).

S1 = set([1, 2, 2, 3])  # duplicates removed -> {1, 2, 3}
S2 = {3, 4, 5}

print("S1:", S1)
print("S2:", S2)

# Add items
S1.add(6)             # add single element
S1.update([7, 8, 3])  # add multiple elements (duplicates ignored)

# Remove items
# S1.remove(x) raises KeyError if x not present
S1.discard(99)   # safe remove (no error if missing)
# pop() removes an arbitrary element from set
removed = S1.pop() if len(S1) else None

# Membership check
print("Is 3 in S1?", 3 in S1)

# Set algebra
union = S1 | S2                # union
intersection = S1 & S2         # intersection
difference = S1 - S2           # items in S1 not in S2
symmetric = S1 ^ S2            # items in either S1 or S2 but not both

print("union:", union)
print("intersection:", intersection)
print("difference:", difference)
print("symmetric difference:", symmetric)

# Utilities
S_copy = S2.copy()
print("sorted S2 as list:", sorted(S2))  # sorting returns a list
print("len(S2):", len(S2))


# -------------------------
# All About Dict
# -------------------------
# Dictionaries map keys to values. Keys must be hashable and are unique.

D1 = {"a": 1, "b": 2}
D2 = dict(c=3, d=4)

print("D1:", D1)
print("D2:", D2)

# Access
val_a = D1["a"]            # KeyError if missing
val_z = D1.get("z", 0)     # returns default if key not present

# Add / Update
D1["e"] = 5                # add new key
D1.update({"a": 10, "f": 6})  # update existing and add new

# Remove
del D1["b"]                # remove by key, raises KeyError if missing
pop_c = D2.pop("c", None)  # remove and return value or default
last_item = D2.popitem()     # removes and returns last inserted pair

# Iterate
for k in D1.keys():
	print(f"key: {k}")

for k, v in D1.items():
	print(f"key,value -> {k}, {v}")

# Utilities
D_copy = D1.copy()
print("sorted keys of D1:", sorted(D1))
print("len(D1):", len(D1))

# Merge dictionaries (Python 3.9+ supports | operator)
merged = D1 | {"g": 7}
print("merged:", merged)

# Clear
D1.clear()

# Quick Decision Guide:
# - Order matters, can change -> LIST
# - Fixed data, never changes -> TUPLE
# - Unique items, fast lookup -> SET
# - Key-value pairs -> DICT

