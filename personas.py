class Persona:
    def __init__(self,name,age) -> None:
        self.name =name 
        self.age = age
        
    def say_hello(self):
        print('hello, my name is {} and i am {} years old'.format(self.name,self.age))
            
if __name__ =='__main__':
    person = Persona('Santiago',24)
    
    
    print('age:{}'.format(person.age))
    person.say_hello()