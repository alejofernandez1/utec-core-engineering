#!/usr/bin/env python3
for letter in range(97, 124):
    if letter != 101 and letter != 113:
        print("{}".format(chr(letter) if letter < 123 else "\n"),
              end="")
