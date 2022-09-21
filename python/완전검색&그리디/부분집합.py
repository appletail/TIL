# 비트(반복구조)를 이용한 모든 부분집합
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1, 1 << n):    # range안에 1, 를 빼고 만들면 공집합 없이 구할 수 있다.
    for j in range(n):
        if i & (i << j):
            print(arr[j], end=' ')
    print()


# 재귀를 이용한 부분 집합
def f(i, k):
    if i == k:
        # print(bit)
        for j in range(k):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    else:
        bit[i] = 0
        f(i + 1, k)
        bit[i] = 1
        f(i + 1, k)


arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
bit = [0] * n
f(0, n)
