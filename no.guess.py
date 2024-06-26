import random

print("welcome to guess the number game in this game program randomly generate one integer number from 1 to 100 you have to guess one integer no. from 1 to 100 if your guess is equal to random no. you win otherwise you lose, you have 7 chances")
count = 0

f = int(input("enter first number: "))
l = int(input("enter last nummber: "))
r = random.randint(f,l)


while count>=0:
    user = int(input("enter your guess: "))
    count+=1
    if user > r:
        print("to high")

    elif user < r:
        print("to low")

    elif user == r:
        print("Congratulation, you guess it right in:",count," chance ")
        break
    if count == 7:
        print("try again")
        break 




    

    


