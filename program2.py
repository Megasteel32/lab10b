# By submitting this assignment, I agree to the following:
#  Aggies do not lie, cheat, or steal, or tolerate those who do�
#  I have not given or received any unauthorized aid on this assignment�
#
# Name:         Luca Maddaleni
# Section:      273
# Assignment:   Lab 10b Program 2
# Date:         10/31/2020

loan_amount = float(input("What is the amount of the loan? "))
interest_rate = float(input("What is the interest rate? ")) / 100
monthly_payment = float(input("What is the monthly payment? "))
file_name = input("What is the name you would like to call the file? ")
interest = 0
month = 0

file_name = file_name + ".csv"

with open(file_name, "w") as file:
    file.write("Month, Loan Amount, Interest\n")
    file.write("0, {}, 0\n".format(loan_amount))
    while loan_amount >= 0 and month <= 30:
        month += 1
        interest = loan_amount * (interest_rate * (1 / 12))
        loan_amount = loan_amount + interest - monthly_payment
        if loan_amount >= 0 and month <= 30:
            file.write("{}, {}, {}\n".format(month, round(loan_amount,2), round(interest,2)))