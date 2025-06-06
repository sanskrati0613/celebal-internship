def is_leap(year):
    leap = False
    
    leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    return leap

if __name__ == '__main__':
    year = int(input("Enter the year: "))
    print(is_leap(year))