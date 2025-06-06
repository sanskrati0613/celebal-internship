from itertools import groupby

s = input("Enter the string:")
for key, group in groupby(s):
    print(f"({len(list(group))}, {key})", end=' ')