import random
import string


def findLastIndex(str, x):
    for i in range(len(str) - 1, -1, -1):
        if (str[i] == x):
            return i

    return -1


# Driver code
str = "brainacademy"
x = 'a'
index = findLastIndex(str, x)

if (index == -1):
    print("Character not found")
else:
    print("Last index is ", index)