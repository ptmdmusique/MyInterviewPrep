# 29/03/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


def minimumSwaps(arr):
    minSwap = 0
    i = 0
    while(i < len(arr) - 1):
        curVal = arr[i] - 1
        if curVal != i:
            arr[i], arr[curVal] = arr[curVal], arr[i]
            minSwap += 1
        else:
            i += 1
    return minSwap


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()
    arr = [int(num) for num in lines[1].split()]
print(minimumSwaps(arr))
