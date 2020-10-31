# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do�
#  I have not given or received any unauthorized aid on this assignment�
#
# Name:         Luca Maddaleni
# Section:      273
# Assignment:   Lab 10b Program 3
# Date:         10/31/2020

from matplotlib import pyplot as plt
file_name = input("What is the name of the file you would like to open? ")

with open(file_name, "r") as file:
    listy_list = file.read().splitlines()
    listy_list_2 = []
    for x in range(len(listy_list)):
        listy_list_2.append(listy_list[x].split(","))

month = []
balance = []
for x in range(1, len(listy_list_2)):
    month.append(listy_list_2[x][0])
    balance.append(float(listy_list_2[x][1]))

print(month)
print(balance)

plt.plot(month, balance, ".")
plt.show()