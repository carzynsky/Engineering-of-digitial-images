from math import sin
from math import cos


def mathFunction(arg):
    return sin(arg)**2*cos(arg)


numbs = []
with open('./input.txt', 'r') as inputFile:
    for x in inputFile:
        numbs.append(float(x))

with open('./output.txt', 'w') as outputFile:
    for number in numbs:
        s = 'Argument: {}, Wynik: {}\n'.format(number, mathFunction(number))
        outputFile.write(s)
