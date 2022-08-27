#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in range(length):
        letter = str[i]
        letterCode = ord(letter)
        if letterCode >= 97 and letterCode <= 122:
            letterCode -= 32
            letter = chr(letterCode)

        if i == (length - 1):
            print("{}".format(letter))
        else:
            print("{}".format(letter), end="")
