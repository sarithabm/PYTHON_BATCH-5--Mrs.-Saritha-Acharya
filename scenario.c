//competitive coding using PYTHON, c,c++

1. //Beautiful Numbers :/
A number is beautiful if the xor sum of the 
digits of the number is strictly 
greater than the average of the minimum and 
maximum digit of the number. 
Given A and B find the count of beautiful numbers 
in the range [A,B].
Since the answer can be very large, output the 
remainder after dividing the answer 
by 10 pow 6+7
Note: The xor sum of the digits of a number is 
the bitwise XOR of all its digits.

Input:

The input consist of two space-separated integers 1≤A≤10 
pow 18
 1≤B≤10 pow 18
Output:

Output number of beautiful integers in range [A,B]
modulo 10 pow 6 + 7
 
Examples:

input
32 35 
output
2
input
10 12
output
2

2. An automobile company manufactures both a 
two wheeler (TW) and 
a four wheeler (FW). 
A company manager wants to make the production 
of both types of 
vehicle 
according to the given data below:

1st data, Total number of vehicle 
(two-wheeler + four-wheeler)
=v =tw+fw
2nd data, Total number of wheels = W
The task is to find how many two-wheelers 
as well as 
four-wheelers need to manufacture 
as per the given data.

Constraints :

2<=W  
W%2=0
V<W
Print “INVALID INPUT” , if inputs did not meet the 
constraints.


Example :

Input :
200  -> Value of V
540   -> Value of W

fw70 tw=130 




1. 70  = (540/2)-200

20070 = 130 
Output :
TW =130 FW=70

2. FW = (W(2 *V))/2

TW = V-FW


M =10

N=3

1+2+4+5+7+8+10 = 37
3+6+9 = 18

37-18=19




//
A Milkman serves milk in packaged bottles of 
varied sizes. 
The possible size of the bottles are 
{1, 5, 7 and 10} litres. 
He wants to supply the desired quantity 
using as fewer bottles
 as possible irrespective of the size. 
 Your objective is to 
help 
him find the minimum number of bottles required to supply the 
given demand for milk.

Input Format:

The first line contains the number of test 
cases N
Next N lines, each contains a positive 
integer Li which 
corresponds to the demand of milk.


Output Format:

For each input Li, print the minimum number of bottles required 
to fulfill the demand



Constraints:

1 <= N <= 1000 Li > 0 1 <= i <= N



Sample Input and Output:
The possible size of the bottles are {1, 5, 7 and 10} litres
i/p:

2

17

65     

o/p:
2    7



// PROGRAM  PASSWORD CHECKER
You are given a function.

int CheckPassword(char str[], int n);

The function accepts string str of size n as 
an argument. 
Implement the function which
returns 1 if given string str is valid 
password else 0.
str is a valid password if it satisfies 
the below conditions.
● At least 4 characters
● At least one numeric digit
● At Least one Capital Letter
● Must not have space or slash (/)
● Starting character must not be a number
Assumption:
Input string will not be empty.
Example:
Input 1:
aA1_67
Input 2:
a987 abC012
Output 1:
1
Output 2:
0

re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.* d)
[a-zA-Z d]{4,}$'

//Valid Parentheses
Problem Statement
Given a string s containing just the 
characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type 
of brackets.
Open brackets must be closed in the correct 
order.

Constraints:
1 ≤ s.length ≤ 104
s consists of parentheses only '()[]{}'.
Examples


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false


//
Given an array of integers A, find the sum 
of min(B), where B ranges over every 
(contiguous) subarray of A.

Since the answer may be large, 
return the answer modulo 10^9 + 7.

Sample I/O:

Example 1
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
Note
1 <= A.length <= 30000
1 <= A[i] <= 30000



Certainly! Let's go through how the algorithm works step by step using the given examples:

Example 1:
Input: n = 19

