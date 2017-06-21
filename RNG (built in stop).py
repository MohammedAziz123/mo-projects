import random #so we can create random numbers

x = 1 #for our built in stop
y = random.randint(1, 100) #for random numbers 

while x == 1:
    y = random.randint(1,100)
    x+=x #will constantly add up x, so we can predict values, to create stop point
    if x >= 256: break #when x exceeds a given value, it will exit
