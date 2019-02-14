from collections import Counter
import re
import string


def checkio3(text: str) -> str:
    counter = Counter(re.sub('[^a-z]', '', text.lower()))
    frequency = counter.most_common()
    count_top = frequency[0][1]
    equal_values = [i for i in frequency if i[1] == count_top]
    return sorted(equal_values)[0][0]


def checkio1(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


def checkio(text): return max(string.ascii_lowercase, key=text.lower().count)

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    assert checkio("Lorem ipsum dolor sit amet") == "m"
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")