#!/bin/python3


if __name__ == '__main__':
    num = int(input())
    count = 1
    for i in range(3, num+1):
        for j in range(2, i+1):
            if (num % i) == 0:
                break
        else:
            count += 1
    print(count*(count+1)//2)


