# 09/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting


def countSwaps(a):
    swap = 0
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                swap += 1
                temp = a[i]
                a[i] = a[j]
                a[j] = temp

    print("Array is sorted in {} swaps.".format(swap))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()

    countSwaps(list(map(int, lines[1].rstrip().split())))
