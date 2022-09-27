def merge(lLst, rLst):
    lp = rp = 0
    result = []

    while lp < len(lLst) and rp < len(rLst):
        if lLst[lp] < rLst[rp]:
            result.append(lLst[lp])
            lp += 1
        else:
            result.append(rLst[rp])
            rp += 1

    result.extend(lLst[lp:])
    result.extend(rLst[rp:])
    return result


def merge_s(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = merge_s(lst[:mid])
    right = merge_s(lst[mid:])
    return merge(left, right)


arr = [1, 16, 65, 20, 3, 5]
print(merge_s(arr))
