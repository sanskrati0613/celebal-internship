Task 1 =  http://hackerrank.com/challenges/capitalize/problem?isFullScreen=true
capitalize : Task to make the first letter of every words as capital

CODE:
def capitalize_name(name):

  words = name.split()
  capitalized_words = []

  for word in words:
    if word:
      capitalized_words.append(word.capitalize())
    else:
      capitalized_words.append("")

  return " ".join(capitalized_words)

if __name__ == "__main__":
    name = input("Enter your full name: ")

    capitalized_name = capitalize_name(name)
    print(capitalized_name)


Task 2 = https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
py-introduction-to-sets : Calculate the avarges of items present inside a python set

CODE:
average(array):
    distinct_heights = set(arr)
    total = sum(distinct_heights)
    count = len(distinct_heights)
    avg= total / count
    return round(avg , 3)
    
if __name__ == '__main__':
    n = int(input("Enter size of array: "))
    arr = list(map(int, input(f"Enter {n} integers: ").split()))
    result = average(arr)
    print(result)

INPUT = 10
161 182 161 154 176 170 167 171 170 174
OUTPUT = 169.375


Task 3 = https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
text-wrap : Task to wrap the string into a paragraph of given width

CODE:
import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string = input("Enter a string: ")
    max_width = int(input("Enter the maximum width: "))
    result = wrap(string, max_width)
    print(result)

INPUT = ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
OUTPUT = ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ


Task 4 https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
alphabet-rangoli : pattern printing with the help of alphabets

CODE:
def print_rangoli(size):
    a = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    for row in range(size):
        print_ = "-".join(a[row:size])
        lines.append(print_[::-1] + print_[1:])
    width = len(lines[0])
    
    for row in range(size-1, 0, -1):
        print(lines[row].center(width, '-'))
        
    for row in range(size):
        print(lines[row].center(width, '-'))

if __name__ == '__main__':
    n = int(input("Enter the size: "))
    print_rangoli(n)

INPUT = 5
OUPUT = --------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------


Task 5 = https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
merge-the-tools : Split a string into equal parts of length and Convert each parts by removing any subsequent occurrences of non-distinct

CODE:
import string
def merge_the_tools(string, k):
    for i in range (0 , len(string), k):
        part = string[i:i+k]
        seen = ''
        for char in part:
            if char not in seen:
                seen += char
        print(seen)
if __name__ == '__main__':
    string = input("Enter the string: ")
    k= int(input("Length of each substring: "))
    merge_the_tools(string, k)

INPUT = AABCAAADA
3
OUPUT = AB
CA
AD


Task 6 - https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
collections-counter : calculate the total earned amount

CODE:
from collections import Counter
x = int(input("Enter the number of shoes: "))


shoe_sizes = list(map(int, input("All shoe sizes: ").split()))
shoe_inventory = Counter(shoe_sizes)  

n = int(input("Number of customers: "))

earnings = 0
print(f"{n} values of the shoe size desired by the customer and the price of the shoe: ")
for _ in range(n):
    size, price = map(int, input().split())
    if shoe_inventory[size] > 0:
        earnings += price
        shoe_inventory[size] -= 1 

print(earnings)

INPUT = 10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
OUTPUT = 200


Task 7 = https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
exceptions : implementing exception handling

CODE:
t = int(input("Number of test cases: "))
print("Enter the test cases: ")
for _ in range(t):
    a, b = input("").split()
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)

  INPUT = 3
1 0
2 $
3 1
OUTPUT = Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3


Task 8 = https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
incorrect-regex : regex based problem statement

CODE:
import re
n = int(input())
for i in range(0,n):  
    try:
        input_ = input()
        a = (re.compile(input_))
        print(bool(a))
    except re.error:
        print('False')


Task 9 = https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
py-set-discard-remove-pop : task based on discard(),remove() & pop()

CODE:
n = int(input("Number of elements: "))
print(f"Enter {n} elements: ")
s = set(map(int, input().split()))
print("Enter number of commands: ")

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'pop' and s:
        s.pop()
    elif cmd[0] in ('remove', 'discard') and len(cmd) == 2:
        s.discard(int(cmd[1]))
print(sum(s))

INPUT = 9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
OUTPUT = 4
