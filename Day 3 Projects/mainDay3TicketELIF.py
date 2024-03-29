print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Welcome aboard the rollercoaster!")
    age = int(input("How old are you?\n"))
    if  age <= 18:
        bill = 8
        print("Please pay $8 for the ticket")     
    elif age <=12:
        bill = 6
        print("Please pay $6 for the ticket")  
    elif age >= 45 and age <= 50:
        print("Your Ticket is on us!")      
    else:
        bill = 10
        print("Please pay $10 for the ticket")   
    askPhoto = input("Do you want a photo to be added? Y or N \n")
    if askPhoto == "Y":
        bill += 3
        print(f"Your total will be ${bill}")
    else:   
        print(f"Your total will be ${bill}")
else:
    print("Sorry! You can't ride!")