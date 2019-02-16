def sun_angle2(time):
    sp = time.split(':')
    degrees = (int(sp[0]) * 60 + int(sp[1]) - 360) * 0.25
    print(degrees)
    return degrees if 180 >= degrees > 0 else "I don't see the sun!"


def sun_angle(time):
    angle = (lambda h, m: (h * 60 + m - 6 * 60) * 0.25)(*map(int, time.split(':')))
    return angle if 180 >= angle >= 0 else "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("18:15"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")