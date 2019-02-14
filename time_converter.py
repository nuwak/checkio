from datetime import datetime


def time_converter(time):
    replace = {"PM": "p.m.", "AM": "a.m."}
    res = datetime.strptime(time, '%H:%M').strftime('%-I:%M %p')

    for k, v in replace.items():
        res = res.replace(k, v)

    return res


def time_converter1(time):
    h, m = map(int, time.split(':'))
    return f"{(h-1)%12+1}:{m:02d} {'ap'[h>11]}.m."


if __name__ == '__main__':
    print("Example:")
    print(time_converter('14:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
