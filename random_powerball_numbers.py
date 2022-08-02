import generate_random_number
from datetime import datetime
# Generate and Print 5 Powerball numbers
powerball_num= generate_random_number.powerball_numbers(50)
print("Your numbers are: %s" % (powerball_num))

# Generate and print the Powerball
powerball = generate_random_number.powerball(20)
print("Powerball %s" %(powerball))

now = datetime.now()
print ("Date and time : ")
t=now.strftime("%Y-%m-%d %H:%M:%S")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
    
play_time=["Date %s Powerball Numbers: %s %s" %(t,powerball_num,powerball)]
print(play_time)