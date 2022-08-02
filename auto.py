# Random powerball number generator(Done)
# Automatically run the app every Tuesday and Thursday(Done)
# Generate 2 list of random numbers(Done)
# Email or sms the generated numbers
from calendar import TUESDAY
import schedule
import time
import generate_random_number


def play():
    index = 0
    while index <=  5:
        random_powerball_numbers = generate_random_number.powerball_numbers(50)
        random_powerball_numbers.sort()
        random_powerball = generate_random_number.powerball(20)
        print(random_powerball_numbers,random_powerball)
        index +=1

schedule.every().friday.at("06:33").do(play)
schedule.every().thursday.at("13:00").do(play)


while True:
    schedule.run_pending()
    time.sleep(1)
