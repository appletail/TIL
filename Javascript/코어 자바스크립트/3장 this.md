다른 대부분의 객체지향 언어에서 this는 클래스로 생성한 인스턴스를 의미한다. 클래스에서만 사용할 수 있기 때문에 혼란의 여지가 적다. 그러나 자바스크립트에서의 this는 어디서나 사용할 수 있어서 많은 혼란을 일으킨다.

함수와 객체(메서드)의 구분이 느슨한 자바스크립트에서 this는 실질적으로 이 둘을 구분하는 거의 유일한 기능이다.

# 01 상황에 따라 달라지는 this
---
자바스크립트에서 this는 실행 컨텍스트가 생성될 때 함께 결정된다. 즉, **this는 함수를 호출할 때 결정된다.**

## 3-1-1 전역 공간에서의 this
전역 공간에서 this는 전역 객체를 가리킨다.
![[Pasted image 20240102164744.png]]
![[Pasted image 20240102164754.png]]
자바스크립트의 모든 변수는 특정 개체의 프로퍼티로서 동작하기 때문에 **전역변수를 선언하면 자바스크립트 엔진은 이를 전역객체의 프로퍼티로 할당한다.** 그러므로 변수 a 는 사실 window.a를 생략한 것과 비슷하다.

![[Pasted image 20240102164803.png]]
```jsx
window.d = 4;
delete d;                     // true
console.log(d, window.d, this.d);  
// Uncaught ReferenceError: d is not defined
```
이 둘의 차이는 configurable 속성(변경 및 삭제 가능성)에서 차이가 난다. 전역변수로 선언하면 자바스크립트는 전역객체의 프로퍼티로 할당하면서 추가적으로 configurable 속성을 false로 정의한다.

## 3-1-2 메서드로서 호출할 때 그 메서드 내부에서의 this
### **함수 vs 메서드**
함수를 함수로서 호출하는 경우와 메서드로서 호출하는 경우의 유일한 차이는 **독립성**에 있다.
![[Pasted image 20240102165051.png]]
![[Pasted image 20240102165101.png]]
함수로서 호출 시 this: 전역객체
메서드로서 호출 시 this: 함수 이름(프로퍼티명) 앞에 명시된 객체

### **메서드 내부에서의 this**
this에는 호출한 주체에 대한 정보가 담긴다.
![[Pasted image 20240102165253.png]]

## 3-1-3 함수로서 호출할 때 그 함수 내부에서의 this
### **함수 내부에서의 this**
**함수로서 호출한 경우**에는 호출 주체를 명시하지 않고 실행한 것이기 때문에 this가 지정되지 않아야하지만 설계상의 오류로 **this는 전역 객체**를 가리킨다.

### **메서드의 내부함수에서의 this**
this 바인딩에 관해서는 오직 해당 함수를 호출하는 구문 앞에 점 또는 대괄호 표기가 있는지 없는지가 관건이다.

### **메서드의 내부 함수에서의 this를 우회하는 방법**
**ES5와 그 이전**
![[Pasted image 20240102165436.png]]
self, \_this, that, \_ 등의 이름으로 outer 스코프에서 this를 저장하고 그것을 innerFunc에서 사용하면 된다.

### **this를 바인딩하지 않는 함수**
**ES6 이후**
![[Pasted image 20240102165807.png]]
화살표 함수를 사용하면 LexicalEnvironment에서 this 바인딩 과정 자체가 빠지게 되어, 상위 스코프의 this를 그대로 활용할 수 있다. 그러므로 self 등의 우회법이 불필요하게 된다.

## 3-1-4 콜백 함수 호출 시 그 함수 내부에서의 this
![[Pasted image 20240102170238.png]]
콜백 함수에서의 this는 하나로 정의할 수 없고, 콜백 함수의 **제어권을 가지는 함수(메서드)**\가 콜백 함수에서의 this를 무엇을 할지를 **결정**하며, 특별히 **정의하지 않는 경우 전역객체**를 가리킨다.

## 3-1-5 생성자 함수 내부에서의 this
자바스크립트는 함수에 생성자로서의 역할을 함께 부여했다. new 명령어와 함께 함수를 호출하면 해당 함수가 생성자로서 동작한다. 그리고 이때 함수 내부의 this는 인스턴스(instance)를 가리킨다.
![[Pasted image 20240102170528.png]]

# 02 명시적으로 this를 바인딩하는 방법
---
01에서 본 규칙과 별개로 this에 별도의 대상을 바인딩하는 방법도 있다. 01의 규칙에 부합하지 않는다면 다음 방법 중 하나를 사용했을 것이라고 추측할 수 있다.

