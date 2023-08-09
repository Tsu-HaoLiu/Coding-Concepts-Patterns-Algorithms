## Int, Float, string

**Int (Integer)**: An integer is a whole number without a fractional component. It represents a numerical value that can be either positive, negative, or zero. Integers are commonly used for counting, indexing, and performing arithmetic operations.

**Float (Floating-Point Number)**: A floating-point number is a numerical value that can have both an integer and a fractional component. It is used to represent real numbers, including numbers with decimal places. Floating-point numbers are commonly used in scientific calculations, engineering, and other fields where precise decimal representation is required.

**String**: A string is a sequence of characters, typically used to represent text. It can include letters, numbers, symbols, and spaces. Strings are often used to store and manipulate textual data, such as names, sentences, or any other type of textual information. String manipulation is a fundamental operation in programming and is used for tasks like input/output, data formatting, and text processing.

## Arrays

An array is a data structure that stores a collection of elements, such as numbers, strings, or objects, in a linear sequence. Each element in an array is identified by an index, which is a numeric value indicating the position of the element within the array. Arrays are commonly used to group related data together for easier manipulation and access.

```python
# Creating an array of integers
my_array = [10, 20, 30, 40, 50]

# Accessing elements by index
print(my_array[0])  # Output: 10
print(my_array[2])  # Output: 30

# Modifying elements
my_array[3] = 45

# Looping through the array
for element in my_array:
    print(element)
```

## Matrix

A matrix is a two-dimensional rectangular array of elements, typically numbers, symbols, or other data types. Each element in a matrix is identified by its row and column index.

```python
# Creating a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Accessing elements
print(matrix[0][1])  # Output: 2

# Modifying elements
matrix[1][2] = 8

# Looping through the matrix
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        print(element[row][col])
```

## Hashing and Maps

Hashing and maps are concepts used to efficiently store, retrieve, and manage data. They are often used to implement data structures that allow quick access to information based on a key.
A map, also known as an associative array, dictionary, or hash map, is a data structure that stores a collection of key-value pairs. It allows you to associate a value with a unique key, and then quickly retrieve that value based on the key. Maps are often implemented using hashing to achieve fast access times.

```python
# Creating a map (dictionary)
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values using keys
print(my_dict["name"])  # Output: John

# Adding a new key-value pair
my_dict["occupation"] = "Engineer"

# Iterating through keys and values
for key, value in my_dict.items():
    print(key, ":", value)

```

## Linked Lists

A linked list is a linear data structure used to store a sequence of elements, where each element is represented by a node. Unlike arrays, linked lists do not have a fixed size and do not store elements in contiguous memory locations. Instead, each node in a linked list contains the element itself and a reference (or pointer) to the next node in the sequence.

```python
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Creating a linked list and adding elements
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Displaying the linked list
my_list.display()

```

## Stacks

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, which means that the last element added to the stack is the first one to be removed. Stacks are commonly used to manage data in a way that resembles a physical stack of objects, like a stack of plates.

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return self.size == 0

    def size(self):
        return len(self.items)

# Creating a stack and performing operations
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Top element:", my_stack.peek())  # Output: 30

print("Popped:", my_stack.pop())  # Output: 30
print("Popped:", my_stack.pop())  # Output: 20

print("Is empty?", my_stack.is_empty())  # Output: False
print("Size:", my_stack.size())  # Output: 1

```

## Queues

## Trees

## Graphs

## Heaps

## Greedy Algorithm

