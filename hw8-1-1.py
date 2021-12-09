# Author MB 12/08/2021

def basketball(free, two_point, three_point):
    points = ((three_point * 3) + (two_point * 2) + free)
    return points

print(basketball(1, 1, 1) == 6)
print(basketball(5, 4, 3) == 22)
print(basketball(3, 4, 5) == 26)