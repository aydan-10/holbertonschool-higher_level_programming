#!/usr/bin/python3
"""Roman to Integer module"""


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rd = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    res = 0
    for i in range(len(roman_string)):
        if i > 0 and rd[roman_string[i]] > rd[roman_string[i - 1]]:
            res += rd[roman_string[i]] - 2 * rd[roman_string[i - 1]]
        else:
            res += rd[roman_string[i]]
    return res
