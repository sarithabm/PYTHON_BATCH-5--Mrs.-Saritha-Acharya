#DSA Python 
#data structures:
#LIST, TUPLE, SET, DICTIONARY 
# CREATE , READ, INSERT, UPDATE, DELETE,SELECT
# CRUD IS 
1. Lists
2. Tuple
3. Set  - frozensets
4. Dictionary
5. Strings
6. Matrix
7. LinkedList
8. Stack
9. queues
10. Tries & graphs 

#List Data Structures
#CREATION
1. Creating an empty list:
my_list = []  #[]
2. Creating a list with elements:
my_list = [1, 2, 3, 4, 5]
3. Creating a list with different data types:
mixed_list = [1, "apple", True, 3.14]
4. Creating a list using list comprehension:
x=1
squares = [x**2 for x in range(10)]

5. Creating a nested list:

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

6. Creating a list with repeated elements:
repeated_list = [0] * 5

#LIST COMPREHENSION
# Example 1: Generating a list of squares 
#of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)  

# Example 2: Generating a list of even numbers 
#from 0 to 20
x=0
even = [x for x in range(21) if x % 2 == 0]
print(even)  

# Example 3: Generating a list of tuples 
#containing both the number and its square
number= [(x, x**2) for x in range(1, 6)]
print(number)   

# Example 4: Generating a list of strings 
#with each string capitalized
words = ["hello", "world", "python", "list", 
"comprehension"]
ca_words = [word.capitalize() for word in 
words]
print(ca_words)  

##Accessing elements in a list 
1. Accessing a single element:
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

2. Negative indexing:
print(my_list[-1])  # Output: 5 (last element)
print(my_list[-2])  # Output: 4 (second to last element)

3. Accessing elements through slicing:
(my_list[1:4])  # Output: [2, 3, 4] (elements from index 1 to 3)
print(my_list[:3])   # Output: [1, 2, 3] (elements from the beginning to index 2)
print(my_list[2:])   # Output: [3, 4, 5] (elements from index 2 to the end)


4. Accessing nested lists:
'''If your list contains nested lists, 
you can access elements of the nested 
lists using multiple indices.'''

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[2][1])  # Output: 4 (first element of the second nested list)


5. Accessing elements with steps:
You can specify a step value to skip elements 
while accessing them.
my_list = [1, 2, 3, 4, 5]
print(my_list[::3])  
# Output: [1, 3, 5] (elements with step 2)


#TRAVERSING
1. Using a for loop:

my_list = [1, 2, 3, 4, 5]
for element in my_list:
    print(element)


2. Using a for loop with range and len():
my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    print(my_list[i])

3. Using a while loop:

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1


4. Traversing through a nested list:

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in nested_list:
    for element in sublist:
        print(element)

# FUNCTIONS

1. len(): Returns the number of elements in the list.
    
    my_list = [1, 2, 3, 4, 5]
    length = len(my_list)
    print(length)  # Output: 5
    

2. count(): Returns the number of occurrences of a specified element in the list.
    
    my_list = [1, 2, 2, 3, 2, 4]
    count = my_list.count(2)
    print(count)  # Output: 3
    

3. index(): Returns the index of the first 
occurrence of a specified element in the list.
    
    my_list = [1, 2, 3, 4, 5]
    index = my_list.index(3)
    print(index)  # Output: 2 (index of element 3)
    

4. append(): Adds an element to the end of the list.
    python
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]
    

5. insert(): Inserts an element at a specified position in the list.
    python
    my_list = [1, 2, 3]
    my_list.insert(1, 1.5)
    print(my_list)  # Output: [1, 1.5, 2, 3]
    

6. extend(): Adds elements from another list 
(or any iterable) to the end of the list.
    
    my_list = [1, 2, 3]
    another_list = [4, 5, 6]
    my_list.extend(another_list)
    print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
    
7. remove(): Removes the first occurrence of a specified element from the list.
    python
    my_list = [1, 2, 3, 2, 4]
    my_list.remove(2)
    print(my_list)  # Output: [1, 3, 2, 4]
    

