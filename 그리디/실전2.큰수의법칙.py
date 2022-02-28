# 실전2. 큰수의법칙

n, m, k = map(int,input("n, m, k : ").split())

data = list(map(int,input("배열 입력 : ").split()))

max = data[0]

for i in range(data):
    if (max < data[i]):
        max = data[i]

