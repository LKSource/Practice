greekAlphabet = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Theta']

def my_decorator(func):
    def wrapper(*args, **kwargs):
        for key, value in kwargs.items():
            kwargs[key] = value.capitalize()
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def isGreekAlphabet(name):
    return "True" if name in greekAlphabet else "False"

print(isGreekAlphabet(name="ALPHA"), isGreekAlphabet(name="beta"))  