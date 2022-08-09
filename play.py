from datetime import datetime
import generate_random_number
import sqlite3

# Print out welcome message
print("")
print("Welcome to the Lotto and Powerball random numbers selector.")   
print("")


# Create and Connect to Database

conn = sqlite3.connect("ithuba.db")
cursor = conn.cursor()


# Load game

while True:
    # Create Table
    
    #cursor.execute(""" CREATE TABLE lotto (date Text, lotto_numbers Text)""")
    #cursor.execute(""" CREATE TABLE powerball (date Text, powerball_numbers Text, powerball Text)""")


    try:
        number = int(input("Please enter: \n 1 To select random Lotto numbers \n 2 To select random Powerball numbers\n 3 for Past Lotto numbers \n 4 for Past Powerball Numbers: "))

        if number == 1 :
        # Print 6 Random lotto numbers

            
            lotto_num = generate_random_number.lotto_numbers(52)
            # sorting the list in ascending order
            lotto_num.sort()
            now = datetime.now()
            time = now.strftime("%Y-%m-%d %H:%M:%S")
            lotto = ''.join(str(lotto_num))
            lot = [(time,lotto)]
            # Add data to database
            cursor.executemany("INSERT INTO lotto VALUES (?,?)",lot)
            # Save Data to database
            conn.commit()

            # Display date and time
            print("")
            print("")
            print("L O T T O  N U M B E R S")
            print("")

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

            now = datetime.now()
            time = now.strftime("%Y-%m-%d %H:%M:%S")
            power_balls = ''.join(str(powerball_num))
            power_ball = ''.join(str(powerball))

            power = [(time,power_balls,power_ball)]
            # Add data to database
            cursor.executemany("INSERT INTO powerball VALUES (?,?,?)",power)
            # Save Data to database
            conn.commit()

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

        elif number == 3:

            # Retrieve Data
            for row in cursor.execute('SELECT * FROM lotto ORDER BY date'):
                print(row)

        elif number == 4:

            # Retrieve Data
            for row in cursor.execute('SELECT * FROM powerball ORDER BY date'):
                print(row)




        
        else:
            print("Error! Please choose 1 for lotto and 2 for powerball")
            continue
        break


    except ValueError:
        print("Invalid Selection")
        