years = int(input("Enter the number of years you have "))
minutes = years * 525600 * 1/3
num = 2800000 * minutes / (2800000 * 5)
msg = f'You will be able to see {num} exhibits'
print(msg)
exh = int(input("Enter the number of exhibits you would like to see "))
time = exh * 5
message = f'The amount of time you will need to do so equals {time} minutes'
print(message)