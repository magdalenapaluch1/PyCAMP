
class Password_Checker():

    def is_password_safe(self, password) -> bool:
        len_password = len(password)
        safe = True
        if len_password < 8:
            safe = False


        numbers_in_password = any(chr.isdigit() for chr in password)
        if numbers_in_password is False:
            safe = False
    
        special_char_in_password = any(not chr.isalnum() for chr in password)
        if special_char_in_password is False:
            safe = False

        
        upper_char_in_password = any(chr.isupper() for chr in password)
        if upper_char_in_password is False:
            safe = False
        
        lower_char_in_password = any(chr.islower() for chr in password)
        if lower_char_in_password is False:
            safe = False

        return safe