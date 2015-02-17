# Applies all operators on x and y

x = float(input("Please enter the first number:"))
y = float(input("Please enter the second number:"))
print("%f + %f = %.2f" % (x, y, (x + y)))
print("%f - %f = %.2f" % (x, y, (x - y)))
print("%f * %f = %.2f" % (x, y, (x * y)))
print("%f / %f = %.2f" % (x, y, (x / y)))
print("%f // %f = %.2f" % (x, y, (x // y)))
print("%f ** %f = %.2f" % (x, y, (x ** y)))
print("%f %% %f = %.2f" % (x, y, (x % y)))
print("Done!")

