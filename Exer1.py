#Exer.1
def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

num = int(input("Enter a number: "))
result = calculate_sum(num)
print(f"The sum of all numbers from 1 to {num} is: {result}")