'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''

for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b and b != c and a != c:
                print(a, b, c)
        pass
    pass
"""有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
a=[]
for i in range(1,5):
    for j in range (1,5):
        for k in range(1,5):
            if i==j or j==k or i==k:
                continue
            else:
                tmp=100*i+10*j+k
            a.append(tmp)
            

print(len(a))
print(a)
