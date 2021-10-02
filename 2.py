a = float(input("Enter the first leg "))
b = float(input("Enter the second leg "))
c = (a ** 2 + b ** 2) ** 0.5
P = a + b + c
S = 1/2 * a * b
print("The perimeter of the triangle is " + str(P))
print("The area of the triangle is " + str(S))