8. pop(): Removes and returns the element at a specified index (by default, the last element).
    my_list = [1, 2, 3, 4, 5]
    popped_element = my_list.pop(2)
    print(popped_element)  # Output: 3
    print(my_list)  # Output: [1, 2, 4, 5]
   
9. reverse(): Reverses the order of elements in the list. 
    my_list = [1, 2, 3, 4, 5]
    my_list.reverse()
    print(my_list)  # Output: [5, 4, 3, 2, 1]
    
10. sort(): Sorts the elements of the list in ascending order (by default) or using a custom key function.
    
    my_list = [3, 1, 4, 1, 5, 9, 2]
    my_list.sort()
    print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 9]
   
   my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort(reverse=True)
print(my_list) 
#nested lists to represent a matrix 

1. Creating a matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
2. Accessing elements:
# Accessing a single element
element = matrix[0][0]  # accessing the element in the first row and first column
print(element)  # Output: 1
# Accessing a row
row = matrix[1]
print(row)  # Output: [4, 5, 6]
# Accessing a column
column = [row[2] for row in matrix]  # extracting the third column
print(column)  # Output: [3, 6, 9]

3. Traversing through the matrix:
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # to move to the next line after printing each row

Output:

1 2 3 
4 5 6 
7 8 9 


4. Modifying elements:

matrix[1][1] = 0  # changing the element at the second row and second column to 0
print(matrix)

Output:

[[1, 2, 3], [4, 0, 6], [7, 8, 9]]


5. Matrix operations:
You can perform various matrix operations using nested loops or list comprehensions, such as addition, multiplication, etc. For example:

# Matrix addition
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result = [[matrix_a[i][j] + matrix_b[i][j] 
for j in range(len(matrix_a[0]))] 
for i in range(len(matrix_a))]
print(result)  # Output: [[6, 8], [10, 12]]

####TUPLE DATA STRUCTURE
#CREATION
1. Using parentheses:
my_tuple = (1, 2, 3, 4, 5)
2. Using the tuple() constructor:
my_tuple = tuple([1, 2, 3, 4, 5])
3. Creating an empty tuple:
empty_tuple = ()
4. Creating a tuple with a single element:
single_element_tuple = (1,)  
# Note the comma after the single element
5. Using a tuple literal:
another_tuple = 1, 2, 3, 4, 5

####ACCESSING TUPLE

my_tuple = (10, 20, 30, 40, 50)

# Accessing individual elements
first_element = my_tuple[0]
print(first_element)  # Output: 10

third_element = my_tuple[2]
print(third_element)  # Output: 30

# Accessing elements using negative indexing
last_element = my_tuple[-1]
print(last_element)  # Output: 50

second_last_element = my_tuple[-2]
print(second_last_element)  # Output: 40

my_tuple = (10, 20, 30, 40, 50)

# Slicing to access multiple elements
subset = my_tuple[1:4]
print(subset)  # Output: (20, 30, 40)

# Accessing elements with steps
elements_with_step = my_tuple[::2]
print(elements_with_step)  # Output: (10, 30, 50)

###FUNCTIONS
1. len(): Returns the number of elements in the tuple.
    python
    my_tuple = (1, 2, 3, 4, 5)
    length = len(my_tuple)
    print(length)  # Output: 5
    

2. count(): Returns the number of occurrences of a specified element in the tuple.
    python
    my_tuple = (1, 2, 2, 3, 2, 4)
    count = my_tuple.count(2)
    print(count)  # Output: 3
    

3. index(): Returns the index of the first occurrence of a specified element in the tuple.
    python
    my_tuple = (1, 2, 3, 4, 5)
    index = my_tuple.index(3)
    print(index)  # Output: 2 (index of element 3)
    

4. sorted(): Returns a new sorted list from the elements of the tuple.
    python
    my_tuple = (3, 1, 4, 1, 5, 9, 2)
    sorted_tuple = sorted(my_tuple)
    print(sorted_tuple)  # Output: [1, 1, 2, 3, 4, 5, 9]
    

