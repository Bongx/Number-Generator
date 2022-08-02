import random

# Difine a function to generate random powerball numbers
def powerball_numbers(num):
   return random.sample(range(1,num),5)
  

# Define powerball
def powerball(num):
   return random.sample(range(1,num),1)


# Define a function to generate random lotto numbers
def lotto_numbers(num):
   return random.sample(range(1,num),6) 


   
