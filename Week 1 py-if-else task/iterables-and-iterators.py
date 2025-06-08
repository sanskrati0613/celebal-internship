import itertools

def find_probability(arr, k):
    all_combinations = list(itertools.combinations(arr, k))
    total_combinations = len(all_combinations)
    satisfied_combinations = len([x for x in all_combinations if 'a' in x])
    probability = satisfied_combinations / total_combinations
    print(round(probability, 4))
    
    

if __name__ == "__main__":
    n = int(input("Enter length of the list:"))
    print(f"Enter {n} space-separated lowercase English letters: ")
    arr = list(input().split())
    k = int(input("Enter number of indices to be selected: "))

    find_probability(arr, k)