
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value=", ".join(f"{k}={v}" for k, v in kwargs.items())

        print(f"Calling function {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
        return func(*args, **kwargs)

    return wrapper


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")

# greet("Chetan", greeting="Kanji")

@debug
def hello():
    print("Hello")

hello()