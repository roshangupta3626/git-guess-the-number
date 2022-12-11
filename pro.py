import random
mynum = random.randint(0,9)
print("Hello, You are ready for playing game")
print("I have number in my mind, can you guess my no.")
n=0
score = 0
for i in range(3):
    user = int(input("Enter your no. b/w 0 to 9 the no. is: "))
    if (mynum == user):
        print("You Won... Weldone")  
        score +=1
        break
    else:
        score +=1
        n+=1
        print("try again")

if n == 3 and score == 3:
    print("Sorry you lost")
    print("You're score is 0")

if score == 1 and n == 0:
    print("WOW you're score is 10")

if score == 2:
    print("You're score is 6")
if score == 3 and n == 2:
    print("You're score is 3")