## 3-2-1 call 메서드
```js
Function.prototype.call(thisArg[, arg1[, arg2[, ...]]])

// 첫 번째 인자: this 바인딩
// 이후의 인자: 호출할 함수의 매개변수
```
call 메서드는 메서드의 호출 주체인 함수를 즉시 실행하도록 하는 명령이다.

함수를 그냥 실행하면 this는 전역객체를 참조하지만 call 메서드를 이용하면 임의의 객체를 this로 지정할 수 있다.

*예제 3-14 call 메서드(1) 함수*
```js nums
var func = function (a, b, c) {
	console.log(this, a, b, c);
};

func(1, 2, 3);                  // Window{ ... } 1 2 3
func.call({ x: 1 }, 4, 5, 6);   // { x: 1 } 4 5 6
```


메서드에 대해서도 그냥 호출하면 this는 객체를 참조하지만 call 메서드를 이용하면 임의의 객체를 this로 지정할 수 있다.

*예제 3-15 call 메서드(2) 메서드*
```js nums
var obj = {
	a: 1,
	method: function (x, y) {
		console.log(this.a, x, y);
	}
};

obj.method(2, 3);                // 1 2 3
obj.method.call({ a: 4}, 5, 6);  // 4 5 6
```

## 3-2-2 apply 메서드
```js nums
Function.prototype.apply(thisArg[, argsArray])

// 첫 번째 인자: this 바인딩
// 이후의 인자: 배열의 요소들을 호출할 함수의 매개변수로 지정
```
apply 메서드는 call 메서드와 기능적으로 동일하다.

*예제 3-15 apply 메서드*
```js nums
var func = function (a, b, c) {
	console.log(this, a, b, c);
};
func.apply({ x: 1}, [4, 5, 6]);     // { x: 1 } 4 5 6

var obj = {
	a: 1.
	method: function (x, y) {
		console.log(this.a, x, y);
	}
};
obj.method.apply({ a: 4}, [5, 6]);  // 4 5 6
```

## 3-2-3 call / apply 메서드의 활용
### **1) 유사배열객체(array-like object)에 배열 메서드를 적용**
객체에는 배열 메서드를 직접 적용할 수 없다. 하지만 [[유사배열객체]]의 경우 call 또는 apply 메서드를 이용해 배열 메서드를 차용할 수 있다.

*예제 3-17 call/apply 메서드의 활용 1-1) 유사배열객체에 배열 메서드를 적용*
```js nums
var obj = {
	0: 'a',
	1: 'b',
	2: 'c',
	length: 3
};
Array.prototype.push.call(obj, 'd');
console.log(arr);
// { 0: 'a', 1: 'b', 2: 'c', 3: 'd', length: 4 }

var arr = Array.prototype.slice.call(obj);
console.log(arr);    // [ 'a', 'b', 'c', 'd' ]
```

*예제 3-18 call/apply 메서드의 활용 1-2) [[arguments]], NodeList에 배열 메서드를 적용*
```js nums
function a () {
	var argv = Array.prototype.slice.call(arguments);
	argv.forEach(function (arg) {
		console.log(arg)
	});
};
a(1, 2, 3); // 1
            // 2
            // 3

document.body.innerHtml = '<div>a</div><div>b</div><div>c</div>';
var nodeList = document.querySelectorAll('div');
var nodeArr = Array.prototype.slice.call(nodeList);
nodeArr.forEach(function (node) {
	console.log(node);
});
```

*예제 3-19 call/apply 메서드의 활용 1-3) 문자열에 배열 메서드를 적용*
```js nums
var str = 'abc def'

Array.prototype.push.call(str, ', pushed string');
// Error: Cannot assign to read only property 'length' of object [object String]

Array.prototype.concat.call(str, 'string');
// [String {"abc def"}, "string"]

Array.prototype.every.call(
	str, 
	function (char) { return char !== ' '; }
); // false

Array.prototype.some.call(
	str,
	function (char) { return char === ' '; }
); // true

var newArr = Array.prototype.map.call(
	str,
	function (char) { return char + '!'; }
);
console.log(newArr);
// ['a!', 'b!', 'c!', ' !', 'd!', 'e!', 'f!']

var newStr = Array.prototype.reduce.apply(
	str, 
	[function (string, char, i) { return string + char + i; }, '']
);
console.log(newStr);
// "a0b1c2 3d4e5f6"
```
- 문자열에서도 사용할 수 있으나, length 프로퍼티가 읽기 전용이기 때문에 원본 문자열에 변경을 가하는 메서드(push, pop, shift, unshift, splice 등)는 에러를 던진다.
- concat처럼 대상이 반드시 배열이어야하는 경우에는 에러가 나지 않지만 제대로 된 결과를 얻을 수 없다.


