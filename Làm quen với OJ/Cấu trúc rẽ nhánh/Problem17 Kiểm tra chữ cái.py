c = input()
if(c.islower()):
    print("LOWER")
elif(c.isupper()):
    print("UPPER")
elif(c.isdigit()): 
    print("DIGIT")
else: print("SPECIAL")