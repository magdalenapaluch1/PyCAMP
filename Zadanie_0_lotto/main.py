import random

LOTTO_WIN_PRICES = {"all numbers": 2000000,
                    "5 numbers": 5300,
                    "4 numbers": 170,
                    "3 numbers": 24}


def user_choose_numbers():
    set_user_numbers = set()

    # for num in range(6):
    #     user_number = int(input(f"Choose your {num + 1} number to draw: "))
    #     set_user_numbers.add(user_number)
    set_user_numbers = {3, 45, 34, 2, 13, 32}
    return set_user_numbers


def random_lotto_set():
    set_lotto_numbers = set()
    while len(set_lotto_numbers) < 6:
        random_number = random.randint(1, 50)
        if not random_number in set_lotto_numbers:
            set_lotto_numbers.add(random_number)
    return set_lotto_numbers


def draw_until_win(user_numbers):
    lotto_numbers = set()
    attempts = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    while user_numbers != lotto_numbers:
        lotto_numbers = random_lotto_set()
        attempts += 1
        intersection = user_numbers.intersection(lotto_numbers)
        if user_numbers == lotto_numbers:
            print(f"Win! You won after {attempts} lotteries.")
        elif len(intersection) == 3:
            count_3 += 1
        elif len(intersection) == 4:
            count_4 += 1
        elif len(intersection) == 5:
            count_5 += 1

    results = {"total_attempts": attempts,
               "hit3": count_3,
               "hit4": count_4,
               "hit5": count_5}

    return results


def price_of_coupons(number_of_coupons):
    one_coupon_price = 3

    return one_coupon_price * number_of_coupons


def total_won_money(results: dict):

    return LOTTO_WIN_PRICES['3 numbers'] * results['hit3'] + LOTTO_WIN_PRICES['4 numbers'] * results['hit4'] + \
           LOTTO_WIN_PRICES['5 numbers'] * results['hit5'] + LOTTO_WIN_PRICES['all numbers']


def print_results(results: dict):

    print(f"You hit 3 in lottery {results['hit3']} times.")
    print(f"You hit 4 in lottery {results['hit4']} times.")
    print(f"You hit 5 in lottery {results['hit5']} times.")
    print(f"You spent: {price_of_coupons(results['total_attempts']):,} PLN.")
    print(f"Your total win is: {total_won_money(results):,} PLN.")


if __name__ == '__main__':

    print("""
This is Lotto simulation.
One coupon costs 3PLN.
There are 3 lotteries in a week.
Let's see an example of playing continuously until win.
Good luck!
""")

    numbers = user_choose_numbers()

    all_results = draw_until_win(numbers)

    print_results(all_results)

# TODO
# Czas potrzebny na główną wygraną
# DOCString uzupelnic
