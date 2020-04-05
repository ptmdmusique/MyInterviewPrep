# 04/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

from collections import defaultdict


def countTriplets(arr, r):
    arrMin = arrMax = arr[0]

    # Hash everything first
    rightDict = defaultdict(int)
    leftDict = defaultdict(int)
    for number in arr:
        rightDict[number] += 1
        arrMin = min(number, arrMin)
        arrMax = max(number, arrMax)

    # Instead of checking a, ar, ar^2,
    #   we are checking for a/r, a, ar
    #   so that we can iterate from middle outward
    result = 0
    for number in arr:
        rightDict[int(number)] -= 1
        # Each time we iterate through a number,
        #   we remove it from the rightDict and add it to the leftDict
        if number % r == 0 and number * r <= arrMax:
            # a/r needs to be an integer, so a % r == 0
            result += leftDict[int(number/r)] * rightDict[int(number * r)]

        leftDict[int(number)] += 1

    return result


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()
    _, r = map(lambda n: int(n), lines[0].split())
    arr = list(map(lambda n: int(n), lines[1].rstrip().split()))
    print(countTriplets(arr, r))
