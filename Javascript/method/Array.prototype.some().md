## 1. some()
### **MDN**
some() 메서드는 배열 안의 어떤 요소라도 주어진 판별 함수를 적어도 하나라도 통과하는지 테스트한다. 이 메서드는 boolean 값을 반환한다.
### **정리**
every()는 배열의 요소 중 하나라도 특정 조건을 충족하는지 확인한다. (OR)

## 2. 구문
```js
// 화살표 함수
some((element) => { /* … */ })
some((element, index) => { /* … */ })
some((element, index, array) => { /* … */ })

// 콜백 함수
some(callbackFn)
some(callbackFn, thisArg)

// 인라인 콜백 함수
some(function (element) { /* … */ })
some(function (element, index) { /* … */ })
some(function (element, index, array) { /* … */ })
some(function (element, index, array) { /* … */ }, thisArg)
```
### 매개변수
`callbackFn` 콜백 함수. 다음 세 가지 인수를 가집니다.
	`element` 현재 함수로 전달된 요소
	`index` 현재 요소의 index
	`array` 배열 객체

`thisArg` (Optional) callback을 실행할 때 this로 사용되는 값.

## 3. 예제
*배열 내 요소 중 하나라도 10보다 큰지 판별*
```js
function isBiggerThan10(element, index, array) {
  return element > 10;
}

[2, 5, 8, 1, 4].some(isBiggerThan10); // false
[12, 5, 8, 1, 4].some(isBiggerThan10); // true
```

*`includes()` 메서드 모방*
```js
const fruits = ["apple", "banana", "mango", "guava"];

function checkAvailability(arr, val) {
  return arr.some((arrVal) => val === arrVal);
}

checkAvailability(fruits, "kela"); // false
checkAvailability(fruits, "banana"); // true
```

*`some()`은 빈 슬롯에 조건자를 실행하지 않다.*
```js
console.log([1, , 3].some((x) => x === undefined)); // false
console.log([1, , 1].some((x) => x !== 1)); // false
console.log([1, undefined, 1].some((x) => x !== 1)); // true
```

---
https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/some
