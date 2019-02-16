from itertools import groupby


def long_repeat(line):
    max = 0
    now_count = 1
    last_letter = None
    for letter in line:
        if last_letter == letter:
            now_count += 1
        else:
            now_count = 1

        last_letter = letter
        if now_count > max:
            max = now_count

    return max


def long_repeat2(line):
    return max([len(group) for group
                in [list(g) for k, g in groupby(line)]], default=0)


def long_repeat3(line):
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
