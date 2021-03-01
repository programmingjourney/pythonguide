# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import student

print(len("hello armen"))

# Definition: Calculates sum of two numbers
def sum(x, y):
    print("sum is: ", x + y)

def diff(x, y):
    print("diff is: ", x - y)

x = 5
y = 5.3
str = "hello"
str2 = 'hello'
#print(x, y, str, str2)

# Execution.
#sum(7, 6)
#diff(5, 1)
#sum(1, 2)
#diff(0, 1)

#num = 12
#str3 = "12"

a = sys.argv[1]
b = sys.argv[2]

#if (a.isdigit() and b.isdigit()):
    #sum(int(a), int(b))
#else:
    #print("Wrong input")

x = int(a);

if (x == 1):
    print("one")
elif (x == 2):
    print("two")
elif (x == 3):
    print("three")
elif (x == 4):
    print("four")
else:
    print("ten")

#list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

#print(list1)

#print(student.names[1:len(student.names)])
#print(student.scores)
#print(student.presences)


student.highest_score(student.names, student.presences)

#print(5 ^ 5 ^ 6)

d = {"Anna": 30, "Petros": 25}

print(d, d["Anna"])

#for key in d.keys():
#    print(key)

#for val in d.values():
#    print(val)

#print(d.items())

# identifier -> {name, year}
# key - string
# value - list

students = {"af100": ["Anahit", 1985], "am400": ["Lilit", 1986]}
#for value in students.values():
#    print(value)

d = {}
#list1 = [int(x) for x in sys.argv[1:]]



# See PyCharm help at https://www.jetbrains.com/help/pycharm/