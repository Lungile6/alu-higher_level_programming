#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or not isinstance(roman_string, str)
    or not roman_string:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rep = 0
    for i in range(len(roman_string) - 1):
        if roman_string[i] not in data or roman_string[i+1] not in data:
            return 0  # Invalid Roman numeral characters
        if data[roman_string[i]] >= data[roman_string[i+1]]:
            rep += data[roman_string[i]]
        else:
            rep -= data[roman_string[i]]
    # Add the value of the last Roman numeral character
    rep += data[roman_string[-1]]
    return rep
