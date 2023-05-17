import bcrypt
import pwinput 

userChoice = input("Enter (1) to create an account OR (2) to login an account: ")

if (userChoice == '1'):
    username = input("Enter username: ")
    userPass = pwinput.pwinput("Enter password: ")
    password = bytes(userPass,"utf-8")
    
    ##generate salt and hashed password 
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt) ## le pass

    with  open("db.txt", "a") as file:
        val = file.write("\n" + username + " " + hashed.decode())
        if (val > 0):
            print("Account successfully made!")
        else:
            print("error")
            exit
            
elif (userChoice == '2'):
    username = input("Please enter your registered username: ")
    userPass = pwinput.pwinput("Please enter your password: ")
    userPass = bytes(userPass, "utf-8")

    realpass = ""

    ##read the passwords
    with open("db.txt", "r") as file:
        content = file.read()
        content = content.splitlines()
        for x in content:
            if x.split()[0] == username:
                realpass = x.split()[1]
                realpass = bytes(realpass,"utf-8")

    ##authentication LMFAO, so COOOOOOL
    if (bcrypt.checkpw(userPass,realpass)):
        print("Welcome " + username.capitalize())
    else:
        print("Access Denied")
        exit
        
else:
    print("Wrong input")
    exit 


