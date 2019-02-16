def checkio2(data):
    if len(data):
        res = data[0]
        del data[0]
        return res + checkio2(data)

    return 0


def checkio(data):
    return data.pop() + checkio(data) if data else 0


if __name__ == '__main__':
    assert checkio([1, 2, 3]) == 6
    assert checkio([2, 2, 2, 2, 2, 2]) == 12
