함수에 전달된 인수에 해당하는 [[유사배열객체|Array 형태]]의 객체

```js nums
function func(a, b) {
  console.log(arguments[0]);  // 1
  console.log(arguments[1]);  // 2
  console.log(arguments[2]);  // 3
};
func(1, 2, 3);

function func1() {
  // 눈에 보이지 않는 arguments라는 객체가 존재하고 있다.
  console.log(arguments[0]);  // 1
  console.log(arguments[1]);  // 2
  console.log(arguments[2]);  // 3
};
func1(1, 2, 3);
```
