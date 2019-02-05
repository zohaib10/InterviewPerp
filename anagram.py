# Question: Given two Strings write a function to determine if they are anagrams?
# Run time O(n)


def isAnagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    dict = [0] * 1000

    for c in s1:
        dict[ord(c)] += 1

    for c in s2:
        dict[ord(c)] -= 1

    for i in dict:
        if i != 0:
            return False

    return True




if(isAnagram("Listen", "Silent")):
    print("Is Anagram")
else:
    print("Is not Anagram")
