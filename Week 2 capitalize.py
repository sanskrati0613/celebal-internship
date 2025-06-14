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
