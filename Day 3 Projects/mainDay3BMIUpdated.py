# 1st input: enter height in meters e.g: 1.65
height = float(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
newHeight = float(height)
newWeight = float(weight)
bmiResults = (float(newWeight / (newHeight * newHeight)))

if bmiResults < 18.5:
    print(f"Your BMI is {bmiResults}, you are underweight.")
elif bmiResults < 35:
    if bmiResults < 25:
        print(f"Your BMI is {bmiResults}, you have a normal weight.")
    elif bmiResults >= 25 and bmiResults < 30:
        print(f"Your BMI is {bmiResults}, you are slightly overweight.")
    elif bmiResults >= 30 and bmiResults < 35:
        print(f"Your BMI is {bmiResults}, you are obese.")
else:
    print(f"Your BMI is {bmiResults}, you are clinically obese.")
