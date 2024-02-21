def star(func):
    def wrapper(name):
        print('*'*10)
        func(name)
        print('*'*10)
    return wrapper
        
@star
def hello(name):
    print('hello ',name)
    

# @star
# def bye():
#     print('hello')

hello('ram')
# star(hello)()
# bye()