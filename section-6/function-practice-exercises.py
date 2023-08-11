def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a if a < b else b
    elif a % 2 != 0 or b % 2 != 0:
        return a if a > b else b


print('lesser_of_two_evens')
print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))


def animal_crackers(text):
    a, b = text.split()
    if a[0].lower() == b[0].lower():
        return True
    return False


print('animal_crackers')
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20:
        return True
    elif n1 + n2 == 20:
        return True
    return False


print('makes_twenty')
print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))


def old_macdonald(name):
    nameList = [*name]
    nameList[0] = nameList[0].upper()
    nameList[3] = nameList[3].upper()
    return ''.join(nameList)


print('old_macdonald')
print(old_macdonald('macdonald'))


def master_yoda(text):
    textList = text.split()
    return ' '.join(textList[::-1])


print("""
===========
master_yoda
===========
""")
print(master_yoda('I am home'))
print(master_yoda('We are ready'))


def almost_there(n):
    if 90 <= n <= 110:
        return True
    elif 190 <= n <= 210:
        return True
    return False


print("""
============
almost_there
============
""")
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


def has_33(nums):
    count = 0
    for i, num in enumerate(nums):
        if num == 3:
            count += 1
        else:
            count -= 0 if i == 0 else 1
    return count >= 2


print("""
============
has_33
============
""")
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

def paper_doll(text):
    return ''.join([x*3 for x in text])


print("""
============
paper_doll
============
""")
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


def blackjack(a,b,c):
    total = a + b + c
    if total <= 21:
        return total
    else:
        if 11 in [a,b,c]:
            total -= 10
    return total if total <= 21 else 'BUST'


print("""
============
blackjack
============
""")
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))


def summer_69(arr):
    acc = 0
    star = 0
    end = 0
    total = sum(arr)
    for i, value in enumerate(arr):
        if value == 6:
            star = i
        elif value == 9:
            end = i
    acc = sum(arr[star:end+1])
    return total - acc


print("""
============
summer_69
============
""")
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


def spy_game(nums: list[int]):
    spy = ''
    for value in nums:
        if value == 0:
            spy += str(value)
        elif value == 7:
            spy += str(value)
    return spy == '007'


print("""
============
spy_game
============
""")
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


def count_primes(num):
    count = 0
    for i, value in enumerate(range(num + 1)):
        if i <= 1:
            pass
        isPrime = False
        red = value - 1
        while red > 1:
            if value % red == 0:
                isPrime = False
                break
            else:
                isPrime = True
                red -= 1
        if isPrime:
            count += 1
            print(value)
    return count


print("""
============
count_primes
============
""")
print(count_primes(100))
