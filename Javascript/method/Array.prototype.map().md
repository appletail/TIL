## 1. map()
map() 메서드는 콜백함수에서 return하는 값을 모아 배열로 반환함

## 2. 구문
```js
arr.map(callback(element[, index[, array]])[, thisArg])
```
[[Array.prototype.filter()|filter]], forEach와 같은 구문임
### 매개변수
`callback` 콜백 함수. 다음 세 가지 인수를 가집니다.
	`element` 현재 요소.
	`index` (Optional) 현재 요소의 인덱스.
	`array` (Optional) map()을 호출한 배열.

`thisArg` (Optional) callback을 실행할 때 this로 사용되는 값.

## 3. 예제
```js
const array1 = [1, 4, 9, 16];

const map1 = array1.map((x) => x * 2);
const map2 = array1.map((x) => console.log(x))

console.log(map1);
// Expected output: Array [2, 8, 18, 32]
console.log(map2);
// Expected output: Array [undefined, undefined, undefined, undefined]
```
