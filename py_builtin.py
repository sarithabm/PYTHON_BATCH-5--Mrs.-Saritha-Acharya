#Python all() Function
The python all() function accepts an iterable 
object (such as list, dictionary, etc.). 
.Returns true if all items in passed iterable 
are true.
.Otherwise, it returns False. 
.If the iterable object is empty returns True.

Python all() Function Example
# all values true  
k = [1, 3, 4, 6]  
print(all(k))  
# all values false  
k = [0, False]  
print(all(k))  
# one false value  
k = [1, 3, 7, 0]  
print(all(k))   
# one true value  
k = [0, False, 5]  
print(all(k))  
  
# empty iterable  
k = []  
print(all(k))  
Output:

True
False
False
False
True

#Python any() Function
The python any() function returns true if any 
item in an iterable is true. Otherwise, it returns False.
list = [4, 3, 2, 0]                              
print(any(list))                                   
l = [0, False]  
print(any(l))  
l = [0, False, 5]  
print(any(l))  
l = []  
print(any(l))  
Output:
True
False
True
False

#Python any() Function
The python any() function returns true if any 
item in an iterable is true. Otherwise, it returns False.

a = [4, 3, 2, 0]                              
print(any(a))                                   
a = [0, False]  
print(any(a))  
a = [0, False, 5]  
print(any(a))  
a = []  
print(any(a))  

Output:
True
False
True
False

#Python bin() Function
The python bin() function is used to return the 
binary representation of a specified integer. 
A result always starts with the prefix 0b.

x =  10  
y =  bin(x)  
print (y)  

0b1010

#Python bool()
The python bool() converts a value to 
boolean(True or False) using the standard 
truth testing procedure.

test1 = []  
print(bool(test1))  
test1 = [0]  
print(bool(test1))  
test1 = 0.0  
print(bool(test1))  
test1 = None  
print(bool(test1))  
test1 = True  
print(bool(test1))  
test1 = 'Easy string'  
print(bool(test1))  

[] is False
[0] is True
0.0 is False
None is False
True is True
Easy string is True


#Python bytes()
The python bytes() in Python is used for 
returning a bytes object. 
It is an immutable version of the bytearray() function.
It can create empty bytes object of the specified size.

string = "Hello World."  
array = bytes(string, 'utf-8')  
print(array) 

#Python callable() Function
A python callable() function in Python is 
something that can be called. 
This built-in function checks and returns 
true if the object passed appears to be callable, 
otherwise false.

x = 8  
print(callable(x)) 


def my_function():
    pass
x = my_function
print(callable(x))  

class CallableClass:
    def __call__(self):
        print("I am callable!")
x = CallableClass()
print(callable(x))  # This will print True

#Python compile() Function
The python compile() function takes source code 
as input and returns a code object which can 
later be executed by exec() function.

# compile string source to code  
a = 'x=5\ny=10\nprint("sum =",x+y)'  
b = compile(a, 'sum.py', 'exec')  
print(type(b))  
exec(b)  
exec(x)  

<class 'code'>
sum = 15

#
Python exec() Function
The python exec() function is used for the 
dynamic execution of Python program which can 
either be a string or object code and it accepts 
large blocks of code, unlike the eval() 
function which only accepts a single expression.

x = 8  
exec('print(x==8)')  
exec('print(x+4)')  
Output:

True
12

#Python sum() Function
As the name says, python sum() function is used 
to get the sum of numbers of an iterable, i.e., list.

s = sum([1, 2,4 ])  
print(s)  
s = sum([1, 2, 4], 10)  
print(s)  


7,17

#Python bytearray()
The python bytearray() returns a bytearray object 
and can convert objects into bytearray objects, 
or create an empty bytearray object of the specified 
size.

string = "Python is a programming language."  
arr = bytearray(string, 'utf-8')  
# string with encoding 'utf-8'  
print(arr)  

Output:
bytearray(b'Python is a programming language.')

#Python eval() Function
The python eval() function parses the expression 
passed to it and runs python expression(code) 
within the program.

x = 8  
print(eval('x + 1'))  

#Python format() Function
The python format() function returns a 
formatted representation of the given value.  
# integer  
print(format(123, "d"))  
# float arguments  
print(format(123.4567898, "f"))  
# binary format  
print(format(12, "b")) 


 
#Python frozenset()
The python frozenset() function returns an 
immutable frozenset object initialized with 
elements from the given iterable.

letters = ('m', 'r', 'o', 't', 's') 
print(letters.add(100)) 
fSet = frozenset(letters)  
print(fSet)  
print(frozenset()) 
print(fset.add(200)) 