ES6에서는 [[유사배열객체]] 또는 순회 가능한 모든 종류의 데이터 타입을 배열로 전환하는 [[Array.from()|Array.from]] 메서드를 새로 도입했다.

*예제 3-20 call/apply 메서드의 활용 1-4) ES6의 Array.from 메서드*
```js nums
var obj = {
	0: 'a',
	1: 'b',
	2: 'c',
	length: 3,
};
var arr = Array.from(obj);
console.log(arr)            // ['a', 'b', 'c']
```

### **2) 생성자 내부에서 다른 생성자 호출**
생성자 내부에 다른 생성자와 공통된 내용이 있을 경우 call 또는 apply를 이용해 다른 생성자를 호출하면 간단하게 반복을 줄일 수 있다.

이하 예제에서는 Student, Employee 생성자 함수 내부에서 Person 생성자 함수를 호출해서 인스턴스의 속성을 정의하도록 구현했다.

*예제 3-21 call/apply 메서드의 활용 2) 생성자 내부에서 다른 생성자를 호출*
```js nums
function Person(name, gender) {
	this.name = name;
	this.gender = gender;
};
function Student(name, gender, school) {
	Person.call(this, name, gender);
	this.school = school;
};
function Employee(name, gender, company) {
	Person.apply(this, [name, gender]);
	this.company = company;
};
var by = new Student('보영', 'female', '단국대');
var by = new Employee('재난', 'male', '구골');
```

### **3) 여러 인수를 묶어 하나의 배열로 전달하고 싶을 때 - apply 활용**
- **apply를 사용하지 않는 경우**
*예제 3-22 call/apply 메서드의 활용 3-1) 최대/최솟값을 구하는 코드를 직접 구현*
```js nums
var numbers = [10, 20, 3, 16, 45];
var max = min = numbers[0];
numbers.forEach(function (number) {
	if (number > max) {
		max = number;
	};
	if (number < min) {
		min = number;
	};
});
console.log(max, min);   // 45 3
```

- **apply를 사용하는 경우**
*예제 3-23 call/apply 메서드의 활용 3-2) 여러 인수를 받는 메서드(Math.max\/Math.min)에 apply를 적용*
```js nums
var numbers = [10, 20, 3, 16, 45];
var max = Math.max.apply(null, numbers);
var min = Math.min.apply(null, numbers);
console.log(max, min);   // 45 3
```

※ ES6에서는 펼치기 연산자(spread operator)를 이용하면 더욱 간단히 작성할 수 있다.
*예제 3-24 call/apply 메서드의 활용 3-3) ES6의 펼치기 연산자 활용*
```js nums
var numbers = [10, 20, 3, 16, 45];
var max = Math.max(...numbers);
var min = Math.min(...numbers);
console.log(max, min);   // 45 3
```

call/apply 메서드는 명시적으로 별도의 this를 바인딩하면서 함수 또는 메서드를 실행하는 좋은 방법이지만 오히려 이로 인해 this를 예측하기 어렵게 만들어 코드 해석을 방해한다는 단점이 있다. 하지만 ES5이하 환경헤서는 대안이 없어 실무에서 매우 광범위하게 활용되고 있다.

## 3-2-4 bind 메서드
```js
Function.prototype.bind(thisArg[, arg1[, arg2[, ...]]])
```
call과 비슷하지만 즉시 호출하지는 않고 넘겨 받은 this 및 인수들을 바탕으로 새로운 함수를 반환하기만 하는 메서드이다.

bind 메서드는 함수에 미리 this를 적용하는 것과 부분 적용 함수를 구현하는 두 가지 목적을 지니고 있다.

*예제 3-25 bind 메서드 - this 지정과 부분 적용 함수 구현*
```js nums
var func = function (a, b, c, d) {
	console.log(this, a, b, c, d);
};
func(1, 2, 3, 4);        // Window{ ... } 1 2 3 4

var bindFunc1 = func.bind({ x: 1 });
bindFunc1(5, 6, 7, 8)    // { x: 1 } 5 6 7 8

var bindFunc2 = func.bind({ x: 1 }, 4, 5);
bindFunc2(6, 7);         // { x: 1 } 4 5 6 7
bindFunc2(8, 9);         // { x: 1 } 4 5 8 9
```

### **name 프로퍼티**
bind를 적용해 새로만든 함수는 원본 함수 이름에 'bound'라는 접두어가 붙는다.

*예제 3-26 bind 메서드 - name 프로퍼티*
```js nums
var func = function (a, b, c, d) {
	console.log(this, a, b, c, d);
};
var bindFunc = func.bind({ x: 1 }, 4, 5);
console.log(func.name);         // func
console.log(bindFunc.name);     // bound func
```

