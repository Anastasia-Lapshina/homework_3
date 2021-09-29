name = input("Enter your name ")
surname = input("Enter your surname ")
year = input("Enter your year of birth ")
print(name + "_" + surname + "_" + year)
temp = name
name = surname
surname = temp
year = (60 + int(year))
print(name + "_" + surname + "_" + str(year))