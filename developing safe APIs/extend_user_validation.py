import re

def validate_username(username):
    if not (5 <= len(username) <= 20):
        return False, "Username must be between 5 and 20 characters."
    
    if not username[0].isalpha():
        return False, "Username must start with a letter"
    
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ1234567890_.")
    for char in username:
        if char not in allowed_chars:
            return False, "Username can only contain letters, numbers, underscores, and dots"
        
    return True, "Username is valid"




# Change the function so usernames:
# - start with a letter,
# - contain only letters, numbers, underscores or dots,
# - are 5-20 characters long.
print(validate_username('user_1'))   # True or False?