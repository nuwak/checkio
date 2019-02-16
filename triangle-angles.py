from typing import List
from math import *


def checkio(a: int, b: int, c: int) -> List[int]:
    try:
        beta = degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2.0 * b * c)))
        alfa = degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2.0 * a * c)))
        l = degrees(acos((a ** 2 + b ** 2 - c ** 2) / (2.0 * a * b)))
        res = sorted([round(beta), round(alfa), round(l)])
        if res.count(0):
            return [0, 0, 0]
        return res
    except ValueError:
        return [0, 0, 0]


def checkio2(a: int, b: int, c: int):
    a, b, c = sorted([a, b, c])
    if c >= a + b:
        return [0, 0, 0]

    ribs = [[a, b, c], [b, c, a], [c, a, b]]
    result = []
    for rib in ribs:
        x, y, z = rib
        result.append(round(degrees(acos((x*x + y*y - z*z) / (2*x*y)))))

    return sorted(result)


def get_angle_from_sides(a, b, c):
    return acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))


def checkio4(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return [0, 0, 0]
    angles = [get_angle_from_sides(*abc) for abc in ((a, b, c), (b, c, a), (c, a, b))]
    result = sorted(round(degrees(a)) for a in angles)
    return result


def checkio3(a: int, b: int, c: int) -> List[int]:
    if a >= b + c or b >= a + c or c >= a + b:
        return [0, 0, 0]
    a1 = round(degrees(acos((b * b + c * c - a * a) / (2 * b * c))))
    a2 = round(degrees(acos((a * a + c * c - b * b) / (2 * a * c))))
    a3 = 180 - a1 - a2
    return sorted([a1, a2, a3])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # print("Example:")
    # print(checkio(4, 4, 4))
    print(checkio(3, 4, 5))
    # checkio(2, 2, 5)

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")