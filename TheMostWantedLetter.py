from collections import Counter
import re


def checkio(text: str) -> str:
    text = re.sub('[\W]', '', text)
    frec = Counter(text.lower())
    most_common = frec.most_common(1)

    if most_common[0][1] == 1:
        return sorted(frec)[0]

    return frec.most_common(1)[0][0]


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