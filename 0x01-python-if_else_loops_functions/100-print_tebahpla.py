#!/usr/bin/python3
for i in range(0, 26):
    character = ord('z') - i
    if (i % 2 == 1):
        character = chr(character - ord('a') + ord('A'))
    else:
        character = chr(character)
        print("{}".format(character), end="")
