class Password_Checker():

    def is_password_safe(self, password) -> list:
 
        safe = []
        if len(password) < 8:
            safe.append("too_short")

        if any(chr.isdigit() for chr in password) is False:
            safe.append("no_digit")
    
        if any(not chr.isalnum() for chr in password) is False:
            safe.append("no_special")

        if any(chr.isupper() for chr in password) is False:
            safe.append("no_upper")
        
        if any(chr.islower() for chr in password) is False:
            safe.append("no_lower")

        if len(safe) == 0:
            safe.append("password_safe")

        return safe

    def print_password_results(self, results):

        if "password_safe" in results:
            print("Your password is safe.")

        if "too_short" in results:
            print("Your password is too short.")

        if "no_digit" in results:
            print("Your password does not have digit.")

        if "no_special" in results:
            print("Your password does not have special character.")

        if "no_upper" in results:
            print("Your password does not have uppercase character.")
            
        if "no_lower" in results:
            print("Your password does not have lowercase character.")