# def adult_func(n):
#         if n>=19:
#             return '성인입니다'

#         else:
#             return '미성년자입니다'


# #print(adult_func(18))



# ages = [34,25,17,13,54]
# print('성년 리스트')

# for a in filter(adult_func, ages) :

#     print(a)


#이 상태 오류나와 -> 리턴값이 트루 또는 거짓이어야해

def adult_func(n):
        if n>=19:
            return True

        else:
            return False


#print(adult_func(18))



ages = [34,25,17,13,54]
print('성년 리스트')

for a in filter(adult_func, ages) :

    print(a)