1. Start with the number 19.
2. Compute the sum of the squares of its digits: 1^2 + 9^2 = 1 + 81 = 82
3. Replace 19 with 82 and repeat the process: 8^2 + 2^2 = 64 + 4 = 68
4. Replace 82 with 68 and repeat: 6^2 + 8^2 = 36 + 64 = 100
5. Replace 68 with 100 and repeat: 1^2 + 0^2 + 0^2 = 1
6. The process ends with 1. Since we reached 1, the number 19 is a happy number.

Example 2:
Input: n = 2

1. Start with the number 2.
2. Compute the sum of the squares of its digits: 2^2 = 4
3. Replace 2 with 4 and repeat: 4^2 = 16
4. Replace 4 with 16 and repeat: 1^2 + 6^2 = 1 + 36 = 37
5. Replace 16 with 37 and repeat: 3^2 + 7^2 = 9 + 49 = 58
6. Replace 37 with 58 and repeat: 5^2 + 8^2 = 25 + 64 = 89
7. Replace 58 with 89 and repeat: 8^2 + 9^2 = 64 + 81 = 145
8. Replace 89 with 145 and repeat: 1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42
9. Replace 145 with 42 and repeat: 4^2 + 2^2 = 16 + 4 = 20
10. Replace 42 with 20 and repeat: 2^2 + 0^2 = 4 + 0 = 4


