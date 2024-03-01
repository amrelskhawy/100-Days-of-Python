
print("Welcome to the tip calaculator.")
total_bill = input("What was the total bill? $")
percantage = input("What percentage tip would you like to give? 10, 12, or 15? ")
print(( 1 + int(percantage) / 100))
people_num = input("How many people to split the bill? ")
person_bill = (float(total_bill) / int(people_num)) * ( 1 + int(percantage) / 100)
print("Each person should pay: $" + str(person_bill))
