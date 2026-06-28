"""Write a script that takes a list of 1000 random numbers and: removes duplicates (set), sorts them (list), groups them into ranges 0-10, 11-20, etc. (dict), finds the most common range (max with key). Use type hints on every function"""

import random

def generate_random_numbers(n: int=1000) -> list[int]:
    """Generate a list of n random numbers between 0 and 100."""
    return [random.randint(0, 100) for _ in range(n)]

def remove_duplicates(numbers: list[int]) -> set[int]:
    """Remove duplicates from the list of numbers."""
    return set(numbers)

def sort_numbers(numbers: list[int]) -> list[int]:
    """Sort the list of numbers."""
    return sorted(numbers)

def group_into_ranges(numbers: list[int], range_size: int = 10) -> dict[int, list[int]]:
    """Group numbers into ranges."""
    ranges = {}
    for num in numbers:
        range_key = num // range_size
        if range_key not in ranges:
            ranges[range_key] = []
        ranges[range_key].append(num)
    return ranges

def find_most_common_range(ranges: dict[int, list[int]]) -> int:
    """Find the most common range."""
    return max(ranges, key=lambda k: len(ranges[k]))

generated_numbers = generate_random_numbers()
unique_numbers = remove_duplicates(generated_numbers)
sorted_numbers = sort_numbers(list(unique_numbers))
grouped_ranges = group_into_ranges(sorted_numbers)
most_common_range = find_most_common_range(grouped_ranges)

print("Generated Numbers:", generated_numbers)
print("Unique Numbers:", unique_numbers)
print("Sorted Numbers:", sorted_numbers)
print("Grouped Ranges:", grouped_ranges)
print("Most Common Range:", most_common_range, "with numbers:", grouped_ranges[most_common_range])
