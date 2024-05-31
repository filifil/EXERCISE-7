# Exe.2

def multiplication_table(n):
    table = [n*i for i in range(1, 11)]
    return table

number = int(input("Enter a number: "))
table = multiplication_table(number)

print(f"Multiplication table of {number}: {table}")