#!/usr/bin/python3

def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) is not str):
        return (0)

    prev = roman_string[:1]
    summ = 0
    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    prev = roman_dict.get(prev)
    if prev is None:
        prev = 0

    for c in roman_string[1:]:
        current = roman_dict.get(c)
        if current is None:
            current = 0
        if prev < current:
            prev *= -1
        summ += prev
        prev = current

    summ += prev

    return (summ)