The frozenset type in Python is a powerful tool 
for creating immutable sets. 
Its immutability make it suitable for use as 
dictionary keys and set elements, while ensuring 
data integrity and potentially improving performance. 

Use frozenset whenever you need the functionality of 
a set but with the added guarantee that the set 
cannot be modified.

#Ensuring Immutability:
c = frozenset(["option1", "option2", "option3"])
c.add("option4")  
print(c)
# Using in Sets:Create a set of frozensets
fs = {frozenset([1, 2]), frozenset([3, 4]), 
frozenset([1, 2])}
print(fs)  
#Using as Dictionary Keys:
p = {
frozenset(["read", "write"]): "Read-Write Access",
frozenset(["read"]): "Read-Only Access"
}
print(p[frozenset(["read"])])  
print(p[frozenset(["read", "write"])])  

#Characteristics of frozenset
#1. Immutability:
Once a frozenset is created, it cannot be 
changed (no adding, removing, or updating elements).
This makes frozenset hashable, meaning it can be 
used as a key in dictionaries or stored in other sets.

#2. Uniqueness:
Like sets, frozensets automatically eliminate 
duplicate elements.

#3. Set Operations:
frozensets support the same set operations 
as sets, such as union, intersection, difference, 
and symmetric difference.

####Python iter() Function
The python iter() function is used to return 
an iterator object. It creates an object which 
can be iterated one element at a time.

list = [1,2,3,4,5]  
z  = iter(list)  
print(next(z))   
print(next(z))    
print(next(z))  
print(next(z))
print(next(z))  

#Python next() Function
Python next() function is used to fetch next item from the 
collection. 
It takes two arguments, i.e., an iterator and a default value, 
and returns an element.
This method calls on iterator and throws an error 
if no item is present. 
To avoid the error, we can set a default value.

number = iter([256, 32, 82]) # Creating iterator  
# Calling function  
a = next(number)   
print(a)  
b = next(number)  
print(b)  
c = next(number)  
print(c)  

#Python memoryview() Function
The python memoryview() function returns a 
memoryview object of the given argument.

r = bytearray('ABC', 'utf-8')  
mv = memoryview(r)  
print(mv[0])  
print(bytes(mv[0:2]))  
print(list(mv[0:3]))  

Output:

65
b'AB'
[65, 66, 67]

#Python object()
The python object() returns an empty object. 
It is a base for all the classes and holds the 
built-in properties and methods which are default 
for all the classes.

python = object()  
print(type(python))  
print(dir(python)) 

#Python dir() Function
Python dir() function returns the list of names 
in the current local scope. If the object on which
 method is called has a method named __dir__(), 
 this method will be called and must return the list 
 of attributes. It takes a single object type argument.

att = dir()  
print(att)  

#Python open() Function
The python open() function opens the file 
and returns a corresponding file object.

f = open("python.txt")  
f = open("C:/Python33/README.txt")   

#Python complex()
Python complex() function is used to convert 
numbers or string into a complex number. 

a = complex(1)  
b = complex(1,2)
print(a)  
print(b)  

#Python divmod() Function

result = divmod(10,2)  
print(result)  

#Python filter() Function
Python filter() function is used to get filtered 
elements. This function takes two arguments,
 first is a function and the second is iterable. 
 The filter function returns a sequence of those 
 elements of iterable object for which function 
 returns true value.

The first argument can be none, if the function 
is not available and returns only elements that are 
true.

filter(function, arg)

# Python filter() function example  
def filterdata(x):  
    if x>5:  
        return x  
# Calling function  
result = filter(filterdata,(1,2,6))  
print(list(result))  

# map()
#syntax:
map(function, iterable, ...)
#map(arg1, arg2,....)

function: A function that will be applied to each item 
of the iterable.
iterable: An iterable (e.g., list, tuple) whose elements 
are to be mapped.
... Additional iterables (optional). If more than one 
iterable is provided, function should 
accept that many arguments.

1. def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
a = map(square, numbers)
# Convert the map object to a list to see the results
z = list(a)
print(z)  

2. numbers = [1, 2, 3, 4, 5]
z = map(lambda x: x * x, numbers)
# Convert the map object to a list to see the results
a = list(z)
print(a) 

3.def add(x, y):
    return x + y
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
a = map(add, numbers1, numbers2)
z = list(a)
print(z)  

#Lazy Evaluation of map()
The map() function returns an iterator, 
which means it uses lazy evaluation. 
The function is not actually applied to the items 
until you iterate over the map object. 
This can be useful for performance and memory 
efficiency when working with large datasets.

def to_upper(char):
    return char.upper()
string = "hello"
z = map(to_upper, string)
# Convert the map object to a list to see the results
a = ''.join(z)
print(a)  



