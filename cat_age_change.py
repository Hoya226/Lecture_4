class Cat:
    
    #생성자 메소드
    def __init__(self , name , age):
        self.name = name
        self.age = age
       
    def __str__(self):
       # print('Cat(namte = '+self.name+', age = '+self.age+')')
        return 'Cat(namte = '+self.name+', age = '+str(self.age)+')'

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age


nabi = Cat('나비', 3)
#nero = Cat('네로', '흰색')


print(nabi)
nabi.set_age(4)
nabi.set_age(-5)
#print(nero)
print(nabi)
