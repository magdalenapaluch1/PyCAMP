from password_checker import Password_Checker

if __name__ == '__main__':

    print("Check your password!")
    #user_password = input("Your password: ")
    user_password = "Polska"

    pc = Password_Checker()
    safe_result = pc.is_password_safe(user_password)
    pc.print_password_results(safe_result)
