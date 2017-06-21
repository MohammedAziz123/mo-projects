import random
word1 = input("Write something...") #user inputs 
word2 = input("Write another something")
word3 = input("Write another another something")
word4 = input("Write something pls")

bigword = word1, word2, word3, word4 #list of words

x = 1 #generates the stop code

while x >= 1:
    print(random.choice(bigword)) #picks a word from the list
    x+=x #allows stop code, by using values of x. if it goes over, program exits
    if x >= 256: break #breaks after 8th value
    
