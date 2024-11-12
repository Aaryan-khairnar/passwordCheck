#user has to set a password for his account
#the password must be
#At least 8 characters long.
#A combination of uppercase letters, lowercase letters, numbers, and symbols.

condition1 = False
condition2 = False
condition3 = False
condition4 = False

def length(password):

    if(len(password)>=8):
        return True
    else:
        print("Enter password more than 8 characters.")
        return False
    


def checkupper(password):

    if any(char.isupper() for char in password):
        return True
    else:
        print("Include uppercase characters.")
        return False
    

    
def checknum(password):
    if any (char.isdigit() for char in password): #Learn this
        return True
    else:
        print("Include numbers.")
        return False
    

    
special_chars = "!@#$%^&*{()_+-=}[]|:;'<>,.?/~`" 
    
def checkspecial(password):
    if any (char in special_chars for char in password):
        return True
    else:
        print("Include any Special characters.")
        return False
    
    
    
while not (condition1 and condition2 and condition3 and condition4):  #I GOT TO STUDY THIS

    password= input("enter a password: ")
    
    condition1= length(password)
    condition2= checkupper(password)
    condition3= checknum(password)
    condition4= checkspecial(password)

    if (condition1 and condition2 and condition3 and condition4 == True):
        print(f"Your password is good. Use {password} as your password.")
    else:
        print("Enter another password")
    