### **상위 컨텍스트의 this를 내부함수나 콜백 함수에 전달하기**
메서드의 this를 그대로 바라보게 하기위한 방법(self 등의 변수 이외의 방법)

*예제 3-27 내부함수에 this 전달 - call vs. bind*
```js nums
var obj = {
	outer: function () {
		console.log(this);            // {outer: ƒ}
		var innerFunc = function () {
			console.log(this);        // {outer: ƒ}
		};
		innerFunc.call(this);
	}
};
obj.outer();
```

```js nums
var obj = {
	outer: function () {
		console.log(this);            // {outer: ƒ}
		var innerFunc = function () {
			console.log(this);        // {outer: ƒ}
		}.bind(this);
		console.log(innerFunc.name)   // bound 
		innerFunc();
	}
};
obj.outer();
```

콜백 함수 내에서의 this에 관여하는 함수 또는 메서드에 대해서도 bind 메서드를 이용하면 this값을 임의로 바꿀 수 있다.

*예제 3-28 bind 메서드 - 내부함수에 this 전달
```js nums
var obj = {
	logThis: function () {
		console.log(this);
	},
	logThisLater1: function () {
		setTimeout(this.logThis, 500);
	},
	logThisLater2: function () {
		setTimeout(this.logThis.bind(this), 1000);
	}
};
obj.logThisLater1();   // Window{ ... }
obj.logThisLater2();   // obj { logThis: f, ... }
```

## 3-2-5 화살표 함수의 예외사항
화살표 함수 내부에는 this가 아예 없으며, 접근하고자 하면 스코프체인상 가장 가까운 this에 접근한다.

*예제 3-29 화살표 함수 내부에서의 this*
```js nums
var obj = {
	outer: function () {
		console.log(this);
		var innerFunc = () => {
			console.log(this);
		};
		innerFunc();
	}
};
obj.outer()
```

## 3-2-6 별도의 인자로 this를 받는 경우(콜백 함수 내에서의 this)
콜백 함수를 인자로 받는 메서드 중 일부는 추가로 this로 지정할 객체(thisArg)를 인자로 지정할 수 있는 경우가 있다. 이러한 메서드의 thisArg 값을 지정하면 콜백 함수 내부에서 this 값을 원하는 대로 변경할 수 있다.

*예제 3-30 thisArg를 받는 경우 예시 - forEach 메서드*
```js nums
var report = {
	sum: 0,
	count: 0,
	add: function () {
		var args = Array.prototype.slice.call(arguments);
		args.forEach(function (entry) {
			this.sum += entry;
			++this.count;
		}, this);
	},
	average: function () {
		return this.sum / this.count;
	}
};
report.add(60, 85, 95);
console.log(report.sum, report.count, report.average());
// 240 3 80
```

기타 thisArg를 인자로 받는 메서드와 문법들
*예제 3-31 콜백 함수와 함께 thisArg를 인자로 받는 메서드*
```js
Array.prototype.forEach(callback[, thisArg])
Array.prototype.map(callback[, thisArg])
Array.prototype.filter(callback[, thisArg])
Array.prototype.some(callback[, thisArg])
Array.prototype.every(callback[, thisArg])
Array.prototype.find(callback[, thisArg])
Array.prototype.findIndex(callback[, thisArg])
Array.prototype.flatMap(callback[, thisArg])
Array.prototype.from(arrayLike[, callback[, thisArg]])
Set.prototype.forEach(callback[, thisArg])
Map.prototype.forEach(callback[, thisArg])
```

# 03 정리
---
다음 규칙은 명시적 this 바인딩이 없는 한 언제나 성립한다.
- 전역공간에서는 전역객체(브라우저: window, Node.js: global) 참조
- 어떤 함수를 메서드로서 호출한 경우 메서드 호출 주체(메서드명 앞의 객체) 참조
- 어떤 함수를 함수로서 호출한 경우 전역객체 참조, 메서드 내부함수에서도 같음
- 콜백 함수 내부에서의 this는 해당 콜백 함수의 제어권을 넘겨받은 함수가 정의한 바에 따르며, 정의하지 않은 경우 전역객체 참조
- 생성자 함수에서의 this는 생성될 인스턴스를 참조

다음은 명시적 this 바인딩이다. 위 규칙에 부합하지 않는 경우 다음 내용을 바탕으로 this를 예측할 수 있다.
- call, apply 메서드는 this를 명시적으로 지정하면서 함수 또는 메서드를 호출
- bind 메서드는 this 및 함수에 넘길 인수를 일부 지정해서 새로운 함수를 만듦
- 요소를 순회하면서 콜백 함수를 반복 호출하는 내용의 일부 메서드는 별도의 인자로 this를 받기도 함
