import random

def User_Choose_Numbers():
    set_user_numbers = set()

    # for num in range(6):
    #     user_number = int(input(f"Choose your {num + 1} number to draw: "))
    #     set_user_numbers.add(user_number)
    set_user_numbers = {3, 45, 34, 2, 13, 32}
    return set_user_numbers

def Random_Lotto_Set():
    set_lotto_numbers = set()
    while len(set_lotto_numbers) < 6:
        random_number = random.randint(1, 50)
        if not random_number in set_lotto_numbers:
            set_lotto_numbers.add(random_number)
    return set_lotto_numbers

def Draw_Until_Win(user_numbers):
    lotto_numbers = set()
    i = 0
    while user_numbers != lotto_numbers:
        lotto_numbers = Random_Lotto_Set()
        i += 1
        if user_numbers == lotto_numbers:
            print(f"Win! You won after {i} lotteries.")

if __name__ == '__main__':

    numbers = User_Choose_Numbers()

    Draw_Until_Win(numbers)

#TODO
#Policzyć ile to kosztuje
#Czy wypadła 5, 4, 3
#Kalkulacja opłacalności