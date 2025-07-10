#Data types

#String
print("Hello"[0])

print("123" + "345")

#Integer
print(123 + 345)
#Large Integer
print(1_203_109)

#Float
3.14159

#Boolean
True
False

#Type Conversion
print(type(123))
print(str(123))
print(int("123"))
print(float("123.456"))

#Type Checking
print(type(123) == int)
print(type("Hello") == str)
#Type Casting
print(int(3.14))  # Converts float to int, truncating the decimal
print(float(123))  # Converts int to float
#Complex Numbers
complex_number = 1 + 2j
print(complex_number)
# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accessing the first element
fruits.append("orange")  # Adding an element
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
# Tuples
coordinates = (10.0, 20.0)
print(coordinates[0])  # Accessing the first element
# Sets
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
# Dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Accessing value by key
# None Type
nothing = None
print(nothing)  # Output: None
# Type Aliases
from typing import List, Dict, Tuple, Set
# Using type aliases for better readability
def process_data(data: List[int]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for number in data:
        result[str(number)] = number * 2
    return result
# Example usage of the function
data = [1, 2, 3, 4, 5]
result = process_data(data)
print(result)  # Output: {'1': 2, '2': 4,
# '3': 6, '4': 8, '5': 10}
# Type Hints
def greet(name: str) -> str:
    return f"Hello, {name}!"
# Example usage of the function
greeting = greet("Alice")
print(greeting)  # Output: Hello, Alice!
# Type Annotations
def add_numbers(a: int, b: int) -> int:
    return a + b
# Example usage of the function
sum_result = add_numbers(5, 10)
print(sum_result)  # Output: 15
# Type Checking with isinstance
def is_integer(value) -> bool:
    return isinstance(value, int)
# Example usage of the function
print(is_integer(10))  # Output: True
print(is_integer(10.5))  # Output: False
print(is_integer("Hello"))  # Output: False
# Type Checking with issubclass
def is_subclass_of_number(cls) -> bool:
    return issubclass(cls, (int, float, complex))
# Example usage of the function
print(is_subclass_of_number(int))  # Output: True
print(is_subclass_of_number(float))  # Output: True
print(is_subclass_of_number(complex))  # Output: True
print(is_subclass_of_number(str))  # Output: False
# Type Checking with type()
def is_type_of(value, expected_type) -> bool:
    return type(value) is expected_type
# Example usage of the function
print(is_type_of(10, int))  # Output: True

print(is_type_of(10.5, float))  # Output: True
print(is_type_of("Hello", str))  # Output: True
print(is_type_of([1, 2, 3], list))  # Output: True
print(is_type_of((1, 2), tuple))  # Output: True
print(is_type_of({1, 2, 3}, set))  # Output: True
print(is_type_of({"key": "value"}, dict))  # Output: True
print(is_type_of(None, type(None)))  # Output: True
print(is_type_of(10, float))  # Output: False
print(is_type_of("Hello", int))  # Output: False
print(is_type_of([1, 2, 3], str))  # Output: False
print(is_type_of((1, 2), list))  # Output: False
print(is_type_of({1, 2, 3}, dict))  # Output: False
print(is_type_of({"key": "value"}, set))  # Output: False
