
def my_dec(func):
    def wrapper():
        print("IDK know.")
        func()
        print("what should I say?")
    return wrapper

@my_dec
def say_hello():
    print("Hello!,")
say_hello()