#!/usr/bin/python3
"""
FizzBuzz
Change of logic if (i % 3) == 0 and (i % 5) == 0:
"""
import argparse


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="FizzBuzz")
    parser.add_argument("number", type=int, help="Number to perform FizzBuzz up to.")
    args = parser.parse_args()

    fizzbuzz(args.number)