#
Python help() Function
Python help() function is used to get help related 
to the object passed during the call. 
It takes an optional parameter and returns help 
information. If no argument is given, it shows the 
Python help console. 
It internally calls python's help function.

# Calling function  
info = help() # No argument  
print(info)  

#Python hex() Function
result = hex(1)   
result2 = hex(342)   
print(result)  
print(result2)  

#Python id() Function
Python id() function returns the identity of an object. 
This is an integer which is guaranteed to be unique. 
This function takes an argument as an object and 
returns a unique integer number which 
represents identity.
Two objects with non-overlapping lifetimes may 
have the same id() value.

# Calling function  
val = id("pythonprogram") # string object  
val2 = id(1200) # integer object  
val3 = id([25,336,95,236,92,3225]) # List object  
print(val)  
print(val2)  
print(val3) 

#int(), float(), str(), oct()
val = int(10) # integer value  
val2 = int(10.52) # float value  
val3 = int('10') # string value 
val4 = float('10') # string value  
print(val, val2, val3,val4) 
val5 = oct(10)  
print(val5) 

#Python ord() Function
The python ord() function returns an integer representing 
Unicode code point for the given Unicode character.

# Code point of an integer  
print(ord('8'))  
# Code point of an alphabet   
print(ord('R'))  
# Code point of a character  
print(ord('&'))  
Output:

56
82
38

#pow()
print(pow(4, 2))    # positive x, positive y (x**y)  
print(pow(-4, 2))   # negative x, positive y  
print(pow(4, -2))   # positive x, negative y (x**-y)  
print(pow(-4, -2))  # negative x, negative y  

#Python vars() function
The python vars() function returns the __dict__ 
attribute of the given object.

class Nitte:  
  def __init__(self, x = 7, y = 9):  
    self.x = x  
    self.y = y  
a = Nitte()  
print(vars(a))  

Output:
{'x': 7,'y': 9}


#Python isinstance() Function
Python isinstance() function is used to check whether 
the given object is an instance of that class. 
If the object belongs to the class, it returns true. 
Otherwise returns False. 
It also returns true if the class is a subclass.

The isinstance() function takes two arguments, i.e., 
object and classinfo, and then it returns either True or False.
#syntax:
isinstance(object,classinfo)


class Student:  
    id = 101  
    name = "John"  
    def __init__(self, id, name):  
        self.id=id  
        self.name=name  
z = Student(1010,"John")  
lst = [12,34,5,6,767]  
# Calling function   
print(isinstance(z, Student)) # isinstance of Student class  
print(isinstance(lst, Student)) 
 
Output:
True
False


#Python issubclass() Function
The python issubclass() function returns true if 
object 
argument(first argument) is a subclass of second class(second 
argument).

class Rectangle:  
  def __init__(a):  
    print(a)  
class Square(Rectangle):  
  def __init__(self):  
    Rectangle.__init__('square')     
print(issubclass(Square, Rectangle))  
print(issubclass(Square, list))  
print(issubclass(Square, (list, Rectangle)))  
print(issubclass(Rectangle, (list, Rectangle)))  

Output:
True
False
True
True

#Python reversed() Function
The python reversed() function returns the reversed 
iterator of the given sequence.

# for string  
String = 'Java'  
print(list(reversed(String)))  
# for tuple  
Tuple = ('J', 'a', 'v', 'a')  
print(list(reversed(Tuple)))  
# for range  
Range = range(8, 12)  
print(list(reversed(Range)))   
# for list  
List = [1, 2, 7, 5]  
print(list(reversed(List)))  


#Python hash() Function
Python hash() function is used to get the hash value 
of an object. 
Python calculates the hash value by using the hash algorithm. 
The hash values are integers and used to compare dictionary 
keys during a dictionary lookup. 
We can hash only the types which are given below:
Hashable types: * bool * int * long * float * string * Unicode * 
tuple * code object.


# Calling function  
result = hash(21) # integer value  
result2 = hash(22.2) # decimal value  
# Displaying result  
print(result)  
print(result2)  

Output:
21
461168601842737174

'''built-in functions often used in 
functional programming paradigms.'''

1. map(function, iterable):
   - Applies the given function to each item 
   in the iterable (such as a list) and 
   returns a new iterator with the results.
   - It takes two parameters: a function 
   and an iterable.
   - The function parameter is the function 
   to apply to each item in the iterable.
   - The iterable parameter is a sequence 
   (like list, tuple, etc.) 
   whose items will be processed by the function.

   Example:
   python
   # Doubling each number in a list
   numbers = [1, 2, 3, 4, 5]
   doubled = map(lambda x: x * 2, numbers)
   print(list(doubled))  
   # Output: [2, 4, 6, 8, 10]
   

