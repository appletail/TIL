## 1. from()
from() 메서드는 순회 가능 또는 [[유사배열객체]]에서 얕게 복사된 새로운 `Array` 인스턴스를 생성한다.

## 2. 구문
```js
Array.from(arrayLike)
Array.from(arrayLike, mapFn)
Array.from(arrayLike, mapFn, thisArg)
```
### 매개변수
`arrayLike` 배열로 변환할 순회 가능 또는 유사 배열 객체
`mapFn` (Optional)  mapFn의 return값이 배열에 추가된다.
	`element` 현재 요소.
	`index` 현재 요소의 인덱스.

`thisArg` (Optional) `mapFn`을 실행할 때 this로 사용되는 값.

## 3. 예제
*2차원 배열 만들기*
```js
const getVisited = (row, col) =>
  Array.from(Array(row), () => Array(col).fill(false));
  
console.log(getVisited(2, 2);
// [[false, false], [false, false]]
```

*String으로 배열 만들기*
```js
Array.from("foo");
// [ "f", "o", "o" ]
```

*Set으로 배열 만들기*
```js
const set = new Set(["foo", "bar", "baz", "foo"]);
Array.from(set);
// [ "foo", "bar", "baz" ]
```

*Set으로 배열 만들기*
```js
const map = new Map([
  [1, 2],
  [2, 4],
  [4, 8],
]);
Array.from(map);
// [[1, 2], [2, 4], [4, 8]]

const mapper = new Map([
  ["1", "a"],
  ["2", "b"],
]);
Array.from(mapper.values());
// ['a', 'b'];

Array.from(mapper.keys());
// ['1', '2'];
```

*NodeList으로 배열 만들기*
```js
// DOM 요소의 속성을 기반으로 배열 만들기
const images = document.querySelectorAll("img");
const sources = Array.from(images, (image) => image.src);
const insecureSources = sources.filter((link) => link.startsWith("http://"));
```

