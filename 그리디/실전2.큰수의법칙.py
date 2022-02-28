# 실전2. 큰수의법칙

n, m, k = map(int,input("n, m, k : ").split())

data = list(map(int,input("배열 입력 : ").split()))
data.sort()

first = data[-1]
second = data[-2]
result = 0

while True :
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    
    if m == 0 :
        break
    result += second
    m -= 1

print("결과값 : ", result)    






