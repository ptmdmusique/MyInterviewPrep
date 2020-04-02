# 02/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&h_r=next-challenge&h_v=zen&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps


def twoStrings(s1, s2):
    listLetters = {}
    for letter in s1:
        listLetters[letter] = True

    for letter in s2:
        if letter in listLetters:
            return "YES"

    return "NO"


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()
    for i in range(1, len(lines), 2):
        print(twoStrings(lines[i], lines[i + 1]))
