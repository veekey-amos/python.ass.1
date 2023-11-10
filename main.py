#  user input
principal = float(input("  initial principal amount ;"))
rate = float(input(" annual interest rate : "))
time = float(input(" number of years: "))
n = int(input(" number of times interest is compounded per year: "))

# Calculate simple and compound interest
simple_interest = principal * (1 + rate * time)
compound_interest = principal * (1 + rate/n)**(n*time) - principal

# print results
print("\nYusuf & Sons")
print("Simple Interest: {:.2f}".format(compound_interest))
print("Compound Interest:{:.2f}".format(compound_interest))