x = [1, 3, 2, 4, 6, 7, 0]
print(4 in x)

# Space complexity O(1)
# Time complexity O(n)
def find1(x, l):
    for el in l:
        if el == x:
            return True
    return False

print(find1(4, x))

y = [1, 2, 3, 4, 5, 6, 7, 8]

# sort then search, nlogn + logn -> O(nlogn) > O(n)
# Space complexity O(1)
# Time complexity O(logn)
def find2(x, l, s, e):
    if s == e:
        return False

    m = s + ( e - s ) // 2

    if l[m] == x:
        return True
    if l[m] > x:
        return find2(x, l, s, m)
    return find2(x, l, m + 1, e)

print("binary search approach ", find2(5, y, 0, len(y)))
print("binary search approach ", find2(10, y, 0, len(y)))


# Python3 Optimized implementation
# of Bubble sort

# An optimized version of Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to
            # n-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)

print("Sorted array :")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

print("\n")

strs = ["abc", "abc", "bac", "def", "ghijk"]

def myhash(s):
    return sum(ord(x) for x in s)

for s in strs:
    print(s, myhash(s))

def find3(x, l):
    for el in l:
        if myhash(el) == myhash(x) and el == x:
            return True
    return False

print(find3("bac", strs))
print(find3("acb", strs))