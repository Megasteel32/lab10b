# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do�
#  I have not given or received any unauthorized aid on this assignment�
#
# Name:         Luca Maddaleni
# Section:      273
# Assignment:   Lab 10b Program 1
# Date:         10/31/2020

with open("Celsius.dat", "r") as celcius:
    noblanks = []
    for line in celcius:
        noblanks.append(line.splitlines())

converted = []
for x in range(len(noblanks)):
    noblanks[x] = float(noblanks[x][0])
for x in range(len(noblanks)):
    converted.append(noblanks[x] * (9/5) + 32)

with open("Fahrenheit.dat", "w") as fahrenheit:
    for x in converted:
        fahrenheit.write(str(x) + "\n")