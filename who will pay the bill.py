import random
print("Welcome to the  bill chooser")
string = input("Give your friends name :")
string = string.split(" ")
x=len(string)
i =random.randint(0,x-1)
print(f"{string[i]} please pay the bill")

