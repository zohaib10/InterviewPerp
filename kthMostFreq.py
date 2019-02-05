#Find the kth Most occuring string in a given list...

def kthMost(lst, k):
    #declare a dictonary
    freq = {}
    #go through list and initialize and update values of string based on occurances
    for item in lst:
        if item in freq.keys():
            freq[item] = freq[item] + 1
        else:
            freq[item] = 1
    print(freq)
    # return the size matching kth
    for key, value in freq.items():
        if value == k:
            return key
    return "null"

print(kthMost(["a", "a", "b", "a","dog", "c", "c", "dog", "c"],2))


#References:
    #1. https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3
