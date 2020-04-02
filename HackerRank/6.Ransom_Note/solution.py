# 02/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


def checkMagazine(magazine, note):
    listWords = {}
    for word in magazine:
        if word not in listWords:
            listWords[word] = 1
        else:
            listWords[word] += 1

    for word in note:
        if word not in listWords or listWords[word] <= 0:
            print("No")
            return
        listWords[word] -= 1

    print("Yes")


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()
    checkMagazine(lines[1].split(), lines[2].split())
