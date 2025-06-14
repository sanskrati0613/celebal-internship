Task 1 =  http://hackerrank.com/challenges/capitalize/problem?isFullScreen=true

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