This algorithm essentially iteratively computes the sum of the squares of the digits of the number until either it reaches 1 (in which case it's a happy number) or it enters a cycle, indicating it's not a happy number.


//JAR 
There is a JAR full of candies for sale at a 
mall counter. JAR has the capacity N, 
that is JAR can contain maximum N candies 
when JAR is full. At any point of time. 
JAR can have M number of Candies where M<=N. 
Candies are served to the customers. 
JAR is never remain empty as when last k 
candies are left. JAR if refilled with new 
candies in such a way that JAR get full.
Write a code to implement above scenario. 
Display JAR at counter with available 
number of candies. Input should be the 
number of candies one customer can order 
at point of time. 
Update the JAR after each purchase and 
display JAR at Counter.

Output should give number of Candies 
sold and updated number of Candies in JAR.

If Input is more than candies in JAR, 
return: “INVALID INPUT”
Given,
N=10, where N is NUMBER OF CANDIES AVAILABLE
K =< 5, where k is number of minimum 
candies that must be inside JAR ever.
Example 1:(N = 10, k =< 5)

Input Value
3  
Output Value
NUMBER OF CANDIES SOLD : 3 
NUMBER OF CANDIES AVAILABLE : 7(5<=5)


Example : (N=10, k<=5)

Input Value
0
Output Value
INVALID INPUT 
NUMBER OF CANDIES LEFT : 10



##Question 14 : Mr. Robot’s Password
Problem Statement – Mr. Robot is making a 
website, in which there is a tab to create 
a password. As other websites, there are 
rules so that the password gets complex 
and none can predict the password for another. 
So he gave some rules like:

At least one numeric digit
At Least one Small/Lowercase Letter
At Least one Capital/Uppercase Letter
Must not have space 
Must not have slash (/)
At least 6 characters
If someone inputs an invalid password, 
the code prints: “Invalid password, try again”.

Otherwise, it prints: “password valid”.

Input Format:

A line with a given string as a password

Output Format:

If someone inputs an invalid password, the code prints: “Invalid password, try again”.
Otherwise, it prints: “password valid”, without the quotation marks.
Constraints:

Number of character in the given string <=10^9
Sample input 1: 

abjnlL09

Sample output 1: 

password valid

Sample input 2: 

jjnaskpk

Sample output 2: 

Invalid password, try again

//Question 10 : Minimum Occurrence
Problem Statement – 
Given a sting , 
return the character that appears 
the minimum number of times in the string. 
The string will contain only ascii characters,
 from the ranges (“a”-”z”,”A”-”Z”,0-9), 
 and case matters . 
 If there is a tie in the minimum number 
 of times a character appears in the 
 string return the character 
 that appears first in the string.

Input Format:
Single line with no space denoting 
the input string.

OutputFormat:
Single character denoting the least 
frequent character.

Constraints:
Length of string <=10^6

Sample Input:
cdadcda

Sample Output:
c

Explanation:
C and A both are with minimum frequency. 
So c is the answer because it comes 
first with less index.


//Question  : Devil Groups
Problem Statement –

There are some groups of devils and they 
splitted into people to kill them. 
Devils make People to them left as their 
group and at last the group with maximum 
length will be killed. Two types of devils 
are there namely “@” and “$”
People is represented as a string “P”

Input Format:
First line with the string for input

Output Format:
Number of groups that can be formed.

Constraints:
2<=Length of string<=10^9

Input string
PPPPPP@PPP@PP$PP

Output
7

Explanation
4 groups can be formed

PPPPPP@
PPP@
PP$
PP
Most people in the group lie in group 
1 with 7 members.


//Question 13 : Copycat in exam

Problem Statement – Rahul copies in the 
exam from his adjacent students. 
But he doesn’t want to be caught, 
so he changes words keeping the letter 
constant. That means he interchanges the 
positions of letters in words. 
You are the examiner and you have to 
find if he has copied a certain word from 
the one adjacent student who is giving 
the same exam, and give Rahul the markings 
he deserves.

Note that: Uppercase and lowercase are the  
same.

Input Format:

First line with the adjacent student’s word
Second line with Rahul’s word
Output Format:

0 if not copied
1 if copied
Constraints:

1<=Length of string<=10^6
Sample Input:

CAR

Acr

Sample Output:

1


//Question : Duplicates
Problem Statement – The principal has a 
problem with repetitions. Everytime someone 
sends the same email twice he becomes angry 
and starts yelling. 
His personal assistant filters the mails 
so that all the unique mails are sent only 
once, and if there is someone sending the 
same mail again and again, he deletes them. 
Write a program which will see the list of 
roll numbers of the student and find how many 
emails are to be deleted.

Sample Input:
6
1
3
3
4
3
3

Sample Output:
3

//Question : Solve equations
Solve the given equations: You 
will be given an array, and T number of 
equations. Solve that equation and update 
the array for every equation you solve
Input Example:
2 3 4 5 1 → input array
3 → number of equations
x*x
x+x
3*x+x

Output:
32 72 128 200 8
Explanation :

For first case array becomes arr=[ 4 9 16 25 1]
For second case array becomes arr=[8 18 32 50 2]
For third case array becomes arr=[32 72 128 200 8]
Output will be : 32 72 128 200 8



#Problem Statement – Given a string S(input 
consisting) of ‘*’ and ‘#’. 
s= "*###*"
The length of the string is variable.
 The task is to find the minimum number of 
 ‘*’ or ‘#’ to make it a valid string. 
 The string is considered valid if the number 
 of ‘*’ and ‘#’ are equal.
 The ‘*’ and ‘#’ 
 can be at any position in the string.
Note : The output will be a positive or
 negative integer based on number of ‘*’
 and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0


Example 1:
Input 1:
###*   -> Value of S
Output :0
input 2:
#### 
o/p : -1


0   → number of * and # are equal

##happy number

### Test Case 1:  ( n = 19  )

1. Initial number: 19
  Calculate the sum of the squares of its digits:
      
     1^2 + 9^2 = 1 + 81 = 82
    

2. Next number: 82
  Calculate the sum of the squares of its digits:
      
     8^2 + 2^2 = 64 + 4 = 68
    

3. Next number: 68
  Calculate the sum of the squares of its digits:
      
     6^2 + 8^2 = 36 + 64 = 100
    

4. Next number: 100
  Calculate the sum of the squares of its digits:
      
     1^2 + 0^2 + 0^2 = 1 + 0 + 0 = 1
    

Since the sequence reaches 1, 
the number 19 is a happy number. 
The algorithm will return `True`.

### Test Case 2:  ( n = 2  )

1. Initial number: 2
  Calculate the sum of the squares of its digits:
      
     2^2 = 4
    

