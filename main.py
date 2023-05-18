from password_strength_checker import check_password_strength

def main():
    password = input("Enter a password: ")
    strength = check_password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
