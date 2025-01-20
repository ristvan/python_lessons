# The constant name is written in all uppercase snake_case format.
# The snake_case format means that the words are separated by underscores.
GLOBAL_CONSTANT = 4


# The global variable name is written in snake_case format.
# The snake_case format means that the words are separated by underscores.
global_variable = 0


# The class name is written in PascalCase format.
# The PascalCase format means that the first letter of each word is capitalized.
class ClassName:
   def __init__(self):
       # The variable name is written in snake_case format.
       # The snake_case format means that the words are separated by underscores.
       self.__private_variable_1 = 0
       self.public_variable_1 = 1

   # The method name is written in snake_case format.
   # The snake_case format means that the words are separated by underscores.
   def method_name_1(self, parameter_1, parameter_2):
       # The global keyword is needed in order to use and modify a global variable.
       global global_variable
       global_variable += 1
       print(f"{' ' * GLOBAL_CONSTANT * global_variable}method_name_1' begin")
       print(f"{' ' * GLOBAL_CONSTANT * (global_variable + 1)}{parameter_1=}, {parameter_2=}")
       print(f"{' ' * GLOBAL_CONSTANT * (global_variable + 1)}{self.__private_variable_1=}")
       print(f"{' ' * GLOBAL_CONSTANT * global_variable}'method_name_1' end")
       global_variable -= 1

   def method_name_2(self):
       # The global keyword is needed in order to use and modify a global variable.
       global global_variable
       global_variable += 1
       print(f"{' ' * GLOBAL_CONSTANT * global_variable}'method_name_2' begin")
       print(f"{' ' * GLOBAL_CONSTANT * (global_variable + 1)}{self.__private_variable_1=}")
       print(f"{' ' * GLOBAL_CONSTANT * global_variable}'method_name_2' end")
       global_variable -= 1


# The function name is written in snake_case format.
# The snake_case format means that the words are separated by underscores.
def function_name(parameter_1, parameter_2):
   # The global keyword is needed in order to use and modify a global variable.
   global global_variable
   global_variable += 1
   print(f"{' ' * GLOBAL_CONSTANT * global_variable}'function_name' begin")
   class_object = ClassName()
   class_object.method_name_1(parameter_1, parameter_2)
   print(f"{' ' * GLOBAL_CONSTANT * global_variable}{class_object.public_variable_1=}")
   print(f"{' ' * GLOBAL_CONSTANT * global_variable}'function_name' end")
   global_variable -= 1


if __name__ == "__main__":
   print("main begin")
   function_name("parameter_1", "parameter_2")
   print("main end")