#decimal to binary converter
from collections import deque
import argparse

def twos_comp(num):
    num = abs(num)
    oldBinary = convert_to_binary(num)
    spot = len(oldBinary) - 1
    newBinary = deque()
    c = 0   # column sum
    carry = 0
    addOne = [0] * spot
    addOne.append(1)
    for i in range(len(oldBinary)): #one's comp
        if oldBinary[i] == 1:
            oldBinary[i] = 0
        elif oldBinary[i] == 0:
            oldBinary[i] = 1
    while spot >= 0:
        c = oldBinary[spot] + addOne[spot] + carry
        if c == 0:
            newBinary.appendleft(0)
        if c == 1:
            newBinary.appendleft(1)
            carry = 0
        if c == 2:
            newBinary.appendleft(0)
            carry = 1
        if c == 3:
            newBinary.appendleft(1)
            carry = 1
        if spot == 0 and carry == 1:
            newBinary.appendleft(1)
        spot -= 1
    if newBinary[0] == 0:
        newBinary.appendleft(1)
    return newBinary


def convert_to_binary(num):
    if num < 0:  #if a negative nuber was entered
        return twos_comp(num)
    else:
        result = deque()
        while(num != 0):
            if num % 2 == 1:
                result.appendleft(1)
            elif num % 2 == 0:
                result.appendleft(0)
            num = num // 2
        return result

def get_input():
    parser = argparse.ArgumentParser()

    parser.add_argument('decimal', type=int)
    arg = parser.parse_args()
    return arg.decimal

def main():
    num = get_input()
    result = convert_to_binary(num)
    result = ''.join(map(str, result))
    print("\nDecimal number: {0} Binary number(signed if negative): {1} \n" .format(num, result))

if __name__ == "__main__":
    main()
