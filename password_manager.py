master_pwd = input ("What is master password?")

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip ()
            user,passw =data.split("|")
            print("User:",user,"| Password:",passw)
    
    
def add():
    name = input("Account name: ")
    pwd =input("Password: ")
    
    with open("password.txt","a") as f:
        f.write(name+"|"+pwd+"\n")


    
while True:
    mode = input("Would you like to add a new passwod or view existing ones(view/add),press q to quit: ").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print ("Invalid mode.")