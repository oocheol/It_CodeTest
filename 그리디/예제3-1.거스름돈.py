# 예제 3-1 거스름돈

money = [500, 100, 50, 10]
count = 0
cash = int(input("잔액 : "))

for x in money:
    count += cash // x
    cash %= x

print(count)
