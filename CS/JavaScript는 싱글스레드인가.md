JavaScript는 Single thread 지만 논 블라킹이다.

### 자바스크립트는 정말 싱글 쓰레드일까?

맞다, 정확하게 말하면 자바스크립트의 메인 쓰레드인 이벤트 루프가 싱글 쓰레드이기 때문에 자바스크립트를 싱글 쓰레드 언어라고 부른다. 하지만 이벤트 루프만 독립적으로 실행되지 않고 **웹 브라우저나 NodeJS같은 멀티 쓰레드 환경에서 실행**된다. 즉, **자바스크립트 자체는 싱글 쓰레드가 맞지만 자바스크립트 런타임은 싱글 쓰레드가 아니다**.

> 질문 : JavaScript는 싱글 스레드입니다. 어떻게 싱글 스레드 방식으로 비동기 호출을 할 수 있는 지에 대해 설명할 수 있나요?Section4 Unit4 Chapter2-3. 싱글 스레드와 멀티 스레드 : 세션 중 설명한 내용)

이벤트 루프(Event Loop) 동작 방식에 대해 설명할 수 있으면 되는 문제입니다. JavaScript는 싱글 스레드 방식으로 돌아가지만 **실제 자바스크립트가 구동되는 환경(브라우저, Node.js등)에서는 주로 여러 개의 스레드가 사용되기 때문에 필요한 장치가 이벤트 루프이기 때문입니다.**

> 자바스크립트의 함수가 실행되는 방식을 보통 "Run to Completion" 이라고 말합니다. 이는 하나의 함수가 실행되면 이 함수의 실행이 끝날 때까지는 다른 어떤 작업도 중간에 끼어들지 못한다는 의미입니다. 앞서 말했듯이 자바스크립트 엔진은 단일 호출 스택을 사용하며, 현재 스택에 쌓여있는 모든 함수들이 실행을 마치고 스택에서 제거되기 전까지는 다른 어떠한 함수도 실행될 수 없습니다.
> 
> 자바스크립트에서는 함수 호출을 관리하는 call stack과 비동기 작업 처리를 위한 Web API가 함께 작업을 처리합니다. Web API는 특히 작업 완료에 시간이 오래 걸리는 작업을 처리하게 되는데, 이 결과값을 처리할 수 있는 callback 함수를 task queue에 쌓습니다.
> 
> 하나의 js파일이 실행되면, 코드가 차례로 실행됩니다. 코드가 실행되는 도중에 함수가 호출이 되는 순간 call stack에 해당 함수 실행을 위한 모든 정보가 실행 컨텍스트에 담깁니다. 이 함수 내에서 또 함수가 호출되면, call stack에 새로운 실행 컨텍스트가 생깁니다. 함수 실행이 마무리 될 때 마다 결과값을 반환하고 해당 실행 컨텍스트는 없어집니다. 마지막 실행 컨텍스트부터 하나씩 빠지기 때문에 Stack 구조라고 부를 수 있는 것입니다.
> 
> 이 과정 중에 호출되는 함수가 비동기로 작동되는 경우, 이 비동기 작업은 (브라우저는) Web API에서 처리됩니다. 이 작업의 결과를 처리하는 callback 함수는 이후에 call stack에서 따로 실행이 되어야 하는데, call stack에서 실행 컨텍스트가 아직 남아있는 경우 task queue에서 "대기"하게 됩니다.
> 
> 시간이 오래 걸리는 작업이 call stack에 머물러서 싱글스레드로 작동되는 event loop를 막지 않도록 도와줍니다. 그래서 연산이 많고 시간이 오래 걸리는 작업은 비동기로 처리하는 것이 효율적인 것입니다.

- *Event Loop에 대해 설명할 수 있나요? JavaScript는 싱글 스레드 방식으로 돌아가지만 실제 자바스크립트가 구동되는 환경(브라우저, Node.js등)에서는 주로 여러 개의 스레드가 사용되기 때문에 필요한 장치가 이벤트 루프입니다. 핵심만 말하자면, JavaScript event loop는 call stack이 비어있는 경우, task queue에서 대기하던 callback을 call stack으로 옮겨서 callback을 실행시켜주는 역할을 합니다.


#### 자바스크립트 비동기 런타임 과정

자바스크립트가 비동기 코드를 어떻게 동작시키는지 알아보기 위해선 일단 자바스크립트 런타임 환경에 대해 알아야 한다. 여기서는 간단하게 비동기를 동작하는데 필요한 요소들만 살펴보자!
![[Pasted image 20231216165552.png]]


자바스크립트가 실행될 때는 다음과 같은 요소들이 실행을 도와준다.

- **Call Stack**: 자바스크립트에서 수행해야 할 함수들을 순차적으로 스택에 담아 처리
- **Web API**: 웹 브라우저에서 제공하는 API로 AJAX나 Timeout등의 비동기 작업을 실행
- **Task Queue**: Callback Queue라고도 하며 Web API에서 넘겨받은 Callback함수를 저장
- **Event Loop**: Call Stack이 비어있다면 Task Queue의 작업을 Call Stack으로 옮김

그러면 실제 코드를 예시로 비동기 코드가 동작하는 과정을 알아보자!

```jsx
setTimeout(() => console.log('async chanyeong'));
console.log('hello chanyeong');

// hello chanyeong
// async chanyeong
```

다음 코드는 `'hello chanyeong'`과 `'async chanyeong'`이라는 문자열을 콘솔에 출력하는 간단한 코드이다. 하지만 `'async chanyeong'`이 위에 위치함에도 비동기 코드라 나중에 출력되는 것을 볼 수 있다. 어떻게 이렇게 동작하는 것일까?

![[Pasted image 20231216165612.png]]

처음에 우선 `setTimeout` 함수가 실행되며 Call Stack에 `setTimeout` 함수가 추가된다.

![[Pasted image 20231216165618.png]]

`setTimeout` 함수는 자바스크립트 엔진이 처리하지 않고 Web API가 처리한다. (NodeJS의 경우 Timers 모듈) `setTimeout`함수는 Web API의 Timeout작업을 요청한 시간이 지나면 Task Queue로 인자로 받은 callback함수를 전달한다.

![[Pasted image 20231216165634.png]]

그리고는 두 번째 라인에 작성한 `console.log`가 Call Stack에 추가된다. 그리고 Call Stack의 `console.log`가 실행되며 콘솔에는 `'hello chanyeong'`이라는 문자열이 출력된다.

![[Pasted image 20231216165652.png]]

이 때, 자바스크립트의 Event Loop는 Call Stack이 비어있는지 항상 확인하는데 방금 `console.log`가 실행되며 Call Stack이 비워진 것을 확인한다.

![[Pasted image 20231216165704.png]]

Call Stack이 비워진 것을 확인한 Event Loop는 Task Queue에 있던 callback함수를 Call Stack으로 옮겨 작업을 수행한다. 콘솔에는 `'async chanyeong'`이 추가로 출력된 것을 볼 수 있다.

![[Pasted image 20231216165723.png]]

모든 작업이 끝나게 되면 다음과 같이 Call Stack과 Task Queue가 비워진 것을 볼 수 있다.


## [[CS관련 예상 질문|돌아가기]]
---
#javascript 
