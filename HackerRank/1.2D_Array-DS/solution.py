# 28/03/2020 (DD-MM-YYYY)
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import sys


def calculateHourGlass(arr, centerX, centerY):
    return arr[centerY][centerX] \
        + arr[centerY - 1][centerX] \
        + arr[centerY - 1][centerX - 1] \
        + arr[centerY - 1][centerX + 1] \
        + arr[centerY + 1][centerX] \
        + arr[centerY + 1][centerX - 1] \
        + arr[centerY + 1][centerX + 1]


def hourglassSum(arr):
    maxSum = -100

    for i in range(1, 5):
        for j in range(1, 5):
            curSum = calculateHourGlass(arr, i, j)
            if curSum > maxSum:
                maxSum = curSum

    return maxSum


inFileName = sys.argv[1]
with open(inFileName, 'r') as inFile:
    matrix = [[int(num) for num in line.split()] for line in inFile]

print(hourglassSum(matrix))
