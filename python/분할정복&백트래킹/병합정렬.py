# 병합하는 함수
def merge(lLst, rLst):
    lp = rp = 0  # 좌우 리스트의 현재 인덱스
    result = []  # 병합 결과를 저장할 빈 리스트

    # 어느 한 리스트가 비기 전까지 반복
    while lp < len(lLst) and rp < len(rLst):
        # lp가 가리키는 값이 더 작다면
        if lLst[lp] < rLst[rp]:
            result.append(lLst[lp])  # 결과 리스트에 lp가 가리키는 값 추가
            lp += 1  # lp 한 칸 앞으로
        else:  # rp가 가리키는 값이 더 작다면
            result.append(rLst[rp])  # 결과 리스트에 rp가 가리키는 값 추가
            rp += 1  # rp 한 칸 앞으로

    # 값이 남아있는 리스트를 결과리스트 끝에 붙임
    # 빈리스트의 경우 붙여도 변화가 없으므로 if 없이 둘 다 붙임
    result.extend(lLst[lp:])
    result.extend(rLst[rp:])
    return result  # 결과 값 리턴


# 둘로 나누는 함수
def merge_s(lst):
    if len(lst) == 1:  # 제일 마지막까지 나눈 경우
        return lst  # 리스트를 반환
    mid = len(lst) // 2  # 중간지점
    # 중간 지점 기준으로 좌우 분할
    left = merge_s(lst[:mid])  # 왼쪽 부분을 두 개로 나누고, 정렬된 리스트를 받기 위함
    right = merge_s(lst[mid:])  # 오른쪽 부분을 두 개로 나누고, 정렬된 리스트를 받기 위함
    return merge(left, right)  # 나눈 리스트를 병합해서 리턴


arr = [1, 16, 65, 20, 3, 5]
print(merge_s(arr))
