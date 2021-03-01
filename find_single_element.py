
import sys

# In: 1 3 4 5 5 2
# Out: 4
# size = n
# time complexity n * n

# list comprehension
list1 = [int(x) for x in sys.argv[1:]]

# samw with a loop
list2 = []
for el in sys.argv[1:]:
    list2.append(int(el))

# find element in list
#x = 1
#print(x in list1)
#print(1 in list2)

def find_single_element(a):
    n = len(a)
    i = 0
    while i < n:
        #print(a, i, n)
        if a[i] in a[i + 1:]:
            j = a[i + 1:].index(a[i])
            #print(a[i], j)
            del a[i + 1 + j]
            n = len(a)
            i += 1
        else:
            print(a[i])
            break

def find_single_element2(a):
    for i in range(0, len(a)):
        if a.count(a[i]) == 1:
            print(a[i])
            break

# 1 2 2 1 3 4 7 4 3 5 5
def find_single_element3(a):
    xored = 0
    for el in a:
        xored = xored ^ el
    print(xored)

find_single_element(list2)
print(min(list1, key=list1.count))
find_single_element2(list1)
find_single_element3(list1)
