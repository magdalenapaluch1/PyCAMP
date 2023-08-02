from password_checker import Password_Checker
    
if __name__ == '__main__':

    print("Check your password!")
    #user_password = input("Your password: ")
    user_password = "Polska1@"

    password = Password_Checker()
    safe_result = password.is_password_safe(user_password)

    if safe_result is False:
        print("Your password is not safe, please change it!")
    else:
        print("Your password is safe.")