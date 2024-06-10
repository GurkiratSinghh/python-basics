'''
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Sum of numbers: {sum_of_numbers}")
'''

'''
numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x ** 3, numbers))
print(f"Cubes of numbers: {cubes}")
'''


'''
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
'''

'''
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
zipped_list = list(zip(names, scores))
print(f"Zipped names and scores: {zipped_list}")
'''


'''
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(f"After appending 6: {numbers}")

'''


'''
numbers.insert(0, 0)
print(f"After inserting 0 at the beginning: {numbers}")
'''

'''
last_element = numbers.pop()
print(f"Last element popped: {last_element} Remaining list: {numbers}")
'''

'''
count_of_2 = numbers.count(2)
print(f"Count of '2': {count_of_2}")

'''

'''
fruits = ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']

a = 'cherry' in fruits
print(f"Is 'cherry' in the list? {a}")


index = fruits.index('date')
print(f"Index of 'date': {index}")

Sorted_fruits = sorted(fruits)
print(f"Fruits sorted in ascending order: {sorted_fruits}")

'''
'''
fruits = ('apple', 'banana', 'kiwi', 'orange', 'grape', 'mango')

a = 'kiwi' in fruits
print(f"Is 'kiwi' in the tuple? {a}")

j = fruits.index('orange')
print(f"Index of 'orange': {j}")

sorted_fruits = tuple(sorted(fruits))
print(f"Fruits sorted in ascending order: {sorted_fruits}")
'''



'''
my_dict = {'cherry': 5, 'kiwi': 10, 'mango': 15}
removed_value = my_dict.pop('kiwi')
print(removed_value)
print(my_dict)  # Output: {'cherry': 5, 'mango': 15}
'''


'''

numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
print(even_squares)
'''

'''
def group(a_list, key):
    grouped = {}
    for a in a_list:
        b = a[key]
        if b in grouped:
            grouped[b].append(a)
        else:
            grouped[b] = [a]
    return grouped

a_list = [
    {'product': 'Laptop', 'price': 1000, 'brand': 'Dell'},
    {'product': 'Phone', 'price': 800, 'brand': 'Apple'},
    {'product': 'Tablet', 'price': 600, 'brand': 'Samsung'},
    {'product': 'Monitor', 'price': 200, 'brand': 'Dell'}
]

grouped = groua_list, 'brand')
print(grouped)
'''

'''
set1 = {'red', 'blue', 'green'}
set2 = {'yellow', 'blue', 'pink'}

union_set = set1 | set2
print("Union of sets:", union_set)

'''
'''

s = {1, 2, 3}


s.add(4)
s.add(5)

print("After adding elements:", s)
s.remove(2)
print("After removing an element:", s)
'''



'''
set1 = {'dog', 'cat', 'rabbit'}
set2 = {'rabbit', 'hamster', 'cat'}

intersection_set = set1 & set2
print("Intersection of sets:", intersection_set)
'''

'''
set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'date', 'fig'}

difference_set = set1 - set2
print("Difference of sets:", difference_set)
'''
