# 11/04/2020 --- DD/MM/YYYY
# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&h_r=next-challenge&h_v=zen&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting&h_r=next-challenge&h_v=zen


def cmp_to_key(key):
    return key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(self):
        return(-self.score, self.name)


with open("./test.txt", "r") as inFile:
    lines = inFile.readlines()

    data = []
    for i in range(1, len(lines)):
        name, score = lines[i].split()
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)
