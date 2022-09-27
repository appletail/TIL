# Hoare-Partition
# 양 끝에서 출발하여 서로 피벗보다 작고 큰게 나오면 서로 교환
# 피벗 기준으로 좌우 나눠서 각각 다시 진행
def partitionH(L, R):
    p = L
    i = L + 1
    j = R

    while i <= j:
        while i <= j and arr[i] <= arr[p]:
            i += 1
        while i <= j and arr[j] >= arr[p]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        # 한 번 끝낸 경우
        # 3 2 1 0 6 5 4 8 7 5
        # p     j i
        # 따라서 j와 p를 바꿔줘야함
    arr[p], arr[j] = arr[j], arr[p]
    return j


# Lomuto-Partiotion
# 왼쪽에서 i와 j를 같이 출발하여 더 p보다 더 큰게 나오면 i는 멈추고 j만 계속 이동
def partitionL(L, R):
    p = R
    i = L - 1  # 현재 p보다 작은 것의 위치(시작 점은 -1을 하여 아무것도 안 가리키게 한다.
    # j = L 아래 for에서 j를 설정해주기 때문
    for j in range(L, R):   # p가 R이라서 R인덱스 제외
        if arr[j] < arr[p]:
            i += 1
            # i += 1을 하면 i와 j가 같아지는 경우는 자기 자신과 자신을 교환
            # 안 같아지는 경우는 피벗 기준으로 교환
            arr[j], arr[i] = arr[i], arr[j]

    # arr[p], arr[i + 1] = arr[i + 1], arr[p]
    i += 1
    arr[p], arr[i] = arr[i], arr[p]
    return i


def quick_s(L, R):
    if L < R:
        p = partitionH(L, R)
        # p = partitionL(L, R)
        quick_s(L, p - 1)
        quick_s(p + 1, R)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5, -1, 2]
quick_s(0, len(arr) - 1)
print(arr)

