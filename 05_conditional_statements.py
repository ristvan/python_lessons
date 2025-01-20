def check_age(age):
    if age >= 18:
        print('You are an adult')
    elif age <= 2:
        print('You are a baby')
    elif age < 14:
        print('You are a child')
    else:
        print('You are not an adult')


def conditional_branching():
    color = 'blue'
    device = 'monitor'
    is_rgb_color = (color == 'red' or color == 'blue' or color == 'green')
    if (device == 'monitor' or device == 'smartphone') and is_rgb_color:
        print('Red or blue or green (RGB)')
    else:
        print('Not RGB')
    x1 = 1
    x2 = 2
    y1 = 3
    y2 = 4
    if x1 == x2 and y1 == y2:
        print('The two points are the same')
    elif x1 == x2:
        print('The two points are on the same vertical line')
    elif y1 == y2:
        print('The two points are on the same horizontal line')
    else:
        print('The line is not horizontal or vertical')
    if 100 <= x <= 200 or 300 <= x <= 400:
        print('x is between 100 and 200 or between 300 and 400')


def check_score(nationality, score):
    if nationality == 'Magyar' and score >= 95:
        print('5')
    elif nationality != 'Magyar' and score >= 90:
        print('A')
    elif nationality == 'Magyar' and score >= 85:
        print('4')
    elif nationality != 'Magyar' and score >= 80:
        print('B')
    elif score >= 75:
        print('3')
    elif score >= 50:
        print('2')
    else:
        print('1')


def main():
    age = 3
    check_age(age)
    # nationality = 'Magyar'
    nationality = 'Nem magyar'
    score = 84
    check_score(nationality, score)
    conditional_branching()


if __name__ == '__main__':
    main()
    