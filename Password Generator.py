# function to generator random password
import random
import string

def password(length = 8):
    
    characters = string.ascii_letters + string.digits + string.punctuation
  
    password = ''.join(random.choice(characters) for _ in range(length))
  
    return password
  
  
  
pw = password()  
print(pw)