2. Next number: 4
  Calculate the sum of the squares of its digits:
      
     4^2 = 16
    

3. Next number: 16
  Calculate the sum of the squares of its digits:
      
     1^2 + 6^2 = 1 + 36 = 37
    

4. Next number: 37
  Calculate the sum of the squares of its digits:
      
     3^2 + 7^2 = 9 + 49 = 58
    

5. Next number: 58
  Calculate the sum of the squares of its digits:
      
     5^2 + 8^2 = 25 + 64 = 89
    

6. Next number: 89
  Calculate the sum of the squares of its digits:
      
     8^2 + 9^2 = 64 + 81 = 145
    

7. Next number: 145
  Calculate the sum of the squares of its digits:
      
     1^2 + 4^2 + 5^2 = 1 + 16 + 25 = 42
    

8. Next number: 42
  Calculate the sum of the squares of its digits:
      
     4^2 + 2^2 = 16 + 4 = 20
    

9. Next number: 20
  Calculate the sum of the squares of its digits:
      
     2^2 + 0^2 = 4 + 0 = 4
    

At this point, the number 4 has already appeared 
in the sequence, indicating the start of a cycle 
that does not include 1. 
This means that the number 2 is not a happy number. 
The algorithm will return `False`.

### Summary
- For  ( n = 19  ):
 The sequence: 19 → 82 → 68 → 100 → 1
 Since the sequence ends at 1, 19 is a happy number.
- For  ( n = 2  ):
 The sequence: 2 → 4 → 16 → 37 → 58 → 89 → 145 → 
 42 → 20 → 4 (cycle starts here)
 Since the sequence enters a cycle without 
 reaching 1, 2 is not a happy number.

def is_happy(n: int) -> bool:
    def get_next_number(num: int) -> int:
        return sum(int(digit) ** 2 for digit in str(num))
    seen_numbers = set()
 
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = get_next_number(n)
    return n == 1
print(is_happy(19))  # Output: True
print(is_happy(2))   # Output: False

//c++
#include <iostream>
#include <unordered_set>

int get_next_number(int num) 
{
    int sum = 0;
    while (num > 0) {
        int digit = num % 10;
        sum += digit * digit;
        num /= 10;
    }
    return sum;
}

bool is_happy(int n) {
    std::unordered_set<int> seen_numbers;

while (n != 1 && seen_numbers.find(n) == 
seen_numbers.end()) 
{
        seen_numbers.insert(n);
        n = get_next_number(n);
} 
    return n == 1;
}

int main() {
    std::cout << is_happy(19) << std::endl;  // Output: 1 (true)
    std::cout << is_happy(2) << std::endl;   // Output: 0 (false)
    return 0;
}

//Question : Vampire Battle
Problem Statement – Stephan is a vampire. 
And he is fighting with his brother Damon. 
Vampires get energy from human bloods, 
so they need to feed on human blood, 
killing the human beings. 
Stephan is also less inhuman, 
so he will like to take less life in 
his hand. Now all the people’s blood 
has some power, which increases the powers 
of the Vampire. Stephan just needs to be 
more powerful than Damon, killing the least 
human possible. Tell the total power Steohan 
will have after drinking the bloods before 
the battle.

Note that: Damon is a beast, so no human 
being will be left after Damon drinks 
everyone’s blood. But Stephan always 
comes early in the town.
Input Format:

First line with the number of people 
in the town, n.

Second line with a string with n 
characters, denoting the one digit power 
in every blood.

Output Format:

Total minimum power Stephan will gather 
before the battle.

Constraints:

n<=10^4
Sample input :

6   

093212

Sample output :

9

Explanation:

Stephan riches the town, 
drinks the blood with power 9. 
Now Damon cannot reach 9 by drinking 
all the other bloods.

