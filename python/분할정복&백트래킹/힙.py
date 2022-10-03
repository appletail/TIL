# 최소힙
def add_heap(k):
    global last
    last += 1
    arr[last] = k
    p = last // 2
    c = last
    while p and arr[p] > arr[c]:
        arr[p], arr[c] = arr[c], arr[p]
        c = p
        p = p // 2


def delete_heap(k):
    global last
    if last <= 0:
        return 0

    tmp = arr[1]
    arr[1] = arr[last]
    last -= 1

    p = 1
    c = 2
    while c <= last:
        if c + 1 <= last and arr[c] > arr[c + 1]:
            c += 1
        if arr[p] > arr[c]:
            arr[p], arr[c] = arr[c], arr[p]
            p = c
            c = p * 2
        else:
            break

    return tmp


n = int(input())

arr = [0] * (n + 1)
last = 0
for _ in range(n):
    a = int(input())
    if a:
        add_heap(a)
    else:
        print(delete_heap(1))


# 최대 힙
def add_heap(k):
    global last
    last += 1
    arr[last] = k
    p = last // 2
    c = last
    while p and arr[p] < arr[c]:
        arr[p], arr[c] = arr[c], arr[p]
        c = p
        p = p // 2


def delete_heap(k):
    global last
    if last <= 0:
        return 0

    tmp = arr[1]
    arr[1] = arr[last]
    last -= 1

    p = 1
    c = 2
    while c <= last:
        if c + 1 <= last and arr[c] < arr[c + 1]:
            c += 1
        if arr[p] < arr[c]:
            arr[p], arr[c] = arr[c], arr[p]
            p = c
            c = p * 2
        else:
            break

    return tmp


n = int(input())

arr = [0] * (n + 1)
last = 0
for _ in range(n):
    a = int(input())
    if a:
        add_heap(a)
    else:
        print(delete_heap(1))
