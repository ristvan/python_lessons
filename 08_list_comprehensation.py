def list_comprehension():
    # The list comprehension is a concise way to create lists.
    # The list comprehension is a more readable and faster way to create lists.
    # The list comprehension is a more readable way to create lists.
    l = [i for i in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(l)
    # The list comprehension is equivalent to the following code:
    # l = list()
    # for i in range(10):
    #     l.append(i)

    # The general syntax of the list comprehension is:
    #     [expression for item in iterable if condition]
    # The expression is the value that is added to the list.
    # The item is the value that is iterated over.
    # The iterable is the object that is iterated over.
    # The condition is the filter that is applied to the item.
    l = [i for i in range(10) if i % 2 == 0]  # [0, 2, 4, 6, 8]
    print(l)
    # The list comprehension is equivalent to the following code:
    # l = list()
    # for i in range(10):
    #     if i % 2 == 0:
    #         l.append(i)

    l = [i ** 2 for i in range(10) if i % 2 == 0]  # [0, 4, 16, 36, 64]
    print(l)
    # The list comprehension is equivalent to the following code:
    # l = list()
    # for i in range(10):
    #     if i % 2 == 0:
    #         l.append(i ** 2)

    coordinates = [(x, y) for x in range(3) for y in range(3)] # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    print(coordinates)
    # The list comprehension is equivalent to the following code:
    # coordinates = list()
    # for x in range(3):  # [0, 1, 2]
    #     for y in range(3):  # [0, 1, 2]
    #         coordinates.append((x, y))

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    flat_matrix = [number for row in matrix for number in row]
    print(flat_matrix) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # The list comprehension is equivalent to the following code:
    # flat_matrix = list()
    # for row in matrix:
    #     for number in row:
    #         flat_matrix.append(number)



if __name__ == '__main__':
    list_comprehension()

# Exercises:
#   1. Find all the numbers from 1-1000 that are divisible by 7.
#   2. Given numbers = range(20), produce a list containing the word 'even' if the number is even and 'odd' if the number
#      is odd. The list should look like this: ['odd', 'even', 'odd', ...],
#   3. Given a list of words, create a new list that contains only the words that have an even number of characters.