2. filter(function, iterable):
   - Filters the elements of an iterable based 
   on whether the function returns True or False.
   - It takes two parameters: a function and 
   an iterable.
   - The function parameter is a function 
   that returns True or False.
   - The iterable parameter is a sequence 
   whose elements are filtered based on the 
   function.

   Example:
   python
   # Filtering even numbers from a list
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   evens = filter(lambda x: x % 2 == 0, numbers)
   print(list(evens))  # Output: [2, 4, 6, 8, 10]
   

3. reduce(function, iterable [, initializer]):
   - Applies a rolling computation to sequential 
   pairs of values in an iterable.
   - It takes three parameters: a function, 
   an iterable, and an optional initializer.
   - The function parameter is a function 
   that takes two arguments and returns a 
   single value.
   - The iterable parameter is a sequence 
   of values to be reduced.
   - The initializer parameter is an optional 
   initial value for the reduction.

   Note: In Python 3, reduce() is no longer a built-in function and has been moved to the functools module.

   Example:
   python
   from functools import reduce
   
   # Summing all the numbers in a list
   numbers = [1, 2, 3, 4, 5]
   total = reduce(lambda x, y: x + y, numbers)
   print(total)  # Output: 15
   

#include <stdio.h>  
#pragma pack(1)  
struct base  
{  
    int a;  
    char b;  
    double c;  
};  
int main()  
{  
  struct base var; // variable declaration of type base  
  // Displaying the size of the structure base  
  printf("The size of the var is : %d", sizeof(var));  
return 0;  
}  


#include <stdio.h>  
  
struct base  
{  
    int a;  
    char b;  
    double c;  
}__attribute__((packed));  ;  
int main()  
{  
  struct base var; // variable declaration of type base  
  // Displaying the size of the structure base  
  printf("The size of the var is : %d", sizeof(var));  
  
    return 0;  
}  


// C Program to demonstrate the structure padding property 
#include <stdio.h> 

// Alignment requirements 
// (typical 64 bit machine) 

// char     1 byte 
// short int  2 bytes 
// int     4 bytes 
// double    8 bytes 

// structure A 
typedef struct structa_tag { 
	char c; 
	short int s; 
} structa_t; 

// structure B 
typedef struct structb_tag { 
	short int s; 
	char c; 
	int i; 
} structb_t; 

// structure C 
typedef struct structc_tag { 
	char c; 
	double d; 
	int s; 
} structc_t; 

// structure D 
typedef struct structd_tag { 
	double d; 
	int s; 
	char c; 
} structd_t; 

int main() 
{ 
	printf("sizeof(structa_t) = %lu\n", sizeof(structa_t)); 
	printf("sizeof(structb_t) = %lu\n", sizeof(structb_t)); 
	printf("sizeof(structc_t) = %lu\n", sizeof(structc_t)); 
	printf("sizeof(structd_t) = %lu\n", sizeof(structd_t)); 

	return 0; 
}


#Importing Standard Library Modules
import math
import os
import sys
import datetime
import random

#Importing Specific Functions or Classes from Modules
from math import sqrt, pi
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from itertools import permutations, combinations

#Importing Modules with Aliases
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

#Importing Custom Modules
#importing one module into another:

#Creating a Module:
# my_module.py
def greet(name):
    return f"Hello, {name}!"
def add(a, b):
    return a + b
    
1. Using import Statement:
import my_module

print(my_module.greet("Alice"))
print(my_module.add(5, 3))

2. Using from...import Statement:

from my_module import greet, add
print(greet("Bob"))
print(add(7, 2))

#Random Number
import random
a = random.randint(1, 100)
print(a)
import random
random_float = random.random()
print(random_float)

random_float = random.random()
print(random_float)

mu = 0  # mean
sigma = 1  # standard deviation
random_gaussian = random.gauss(mu, sigma)
print(random_gaussian)

#Generate a Random Choice from a List
items = ['apple', 'banana', 'cherry', 'date']
z = random.choice(items)
print(z)

#Generate a Random Sample from a List
items = ['apple', 'banana', 'cherry', 'date']
z1 = random.sample(items, 2)
print(z1)

#Shuffle a List Randomly
items = ['apple', 'banana', 'cherry', 'date']
random.shuffle(items)
print(items)

#date time syntax
class datetime.date(year, month, day)

#
# import the date class
from datetime import date
my_date = date(1996, 12, 11)
print(my_date)

# Python program to print current date
from datetime import date
today = date.today()# function of date class
print("Today's date is", today)

