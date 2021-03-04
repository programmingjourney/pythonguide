import sys

n = int(sys.argv[1])

# 1 2 3 2 1
# 1 2 2 1
# 0 : n / 2 , n : n/ 2 - 1
def palindrome(n):
    number = n
    reversed_list = []
    while n > 0:
        last_num = n % 10
        reversed_list.append(last_num)
        n = n // 10
    print(reversed_list)

    reverse = 0
    k = len(reversed_list) - 1
    for i in range(len(reversed_list)):
        reverse += reversed_list[i] * 10 ** k
        k -= 1

    if number == reverse:
        return 'Number is palindromee'
    else:
        return 'Number is not palindromee'

result = palindrome(n)
print(result)