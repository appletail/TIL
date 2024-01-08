## 1. React Hooks란?

리액트 훅은 리액트 클래스형 컴포넌트에서 이용하던 코드를 작성할 필요없이 함수형 컴포넌트에서 다양한 기능을 사용할 수 있게 만들어준 라이브러리라고 할 수 있는데 React 16.8버전에 새로 추가된 기능이다. 이는 함수형 컴포넌트에 맞게 만들어진 것으로 함수형 컴포넌트에서만 사용 가능하다.

## 2. Hook 규칙

#### **1) 최상위에서만 Hook을 호출해야한다.**

- 반복문이나 조건문 혹은 중첩된 함수 내에서 Hook을 호출하면 안된다.
- 리액트 훅은 호출되는 순서에 의존하기 때문에 조건문이나 반복문 안에서 실행하게 될 경우 해당 부분을 건너뛰는 일이 발생할 수도 있기 때문에 순서가 꼬여 버그가 발생할 수 있다. 
- 그렇기 때문에 이 규칙을 따르면 useState 와 useEffect가 여러번 호출되는 경우에도 Hook의 상태를 올바르게 유지할 수 있게 된다.

#### **2) 리액트 함수 내에서만 Hook을 호출해야한다.**

- Hook은 일반적인 js 함수에서는 호출하면 안된다.
- 함수형 컴포넌트나 custom hook에서는 호출 가능하다.

## 3. 자주 사용하는 React Hook 알아보기
### 1) useState

**useState는 상태를 관리하는 훅으로 다음과 같은 특징을 가진다.**

- 함수형 컴포넌트 안에 state를 추가하여 사용한다.
- 현재 상태를 나타내는 state값과 이 상태를 변경하는 setState값을 한 쌍으로 제공한다.
- state는 초기값을 설정할 수 있으며, 초기값은 첫 렌더링 때 한번 사용된다.
- state는 객체일 필요 없이 문자열, 숫자, boolean, 배열, null, 객체 등의 여러가지 다양한 값을 넣을 수 있다.

```javascript
import React, { useState } from 'react';

function Example() {
  // "count"라는 새 상태 변수를 선언합니다
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      // 버튼을 클릭할 때마다 기존의 state 기본값인 0에 1이 더해진다.
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

### 2) useEffect

**useEffect는 기존 클래스형 컴포넌트에서 사용했던 componentDidMount, componentDidUpdate, componentWillUnmount를 하나의 API로 통합한 것으로 다음과 같은 특징을 가진다.**

- useEffect는 기본적으로 useEffect(function, deps)의 형태를 사용한다.
- function에는 실행시킬 함수를 넣고 deps에는 의존성 배열을 담는다.
- 의존성 배열에 어떤 것이 담기느냐에 따라 부수적인 효과 함수가 실행된다.
- 가장 먼저 의존성 배열 없이 useEffect를 실행시키게 되면 페이지가 렌더링 될 때마다 데이터를 불러온다.

```javascript
import React from 'react';

React.useEffect(() => {
  dispatch(getActions.getFundingAC(page));
});
```

- 두번째로 의존성 배열에 빈배열을 담아주게 될 경우에는 첫 렌더링 시에만 함수를 실행한다.

```javascript
import React from 'react';

React.useEffect(() => {
  dispatch(getActions.getFundingAC(page));
}, []);
```

- 마지막으로 의존성 배열에 state값이나 props로 상속받은 데이터값 등을 담아주게 되면 해당값이 변할 때마다 함수를 실행한다.

```javascript
import React from 'react';

const [page, setPage] = React.useState(1)

React.useEffect(() => {
  dispatch(getActions.getFundingAC(page));
}, [page]);
```

이 외에도 useEffect에서는 언마운트시에 cleanup함수를 적용시킬 수 있다.

```javascript
import React, { useState, useEffect, useRef } from "react";

useEffect(() => {
    dispatch(getActions.getFundingDetailAC(fundId));
    return () => {
      dispatch(getActions.clean())
    }
}, []);
```

### 3) useRef

**useRef는 특정 DOM에 접근하여 DOM 조작을 가능하게 하는 훅이다. 리액트 프로젝트에서도 특정 요소를 선택해야하는 상황이 생길 수 있는데 이러한 상황에서 useRef 함수를 사용할 수 있게 된다.**

```javascript
import React, { useState, useEffect, useRef } from "react";
import AudioPlayer from "react-h5-audio-player";
import "react-h5-audio-player/lib/styles.css";

const FundingDetail = () => {

  // 오디오플레이어에 접근하기 위함
  const player = useRef();
  
  // 오디오 플레이어 자동재생막기
  useEffect(() => {
    player.current.audio.current.pause();
  }, [fundingDetail]);
  
  return (
	<React.Fragment >
      {/* 오디오 플레이어 */}
      <AudioPlayer
        className="audio"
        autoPlay={false}
        src={fundingDetail.File}
        volume={1}
        showJumpControls={false}
        // useRef 사용을 위한 ref 지정
        ref={player}
      />            
    </React.Fragment >
  );
};

export default FundingDetail;
```

### 4) useMemo, useCallback

useMemo와 useCallback은 모두 메모이제이션과 관련이 있어 리액트를 사용하며 성능 개선을 위해 많이 사용한다. 여기서 메모이제이션이라는 것은 기존에 수행한 연산의 결과 값을 어딘가에 저장해두었다가 동일한 입력이 들어오면 재활용하겠다는 프로그래밍 기법이라고 할 수 있다. 그렇기 때문에 useMemo나 useCallback 훅을 적절하게 사용하면 중복된 연산을 피할 수 있어 **애플리케이션의 성능을 최적화**할 수 있다는 장점이 있다.

useMemo와 useCallback이 비슷한 동작을 하긴하지만 두가지의 차이도 존재한다. 먼저 useMemo의 경우에는 메모이제이션된 값을 반환하는 훅이고 useCallback은 메모이제이션 된 함수를 반환한다는 특징을 가진다.

## [[CS관련 예상 질문|돌아가기]]
---
#web  #react 

