# 30/03/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&h_r=next-challenge&h_v=zen&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays


def arrayManipulation(size, queries):
    # Prefix sum algorithm

    # First initialize the empty array
    arr = [0] * (size + 1)

    for query in queries:
        # Keep track only at the start of the chain
        arr[query[0] - 1] += query[2]
        # And substract at the end + 1 so that when we use
        #   prefix sum, we will eliminate the redundance
        arr[query[1]] -= query[2]

    result = accumulator = 0
    for number in arr:
        accumulator += number
        result = max(result, accumulator)

    return result


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()
    size, _ = map(lambda n: int(n), lines[0].split())
    queries = [[int(num) for num in line.split()] for line in lines[1:]]

print(arrayManipulation(size, queries))
