import hashlib
import os
# Function to generate a random salt
def generate_salt():
    return os.urandom(16)  

# Function to hash the password with the salt
def generate_hash(password,salt:bytes):
    salted_password = salt + password.encode('utf-8')  
    hashed_password = hashlib.sha256(salted_password).hexdigest() 
    return hashed_password

# database
user_database = {}

# Function to sign up a new user
def sign_up():
    username = input("Enter a username: ")
    while True:
        if username in user_database:
             print("Username already exists!!Try with some other username")
             username = input("Enter a username: ")
        else:
            break     


    password = input("Enter a password: ")
    salt = generate_salt()
    hashed_password = generate_hash(password, salt)
    user_database[username] = {'salt': salt, 'password': hashed_password}
    print("Sign-up successful! You can now log in with your username "+username+".")

# Function to log in
def log_in():
    username = input("Enter your username: ")
    
    # Check if the username exists in the database
    if username not in user_database:
        print("Login failed! Username not found.")
        return
    
    password = input("Enter your password: ")
    
    stored_salt = user_database[username]['salt']
    stored_hash = user_database[username]['password']
    
    # Hash the entered password with the stored salt and compare it
    hashed_entered_password = generate_hash(password, stored_salt)
    i=1
    while i<3:
         if hashed_entered_password == stored_hash:
             print("Login successful!")
             break
         else:
             print("Login failed! Incorrect password.")
             
             print("you have more only",3-i,"attempts left")
             password = input("Enter your password: ")
             hashed_entered_password = generate_hash(password, stored_salt)
             i+=1


while True:
    action = input("Select an action: 'sign up' or 'log in': ").strip().lower()
        
    if action == "sign up":
        sign_up()
    elif action == "log in":
        log_in()
    else:
        print("Invalid action :(")
        continue
        
        
    continue_action = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_action != "yes":
        print("Thank you!! :)")
        break


