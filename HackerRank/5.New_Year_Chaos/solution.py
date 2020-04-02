# 01/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


def minimumBribes(q):
    # Count Inversions problem
    counter = 0
    for i in range(len(q)):
        # Check if that person bribed to many times or not
        if q[i] - 1 - i > 2:
            print("Too chaotic")
            return

        for j in range(max(q[i] - 2, 0), i):
            if q[j] > q[i] - 1:
                counter += 1

    print(counter)


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()
    for i in range(1, len(lines), 2):
        queue = [int(num) for num in lines[i + 1].split()]
        minimumBribes(queue)
