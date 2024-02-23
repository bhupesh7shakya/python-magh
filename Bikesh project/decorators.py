def star(func):
    def wrapper(name):
        print('*'*25)
        func(name)
        print('*'*25)
    return wrapper
#@star
def hello(name):
    print('hello', name)

# @star
def bye():
    print('hello')
star(hello)('Bikesh Kumar Yadav')