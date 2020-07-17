def add(x, y):
    return x + y


add_other = lambda x, y : x+y #여기서만 사용하는 임시적인 함수(람다함수로 지정만하면됨)


#print(add(10, 50))
print(add_other(10,50))


def add_plus(x,y,z):
    result_1 = x+y
    result_2 = lambda z : z**3


    return result_2



print(add_plus(10,20,30))