# date object of today's date
from datetime import date
a = date.today() 
print("Current year:", a.year)
print("Current month:", a.month)
print("Current day:", a.day)

# Getting Datetime from timestamp
from datetime import datetime

a = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", a)

#date to string 
from datetime import date
a = date.today() # function of date class
# Converting the date to the string
z = date.isoformat(a)
print("String Representation", z)
print(type(z))

# Python program to demonstrate time class
 
from datetime import time
# calling the constructor
my_time = time(13, 24, 56)
print(my_time)
# calling constructor with 1 argument
my_time = time(minute=12)
print("\nTime with one argument", my_time)
my_time = time()  #constructor with 0 arg
print("\nTime without argument", my_time)

#Get hours, minutes, seconds, and microseconds

from datetime import time

Time = time(11, 34, 56)

print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

#Convert Time object to String
from datetime import time
Time = time(12,24,36,1212)
Str = Time.isoformat() # Convert Time obj-string
print("String Representation:", Str)
print(type(Str))

'''Python Datetime class'''
from datetime import datetime
# Initializing constructor
a = datetime(1999, 12, 12)
print(a)
# Initializing constructor
# with time parameters as well
a = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(a)

''' Get year, month, hour, minute, and 
timestamp
 '''
from datetime import datetime

a = datetime(1999, 12, 12, 12, 12, 12)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

'''Current date and time'''
from datetime import datetime
# Calling now() function
z = datetime.now()
print(z)

'''Convert Python Datetime to String
'''
from datetime import datetime as dt

# Getting current date and time
now = dt.now()

string = dt.isoformat(now)
print(string)
print(type(string))
'''Python Timedelta Class'''
Python timedelta class is used 
for calculating differences in dates 
and also can be used for date manipulations 
in Python. 

It is one of the easiest ways to perform 
date manipulations.

#
from datetime import datetime, timedelta
# Using current time
for_now = datetime.now()
# printing initial_date
print(str(for_now)) 
# Calculating future dates for two years
after_2yrs = for_now + timedelta(days=730)
after_2days = for_now + timedelta(days=2)
# printing calculated future_dates
print(str(after_2yrs))
print(str(after_2days))
'''Difference between two date and times
'''
## Timedelta function demonstration
from datetime import datetime, timedelta
a = datetime.now()
# printing initial_date
print("initial_date", str(a))
# Some another datetime
final_time = a + \timedelta(days=2)
# printing new final_date
print(str(final_time))
# printing calculated past_dates
print(str(final_time -a))

'''Python Datetime strftime                    
 '''
 from datetime import datetime as dt
# Getting current date and time
a = dt.now()
print("Without formatting", a)

s = a.strftime("%A %m %-Y")
print('\nExample 1:', s)
# Example 2
s = now.strftime("%a %-m %y")
print('\nExample 2:', s)
# Example 3
s = now.strftime("%-I %p %S")
print('\nExample 3:', s)
# Example 4
s = now.strftime("%H:%M:%S")
print('\nExample 4:', s)
'''Python DateTime strptime
The strptime() creates a DateTime 
object from the given string.'''

# import datetime module from datetime
from datetime import datetime

# consider the time stamps from a list in 
#string format DD/MM/YY H:M:S.micros
time_data = ["25/05/99 02:35:8.023", "26/05/99 12:45:0.003",
			"27/05/99 07:35:5.523", "28/05/99 05:15:55.523"]

# format the string in the given format : 
#day/month/year 
# hours/minutes/seconds-micro seconds
format_data = "%d/%m/%y %H:%M:%S.%f"

# Using strptime with datetime we will 
#format string into datetime
for i in time_data:
	print(datetime.strptime(i, format_data))

'''Python DateTime.tzinfo()
'''
import datetime as dt
from dateutil import tz
tz_string = dt.datetime.now(dt.timezone.utc).
astimezone().tzname()
print("datetime.now() :", tz_string)
NYC = tz.gettz('Europe / Berlin')
dt1 = dt.datetime(2022, 5, 21, 12, 0)
dt2 = dt.datetime(2022, 12, 21, 12, 0, 
tzinfo=NYC)

print("Naive Object :", dt1.tzname())
print("Aware Object :", dt2.tzname())

'''Python DateTime timezone
'''
from datetime import datetime
from pytz import timezone
format = "%Y-%m-%d %H:%M:%S %Z%z"
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))

timezones = ['Asia/Kolkata', 'Europe/Kiev', 'America/New_York']

for tzone in timezones:

	# Convert to Asia/Kolkata time zone
	now_asia = now_utc.astimezone(timezone(tzone))
	print(now_asia.strftime(format))