def basic_number_operations(a, b):
   # The + adds two numbers
   total = a + b
   # The - subtracts the second number from the first one
   difference = a - b
   # The * multiplies two numbers
   product = a * b
   # The / divides the first number by the second. The result will be a Real number.
   quotient = a / b
   # The % calculates the remained of the division of the numbers. The result is a Natural number.
   remainder = a % b
   # The // divides the first number by the second. The result will be an Integer number (Z).
   integer_quotient = a // b
   print(a, "+", b, "=", total)
   print(a, "-", b, "=", difference)
   print(a, "*", b, "=", product)
   print(a, "/", b, "=", quotient)
   print(a, "%", b, "=", remainder)
   print(a, "//", b, "=", integer_quotient)


def basic_string_operations():
   a = "Hello"
   b = "World"
   # Strings can be added to each other. It will result a concatenation
   print(a, "+", b, "=", a + b)
   # A string can be multiplied by a number. It will result the string by the number times.
   print(a, "*", 3, "=", a * 3)


if __name__ == '__main__':
   basic_number_operations(5, 3)
   basic_string_operations()
