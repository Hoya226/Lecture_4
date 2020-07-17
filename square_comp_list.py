#n_lists = [1,2,3,4,5,6,7,8,9]
n_lists = list(range(1, 101))

square_arr = [a**2 for a in n_lists]

#for문 기본 for a in n_lists -> 앞에 식을 써서 축약가능 a**2 for a in n_lists 처럼


print(square_arr)

