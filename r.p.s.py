
import random
u = input("your turn: ")
l = ["rock","paper","scissor"]
a = random.choice(l)
print("computer choose:",a)
if (a=="scissor" and u=="rock"):
    print("you wins")
elif (a=="rock" and u=="paper"):
    print("you wins")
elif (a=="paper" and u=="scissor"):
    print("you wins")
elif (a==u):
    print("Tie")
else:
    print("computer wins")








