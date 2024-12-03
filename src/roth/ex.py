"""
Advent of Code 2023: Day 1, Part 1
- Unscramble a list of calibration values
- Sum the calibration values

Unscrambling:
  - each calibration value is an alphanumeric string
  - take the first digit and the last digit (in that order) and cast to int
  - if only one digit in scrambled string, take it twice (it is first and last) 
"""

from utils.files import readlines
lines = readlines('ex.txt')


def getFirstNum(string):
    """
    Iterate through inputstring and return first digit.
    If no digit is found, return an empty string.
    Provide a reversed string to get the *last* digit.
    """
    for char in string:
        if char.isdigit(): # isdigit returns true if char can be cast to an int
            return char
    return ''

def unscramble(string):
    """Get first and last digit from string, join, and cast to int."""
    # string[::-1] reverses the string, which means getFirstNum will return the *last* digit
    first_and_last = getFirstNum(string) + getFirstNum(string[::-1])
    return int(first_and_last, 10)

"""
map creates a new list by calling unscramble on each element of lines and adding the result
Equivalent to:
unscrambled = []
for scrambled in lines:
  unscrambled.append(unscramble(scrambled))
"""
unscrambled = map(unscramble, lines)
# sum all the unscrambled elements
unscrambled_sum = sum(unscrambled)

# print answer
print(unscrambled_sum)