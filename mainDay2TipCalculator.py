#If the bill was $150.00, split between 5 people, with 12% tip. 
askBill = float(input("How much is your total bill? \n"))
askTipping = float(input("How much are you tipping %? \n"))
askPeople = float(input("How many are splitting the bill \n"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

totalTip = askTipping / 100
serverBill = totalTip * askBill
splitBill = serverBill + askBill
totalBill = splitBill / askPeople

print(f"Each person will pay ${round(totalBill,2)}")