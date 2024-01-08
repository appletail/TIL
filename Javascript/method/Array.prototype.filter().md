## 1. filter()
filter() 메서드는 콜백함수에서 true를 return하는 element를 모아 배열로 반환함

## 2. 구문
```js
arr.filter(callback(element[, index[, array]])[, thisArg])
```
[[Array.prototype.map()|map]], forEach와 같은 구문임
### 매개변수
`callback` 콜백 함수. 다음 세 가지 인수를 가집니다.
	`element` 현재 요소.
	`index` (Optional) 현재 요소의 인덱스.
	`array` (Optional) filter()를 호출한 배열.

`thisArg` (Optional) callback을 실행할 때 this로 사용되는 값.

## 3. 예제
```js
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];

const result = words.filter((word) => word.length > 6);

console.log(result);
// Expected output: Array ["exuberant", "destruction", "present"]
```
