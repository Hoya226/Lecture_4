#class Cat:
 #   color = 'red'
  #  sound = '야옹'
    #생성자 메소드
   # def __init__(self , name , color):
    #    self.name = name
    #    self.color = color
    #    self.sound = sound

  #  def meow(self, name):

   #     print('우리 고양이는 못생긴 {}에요'.format(name))
    #    print("길냥이 {}이는 색깔이 {}구요 자주 야옹~! 야옹~! 거려요".format(self.name, self.color))

#gang_cat('미옹', '컬러플하', '미야옹')
#jong_cat('태경', '똥')
#gang_cat.meow('라온', '미야옹')
#jong_cat.mewo('미옹')


class Cat:
    color = 'red'
    sound = '야옹'
    #생성자 메소드
    def __init__(self , name , color , sound):
        self.name = name
        self.color = color
        self.sound = sound
    def meow(self ,name  , sound):
        print('우리 고양는 못생긴 {} 예요'.format(name))
        print("길냥이 {}이는 색깔이 {}구요 자주 {}~! {}~! 거려요".format(self.name, self.color , self.sound ,sound ))
gang_cat = Cat('미옹', '컬러플하', '미아옹')
# jong_cat = Cat('태경', '똥이')
gang_cat.meow('라온','미웅')
# jong_cat.meow('라온')