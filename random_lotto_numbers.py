import generate_random_number

# Print 6 Random lotto numbers

index =0

while index <=2:
    lotto_num = generate_random_number.lotto_numbers(52)
    lotto_num.sort()
    print("Lotto numbers: %s" %(lotto_num))
    index +=1
