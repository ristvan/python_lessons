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
       for j in range(5):
           if j > i:
               break
           text += f" {j}"
       print(text)


if __name__ == '__main__':
   loops()
