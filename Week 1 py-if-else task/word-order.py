def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

if __name__=="__main__":
    s=input("Enter a string: ")
    print(word_count(s))
