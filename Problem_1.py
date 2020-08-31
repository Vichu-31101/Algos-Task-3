#!/bin/python3


if __name__ == '__main__':
    num = int(input())
    count = 0
    while num // 10 > 0:
        sum = 0
        for i in str(num):
            sum += int(i)
        count += 1
        num = sum
    print(count)
