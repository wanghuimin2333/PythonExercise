'''
题目：斐波那契数列。
'''

arr = [0, 1]

tmp, num = 0, 1

dep = 20  # 数列长度

for i in range(dep - 2):
    tmp, num = num, tmp + num
    arr.append(num)

print(arr)

def fibonacci(n):
    fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2)
    for i in range(1,n+1):
        print(fib(i))
