import math
import string


def vol(rad):
    return 4 / 3 * math.pi * rad**3


print(vol(2))


def ran_check(num, low, high):
    return low <= num <= high


print(ran_check(3, 1, 10))


def up_low(s: str):
    lowercaseCount = 0
    uppercaseCount = 0
    for value in s:
        if value.islower():
            lowercaseCount += 1
        elif value.isupper():
            uppercaseCount += 1

    print(f'No. of upper case characters: {uppercaseCount}')
    print(f'No. of lower case characters: {lowercaseCount}')


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


def unique_list(lst: list[int]):
    print(list(set(lst)))


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


def multiply(numbers: list[int]):
    acc = 1
    for value in numbers:
        acc *= value

    print(acc)


multiply([1, 2, 3, -4])


def palindrome(s: str):
    strippedStr = s.replace(' ', '')
    print(strippedStr == strippedStr[::-1])


palindrome('nurses run')


def ispangram(str1: str, alphabet=string.ascii_lowercase):
    strippedStr = str1.replace(' ', '')
    for value in alphabet:
        if not value in strippedStr:
            return False
    return True


print(ispangram("The quick brown fox jumps over the lazy dog"))
