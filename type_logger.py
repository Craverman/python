def type_logger(func):
    def wrapper(*x):
        for el in x:
            print(f"{el}: {type(el)}")
        return func(*x)
    return wrapper

@type_logger
def calc_cube(*x):
    for arg in x:
        print(arg**3)

calc_cube(5,6,7)

