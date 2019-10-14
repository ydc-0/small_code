
# 获取最长单调递增子序列
# https://blog.csdn.net/u013178472/article/details/54926531
# https://blog.csdn.net/zhangguixian5/article/details/8205631


def search_idx(A,v):
    for i,n in enumerate(A):
        if v < n:
            return i

L = [2,1,5,3,6,4,8,9,7]

B = [L[0]]
C = [1]

for i,n in enumerate(L):
    if i == 0:
        continue
    if n > B[-1]:
        B.append(n)
        C.append(len(B))
    else:
        j = search_idx(B, n)
        B[j] = n
        C.append(j+1)

print(B)
print(C)

max_len = len(B)

for i in range(8,-1,-1):
    if C[i] == max_len:
        print(L[i])
        max_len -= 1
