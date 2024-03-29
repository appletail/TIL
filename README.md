# TIL-Today-I-Learned

## 오늘 배운 것을 정리해서 올립니다.
---

# 22.07.19

- type(x): int, str, Tuple 등 타입을 알 수 있는 함수
- x, y = 10, 20 이런 식으로 변수 할당 가능
 
```python
 name = input('이름을 입력 해 주세요. : ')
 print(name)
>>> 이름을 입력 해 주세요.
```
 : 이렇게 입력할 수 있음
---

- bool() 함수 : 특정데이터가 True인지 False인지 검증

- int 정수형 진수로도 표현가능
    - 0b01(2진수), 0o10(8진수), 0x10(16진수)
    - 실수에 int 씌우면 정수부분 출력
    - 참고: 02 는 문자형이다.

- float: e(E) 사용 가능

- 실수 오류 처리시

    1. 기본적인 처리방법을 알아봅시다.
    변수 a, b에 각각의 실수 값을 저장합니다.
    그리고 abs()를 이용하여 a와 b의 차이를 구합니다.
    a와 b의 차이가 1e-10 값 이하이면 a 와 b 는 같다고 볼 수 있습니다.

    2. sys 모듈을 통해 처리하는 방법을 알아봅시다.
    `epsilon` 은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
    abs() 를 이용하여 a, b의 차이를 구합니다.
    a와 b의 차이가 sys.float_info.epsilon의 값 이하이면 a, b 는 같다고 볼 수 있습니다

    3. math.isclose() 를 이용해서 a와 b의 값이 같은지 확인할수 있습니다.
    ```python
    import math
    math.isclose(a, b)
    ```

