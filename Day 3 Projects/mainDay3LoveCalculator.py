print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combinedNames = name1 + name2
lowerNames = str.lower(combinedNames) 

t = lowerNames.count('t')
r = lowerNames.count('r')
u = lowerNames.count('u')
e = lowerNames.count('e')
firstScore = t + r + u + e

l = lowerNames.count('l')
o = lowerNames.count('o')
v = lowerNames.count('v')
e = lowerNames.count('e')
secondScore = l + o + v + e
totalScore = int(firstScore) + int(secondScore)