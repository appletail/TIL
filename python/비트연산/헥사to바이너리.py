#1 16진수  문자열을 이진수 문자열로

# 문자열 16진수를 2진수 문자열로 만들어 return
def htob(c):
    # 일반적인 경우 16진수 → 10진수 → 2진수
    if c.isdecimal(): # 0 ~ 9
        intC = int(c)
    else:  # A → 10, B → 11, F → 15
        intC = ord(c) - ord('A') + 10

    result = ''
    # for i in range(4):  # 뒤에서부터
    #     result = str(intC % 2) + result
    #     intC //= 2

    for i in range(4):  # 앞에서부터
        if intC & 8:
            result = result + '1'
        else:
            result = result + '0'

        # intC *= 2
        intC <<= 1
    return result


a = '0F97A3'
b = ''
for c in a:
    b = b + htob(c)
print(b)


# 2 2진수 문자열을 10진수 숫자로
def btod(s):
    result = 0
    for c in s:
        result = result * 2 + int(c)
    return result


def btodb(s):
    result = 0
    for c in s:
        result = (result << 1) | int(c)
        # bit연산 << 1 곱하기 2 / >> 1 나누기 2 / << 4 곱하기 16
    return result


# b = '0000000111100000011000000111100110000110000111100111100111111001100111'

for i in range(0, len(b), 7):
    print(btodb(b[i:i+7]))

print(8 >> 2)