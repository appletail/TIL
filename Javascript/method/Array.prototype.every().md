## 1. every()
### **MDN**
every() 메서드는 배열의 모든 요소가 제공된 함수로 구현된 테스트를 통과하는지 테스트한다. 이 메서드는 boolean 값을 반환한다.
### **정리**
every()는 배열의 모든 요소가 조건을 충족하는지 확인한다. (AND)

## 2. 구문
```js
every(callbackFn)
every(callbackFn, thisArg)
```
### 매개변수
`callbackFn` 콜백 함수. 다음 세 가지 인수를 가집니다.
	`element` 현재 함수로 전달된 요소
	`index` 현재 요소의 index
	`array` 배열 객체

`thisArg` (Optional) callback을 실행할 때 this로 사용되는 값.

## 3. 예제
*배열의 모든 요소가 9보다 더 큰지 테스트*
```js
function isBigEnough(element, index, array) {
  return element >= 10;
};

[12, 5, 8, 130, 44].every(isBigEnough); // false
[12, 54, 18, 130, 44].every(isBigEnough); // true
```

*배열의 모든 요소가 다른 배열에 존재하는지 테스트*
```js
const isSubset = (array1, array2) =>
  array2.every((element) => array1.includes(element));

console.log(isSubset([1, 2, 3, 4, 5, 6, 7], [5, 7, 6])); // true
console.log(isSubset([1, 2, 3, 4, 5, 6, 7], [5, 8, 7])); // false
```

*`every()` 는 빈 슬롯에 콜백 함수를 실행하지 않는다*
```js
console.log([1, , 3].every((x) => x !== undefined)); // true
console.log([2, , 2].every((x) => x === 2)); // true
```

*배열이 수정되었을 때 `every` 메서드의 동작을 테스트*
```js
// ---------
// 항목 수정
// ---------
let arr = [1, 2, 3, 4];
arr.every((elem, index, arr) => {
  arr[index + 1]--;
  console.log(`[${arr}][${index}] -> ${elem}`);
  return elem < 2;
});

// 루프는 3번 순회하지만,
// 수정이 없었다면 2번만 순회했을 것입니다.
//
// 첫 번째 순회: [1,1,3,4][0] -> 1
// 두 번째 순회: [1,1,2,4][1] -> 1
// 세 번째 순회: [1,1,2,3][2] -> 2

// ---------
// 항목 추가
// ---------
arr = [1, 2, 3];
arr.every((elem, index, arr) => {
  arr.push("new");
  console.log(`[${arr}][${index}] -> ${elem}`);
  return elem < 4;
});

// 새로운 요소가 추가된 후에도 3번만 순회합니다.
//
// 첫 번째 순회: [1, 2, 3, new][0] -> 1
// 두 번째 순회: [1, 2, 3, new, new][1] -> 2
// 세 번째 순회: [1, 2, 3, new, new, new][2] -> 3

// ---------
// 항목 삭제
// ---------
arr = [1, 2, 3, 4];
arr.every((elem, index, arr) => {
  arr.pop();
  console.log(`[${arr}][${index}] -> ${elem}`);
  return elem < 4;
});

// 기존 요소가 `pop()` 되어 2번만 순회합니다.
//
// 첫 번째 순회: [1,2,3][0] -> 1
// 두 번째 순회: [1,2][1] -> 2
```

---
https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/every
