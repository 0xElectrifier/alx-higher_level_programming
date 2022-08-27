#!/usr/bin/python3
def uppercase(str):
    length = len(str)

    for i in range(length):
        if length > 0:
            letter = str[i]
            letterCode = ord(letter)
            if letterCode >= 97 and letterCode <= 122:
                letterCode -= 32
                letter = chr(letterCode)
            print("{}".format(letter), end="")

    print("")
