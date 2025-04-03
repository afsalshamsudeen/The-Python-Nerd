from cryptography.fernet import Fernet

'''
def key_generation():
    key = Fernet.generate_key()
    with open("key.key" , "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)
master_key = input("Enter Your Master Key: ")

def add():
    user_name = input("Enter the account name: ")
    psw = input("Enter the password: ")
    with open('password.txt', 'a') as f:
        f.write(user_name+ "|" + fer.encrypt(psw.encode()).decode() + "\n")

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            username, passw = data.split("|")
            print("Username:",username , "\n","Password:",fer.decrypt(passw.encode()).decode())


while True:
    mode = input("Would you like to add a password or view an existing one? (view 0r add) and q to Quite ").lower()
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Mode!")