5. min() and max(): Returns the smallest and largest elements in the tuple, respectively.
    python
    my_tuple = (3, 1, 4, 1, 5, 9, 2)
    min_value = min(my_tuple)
    max_value = max(my_tuple)
    print(min_value, max_value)  # Output: 1 9
    

6. Comparison (cmp()): 
There's no direct equivalent of the cmp() 
function in Python 3 for tuples. In Python 2, 
cmp() was used to compare two objects. 

In Python 3, you can use comparison operators like 
<, >, <=, >=, and == directly to compare
 tuples.

#CREATE SET  {}
# Example 1: Creating a set of numbers
number_set = {1, 2, 3, 4, 5}
print(number_set)  # Output: {1, 2, 3, 4, 5}

# Example 2: Creating a set of strings
string_set = {"apple", "banana", "orange", "kiwi"}
print(string_set)  # Output: {'banana', 'kiwi', 'apple', 'orange'}

# Example 3: Creating a set from a list (removes duplicates)
list_of_numbers = [1, 2, 3, 3, 4, 4, 5]
set_from_list = set(list_of_numbers)
print(set_from_list)  # Output: {1, 2, 3, 4, 5}

# Example 4: Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

###ACCESSING
# Example 1: Checking for membership
fruits = {"apple", "banana", "orange", "kiwi"}
# Using the 'in' operator to check if an element is in the set
print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False

# Example 2: Iterating over elements
for i in fruits:
    print(i)

# Example 3: Using the 'in' operator with conditional statements
if "kiwi" in fruits:
    print("Kiwi is in the set.")
else:
    print("Kiwi is not in the set.")

# Example 4: Converting the set to a list or tuple for indexing (not recommended due to unordered nature)
# Note: This approach is not reliable as the order is not guaranteed in a set.
fruits_list = list(fruits)
print(fruits_list[0])  # Output: Randomly chosen element

# Example 5: Using the 'pop()' method to remove and return a random element
random_fruit = fruits.pop()
print("Randomly chosen fruit:", random_fruit)

# Example 6: Using the 'remove()' method to remove a specific element
fruits.remove("banana")
print(fruits)  # Output: {'orange', 'kiwi', 'apple'}


###SET FUNCTIONS
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set = {1, 2, 3}
my_set.update({4, 5, 6})
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set = {1, 2, 3}
copied_set = my_set.copy()

my_set = {1, 2, 3}
popped_element = my_set.pop()

my_set = {1, 2, 3}
my_set.remove(2)

my_set = {1, 2, 3}
my_set.discard(2)

my_set = {1, 2, 3}
my_set.clear()
##MATHEMATICAL OPERATIONS
# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union: Returns a new set containing all unique 
#elements from both sets
union_set = set1.union(set2)
print("Union:", union_set)  
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: Returns a new set containing elements that are common to both sets
inter = set1.intersection(set2)
print(inter)  # Output: {4, 5}

# Difference: Returns a new set 
#containing elements that are present
 #in the first set but not in the second set
dif = set1.difference(set2)
print(dif)  # Output: {1, 2, 3}

# Symmetric Difference: Returns a new set containing elements that are present in either of the sets, but not in both
symm = set1.symmetric_difference(set2)
print(symmetric_difference_set)  
# Output: {1, 2, 3, 6, 7, 8}


'''DICTIONARY CREATION'''
# Example 1: Creating a dictionary with literal 
syntax
my_dict = {"name": "Alice", "age": 30, 
"city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Example 2: Creating a dictionary using the dict() 
#constructor
another_dict = dict(name="Bob", age=25, 
city="Los Angeles")
print(another_dict)  # Output: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

# Example 3: Creating a dictionary from 
#key-value pairs using zip() function
keys = ["a", "b", "c"]
values = [1, 2, 3]
x = dict(zip(keys, values))
print(x)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Example 4: Creating an empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}



'''ACCESSING'''
my_dict = {"name": "Alice", "age": 30, 
"city": "New York"}
# Accessing value by key
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30

