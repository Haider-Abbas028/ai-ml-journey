"""
Day 1: Python Basics - Data Types, Lists, Tuples, Sets, Dictionaries
AI/ML Journey - Day 1
"""

# ============================================
# 1. BASIC PRINT STATEMENT
# ============================================
print("Hello World! I'm starting my AI journey today!")

# ============================================
# 2. VIRTUAL ENVIRONMENT NOTES (Comments)
# ============================================
"""
Virtual environment ek isolated Python environment hai. 
Har project ka apna alag environment hota hai, jiski apni libraries 
aur Python version hoti hai. Isse projects aapas mein interfere nahi karte.

Commands:
- Create: python -m venv venv
- Activate: venv\Scripts\activate (Windows)
- Deactivate: deactivate
- Check packages: pip list
- Save requirements: pip freeze > requirements.txt
- Install from requirements: pip install -r requirements.txt
"""

# ============================================
# 3. VARIABLES WITH TYPE HINTS
# ============================================
name: str = "Haider Abbas"
roll_Number: str = "F23-0632"
age: int = 21
cgpa: float = 3.0
single: bool = True  # 😓

print(f"\nStudent Info:")
print(f"Name: {name}")
print(f"Roll Number: {roll_Number}")
print(f"Age: {age}")
print(f"CGPA: {cgpa}")
print(f"Single: {single}\n")

