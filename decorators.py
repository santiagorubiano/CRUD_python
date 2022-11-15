PASSWORD='12345678'

def password_required(func):
    def wrapper():
        """
        The function password_required is a decorator that takes a function as an argument and returns a
        wrapper function. 
        
        The wrapper function checks if the password is correct and if it is, it calls the function that was
        passed in as an argument. 
        
        If the password is incorrect, the wrapper function prints a message and returns None
        :return: The function wrapper
        """
        password= input('Cual es tu contraseña')
        
        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta')
    return wrapper
@password_required
def needs_pasworrd():
    print('La contraseña es correcta')

def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        
        return result.upper()
    return wrapper

@upper
def say_my_name(name):
     return 'hola, {}'.format(name)


if __name__ == '__main__':
    # needs_pasworrd()
     print(say_my_name('Santiago'))