years = int(input("Enter the number of years you have "))
minutes = years * 525600 * 1/3
num = 2800000 * minutes / (2800000 * 5)
print("You'll be able to see " + str(num) + " exhibits")
exh = int(input("Enter the number of exhibits you would like to see "))
time = exh * 5
print("The amount of time you will need to do so equals " + str(time) + " minutes")