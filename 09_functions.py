
def function():
    print("Hello from a function")


def function_with_parameters(parameter_1, parameter_2):
    print(f"{parameter_1=}, {parameter_2=}")
    return parameter_1 + parameter_2


def function_with_default_parameters(parameter_1, parameter_2=1):
    print(f"{parameter_1=}, {parameter_2=}")
    return parameter_1 + parameter_2

def function_without_body():
    pass


if __name__ == '__main__':
    print(function())
    print(function_with_parameters(1, 2))
    print(function_with_default_parameters(1))
    print(function_with_default_parameters(3, 4))
    print(function_without_body())