# Using the get() method
print(my_dict.get("city"))      # Output: New York
print(my_dict.get("gender"))    # Output: None
print(my_dict.get("gender", "Unknown"))  
# Output: Unknown (with default value)

my_dict = {"name": "Alice", "age": 30, 
"city": "New York"}
# Iterating over keys
for key in my_dict:
    print(key, ":", my_dict[key])

# Using the items() method
for key, value in my_dict.items():
    print(key, ":", value)

'''FUNCTIONS'''
dict(): Creates a new dictionary. 
You can pass key-value pairs as arguments or pass an iterable of key-value pairs.

my_dict = 
dict(name="Alice", age=30, city="New York")

len(): Returns the number of items 
(key-value pairs) in the dictionary.

num_items = len(my_dict)

'''Methods:'''
clear(): Removes all items from the dictionary.
my_dict.clear()

get(): Returns the value for the specified key. 
If the key is not found, 
it returns a default value (None by default).
age = my_dict.get("age")

pop(): Removes the item with the specified key 
and returns its value. Raises a KeyError 
if the key is not found.
age = my_dict.pop("age")


popitem(): Removes and returns an arbitrary 
key-value pair from the dictionary as a tuple. 
Raises a KeyError if the dictionary is empty.
item = my_dict.popitem()

keys(): Returns a view object that displays a 
list of all the keys in the dictionary.
all_keys = my_dict.keys()

values(): Returns a view object that displays 
a list of all the values in the dictionary.
all_values = my_dict.values()

items(): Returns a view object that displays 
a list of all the key-value tuple pairs 
in the dictionary.
all_items = my_dict.items()


copy(): Returns a shallow copy of the dictionary.

copied_dict = my_dict.copy()


setdefault(): Returns the value of the 
specified key. If the key does not exist, 
inserts the key with a specified value 
(None by default).
age = my_dict.setdefault("age", 0)

update(): Updates the dictionary with 
the specified key-value pairs from another 
dictionary or iterable.

my_dict.update({"city": "Los Angeles", 
"gender": "female"})

#matrix
A matrix is a 2D array where each element 
is of strictly the same size. 

'''To create a matrix we will be using the 
"NumPy package."'''
#NumPy
Numpy is a general-purpose array-processing 
package. 
It provides a high-performance multidimensional 
array object, and tools for working with 
these arrays. 
It is the fundamental package for scientific 
computing with Python.
Besides its obvious scientific uses, 
Numpy can also be used as an efficient 
multi-dimensional container of generic data.

#example
import numpy as np
a = np.array([[1,2,3,4],[4,55,1,2],
              [8,3,20,19],[11,2,22,21]])
m = np.reshape(a,(4, 4))
print(m)
# Accessing element
print("\nAccessing Elements")
print(a[1])
print(a[2][0])
# Adding Element
m = np.append(m,[[1, 15,13,11]],0)
print("\nAdding Element")
print(m)
# Deleting Element
m = np.delete(m,[1],0)
print("\nDeleting Element")
print(m)


'''Linked List'''
A linked list is a linear data structure, 
in which the elements are not stored at 
contiguous memory locations. 

The elements in a linked list are linked 
using pointers as shown in the below image:

A linked list is represented by a pointer 
to the first node of the linked list. 
The first node is called the head. 
If the linked list is empty, 
then the value of the head is NULL. 

Each node in a list consists of at 
least two parts:
1. Data
2. Pointer (Or Reference) to the next node

#example:
# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize
                        # next as null
class LinkedList:# Linked List class
 # Function to initialize the LinkedList object
    def __init__(self):
        self.head = None

'''# A simple Python program to introduce a 
linked list
'''
class Node:# Node class
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
# Code execution starts here
if __name__=='__main__'
    # Start with the empty list
    llist = LinkedList()

    

    '''
    Three nodes have been created.
    We have references to these three 
    blocks as head,
    second and third'''
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    '''llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | None |     | 2 | None |     | 3 | None |
    +----+------+     +----+------+     +----+------+
    '''

    llist.head.next = second; 
    # Link first node with second

    '''
    Now next of first Node refers to second. 
    So they both are linked.

    llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | o-------->| 2 | null |     | 3 | null |
    +----+------+     +----+------+     +----+------+
    '''

    '''
    Now next of second Node refers to third. So all three
    nodes are linked.

    llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | o-------->| 2 | o-------->| 3 | null |
    +----+------+     +----+------+     +----+------+
    '''
