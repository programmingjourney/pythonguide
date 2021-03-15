# Find out if a string is an anagram of the given input
# aadbc = adbac
# map symbol to count
# Time complexity - sort's complexity O(nlogn)
# dict1 - a:0 d:0 b:0 c:0
# dict2 - ....

# abc abd
# dict - a:0 b:0 c:1

# aab bba
# dict a:2 b:0

def is_anagram(a, b):
    return len(a) == len(b) and sorted(a) == sorted(b)

def is_anagram2(a, b):
    if len(a) != len(b):
        return False

    dict = {}

    # iterate over a and fill in the dictionary
    for el in a:
        if el in dict:
            dict[el] += 1
        else:
            dict[el] = 1

    #print(dict)

    for el in b:
        if el in dict and dict[el] > 0:
            dict[el] -= 1
        else:
            return False

    return True

print(is_anagram2("abcd", "bacd"))
print(is_anagram2("aab", "bac"))