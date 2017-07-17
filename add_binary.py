# This program will add binary numbers and also shows result in decimal (unsigned)
from collections import deque
import argparse

def equate_length(firstN, secondN):
    if len(firstN) < len(secondN):
        firstN = ''.join(map(str, firstN))
        firstN = firstN.zfill(len(secondN)) #fill zeros in front to match lengths
    if len(secondN) < len(firstN):
        secondN = ''.join(map(str, secondN))
        secondN = secondN.zfill(len(firstN))
    return (list(firstN),list(secondN))

def convert_to_decimal(a_list):
    spot = len(a_list) - 1
    dec = 0
    count = 0
    while spot >= 0:
        dec += (2 ** count) * a_list[spot]
        count += 1
        spot -= 1
    return dec

def add_them(firstN, secondN):
    if len(firstN) != len(secondN):
        firstN, secondN = equate_length(firstN, secondN)
    spot = len(firstN) - 1
    result = deque()
    c = 0     # column sum
    carry = 0
    while spot >= 0:
        c = int(firstN[spot]) + int(secondN[spot]) + carry
        if c == 0:
            result.appendleft(0)
        if c == 1:
            result.appendleft(1)
            carry = 0
        if c == 2:
            result.appendleft(0)
            carry = 1
        if c == 3:
            result.appendleft(1)
            carry = 1
        if spot == 0 and carry == 1:
            result.insert(0, 1)
        spot -= 1
    return result

def is_invalid(the_list):
    for item in the_list:
        if int(item) != 0 and int(item) != 1:
            return True

def get_input():
    parser = argparse.ArgumentParser()

    parser.add_argument('first_binary')
    parser.add_argument('second_binary')
    arg = parser.parse_args()

    list1 = list(arg.first_binary)
    list2 = list(arg.second_binary)

    if is_invalid(list1) or is_invalid(list2):
        raise ValueError("Invalid input")
    else:
        return list1, list2

def main():
    list1, list2 = get_input()
    
    result = add_them(list1, list2)
    result1 = ''.join(map(str, result)) #convert to string
    print ("\nAdded result: {0} or {1} in decimal.\n" .format(result1, convert_to_decimal(result)))

if __name__ == "__main__":
    main()
