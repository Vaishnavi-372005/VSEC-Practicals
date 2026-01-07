def is_armstrong(num):
    n = len(str(num))  # Number of digits
    sum_of_powers = 0  # Initialize sum

    # Iterate through each digit and calculate power
    for digit in str(num):
        sum_of_powers += int(digit) ** n

    return num == sum_of_powers

# User input
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is Armstrong number.")
else:
    print(f"{num} is not Armstrong number.")