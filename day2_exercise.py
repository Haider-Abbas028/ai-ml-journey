"""Write a script that takes a list of 1000 random numbers and: removes duplicates (set), sorts them (list), groups them into ranges 0-10, 11-20, etc. (dict), finds the most common range (max with key). Use type hints on every function"""

import random 

def generate_numbers(n: int = 1000) -> list :
    return [random.randint(0,100) for _ in range(n)]

def rmv_duplicates(li: list[n])-> set:
    return set(li)

def sorted_list (s : set)-> list:
    return sorted(s)

def range_group(li: list, rang: int = 10) -> dict:
    ranges={}
    for i in range(0, 101, rang):
        ranges[f"{i}-{i+rang-1}"] = [x for x in li if i <= x <= i+rang-1]
    return ranges

def most_common_range(ranges: dict) -> str:
    return max(ranges, key=lambda k: len(ranges[k]))

#_________________________________________________________
generate_num = generate_numbers(200)
unique_elem = rmv_duplicates(generate_num)
sorted_list=sorted_list(unique_elem)
range_dict=range_group(sorted_list)
most_common=most_common_range(range_dict)
#_________________________________________________________
print(f"*"*50)
print(f"{generate_num}")
print(f"*"*50)
print (len(generate_num))
print (generate_num.count(28))
print(f"*"*50)
print (f"{unique_elem}",type(unique_elem))
print(f"*"*50)
print ("Sorted List ")
print (f"{sorted_list}",type(sorted_list))
print(f"*"*50)
print(f"Range Groups: {range_dict}")
print(f"Most Common Range: {most_common}")