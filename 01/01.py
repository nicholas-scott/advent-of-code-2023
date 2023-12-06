import regex as re

"""
--- Part One ---
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""

input_file = "input.txt"
example_one = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
example_two = ['eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']

def main():
    with open(input_file) as input:
        # sum = solution1(input)
        # print(f'Solution 1: {sum}')

        sum = solution2(input)
        print(f'Solution 2: {sum}')

def solution1(input):
    sum = 0
    for line in input:
        digits = re.findall(r'\d', line)
        sum += int(digits[0] + digits[-1])
    return sum

def solution2(input):
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six':6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': '0'}
    sum = 0
    for line in input:
        digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine|zero', line, overlapped=True)
        left = numbers[digits[0]] if digits[0] in numbers else digits[0]
        right = numbers[digits[-1]] if digits[-1] in numbers else digits[-1]

        sum += int(str(left) + str(right))
    return sum



if __name__ == "__main__":
    main()
