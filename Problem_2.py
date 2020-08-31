#!/bin/python3


if __name__ == '__main__':
    elem = int(input())
    num = int(input())
    strength = list(map(int, input().split()))
    strength.sort()
    while len(strength) > elem:
        temp = strength[0] + strength[1]
        strength = strength[2:]
        for i in strength:
            if temp <= i:
                strength.insert(strength.index(i), temp)
                break

    print(strength[0])

