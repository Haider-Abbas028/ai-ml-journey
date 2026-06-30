print("Day 3 of my Ai-ML Journey")

# List comprehensions (Modern way of creating lists)

"[expression for item in iterable]"
#   ↑              ↑        ↑
# kya karna hai  variable  source

# Example: Create a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1,11)]
print(squares)
prime_num=[x for x in range(1, 101) if all(x % y != 0 for y in range(2, int(x**0.5) + 1)) and x > 1]
print(prime_num)

names = ["ali", "sara", "ahmed"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

words=["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)

"[expression for item in iterable if condition]"
#   ↑              ↑        ↑
# kya karna hai  variable  source
"Nested List Comprehensions"
# 3x4 matrix (3 rows, 4 columns)
rows = 3
cols = 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(matrix)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Identity Matrix (diagonal 1, baaki 0)
size = 4
identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
print(identity)
# [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

#Use cases in AI/ML:
# 1. Data Preprocessing: Transforming raw data into a suitable format for machine learning

"Dictionary Comprehensions"
"{key_expression: value_expression for item in iterable}"

# 1. Number ka square as dictionary
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2. Strings ko unke length ke saath
words = ["python", "code", "machine"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # {'python': 6, 'code': 4, 'machine': 7}

# 3. Condition ke saath (only even numbers)
nums = [1, 2, 3, 4, 5, 6]
even_squares = {x: x**2 for x in nums if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16, 6: 36}

# 4. Two lists ko combine karna
names = ["Ali", "Sara", "Ahmed"]
ages = [25, 30, 28]
students = {name: age for name, age in zip(names, ages)}
print(students)  # {'Ali': 25, 'Sara': 30, 'Ahmed': 28}

"Set Comprehension "
# 1. Unique squares
numbers = [1, 2, 2, 3, 3, 3, 4]
squares_set = {x**2 for x in numbers}
print(squares_set)  # {1, 4, 9, 16}  # duplicates removed automatically

# 2. Unique vowels in a string
text = "machine learning"
vowels = {char for char in text if char in 'aeiou'}
print(vowels)  # {'a', 'e', 'i', 'u'}  # unique vowels

# 3. Unique first letters of words
words = ["python", "code", "machine", "learning"]
first_letters = {word[0] for word in words}
print(first_letters)  # {'p', 'c', 'm', 'l'}
