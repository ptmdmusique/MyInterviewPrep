# 03/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&h_r=next-challenge&h_v=zen&playlist_slugs%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=dictionaries-hashmaps

from collections import Counter


def sherlockAndAnagrams(s):
    count = 0
    for i in range(1, len(s)+1):
        # Generate all subStr, and
        #   for each combination, sort the subStr by character
        # -> Duplicates are anagram
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        # Then count the duplicates (the one with counter > 1)
        b = Counter(a)
        for j in b:
            count += b[j]*(b[j]-1)/2
    return int(count)


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()
    for i in range(1, len(lines)):
        print(sherlockAndAnagrams(lines[i]))
