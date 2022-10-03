# 반복구조
def binarySearchW(n, key):
    low = 0  # 시작 지점
    high = n - 1  # 끝 지점

    while low <= high:  # 시작 지점이 끝 지점보다 작거나 같은 경우 ※ 시작과 끝이 같은 경우는 마지막 하나만 남았을 때임
        mid = (low + high) // 2  # 중간 지점

        if arr[mid] == key:  # 찾는 값과 중간값이 같다면
            return mid  # 중간 인덱스 리턴
        elif arr[mid] > key:  # 찾는 값이 왼쪽에 있다면
            high = mid - 1  # 끝 지점을 당겨줌
        elif arr[mid] < key:  # 찾는 값이 오른쪽에 있다면
            low = mid + 1  # 시작 지점을 당겨줌

    return -1  # 찾는 값이 없을 때 리턴값


# 재귀구조
def binarySearchR(low, high, key):
    if low > high:  # 찾는 값이 없는 경우
        return -1
    else:
        mid = (low + high) // 2  # 중간 지점

        if arr[mid] == key:  # 찾는 값과 중간값이 같다면
            return mid  # 중간 인덱스 리턴
        elif arr[mid] > key:  # 찾는 값이 왼쪽에 있다면
            return binarySearchR(low, mid - 1, key)  # 끝 지점을 당겨줌
        elif arr[mid] < key:  # 찾는 값이 오른쪽에 있다면
            return binarySearchR(mid + 1, high, key)  # 시작 지점을 당겨줌
    # 안으로 들어가면서 찾은 값을 바통을 넘겨주듯이 리턴하는 구조


N = 10
arr = [8, 11, 17, 22, 23, 28, 34, 45, 81, 99]
print(binarySearchW(N, 81))
print(binarySearchR(0, N - 1, 45))


import sys
input = sys.stdin.readline

N = int(input())
n_num = set(map(int, input().split()))
M = int(input())
m_num = list(map(int, input().split()))

for j in m_num:
    if j in n_num:
        print(1)
    else:
        print(0)