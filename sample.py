counts = []

for i in range(10):
#for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
   counts.append(0)

print(counts, len(counts))

while True:
   num = input("Please insert a number in range 1-10, or -1 for break")
   if (num.isdigit()):
       num = int(num)

       if (num >= 1 and num <= 10):
           counts[num-1] += 1
       else:
           print("Please be in range 1-10")
   elif (num == "-1"):
       break

for id in range(len(counts)):
   print(id + 1, "the count is: ", counts[id])