second.next = third; 
    # Link second node with the third node
    
    
'''# A simple Python program for traversal 
of a linked list
'''
class Node:# Node class
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None #Initializ next as null
class LinkedList: #class
    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked 
    #list starting from head
    def printList(self): #display function
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
# Code execution starts here
if __name__=='__main__':
    # Start with the empty list
    list1 = LinkedList()
    list1.head = Node(1)
    second = Node(2)
    third = Node(3)

    list1.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node

    list1.printList()


#stack 
stack = []
# append() function to push
# element in the stack
stack.append(10)
stack.append(20)
stack.append(30)

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

'''Python3 program to check for balanced 
brackets.function to check if brackets 
are balanced'''
def areBracketsBalanced(expr):
	stack = []
	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:

			# Push the element in the stack
			stack.append(char)
		else:
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False
	# Check Empty Stack
	if stack:
		return False
	return True
# Driver Code
if __name__ == "__main__":
	expr = "{()}[]"

	# Function call
	if areBracketsBalanced(expr):
		print("Balanced")
	else:
		print("Not Balanced")

'''Python program to evaluate value of 
a postfix expression
 '''
# Class to convert the expression
class Evaluate:
	# Constructor to initialize the class variables
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		
		# This array is used a stack
		self.array = []

	# Check if the stack is empty
	def isEmpty(self):
		return True if self.top == -1 else False

	# Return the value of the top of the stack
	def peek(self):
		return self.array[-1]

	# Pop the element from the stack
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"

	# Push the element to the stack
	def push(self, op):
		self.top += 1
		self.array.append(op)

	def evaluatePostfix(self, exp):
		# Iterate over the expression for conversion
		for i in exp:

			# If the scanned character is an operand
			# (number here) push it to the stack
			if i.isdigit():
				self.push(i)

			# If the scanned character is an operator,
			# pop two elements from stack and apply it.
			else:
				val1 = self.pop()
				val2 = self.pop()
				self.push(str(eval(val2 + i + val1)))

		return int(self.pop())
# Driver code
if __name__ == '__main__':
	exp = "231*+9-"
	obj = Evaluate(len(exp))
	# Function call
	print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))

###Queue
'''As a stack, the queue is a linear data 
structure that stores items in a First 
In First Out (FIFO) manner'''
# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)
'''Uncommenting print(queue.pop(0))will raise 
and IndexError as the queue is now empty'''

'''Python3 program to implement Queue using 
two stacks with costly enQueue()''' 
class Queue: 
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enQueue(self, x):
		
		# Move all elements from s1 to s2 
		while len(self.s1) != 0: 
			self.s2.append(self.s1[-1]) 
			self.s1.pop()

		# Push item into self.s1 
		self.s1.append(x) 

		# Push everything back to s1 
		while len(self.s2) != 0: 
			self.s1.append(self.s2[-1]) 
			self.s2.pop()

	# Dequeue an item from the queue 
	def deQueue(self):
		
			# if first stack is empty 
		if len(self.s1) == 0: 
			return -1;
	
		# Return top of self.s1 
		x = self.s1[-1] 
		self.s1.pop() 
		return x

# Driver code 
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1) 
	q.enQueue(2) 
	q.enQueue(3) 
	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())

'''Program to implement a stack using
two queues'''

from _collections import deque
class Stack:
    def __init__(self):

        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):

        # Push x first in empty q2
        self.q2.append(x)

        # Push all the remaining
        # elements in q1 to q2.
        while (self.q1):
            self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):

        # if no elements are there in q1
        if self.q1:
            self.q1.popleft()

    def top(self):
        if (self.q1):
            return self.q1[0]
        return None
    def size(self):
        return len(self.q1)
