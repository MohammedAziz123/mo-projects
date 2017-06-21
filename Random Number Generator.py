import random #so we can use random module

x = "" #used for while loop 
y = random.randint(1, 100) #so we can print our random numbers easily

while x == "":
    y = random.randint(1,100) 
    print(y) #printing our numbers
    if y > 99: break #if one of our numbers exceeds 99, loop exits
