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
    count_3 = 0
    count_4 = 0
    count_5 = 0
    while user_numbers != lotto_numbers:
        lotto_numbers = Random_Lotto_Set()
        i += 1
        intersection = user_numbers.intersection(lotto_numbers)
        if user_numbers == lotto_numbers:
            print(f"Win! You won after {i} lotteries.")
        elif len(intersection) == 3:
            count_3 += 1
        elif len(intersection) == 4:
            count_4 += 1
        elif len(intersection) == 5:
            count_5 += 1

    print(f"You hit 3 in lottery {count_3} times.")
    print(f"You hit 4 in lottery {count_4} times.")
    print(f"You hit 5 in lottery {count_5} times.")

    return i

def Price_Of_Coupons(number_of_coupons):
    one_coupon_price = 3

    return (one_coupon_price * number_of_coupons)

if __name__ == '__main__':

    print("""
    This is Lotto simulation.
    One coupon costs 3PLN.
    There are 3 lotteries in a week.
    Let's see an example of playing continuously until win.
    Good luck!
    """)

    numbers = User_Choose_Numbers()

    number_of_coupons = Draw_Until_Win(numbers)

    print(f"You spent: {Price_Of_Coupons(number_of_coupons):,} PLN.")

#TODO
#Kalkulacja opłacalności
#zwrócić wyniki z funkcji Draw_To_Win
#Określenie wartości wygranych

