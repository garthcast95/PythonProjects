#Type Checking
charName = len(input("What is your name? \n"))

#prints Value Type
print (type(charName))

#This will give an error since its an int value
#print("Your Name has " + charName + " characters.")

#Type Conversions

newCharName = str(charName)
print("Your Name has " + newCharName + " characters.")
