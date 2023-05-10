#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord('a')<=ord(character)<=ord('z'):
            capsLetter= chr(ord(character)-32)
        print("{}".format(capsLetter), end="")
    print()