# Driver Code
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
    print("current size: ", s.size())
'''program to implement stack using a 
single queue '''
q = []
# append operation 
def append(val):
	# get previous size of queue 
	size = len(q)
	# Add current element 
	q.append(val);
	for i in range(size):
		x = q.pop(0); 
		q.append(x); 
# Removes the top element 
def pop():
	if (len(q) == 0):
		print("No elements"); 
		return -1; 
	x = q.pop(0); 
	return x; 
# Returns top of stack 
def top():
	if(len(q) == 0):
		return -1; 
	return q[-1]
# Returns true if Stack is empty else false 
def isEmpty():
	return len(q)==0; 
# Driver program to test above methods 
if __name__=='__main__':
	s = []
	s.append(10); 
	s.append(20); 
	print("Top element :" + str(s[-1])); 
	s.pop(); 
	s.append(30); 
	s.pop(); 
	print("Top element :" + str(s[-1]));
	
'''Binary Tree'''
A binary tree is a tree whose elements 
can have almost two children. 
Since each element in a binary tree 
can have only 2 children, we typically 
name them the left and right children. 
A Binary Tree node contains the following 
parts.:
    Data
    Pointer to left child
    Pointer to the right child

'''A Python class that represents an 
individual node in a Binary Tree'''
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

'''Python program to introduce Binary Tree'''

# A class that represents an individual 
#node in a Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
# create root
root = Node(1)
 ''' 1
    / \
    None None'''
root.left     = Node(2);
root.right     = Node(3);
  '''    1
        / \
     2   3
    / \ / \
None None None None'''
root.left.left = Node(4);
'''4 becomes left child of 2
        1
    /     \
     2       3
    / \     / \
4 None None None
/ \
None None'''

'''Binary Search Tree'''
Binary Search Tree is a node-based binary 
tree data structure that has the 
following properties:

The left subtree of a node contains 
only nodes with keys lesser than the node’s 
key.

The right subtree of a node contains 
only nodes with keys greater than the 
node’s key.

The left and right subtree each must 
also be a binary search tree.

#Searching Element
1. Start from the root.

2. Compare the searching element with root, 
    if less than root, then recurse for left, 
    else recurse for right.

3. If the element to search is found anywhere,
    return true, else return false.
    
'''A utility function to search a given key 
in BST'''

def search(root,key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
    # Key is smaller than root's key
    return search(root.left,key)

'''Python program to demonstrate
insert operation in binary search tree'''
# A utility class that represents
# an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
# A utility function to insert
# a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
# Driver program to test the above functions
# 50
# /     \
# 30     70
# / \ / \
# 20 40 60 80
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
# Print inorder traversal of the BST
inorder(r)

'''Graphs'''
Graph can be defined as a Graph 
consisting of a finite set of vertices
(or nodes) and a set of edges that 
connect a pair of nodes.

In the above Graph, the set of vertices 
V = {0,1,2,3,4} and the 
set of edges E = {01, 12, 23, 34, 04, 14, 13}. 

#The following two are the most commonly 
#used representations of a graph.
Adjacency Matrix
Adjacency List


'''A simple representation of graph using
 Adjacency Matrix'''
 
class Graph:
    def __init__(self,numvertex):
        self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {}
        self.verticeslist =[0]*numvertex

    def set_vertex(self,vtx,id):
        if 0<=vtx<=self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id

    def set_edge(self,frm,to,cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost
        
        # for directed graph do not add this
        self.adjMatrix[to][frm] = cost

    def get_vertex(self):
        return self.verticeslist

    def get_edges(self):
        edges=[]
        for i in range (self.numvertex):
            for j in range (self.numvertex):
                if (self.adjMatrix[i][j]!=-1):
                    edges.append((self.verticeslist[i],self.verticeslist[j],self.adjMatrix[i][j]))
        return edges
        
    def get_matrix(self):
        return self.adjMatrix

G =Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)

print("Vertices of Graph")
print(G.get_vertex())

print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())

'''A class to represent the adjacency 
list of the node'''

class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
    
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


# Driver program to the above graph class
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()



