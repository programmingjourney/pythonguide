names = ["Anna", "Artak", "Stepan", "Poghos"]
presences = [100, 95, 98, 80]
scores = [96, 100, 100, 90]

presence_coef = 0.5
score_coef = 0.5

# 98.0 97.5 99.0 85.0
# list[0] list[1]    2    3
# max = 0
# 98 > 0 -> max = 98
# 97.5 > 98 -> max = 98
# 99.0 > 98 -> max = 99
# 85 > 99 -> max 99
# result max == 99

def max_score(list):
    max = 0 # the minimum possible value
    for el in list:
        print("el:", el)
        if (el > max):
            max = el

    return max

def max_score2(list):
    max = 0 # the minimum possible value
    index = 0
    for i in range(0, len(list)):
        print("i:", i)
        if (list[i] > max):
            max = list[i]
            index = i

    return {max, i}

def min_score(list):
    min = 100 # the maximum possible value
    for el in list:
        if (el < min):
            min = el

    return min

# Choose the student with the highest score and presence score.
# a * score + b * presence
# 0.5 - score
# 0.5 - presence
def highest_score(n, p):

    result = []
    for i in range(0, len(n)):
        #print(presence_coef * p[i] + score_coef * scores[i])
        result.append(presence_coef * p[i] + score_coef * scores[i])

    print("Max: ", max_score(result))
    print("Max: ", max_score2(result))
    print("Min: ", min_score(result))
