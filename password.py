import re


def checkio(data: str) -> bool:
    if re.match('^[\da-zA-Z]{11,}$', data) and re.search("[A-Z]", data) and re.search("\d", data) and re.search("[a-z]", data):
        return True

    return False

# print(checkio('bAse730onE4'))
#
# print(re.match(".*[A-Z].*", 'bAse730onE4'))
# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
