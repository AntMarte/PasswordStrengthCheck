
#We define the function "check_password_strength"

def check_password_strength(password):

    # We create the criteria for the password with length, presence of uppercase and lowercase letters, numbers, and special characters
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    numeric = any(char.isdigit() for char in password)
    special = any(char.isalnum() == False for char in password)

    if length >= 8 and uppercase and lowercase and numeric and special:
        return "Strong"
    elif length >= 6 and uppercase and lowercase and numeric:
        return "Moderate"
    else:
        return "Weak"

    pass