# ============================================
# 4. QUICK CHEAT SHEET (Comments)
# ============================================
"""
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

# ============================================
# 5. ALL ABOUT LIST
# ============================================
print("=" * 50)
print("LIST OPERATIONS")
print("=" * 50)

# Creating a list
L1 = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original List: {L1}")

# --- Adding Methods ---
L1.append(11)          # Add at end
L1.insert(0, 0)        # Add at specific index
print(f"After adding (append 11, insert 0 at start): {L1}")

# --- Removing Methods ---
L1.remove(5)           # Removes first occurrence of 5
print(f"After removing 5: {L1}")

L1.pop(0)              # Removes first element (index 0)
print(f"After pop(0): {L1}")

L1.pop()               # Removes last element
print(f"After pop(): {L1}")

# --- Accessing / Searching Methods ---
first_element = L1[0]           # Returns first element
last_element = L1[-1]           # Returns last element
index_of_3 = L1.index(3)        # Returns index of first occurrence of 3
count_of_3 = L1.count(3)        # Returns count of 3 in list

print(f"First element: {first_element}")
print(f"Last element: {last_element}")
print(f"Index of 3: {index_of_3}")
print(f"Count of 3: {count_of_3}")

# --- Membership Check ---
is_present = 3 in L1
print(f"Is 3 in L1? {is_present}")

# --- Sorting and Reversing ---
L1.sort()              # Sorts in ascending order
print(f"After sort(): {L1}")

L1.reverse()           # Reverses the list
print(f"After reverse(): {L1}")

# --- Merging / Extending ---
L2 = [12, 13, 14]
print(f"L2: {L2}")

# Correct way to merge lists
L3 = L1 + L2           # Returns a new list
print(f"L1 + L2 = {L3}")

L1.extend(L2)          # Extends L1 with elements of L2
print(f"After extend(L2): {L1}")

# --- Copy and Clear ---
L1_copy = L1.copy()    # Returns a shallow copy
print(f"Copy of L1: {L1_copy}")

L1.clear()             # Removes all elements
print(f"After clear(): {L1}")

# --- Length ---
# CORRECT: Use len() function, not method
length = len(L1_copy)  # ✅ CORRECT WAY
print(f"Length of L1_copy: {length}")

print("\n" + "=" * 50)

# ============================================
# 6. ALL ABOUT TUPLE
# ============================================
print("TUPLE OPERATIONS")
print("=" * 50)

# Creating a tuple
T1 = tuple(range(1, 11))
print(f"Original Tuple: {T1}")

# --- Accessing Elements ---
x = T1[0]              # First element
y = T1[-1]             # Last element
print(f"First element: {x}")
print(f"Last element: {y}")

# --- Searching ---
index_of_3_tuple = T1.index(3)    # Index of first occurrence of 3
count_of_3_tuple = T1.count(3)    # Count of 3 in tuple
print(f"Index of 3 in tuple: {index_of_3_tuple}")
print(f"Count of 3 in tuple: {count_of_3_tuple}")

# --- Concatenation ---
T2 = (12, 13, 14)
T3 = T1 + T2
print(f"T1 + T2 = {T3}")

# --- Sort and Reverse (Tuples are immutable) ---
# T3.sort()     # ❌ ERROR: Tuples don't have sort()
# T3.reverse()  # ❌ ERROR: Tuples don't have reverse()

# Correct way to sort a tuple
sorted_T3 = sorted(T3)  # Returns a sorted LIST
print(f"Sorted T3 (as list): {sorted_T3}")

# --- Length ---
length_T3 = len(T3)
print(f"Length of T3: {length_T3}")

print("\n" + "=" * 50)

# ============================================
# 7. ALL ABOUT SET
# ============================================
print("SET OPERATIONS")
print("=" * 50)

# Creating sets
S1 = set([1, 2, 2, 3])  # Duplicates removed -> {1, 2, 3}
S2 = {3, 4, 5}

print(f"S1: {S1}")
print(f"S2: {S2}")

# --- Add Items ---
S1.add(6)              # Add single element
S1.update([7, 8, 3])   # Add multiple elements (duplicates ignored)
print(f"After add(6) and update([7,8,3]): {S1}")

# --- Remove Items ---
S1.discard(99)         # Safe remove (no error if missing)
print(f"After discard(99): {S1}")

# pop() removes arbitrary element
if len(S1) > 0:
    removed = S1.pop()
    print(f"Removed arbitrary element: {removed}")
    print(f"S1 after pop(): {S1}")

# --- Membership Check ---
is_in_set = 3 in S1
print(f"Is 3 in S1? {is_in_set}")

# --- Set Algebra ---
union = S1 | S2                # Union
intersection = S1 & S2         # Intersection
difference = S1 - S2           # Items in S1 not in S2
symmetric = S1 ^ S2            # Items in either but not both

print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference (S1 - S2): {difference}")
print(f"Symmetric Difference: {symmetric}")

# --- Utilities ---
S_copy = S2.copy()
print(f"Copy of S2: {S_copy}")

# Sorting a set returns a list
sorted_S2 = sorted(S2)
print(f"Sorted S2 (as list): {sorted_S2}")

length_S2 = len(S2)
print(f"Length of S2: {length_S2}")

print("\n" + "=" * 50)

# ============================================
# 8. ALL ABOUT DICT
# ============================================
print("DICT OPERATIONS")
print("=" * 50)

# Creating dictionaries
D1 = {"a": 1, "b": 2}
D2 = dict(c=3, d=4)

print(f"D1: {D1}")
print(f"D2: {D2}")

# --- Access ---
val_a = D1["a"]                    # KeyError if missing
val_z = D1.get("z", 0)             # Returns default if key not present
print(f"Value of 'a': {val_a}")
print(f"Value of 'z' (with default): {val_z}")

# --- Add / Update ---
D1["e"] = 5                        # Add new key
D1.update({"a": 10, "f": 6})       # Update existing and add new
print(f"After updates: {D1}")

# --- Remove ---
del D1["b"]                        # Remove by key
print(f"After deleting 'b': {D1}")

pop_c = D2.pop("c", None)          # Remove and return value or default
print(f"Popped 'c': {pop_c}")
print(f"D2 after pop: {D2}")

if len(D2) > 0:
    last_item = D2.popitem()       # Removes and returns last inserted pair
    print(f"Last item popped: {last_item}")
    print(f"D2 after popitem(): {D2}")

# --- Iterate ---
print("\nIterating through D1:")
for k in D1.keys():
    print(f"Key: {k}")

print("\nIterating through D1 items:")
for k, v in D1.items():
    print(f"Key: {k}, Value: {v}")

# --- Utilities ---
D_copy = D1.copy()
print(f"\nCopy of D1: {D_copy}")

sorted_keys = sorted(D1)
print(f"Sorted keys of D1: {sorted_keys}")

length_D1 = len(D1)
print(f"Length of D1: {length_D1}")

# --- Merge Dictionaries (Python 3.9+) ---
merged = D1 | {"g": 7}
print(f"Merged D1 with {{'g': 7}}: {merged}")

# --- Clear ---
D1.clear()
print(f"D1 after clear(): {D1}")

print("\n" + "=" * 50)

# ============================================
# 9. QUICK DECISION GUIDE
# ============================================
print("QUICK DECISION GUIDE")
print("=" * 50)
print("""
- Order matters, can change -> LIST
- Fixed data, never changes -> TUPLE
- Unique items, fast lookup -> SET
- Key-value pairs -> DICT
""")

print("=" * 50)
print("✅ Day 1 Complete! All concepts covered.")
print("=" * 50)