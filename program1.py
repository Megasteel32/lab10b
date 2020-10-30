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