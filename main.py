print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

total_bill *= (1 + tip * 0.01)

people_count = int(input("How many people to split the bill? "))

payment = round((total_bill / people_count), 2)

print(f"Each person should pay: ${payment}")