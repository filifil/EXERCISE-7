def create_password():
    while True:
        password = input("Please create a password (at least 4 and not longer than 6 characters, letters only): ")
        if len(password) < 4 or len(password) > 6:
            print("Password must be at least 4 characters long and not longer than 6 characters.")
        elif not password.isalpha():
            print("Password can only contain letters.")
        else:
            return password

def validate_password(password):
    while True:
        user_input = input("Please enter your password: ")
        if user_input == password:
            print("Password successfully validated.")
            break
        else:
            print("Invalid password. Please try again.")

# Main program
password = create_password()
validate_password(password)