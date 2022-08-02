from datetime import datetime

import generate_random_number

# Print out welcome message
print("")
print("Welcome to the Lotto and Powerball random numbers selector.")   
print("")

while True:

    try:
        number = int(input("Please enter 1 for Lotto or 2 for Powerball: "))

        if number == 1 :
        # Print 6 Random lotto numbers
            lotto_num = generate_random_number.lotto_numbers(52)
            # sorting the list in ascending order
            lotto_num.sort()

            # Display date and time
            print("")
            print("")
            print("L O T T O  N U M B E R S")
            print("")

            now = datetime.now()
            print ("Date and time : ")
            print (now.strftime("%Y-%m-%d %H:%M:%S"))

            #Print numbers
            print("")
            print("Lotto numbers: %s" %(lotto_num))

        elif number == 2:

            # Generate and Print Powerball numbers
            powerball_num= generate_random_number.powerball_numbers(50)
            # sorting the list in ascending order
            powerball_num.sort()
            powerball = generate_random_number.powerball(20) 

            # Display date and time
            print("")
            print("")
            print("P O W E R B A L L  N U M B E R S")
            
            print("")
            now = datetime.now()
            print ("Date and time : ")
            print (now.strftime("%Y-%m-%d %H:%M:%S"))

            #Print numbers
            print("")
            print("%s %s" % (powerball_num,powerball))        
            print("")

        
        else:
            print("Error! Please choose 1 for lotto and 2 for powerball")
            continue
        break


    except ValueError:
        print("Invalid Selection")
        