###
Question  – Maximize Earnings
Problem Statement -: A company has a list 
of jobs to perform. 
Each job has a start time, end time and profit 
value. The manager has asked his employee 
Anirudh to pick jobs of his choice. 
Anirudh being greedy wants to select jobs 
for him in such a way that would maximize 
his earnings. 

Given a list of jobs how many jobs and 
total earning are left for other employees 
once Anirudh
Picks jobs of his choice.

Note: Anirudh can perform only one job 
at a time.
Input format:
Each Job has 3 pieces of info – Start Time,
End Time and Profit
The first line contains the number 
of Jobs for the day. Say ‘n’. 
So there will be ‘3n lines following as 
each job has 3 lines.
Each of the next ‘3n’ lines contains 
jobs in the following format:
start_time
end-time
Profit
start-time and end-time are in HHMM 
24HRS format i.e. 9am is 0900 and 9PM is 2100
Constraints:
The number of jobs in the day is less than 
10000 i.e. 0<_n<_10000
Start-time is always less than end time.
Output format :-
Program should return an array of 2 
integers where 1st one is number of 
jobs left and earnings of other employees.

Sample Input 1 :
3
0900
1030
100
1000
1200
500
1100
1200
300

Sample Output 1:
2
400
Sample Explanation 1

Anirudh chooses 1000-1200 jobs. His earnings 
is 500. The 1st and 3rd jobs i.e. 0900-1030 
and 1100-1200 respectively overlap with the 
2nd jobs. But profit earned from them will be 
400 only. Hence Anirudh chooses 2nd one. 
Remaining 2 Jobs & 400 cash for other 
employees.
Sample Input 2:
5
0805
0830
100
0835
0900
100
0905
0930
100
0935
1000
100
1005
1030
100
Sample output 2:
0
0
Sample Explanation 2:
Anirudh can work on all appointments 
as there are none overlapping. 
Hence 0 appointments and 0 earnings for 
other employees.

#Question  – Astronomy Lecture
Problem Statement -: Anirudh is attending 
an astronomy lecture. His professor who 
is very strict asks students to write a program 
to print the trapezium pattern using stars 
and dots as shown below . 
Since Anirudh is not good in astronomy 
can you help him?
Sample Input:
N = 3
Output:
**.**
*…*
…..
*…*
**.**


//Question – Disk Space Analysis
Problem Statement -:  You are given an array, 
You have to choose a contiguous subarray of 
length ‘k’, and find the minimum of that 
segment, return the maximum of those minimums.

Sample input 0 
1 →  Length of segment x =1
5 →  size of space n = 5
1 → space = [ 1,2,3,1,2]
2 
3 
1 
2 

Sample output
3
Explanation
The subarrays of size x = 1 are 
[1],[2],[3],[1], and [2],Because 
each subarray only contains 1 element, 
each value is minimal with respect to 
the subarray it is in. 
The maximum of these values is 3. 
Therefore, the answer is 3


//Guess the word
Problem Statement – Kochouseph Chittilappilly 
went to Dhruv Zplanet , a gaming space, 
with his friends and played a game called 
“Guess the Word”.
Rules of games are –

Computer displays some strings on the screen 
and the player should pick one string / 
word if this word matches with the random 
word that the computer picks then the player 
is declared as Winner.
Kochouseph Chittilappilly’s friends played 
the game and no one won the game. 
This is Kochouseph Chittilappilly’s turn 
to play and he decided to must win the game.
What he observed from his friend’s game is 
that the computer is picking up the string 
whose length is odd and also that should be 
maximum. Due to system failure computers 
sometimes cannot generate odd length words. 
In such cases you will lose the game anyways
 and it displays “better luck next time”. 
 He needs your help. Check below cases for 
 better understand
Sample input :
5 → number of strings
Hello Good morning Welcome you
Sample output :
morning

Explanation:

Hello → 5
Good → 4
Morning → 7
Welcome → 7
You → 3
First word that is picked by computer is morning

Sample input 2 :
3
Go to hell

Sample output 2:
Better luck next time

Explanation:
Here no word with odd length so computer 
confuses and gives better luck next time