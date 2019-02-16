from typing import List, Any


def all_the_same4(elements: List[Any]) -> bool:
    if elements == [] or len(elements) == elements.count(elements[0]):
        return True
    else:
        return False


def all_the_same2(elements: List[Any]) -> bool:
    from collections import Counter
    if len(Counter(elements)) == 1 or elements == []:
        return True
    else:
        return False


def all_the_same(elements: List) -> bool:
    return len(set(elements)) <= 1


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
