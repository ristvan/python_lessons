def loops():
   simple_loops()
   nested_loops()
   extra_statements()


def simple_loops():
   # For loop
   for i in range(10):
       print(i)
   # While loop
   i = 0
   while i < 10:
       print(i)
       i += 1


def nested_loops():
   print('Nested loops')
   for i in range(3):
       for j in range(3):
           print(i, j)


def extra_statements():
   print('Extra statements')
   for i in range(5):
       text = ""
       for j in range(5):  # [0, 1, 2, 3, 4]
           if j > i:
               break
           text += " "
           if j < i:
               text += " "
               continue
           text += f"{j}"
       print(text)


# Task 1
# The prime factors of a number are the prime numbers that can be multiplied to get the original number.
# The function returns a list of prime factors.
def prime_factors(number: int) -> list[int]:
    factors = []
    divisor = 2
    while number > 1:
         if number % divisor == 0:
              factors.append(divisor)
              number //= divisor
         else:
              divisor += 1
    return factors


# Task 2
# The prime factors of a number are the prime numbers that can be multiplied to get the original number.
# The function returns a dictionary where the keys are the prime factors and the values are the number of occurrences.
def prime_factors2(number: int) -> dict[int, int]:
    factors = dict()
    divisor = 2
    number_of_divisions = 0
    while number > 1:
         if number % divisor == 0:
             number_of_divisions += 1
             number //= divisor
         else:
             if number_of_divisions > 0:
                 factors[divisor] = number_of_divisions
                 number_of_divisions = 0
             divisor += 1
    return factors


if __name__ == '__main__':
   loops()
   print(prime_factors(1668346680))
   print(prime_factors2(1668346680))
