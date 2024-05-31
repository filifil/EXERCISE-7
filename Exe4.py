def count_even_odd_digits(number):
    even_count = 0
    odd_count = 0
    
    for digit in str(number):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return even_count, odd_count

number = 1234567890
even_count, odd_count = count_even_odd_digits(number)

print(f"Number: {number}")
print(f"Even digits count: {even_count}")
print(f"Odd digits count: {odd_count}")
