![[Pasted image 20231216173518.png]]
## any
- `Any` 는 타입 검사를 항상 만족한다.
- 따라서, 모든 타입의 연산을 할 수 있다.
- 이에 따라 의도치 않은 사이드 이펙트가 있을 수 있다.
- 예를들어 객체에 존재하지 않는 프로퍼티에 접근해도 컴파일러는 아무런 에러를 띄워주지 않는다. (런타임에 문제가 된다)
```typescript
let foo: any = 'bar';

foo.bar // 컴파일러가 뭐가 잘못된지 모른다.
foo() // 컴파일러가 뭐가 잘못된지 모른다. 
```
## unknown
- `unknown` 은 타입스크립트의 **Top-Type** 이다.
- 따라서 타입스크립트에 존재하는 **모든 타입을 할당** 할 수 있다.
- 다시 말해서, **모든 타입의 공통적인 연산밖에 할 수 없다.**
```typescript
let foo: unknown = 'bar';

foo = 10; // ok
foo = ['hello', 'world']; // ok

// 공통된 연산 외에는 할 수 없다. 

foo[0]; // Error 
foo(); // Error 
foo.bar // Error 

// 타입이 지정된 변수에 할당 할 수 없다. 

let bar: boolean = foo; // Error !! 
// foo 변수의 타입이 unknown 이기 때문에 boolean 타입의 변수에 할당 할 수 없다.

// 할당하기 위해서는 아래와 같이 타입을 명시해줘야 한다.
let bar: boolean = (foo as boolean);
```
> any와 unknown 차이🤔?  
> 
> any는 의도치 않은 사이드 이펙트가 발생할 수 있으나 unknown은 최소의 공통적인 연산만 가능하므로 **any 보다 unknown이 좀더 안전한 편**

## never
- Never 타입은 모든 타입의 **하위 타입**이다.
- **그래서 그 어떤 값도 Never 타입에 할당 할 수 없다.**
```typescript
let foo : never = 'bar'; // Error
let bar : never = 10; // Error 
```

### Never는 아래와 같을 때 사용 할 수 있다.

**1. 함수가 아무것도 반환하지 않을 때 -> never 를 반환타입으로 지정하여 타입추론 예외를 제거한다.**

```typescript
function throwError(errorMsg: string): never { 
            throw new Error(errorMsg); 
} 
```

- _반환 타입을 void 로 했을 때와 차이점은 void는 null 혹은 undefined 값의 반환을 허용한다는 것이고 never는 그렇지 않다는 것이다._

**2. 특정 타입 값을 할당받지 못하게 할 때**

```typescript
type NonString<T> = T extends string ? never : T;
```

## [[CS관련 예상 질문|돌아가기]]
---
#typescript
