from datetime import datetime
import generate_random_number 
import random

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

def powerball(num):
    return random.sample(range(1,num),1)

while True:
    try:
        number = int(input("Please select 1 for Lotto or 2 for Powerball: "))

        if number == 1 :
            random_lotto_numbers = generate_random_number.lotto_numbers(52)
            random_lotto_numbers.sort()
            print(random_lotto_numbers)

        elif number == 2 :
            random_powerball_numbers = generate_random_number.powerball_numbers(50)
            random_powerball_numbers.sort()
            random_powerball = powerball(20)
            random_powerball.sort()
            print(random_powerball_numbers,random_powerball)


        else: 
            print("Incorrect selection")
            continue
        break

    except ValueError:
        print("Invalid value")
