# Check if a number is an Armstrong number
number = int(input("Enter a number: "))
temp = number
sum = 0
# Count how many digits (manually)
count = 0
n = number
while n > 0:
    count = count + 1
    n = n // 10
# Add each digit raised to the power of count
n = number
while n > 0:
    digit = n % 10
    sum = sum + (digit ** count)
    n = n // 10
# Check if it's Armstrong
if sum == temp:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")