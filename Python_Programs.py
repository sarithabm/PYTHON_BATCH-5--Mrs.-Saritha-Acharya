#Find the Missing Number
Given an array containing N distinct 
numbers taken from 0 to N, find the 
missing number.
def find_missing_number(nums):
    n = len(nums) #5
    total_sum = n * (n + 1) // 2  # Sum of numbers from 0 to N
    array_sum = sum(nums)         # Sum of elements in the array
    return total_sum - array_sum
nums = [3, 0, 1, 5, 4]  # Example array with missing number 2
missing_number = find_missing_number(nums)
print(missing_number)


#FizzBuzz
Print numbers from 1 to N, but print 
"Fizz" for multiples of 3, 
"Buzz" for multiples of 5, 
and "FizzBuzz" for multiples of both 3 and 5.
def fizz_buzz(n):
    for i in range(1, n+1): 
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
n = int(input("Enter a number: ")) 
fizz_buzz(n)

#Factorial
Compute the factorial of a given number 
using iterative and recursive methods.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # Output: 120


#String Reversal
Reverse a string using iterative and 
recursive approaches.
def reverse_string(s):
    return s[::-1]
s = "hello"
print(reverse_string(s))  # Output: "olleh"

### Iterative Approach
def r(s):
    reversed_string = ""
    for i in s:
        reversed_string = i + reversed_string
    return reversed_string
s = "hello"
print(r(s))  # Output: "olleh"

# Recursive Approach
def r(s):
 if len(s) == 0:
   return s
 else:
   return r(s[1:]) + s[0]    
s = "hello"
print(r(s))  # Output: "olleh"

#Anagrams
Check if two strings are anagrams of 
each other.

def an(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    return sorted(str1) == sorted(str2)
str1 = "listen"
str2 = "silent"
print(an(str1, str2))  # Output: True


#Palindrome Check
Check if a given string is a palindrome.
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Example usage:
s = "A man a plan a canal Panama"
print(is_palindrome(s))  # Output: True

#programs
#Check for Anagrams
def anagrams(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    return sorted(str1) == sorted(str2)
str1 = "listen"
str2 = "silent"
print(anagrams(str1, str2))  

#Reverse a String
def reverse(s):
    return s[::-1]
string = input("Enter a string: ")
print(reverse(string))

//kadene's subarray
#include <stdio.h>

// Function to find the subarray with the maximum sum using max_sum and curr_sum
void maxSubArray(int arr[], int n) {
    int max_sum = arr[0]; // Initialize max_sum with the first element of the array
    int curr_sum = arr[0]; // Initialize curr_sum with the first element of the array
    int start = 0; // Initialize start index of the subarray
    int end = 0; // Initialize end index of the subarray
    int tempStart = 0; // Temporary variable to store start index when updating max_sum

    // Iterate through the array
    for (int i = 1; i < n; i++) {
 // Update curr_sum by adding the current element
        curr_sum += arr[i];

        // If the current element itself is greater than the current sum, update the start index
        if (arr[i] > curr_sum) {
            curr_sum = arr[i];
            tempStart = i;
        }

        // Update max_sum if curr_sum becomes greater
        if (curr_sum > max_sum) {
            max_sum = curr_sum;
            start = tempStart;
            end = i;
        }
    }

    printf("Subarray with the maximum sum %d is: ", max_sum);
    for (int i = start; i <= end; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {-2, -3, 4, -1, -2, 1, 5, -3};
    int n = sizeof(arr) / sizeof(arr[0]);
    maxSubArray(arr, n);
    
    
    #validating email
import re
def valid(email):
  pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]
+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None
email = "test@example.com"
print(valid(email))  # Output: True
invalid_email = "test@.com"
print(valid(invalid_email))  # Output: False


#password
re'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])
[A-Za-z\d@$!%*?&]{4,}$

#Explanation of Lookaheads:
(?=.*[a-z]): Ensures the string contains at 
least one lowercase letter.
(?=.*[A-Z]): Ensures the string contains at 
least one uppercase letter.
(?=.*\d): Ensures the string contains at least
 one digit.
(?=.*[@$!%*?&]): Ensures the string contains at 
least one special character.

#
[A-Za-z\d@$!%*?&]{8,}: Matches a sequence of characters 
that are:
Uppercase letters (A-Z)
Lowercase letters (a-z)
Digits (0-9)
Special characters from the set @$!%*?&
The {8,} specifies that the password must be at least
8 characters long.

# Python program to display all the prime numbers within an interval
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           
# Program to check Armstrong numbers in a certain interval
lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)

# Python Program to Remove Punctuations From a String
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

# Program to check if a string is palindrome or not
my_str = 'aIbohPhoBiA'
# make it suitable for caseless comparison
my_str = my_str.casefold()
# reverse the string
rev_str = reversed(my_str)
# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
   
# Program to perform different set operations like in mathematics
# define three sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};
# set union
print("Union of E and N is",E | N)
# set intersection
print("Intersection of E and N is",E & N)
# set difference
print("Difference of E and N is",E - N)
# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)

'''Python Program to Count the Occurrence of an Item in a List
'''
freq = ['a', 1, 'a', 4, 3, 2, 'a'].count('a')
print(freq)

'''Python Program to Measure the Elapsed Time in Python
'''
import time

start = time.time()

print(23*2.3)

end = time.time()
print(end - start)

