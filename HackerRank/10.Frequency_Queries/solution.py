# 06/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
from collections import Counter


def freqQuery(queries):
    valueDict = Counter()
    counterDict = Counter()
    result = []
    for action, value in queries:
        if action == 1:
            counterDict[valueDict[value]] = max(
                0, counterDict[valueDict[value]] - 1)
            valueDict[value] += 1
            counterDict[valueDict[value]] += 1
        elif action == 2:
            counterDict[valueDict[value]] = max(
                0, counterDict[valueDict[value]] - 1)
            valueDict[value] = max(0, valueDict[value] - 1)
            if valueDict[value] > 0:
                counterDict[valueDict[value]] += 1
        else:
            result.append(0 if counterDict[value] <= 0 else 1)

    return result


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()

    queries = []
    for i in range(1, len(lines)):
        queries.append(list(map(int, lines[i].rstrip().split())))

    ans = freqQuery(queries)
