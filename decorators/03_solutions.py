import time


def cache(func):
    buffer = {}
    print(buffer)
    def wrapper(*args, **kwargs):
        if args in buffer:
            return buffer[args]
        
        result = func(*args, **kwargs)
        buffer[args]=result
        return result
    return wrapper



@cache
def long_running_function(a, b):
    time.sleep(4)
    return a+b

print(long_running_function(4, 8))
print(long_running_function(4, 8))
print(long_running_function(4, 10))

# Why Does This Matter?

# One buffer per Function: Because cache is called once per decorated function, 
# each function gets its own buffer dictionary. This is why long_running_function 
# and multiply (in the example above) would have separate caches.

# Wrapper Reused: The wrapper function, returned by cache, is reused every 
# time the decorated function is called. This allows the buffer to persist across calls, enabling caching.