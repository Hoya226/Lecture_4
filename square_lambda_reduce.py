#reduce의 역할
#라이브러리 -> 라이브러리 설치해야함 from functools import reduce 설치할 필요는 없고 내장
from functools import reduce
n_lists = [10,20,30,40,50]

result = reduce(lambda x, y: x+y, n_lists)

print(result)


#결과값 150 나와 -> 10+20+30+40+50