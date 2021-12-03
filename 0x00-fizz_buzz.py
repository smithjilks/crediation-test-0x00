#!/usr/bin/env python3
""" This module contains FizzBuzz Code"""


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        if i % 3 == 0:
            print("Fizz")
            continue
        if i % 5 == 0:
            print("Buzz")
            continue

        print("{:d}".format(i))


if __name__ == '__main__':
    fizz_buzz()
