print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Welcome aboard the rollercoaster!")
    age = int(input("How old are you?\n"))
    if age >= 18:
        print("Please pay $10")
    elif age <=12:
        print("Please pay $6")    
    else:
        print("Please pay $8")    

else:
    print("Sorry! You can't ride!")