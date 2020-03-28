# 28/03/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()
    _, d = map(lambda n: int(n), lines[0].split())
    arr = [int(num) for num in lines[1].split()]

result = []
for i in range(len(arr)):
    result.append(arr[(i + d) % len(arr)])
print(result)
