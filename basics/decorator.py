import functools

def log(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("call:", func.__name__)
        return func(*args, **kwargs)
    
    return wrapper
@log
def foo():
    print("I am a fool")


def log_with_parameter(text):
    def decorator(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(text, func.__name__)
            return func(*args, **kwargs)
        
        return wrapper
    return decorator