import random as r #alias
file = open("C:\\Users\\asus\\OneDrive\\Desktop\\python basics\\File handling\\raj2.txt", "w")
# 1) Login
login = input("Press Y to login!!")

if(login=="Y"):
    otp = r.randint(1000,9999)
    
    try:
        file.writelines(str(otp))
        
    except(FileNotFoundError):
        print("File doesn't exist")
    except(FileExistsError):
        print("Cannot create file , already exists!!")
    
    file.close()

    print("Your OTP has been sent!!")
    f_otp = int(input("Enter the OTP you have recieved : "))
    if(otp==f_otp):
        print("User Login Successfull")
    else:
        print("OTP Incorrect")
else:
    file.close()
    print("See you soon!!!")
    