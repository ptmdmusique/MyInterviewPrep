# 13/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&h_r=next-challenge&h_v=zen&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


# Count sort is the key
def getMedian(countSortList, midList):
    result = []
    for mid in midList:
        left = mid
        for index, value in enumerate(countSortList):
            left -= value
            if left <= 0:
                result.append(index)
                break

    return sum(result) / len(result)


def activityNotifications(expenditure, d):
    result = 0
    countSortList = [0] * 201   # 200 is the data range

    if d % 2 == 0:
        midList = [d // 2, d // 2 + 1]
    else:
        midList = [d // 2 + 1]

    # First collect all the data first
    for value in expenditure[:d]:
        countSortList[value] += 1

    for index, value in enumerate(expenditure[d:]):
        median = getMedian(countSortList, midList)

        if median * 2 <= value:
            result += 1

        countSortList[value] += 1
        countSortList[expenditure[index]] -= 1

    return result


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()

    _, d = map(lambda i: int(i), lines[0].split())
    print(activityNotifications(list(map(int, lines[1].rstrip().split())), d))
