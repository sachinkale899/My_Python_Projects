#password strength cheaker project
#conditions:
#Ae least 8 characters long,contain both uppercase and lowercase letters,has at least one digit,and at least one special character
def password_strenth_cheaker(password):
    special_characters = "!@#$%^&*()-+"
    if len(password) < 8:
        return "weak:password is less than 8 characters"
    if not any(char.isupper() for char in password):
        return "weak:password does not contain uppercase letters"
    if not any(char.islower() for char in password):
        return "weak:password does not contain lowercase letters"
    if not any(char.isdigit() for char in password):
        return "weak:password does not contain digits"
    if not any(char in special_characters for char in password):
        return "medium:password does not contain special characters"
    return "strong:password is strong"

def password_cheaker():
    password=input("Enter your password(for quite type'exit'):")
    while True:
        if password.lower() == "exit":
            print("thank you for using password cheaker")
            break
        print(password_strenth_cheaker(password))
        password = input("Enter your password(for quite type'exit'):")

if __name__=="__main__":
    password_cheaker()
