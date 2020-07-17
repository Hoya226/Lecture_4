n_list = [1,20,-3,4,-20,100]

#print('음수는 ')

# for a in filter(lambda x: x<0, n_list) :

#     print(a)


#어레이를 활용한 음수 필터

minus_arr = []

for a in filter(lambda x: x<0, n_list):
    minus_arr.append(a)

print(minus_arr)