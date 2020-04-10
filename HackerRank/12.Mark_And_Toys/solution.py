# 10/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&h_r=next-challenge&h_v=zen&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting


def maximumToys(prices, k):
    result = 0
    # Sort first
    prices.sort()

    # Then greedy
    for i in range(len(prices)):
        if k < prices[i]:
            break
        k -= prices[i]
        result += 1

    return result


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()

    print(maximumToys(list(map(int, lines[1].rstrip().split())), int(
        lines[0].split()[1])))
