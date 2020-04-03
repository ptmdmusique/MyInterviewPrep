# 03/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&h_r=next-challenge&h_v=zen&playlist_slugs%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=dictionaries-hashmaps
from collections import defaultdict
import copy


def checkAnagram(s1, s2, listOfLetter):
    # Check s2 against that list
    for letter in s2:
        # If the dict doesn't contain that letter,
        #   then it means th    e words aren't anagram
        if letter not in listOfLetter or listOfLetter[letter] <= 0:
            return 0
        listOfLetter[letter] -= 1

    return 1


def sherlockAndAnagrams(s):
    # Brute force
    subStrDict = defaultdict(list)
    # Generate all substring using 2 loops (n^2)
    #   Starting index:
    #       Length:
    #           Substr[length] = SubStr[length - 1]
    #                          + str[startingindex + length - 1]
    for startIndex in range(len(s)):
        subStr = ""
        for length in range(1, len(s) - startIndex + 1):
            # len(s) - 1 because it we don't need to count
            #   the original str itself
            subStr += s[startIndex + length - 1]
            subStrDict[length].append(subStr)
    subStrDict = dict(subStrDict)

    """ abcd -> {
        "1": [a, b, c, d]   len(4)
        "2": [ab, bc, cd]   len(3)
        "3": [abc, bcd]     len(2)
        "4": [abcd]         len(1)
    }
    """
    # We move downward first,
    #   listOfLetter[length] = listOfLetter[length - 1] + newChar
    counter = 0
    # O( Sigma(1->n-1) { C(len(subStrDict[i]), 2) } * ~O(check anagram) )
    for i in range(len(subStrDict[1])):
        # Going vertically first
        #   so that we can build the list of char one by one
        curDict = defaultdict(int)
        for subStrList in subStrDict.values():
            if len(subStrList) < i + 1:
                # Out of that dict border
                break
            curDict[subStrList[i][-1]] += 1
            for j in range(i + 1, len(subStrList)):
                counter += checkAnagram(subStrList[i],
                                        subStrList[j],
                                        copy.deepcopy(curDict))

    return counter


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()
    for i in range(1, len(lines)):
        print(sherlockAndAnagrams(lines[i]))
