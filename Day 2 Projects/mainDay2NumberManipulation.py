#Round Function
#comma 2 adds the number of decimal points
print(round(8/3,2))

#F String Manipulation. Added to print statement. calls all variables in f.
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}. You are Winning is {isWinning}")

age = input()
newAge = int(age)
currentAge = int(newAge * 52)
yearLast = int(90 * 52)
remainWeeks = int(yearLast - currentAge)
print(f"You have {remainWeeks} weeks left.")