import time
name = input("enter your name: ")
age = int(input("enter your age: "))

if age >= 18:
    print("So the game begin to start")
   
    choose = input("are you really want to play this game yes/no : ")

    if choose == "yes":
        print("Okay;",name,"welcome to bluewhale game, in this game you will gate 10 task to complete one by one once the game start you never go back and quit the game if you quit the game after it start you have to py for it so think twice")
        print("okay my freind lets start the game my name is asuran host of this game")
        t1 = input("show me task 1 y/n: ")
        if t1 == "y":
            print("[IF YOU ARE READY TO BECOME A WHALE WRITE 'YES ON YOUR HAND' AND SEND PIC TO ASURAN, YOU HAVE 1 MINUTE TO DO THAT , IF YOU FAILED YOU HAVE TO PAY FOR IT]")
            t2 = input("show me task 2 y/n: ")
            if t2 == "y":
                print("[WRITE 'I AM QUIT' AND PUT ON YOUR WATSAPP STORY]")
                t3 = input("show me task 3 y/n: ")
                if t3 == "y":
                    print("[WOKE UP AT 4:30 AM AND WATCH HORROR VIDEOS]")
                else:
                    print("now i punish you for that")
            else:
                print("now i punish you for that")         
        else:
            print("now i punish you for that")
    
    else:
        print("as you wish!")


else :
    print("you are underage")            