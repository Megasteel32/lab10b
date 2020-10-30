# loan_amount = float(input("What is the amount of the loan? "))
# interest_rate = float(input("What is the interest rate? "))
# monthly_payment = float(input("What is the monthly payment? "))
file_name = input("What is the name you would like to call the file? ")

file_name = file_name + ".csv"
print(file_name)

with open(file_name, "w") as file:
    file.write("bruh")