#Type Checking
charName = len(input("What is your name? \n"))

#prints Value Type
print (type(charName))

#This will give an error since its an int value which is length
#print("Your Name has " + charName + " characters.")

#Type Conversions

newCharName = str(charName)
print("Your Name has " + newCharName + " characters.")

two_digit_number = input()
type(two_digit_number)
fdigitnumber = int(two_digit_number[0])
sdigitnumber = int(two_digit_number[1])
results = fdigitnumber + sdigitnumber
print(results)
