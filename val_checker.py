def val_checker(func):
    def wrapper(x):
        while x > 0:
            return func(x)
        else:
            print("ValueError: wrong val", x)
    return wrapper

@val_checker
def calc_cube(x):
   print(x ** 3)
a = calc_cube(5)
a = calc_cube(-5)