- 삼중 따옴표(""")
    - 문자열안에 따옴표 넣을 때 사용
    - 여러줄에 걸친 문장에도 사용
    - \n없이도 사용가능

- 이스케이프 시퀀스

|<center>예약문자</center>|내용(의미)|
|:--------:|:--------:|
|\n|줄 바꿈|
|\t|탭|
|\r|캐리지리턴|
|\0|널(Null)|
|\\\\ |`\`|
|\\'|단일인용부호(`'`)|
|\\"|이중인용부호(`"`)|


- 컨테이너
    - 시퀀스: 순서있음
    - 비시퀀스: 순서없음
    - 가변형(mutable): List, Set, Dictionary(key)
    - 불변형(immutable): String, Tuple, Range, Dictionary(value)


<img width="712" alt="container" src="https://user-images.githubusercontent.com/45934087/148164052-3b12d3a2-a95e-4d4d-ae25-86ca1ba9657b.png"

- 튜플 단일항목 생성시 마지막에 쉼표를 꼭 붙여야함

- 레인지: range(start, stop, step)
- 인덱싱, 슬라이싱: [start: stop: step]

- 딕셔너리 
    - 수정
    ```python
    dict = { 'one' : 0, 'two' : 2 }dict['one'] = 1
    ```
    - 추가
    ```python
    dict = { 'one' : 1, 'two' : 2 }dict['three'] = 3
    ```
    - 삭제
    ```python
    dict = { 'one' : 1, 'two' : 2, 'three' : 3 }del(dict['one'])
    ```
    - 결합
    ```python
    dic1 = {1:10, 2:20}
    dic2 = {1:100, 3:300}
    dic1.update(dic2)
    print(dic1)
    
    >>>{1: 100, 2: 20, 3: 300}
    ```
    - .key() / .value() / .items() : 키, 벨류, 키 & 벨류 접근

- 식별 연산자
    - is를 통해 동일한 object인지 확인할 수 있음
    - id(x): id 확인
    - -5 ~ 256 까지 id 같음
    - 257 이후로는 id가 다름

- 멤버십 연산자
    - in : 안에 특정한 것이 속해 있는지
    ```py
    'a' in 'apple'
    >>> True
    ```
    - not in : 안에 특정한 것이 없는지
    ```python
    'a' in 'apple'
    >>> False
    ```

- 산술연산자(+), 반복연산자(*)
    - 리스트, 튜플, 문자열에서 사용가능하지만 레인지에서는 사용불가

- 문자열.strip() 사용법
strip('양쪽 끝 단의 자를 문자를 입력해주세요.')

```py
'@#!test!!#'.strip('@#!')
>>>test
```

- 천 단위 쉼표 표시
    - format(변수, ',d') : 정수일 때 사용
    - format(변수, ',f') : 실수일 때 사용
    - format(변수, '') : 자동 감지
```
format(변수, ',d')
>>> 10,000
```

---

# 22.07.20

- 제어문
    - 조건문
    - 반복문


- 조건 표현식
    - 삼항 연산자(Ternary Operator)라고도 함

```py
true인 경우 값 if 조건 else fasle인 경우 값

num = 2
if num % 2:
    result = '홀수'
else:
    result = '짝수'
print(result)

num = 2
result = '홀수' if num % 2 else '짝수'
print(result)
```



## for

- iterable
    - 순회할 수 있는 자료형(string, list, dict, tuple, range, set 등)
    - 순회형 함수(range, enumerate)

- enumerate(iterable, start = 0) 순회
    - 인덱스와 객체를 쌍으로 담은 열거형 객체
        - (index, value)형태의 tuple로 구성된 열거 객체를 반환
        - f-string 사용시 오류발생
        - formating으로 사용할 것

```py
members = ['민수', '영희', '철수']

for idx, number in enumerate(members):
    print(idx, number)
>>> 0 민수
>>> 1 영희
>>> 2 철수

print(list(enumerate(members)))
>>> [(0, '민수'), (1, '영희'), (2, '철수')]

print(list(enumerate(members, start = 1)))
>>> [(1, '민수'), (2, '영희'), (3, '철수')]
```
- List Comprehension
    - 특정한 값을 가진 리스트 간결하게 생성

[code for 변수 in iterable]  
[code for 변수 in iterable if 조건식]

```py
1 ~ 3의 세제곱 리스트

cubic_list = []
for number in range(1, 4):
    cubic_list.append(number ** 3)
print(cubic_list)

cubic_list = [number ** 3 for number in range(1, 4)]

>>> [1, 8, 27]
```

- Dictionary Comprehension
    - 특정한 값을 가진 딕셔너리 간결하게 생성

{key: value for 변수 in iterable}  
{key: value for 변수 in iterable if 조건식}

```py
1 ~ 3의 세제곱 딕셔너리

cubic_dict = {}

for number in range(1, 4):
    cubic_dict[number] = number ** 3
print(cubic_dict)

cubic_dict = {number: number ** 3 for number in range(1, 4)}

>>> {1: 1, 2: 8, 3: 27}
```


## 반복문 제어

- break
    - break를 만나면 반복문이 바로 종료됨
    - 특정조건에 반복을 종료시킬 때 사용

- cotinue
    - continue 이후의 코드 블록은 수행하지 않고, 다음 반복 수행
```py
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
>>> 1
>>> 3
>>> 5
```
- for-else
    - 반복문 끝까지 실행한 후 else 실행
    - break로 중단시 else 실행 안함

- pass
    - 아무것도 안함
    - 그냥 자리 채우는 용도


## 함수

- 함수
    - Decomposition(분해): 기능분해하고 재사용 가능하게
    - Abstraction(추상화): 재사용성, 가독성, 생산성

- 함수구조
    - def: 함수 선언
    - name: 함수 이름
    - parameters: () 속에 들어갈 변수
    - docstring: ```로 함수 설명, 생략가능
    - function body: 코드
    - return: 결과값

```py
def function_name(parameter):
    ```
    docstring
    ```
    code block
    return retutning_value
```

## 함수 출력

### 값에 따른 함수 종류
- Void function
    - 명시적인 return 값이 없는 경우, None 반환하고 종료
- Value returning function
    - 함수 실행 후, return문을 통해 값 반환 후 종료

- print vs return
    - print: 호출 때마다 값 출력
        - 변수에 저장 불가
    - return: 데이터 처리 위해 사용
        - 항상 하나의 값 만을 반환
        - 두 개 반환하려면 tuple 사용

## 함수 입력

- Parameter: 함수 정의할 떄 함수 내부에서 쓰는 변수
- Argument: 함수 호출할 때 넣는 값
    - 필수 Argument: 반드시 필요
    - 선택 Argument: 값 안넣어도 되는 경우 기본값 전달

- Positional Argument
    - 함수 호출 시 Argument는 위치에 따라 전달되는 것이 기본
- Keyword Argument
    - 변수의 이름으로 특정 Argument 전달 가능
    - Keyword Argument 다음에 Positional Argument 활용 불가

```py
def add(x, y):
    return x + y

add(x = 2, y = 5)
add(2, y = 5)
add(x = 2, 5) -> Error 발생!
```
- Default Argument Values
    - 기본값 지정해서 호출 시 Argument 값 설정 안해도 됨

```py
def add(x, y):
    return x + y

def add(x, y = 0):
    x = 2
    return x + y
```

- 가변 인자(*args)
    - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
    - * 이 중요
```py
def add(*args):
    for arg in args:
        print(arg)

add(2)
add(2, 3, 4, 5)
```

- 패킹 / 언패킹
    - 패킹: 여러 개의 데이터 묶어서 변수에 할당

    - 언패킹: 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당
        - 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야함
        - 왼쪽의 변수에 asterisk(*)를 붙이면 남은 요소를 리스트에 담을 수 있음
- asterisk(*)와 가변 인자
    - 시퀀스를 풀어 헤치는 연산자
    - 주로 튜플이나 리스트 언패킹시 사용
    - *로 만듬
- 가변 키워드 인자(**kwargs)
    - 딕셔너리로 묶여 처리됨
    -- **로 만듬

# Scope

## 파이썬의 범위

- LEGB: Local, Enclosed, Global, Built-in

- global 문
    - 현재 코드 블록 전체에 적용
    -  global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
    - global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야함

```py
a = 10
def func1():
    global a
    a = 3

print(a)
>>> 10

func1()
print(a)
>>> 3
```
```py
a = 10
def func1():
    print(a)    사용 불가
    global a
    a = 3

def func1(a):  parameter에 사용 불가
    global a
    a = 3
```

- nonlocal
    - global 제외 가장 가까운 scope의 변수 연결
    - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
    - nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야함
    - 이미 존재하는 이름과의 연결만 가능

# 함수 활용

- map(function, iterable)
    - iterable의 모든 요소에 함수 적용하고, 그 결과를 map object로 반환

```py
n, m = map(int, input().split())
print(n, m)

>>> 3, 5
```

- filter(function, iterable)
    - iterable의 모든 요소에 함수 적용하고, 그 결과가 True인 것들ㅇ르 filter object로 반환

```py
def odd(n):
    return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(list(result))

>>> [1,3]
```

- zip(*iterables)
    - 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
    - 세로로 모아줌
```py
girls = ['jane', 'ashley']
boys = ['justin', 'eric']
pair = zip(girls, boys)
print(list(pair))

>>> [('jane', 'justin'), ('ashley', 'eric')]
```

- lambda[paramter]: 표현식
    - 람다함수
        - 표현식을 계산한 결과값을 반환하는 함수, 익명한수라고도 함
        - return문을 가질 수 없음
        - 간편 조건문외 조건문이나 반복문을 가질 수 없음
        - 함수 정의보다 간결함
        - def 사용할 수 없는 곳에서도 사용가능
```py
def triangle_area(b, h):
    return 0.5 * b *h
print(triangle_area(5, 6))

>>> 15.0

triangle_area = lambda b , h : 0.5 * b * h
print(triangle_area(5, 6))

>>> 15.0
```

- 재귀함수(recursive function)
    - 자기 자신 호출함수
    - 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

```py
def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n - 1)
print(facto(4))

>>> 24
```

- 모듈 > 패키지 > 라이브러리 > 
- pip 관리자로 관리

---

# 22.07.21

### 딕셔너리 정렬법
- key 값 정렬

```py
d = {"dream": 0, "car": 99, "blockdmask": 1, "error": 30, "app": 20}

# 오리지널 딕셔너리
print(f'origin                 : {d}\n')

# dictionary.items()
d1 = sorted(d.items())
print(f'sorted(d.items())      : {d1}')
print(f'dict(sorted(d.items()) : {dict(d1)}')

# 키 값만 빼서 정렬하려는 경우, key 만 빠지기 때문에 딕셔너리가 될수 없다.
d2 = sorted(d)
print(f'sorted(d)              : {d2}')


# .item(), reverse = True) 로 대입하면 내림차순 정렬
```
```
>>> origin                 : {'dream': 0, 'car': 99, 'blockdmask': 1, 'error': 30, 'app': 20}

>>> sorted(d.items())      : [('app', 20), ('blockdmask', 1), ('car', 99), ('dream', 0), ('error', 30)]
>>> dict(sorted(d.items()) : {'app': 20, 'blockdmask': 1, 'car': 99, 'dream': 0, 'error': 30}

>>> sorted(d)              : ['app', 'blockdmask', 'car', 'dream', 'error']


```

- value 값 정렬
```py
d = {"dream": 0, "car": 99, "blockdmask": 1, "error": 30, "app": 20}

# 오리지널 딕셔너리
print(f'origin         : {d}\n')

# lambda x : x[1]
d2 = sorted(d.items(), key=lambda x: x[1])
print("\n - sorted(d.items(), key=lambda x: x[1])의 결과")
print(d2)

print("\n - dict(sorted(d.items(), key=lambda x: x[1]))의 결과")
print(dict(d2))


# key=lambda x: x[1], reverse = True) 로 대입하면 내림차순 정렬
```
```
 - sorted(d.items(), key=lambda x: x[1])의 결과
[('dream', 0), ('blockdmask', 1), ('app', 20), ('error', 30), ('car', 99)]

 - dict(sorted(d.items(), key=lambda x: x[1]))의 결과
{'dream': 0, 'blockdmask': 1, 'app': 20, 'error': 30, 'car': 99}
```

- 문자열.isdecimal(): 숫자면 True, 문자열이면 False
- ord(문자): 아스키코드 정수로 반환
- chr(숫자): 문자로 변환

- in 명령: 안에 값이 많아지면 하나하나 모두 검사하기 때문에 시간이 많이 걸림. 이때는 그냥 and나 or을 쓰는게 좋음.

- '구분자'.join(리스트)
    - 리스트에 있는 요소들을 합쳐 하나의 문자열로 바꾸어 반환하는 함수
    - 값과 값사이에 구분자를 넣어서 하나의 문자열로 합쳐줌
```py
a = ['a', 'b', 'c']

''.join(a)
>>> 'abc'

'_'.join(a)
>>> 'a_b_c'
```

---

# 22.07.22

## json 오픈법

```py
import json

movie_json = open('data/movie.json', encoding='utf-8') # 파일 열기
movie_dict = json.load(movie_json)  # 로드해야 쓸 수 있음
```

- 숫자 판별
    - .isdecimal(): int로 변환 가능한지 판별
    - .isdigit(): 숫자의 형태인지 판별
    - .isnumeric(): 숫자값 표현에 해당하는지 판별

    - .isnumeirc()이 가장 큰 범위이고 .isdecimal이 가장 좁은 범위
    - 보통은 .isdigit()를 가장 많이 사용한다.

- 문자열 변별
    - .isalpha(): 문자열이 문자로만 구성되어 있는지 판별, 공백이 있으면 False

- 숫자 + 문자열 판별
    - .isalnum(): 문자 + 숫자인지 판별
    - 둘중 하나만 있어도 True, 공백이 있으면 False

---

# 22.07.25

```
문자열 메서드
- '구분자'.join([iterable]) : iterable 요소들을 구분자로 합쳐 문자열 반환
- s.replace( old, new [,count])
    - old글자를 new글자로 바꿈
    - count: 앞부터 카운트 숫자만큼만 바꿈, 기본은 모두 바꾸는 것임
- s.capitalize() : 가장 첫번째 글자를 대문자로 변경
- s.title() : 띄어쓰기 기준으로 단어의 첫글자는 대문자, 나머지는 소문자로 변경
- s.swapcase() : 대소문자 서로 변경
```

```
리스트 메서드
L.insert(i, x) : 리스트 인덱스 i에 x항목 삽입, 삽입되면 나머지는 뒤로 밀림
L.remove(x) : 가장 왼쪽에 있는 항목 x를 제거, 항목 없으면 error 발생
L.pop() : 가장 오른쪽 항목을 반환 후 제거
L.pop(i) : 인덱스 i에 있는 항목 반환 후 제거
L.extend(m) : 순회형 m의 모든 항목들을 리스트에 더해줌
L.index(x, start, end) : 가장 왼쪽에 있는 항목 x의 인덱스를 반환
L.reverse() : 거꾸로
L.sort() : 원본 자체를 정렬 / 2차원 리스트라면 리스트안의 값들 중 같으면 다음 것 기준으로 정렬
L.count(x) : 리스트에 x가 몇 개 존재하는지 갯수 반환
```


```py
복사
a = [1, 2, ['a' ,'b', 'c'], 3]
- 할당 
a = b
  - 주소 공유라서 그냥 같은 것임
  - 새로운 변수의 값을 바꿀 경우 기존 변수에서도 값이 바뀜

- 얕은 복사 
a = b[:]
  - 상자안의 내용물 전체를 복사해서 넣어줌
  - 하지만 리스트 안에 리스트의 경우 기존의 변수와 값을 공유함

- 깊은 복사 
import copy
b = copy.deepcopy(a)
  - 상자안의 상자까지 전부 다 복사해서 넣어줌
  - 완전 별개의 변수가 됨

- 함수를 통한 복사
    - n은 값을 복사하여 동작, lst는 id가 넘어가기 때문에 같은 데이타 변경이 동시에 이루어짐
def test(n, lst):
    n = 10
    lst[1] = 10000
    print(n, lst)

n = 5
lst = [1, 2, 3]
test(n, lst)
print(n, lst)

>>> 10 [1, 10000, 3]
>>> 5 [1, 10000, 3]

- 해결법 얕은 복사 사용

n = 5
lst = [1, 2, 3]
t = lst[::]   # 얕은 복사
test(n, t)
print(n, lst)

>>> 10 [1, 10000, 3]
>>> 5 [1, 2, 3]
```

---

# 22.07.26

