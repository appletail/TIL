## CORS란?
CORS(Cross-Origin Resource Sharing)는 [[출처]](Origin)가 다른 자원(Resource)들을 공유(Sharing)한다는 뜻으로, 한 출처에 있는 자원에서 다른 출처에 있는 자원에 접근하도록 하는 개념이다.
#### 출처(Origin)란?
![[출처]]


### 다른 출처 요청의 위험성
\<img>, \<script>, \<frame>, \<video>, \<audio> 등이 웹에 등장하면서, 페이지 로딩 이후 브라우저에서 이러한 하위 자원들을 가져올 수 있게 되었다. 그러므로 동일 출처, 다른 [[출처]] 모두 호출이 가능하게 되었다.

![[Pasted image 20230925153442.png]]
만약, CORS 정책이 없고 모든 다른 [[출처]] 요청이 가능한 브라우저가 있다면, evil.com에 접속했을 때 실행된 script에 의해 은행의 계좌가 삭제될 수 있다.

### 동일 출처 정책(Same-origin policy)
동일 출처 정책은 다른 [[출처]]로부터 조회된 자원들의 읽기 접근을 막아 다른 [[출처]] 공격을 예방한다. [(RFC6454)](https://www.rfc-editor.org/rfc/rfc6454.html)

동일 출처 정책은 다른 출처에서 자원을 가져오는 것을 굉장히 제한적으로 허용했다. 또한 SPA와 미디어 중심 웹사이트들이 늘어나고 있어 관련 규칙들 또한 계속 늘어나고 있다.

따라서 다른 [[출처]] 자원에 대한 접근성을 높이기 위해 CORS가 등장했다.

###  출처 비교와 차단은 브라우저가 한다
출처를 비교하는 로직은 서버에 구현된 스펙이 아닌 **브라우저에 구현된 스펙**이다.
![[Pasted image 20230925172144.png]]
브라우저가 정책으로 차단한다는 말은, 브라우저를 통하지 않고 서버 간에 통신을 할때는 정책이 적용되지 않는다는 말과 같다.

즉, 클라이언트 단 코드에서 API 요청을 하는게 아니라, 서버 단 코드에서 다른 출처의 서버로 API 요청을 하면 CORS 에러로부터 자유로워진다. 그래서 이를 이용한 프록시(Proxy) 서버라는 것이 있다.

### 동일 출처 요청 VS 다른 출처 요청
프론트와 백 서버가 **같은 출처에 있으면 동일 출처, 다른 서버에 있으면 다른 출어 요청**이다.
![[Pasted image 20230925160230.png]]
왼쪽의 핸드폰의 URL은 *domain-a.com* 이다.
오른쪽 서버의 URL은 *domain-a.com*과 *domain-b.com* 2가지다.
  
*domain-a.com* 유저가 *domain-a.com* 서버에 요청하면 동일 정책이기 때문에 아무런 문제가 없지만, *domain-a.com* 유저가 *domain-b.com* 서버에 요청하면 호스트(Host)가 다르기 때문에 다른 출처 요청을 한다.

도메인 이외에, 같은 프로젝트 내에 정의된 *layout.css* 파일 요청은 동일 출처 요청이고, *webfont.eot* 같은 경우에는 다른 외부 사이트에서 실시간으로 import를 통해 가져온다면 다른 출처 요청이다.

**기본적으로 동일 출처 요청만 자유롭게 요청이 가능하며 동일 출처 정책(Same-Origin Policy) 이라고 한다.** 하지만 기준을 완화하여 **다른 출처 요청도 할 수 있도록 기준을 만든 체제가 다른 출처 정책(Cross-Origin Policy)** 이다.

## 다른 출처 요청 정책 3가지
1. [[#단순 요청(Simple Request)]]
2. [[#프리플라이트 요청(Preflighted Request)]]
3. [[#인증정보요청(Credential Request)]]

CORS 체험 사이트 https://chuckchoiboi.github.io/cors-tutorial/
### 단순 요청(Simple Request)
simple request의 경우 단순하게 요청의 Origin 값이 Access-Control-Allow-Origin 이 허용하는 url에 포함될 경우 CORS가 가능하다.

- GET, HEAD, POST 요청만 가능
- Accept, Accept-Language, Contet-Language, Content-Type과 같은 [CORS 안전 리스트 헤더](https://developer.mozilla.org/en-US/docs/Glossary/CORS-safelisted_request_header) 혹은 User-Agent 헤더
- Content-Type 헤더의 값이 application/x-www-form-urlencoded, multipart/form-data, text/plain 중 하나인 경우
- XMLHttpRequest.upload에 아무런 이벤트 핸들러, 리스너가 등록되어있지 않은 경우
- - [ReadableStream](https://developer.mozilla.org/ko/docs/Web/API/ReadableStream) object가 요청에 포함되어 있지 않을 때

```js
const xhr = new XMLHttpRequest(); 
const url = 'https://www.api.com?q=test'; 
xhr.open('GET', url); 
xhr.onreadystatechange = requestHandler; 
xhr.send();
```

- **통신 과정 그림**
![[Pasted image 20230925161833.png]]

브라우저는 자신의 주소 https://www.site.com를 origin에 담아 다른 출처에 요청을 보낸다. 서버는 요청을 확인하고 다른 출처 주소 https://www.site.com에 접근이 가능하다는 access-control-allow-origin에 해당 주소를 담아서 결과를 리턴한다.

특히, access-control-allow-origin은 CORS 헤더의 중요 요소 중 하나로 어떤 요청을 허용할지 결정한다. 이 헤더 값은 하나의 출처가 될 수도 있고 "\*"를 사용해 어떤 [[출처]]도 허용하도록 할 수 있다.

만약 서버가 이 헤더에 응답하지 않거나, 헤더 값이 요청의 [[출처]]와 일치하지 않는 도메인인 경우, 브라우저는 응답을 차단한다. 또한 요청한 출처가 서버의 access-conrol-allow-origin에 포함되어 있지 는 경우도 마찬가지이다.
![[Pasted image 20230925161847.png]]

### 프리플라이트 요청(Preflighted Request)
프리 플라이트는 OPTIONS 메서드로 HTTP 요청을 미리 보내 **실제 요청이 전송하기에 안전한지 확인**하는 것이다. 다른 출처 요청이 유저 데이터에 영향을 줄 수 있기 때문에  미리 전송한다는 의미이다.

요청 헤더에는 다음 값이 포함된다.
- **origin** : 어디서 요청을 했는지 서버에 알려주는 주소
- **access-control-request-method** : 실제 요청이 보낼 HTTP 메서드
- **access-control-request-headers** : 실제 요청에 포함된 header

응답 헤더에는 다음 값이 포함된다.
- **access-control-allow-origin** : 서버가 허용하는 출처
- **access-control-allow-methods** : 서버가 허용하는 HTTP 메서드 리스트
- **access-control-allow-headers** : 서버가 허용하는 header 리스트
- **access-control-max-age** : 프리 플라이트 요청의 응답을 캐시에 저장하는 시간

```js
const xhr = new XMLHttpRequest();
const url = 'https://www.api.com?q=test';
xhr.open(‘GET', url);
xhr.setRequestHeader(‘custom-header', ’test')
xhr.onreadystatechange = requestHandler;
xhr.send();
```

![](https://blog.kakaocdn.net/dn/V76fm/btrI2vW2BOU/kIC4h1nSHkylENopnjtr5k/img.png)

플리플라이트 요청은 OPTIONS 를 사용해 자신의 주소 https://www.api.com?q=test를 보낸다. 또한 origin, access-control-request-method, access-control-request-headers를 같이 보낸다.

정상적인 응답으로 access-control-allow-origin, access-control-allow-method, access-control-allow-headers, access-control-max-age를 응답받는다.

정상 요청과 응답이 가능하다는 프리 플라이트 이후 실제 요청을 한다.

### 인증정보요청(Credential Request)
신용 요청은 쿠키, 인증 헤더, TLS 클라이언트 인증서 등의 신용 정보를 함께 요청한다. 기본적으로 CORS 정책은 다른 출처 요청에 인증 정보 포함을 허용하지 않는다. 하지만 요청에 인증을 포함하는 플래그가 있거나 access-control-allow-credentials을 true로 설정 한다면 요청할 수 있다. 

```js
const xhr = new XMLHttpRequest();
const url = 'https://www.api.com?q=test';
xhr.open('GET', url);
xhr.withCredentials = true;
xhr.send();
```

![](https://blog.kakaocdn.net/dn/xu2pp/btrI2xUUny1/aU7mICsDoJUnjmkHVesL21/img.png)

만약 서버 응답에 access-control-allow-credentials가 true로 설정되지 않았거나 access-control-allow-origin 헤더에 있는 값이 허용된 출처가 아니라면 아래와 같이 오류가 발생다. 

![](https://blog.kakaocdn.net/dn/ng3m6/btrI2xUUeEu/x6etslh1jjbqWKCQhaHw20/img.png)

- **어떤 요청 방식을 사용해야 할까?**
프리플라이트 요청을 사용하는게 좋다. 프리 플라이트 요청으로 실제 요청이 실행되기 이전에 검사하고 허용할지 말지를 결정할 수 있기 때문이다.

## CORS 해결법
### 1. **Chrome 확장 프로그램 이용**
아래 링크에서 'Allow CORS: Access-Control-Allow-Origin' 크롬 확장 프로그램을 설치한다.
[Allow CORS: Access-Control-Allow-Origin](https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf)
그러면 브라우저 오른쪽 상단에서 확장 프로그램을 활성화 시킬 수 있다. 해당 프로그램을 활성화 시키게 되면, **로컬(localhost) 환경에서 API를 테스트 시, CORS 문제를 해결**할 수 있다.

서버 테스트 환경에서 고민하지 않고 빠르게 CORS를 해결하는데 좋은 선택지일 것이다.
![[Pasted image 20230925173305.png]]

### 2. 프록시 사이트 이용하기
프론트에서 직접 서버에 리소스를 요청을 했더니 서버에서 따로 설정을 안해줘서 CORS 에러가 뜬다면, **모든 출처를 허용한 서버 대리점**을 통해 요청을 하면 된다.
![[Pasted image 20230925173350.png]]
다만 현재 무료 프록시 서버 대여 서비스들은 모두 악용 사례 때문에 api 요청 횟수 제한을 두고 있다. 그러므로 테스트용이나 맛보기용으로 사용하되, 실전에서는 직접 프록시 서버를 구축하여 사용해야한다.

### 3. 서버에서 Access-Control-Allow-Origin 헤더 세팅하기
직접 서버에서 HTTP 헤더 설정을 통해 출처를 허용하게 설정하는 가장 정석적인 해결책이다.

서버의 종류도 노드 서버, 스프링 서버, 아파치 서버 등 여러가지가 있으니, 이에 대한 각각 해결책을 나열해본다. 각 서버의 문법에 맞게 위의 HTTP 헤더를 추가해 주면 된다.

참고로 CORS에 연관된 HTTP 헤더 값으로는 다음 종류가 있다. (이들을 모두 설정할 필요는 없다)
```http
# 헤더에 작성된 출처만 브라우저가 리소스를 접근할 수 있도록 허용함.
# * 이면 모든 곳에 공개되어 있음을 의미한다. 
Access-Control-Allow-Origin : https://naver.com

# 리소스 접근을 허용하는 HTTP 메서드를 지정해 주는 헤더
Access-Control-Request-Methods : GET, POST, PUT, DELETE

# 요청을 허용하는 해더.
Access-Control-Allow-Headers : Origin,Accept,X-Requested-With,Content-Type,Access-Control-Request-Method,Access-Control-Request-Headers,Authorization

# 클라이언트에서 preflight 의 요청 결과를 저장할 기간을 지정
# 60초 동안 preflight 요청을 캐시하는 설정으로, 첫 요청 이후 60초 동안은 OPTIONS 메소드를 사용하는 예비 요청을 보내지 않는다.
Access-Control-Max-Age : 60

# 클라이언트 요청이 쿠키를 통해서 자격 증명을 해야 하는 경우에 true. 
# 자바스크립트 요청에서 credentials가 include일 때 요청에 대한 응답을 할 수 있는지를 나타낸다.
Access-Control-Allow-Credentials : true

# 기본적으로 브라우저에게 노출이 되지 않지만, 브라우저 측에서 접근할 수 있게 허용해주는 헤더를 지정
Access-Control-Expose-Headers : Content-Length
```

이때 *Access-Control-Allow-origin* 헤더 값으로 ""\*"" 을 사용하면 모든 Origin에서 오는 요청을 허용한다는 의미이므로 당장은 편할 수 있겠지만, 바꿔서 생각하면 정체도 모르는 이상한 출처에서 오는 요청까지 모두 허용하기 때문에 보안은 더 허술해진다. 그러니 가급적이면 귀찮더라도 다음과 같이 출처를 직접 명시해주도록 하자.
```js
response.setHeader('Access-Control-Allow-origin', 'https://inpa.tistory.com');
```

#### Node.js 세팅
서버에 response 헤더(Header) 값으로 Access-Control 설정을 해준다.
```js
var http = require('http');

const PORT = process.env.PORT || 3000;

var httpServer = http.createServer(function (request, response) {
    // Setting up Headers
    response.setHeader('Access-Control-Allow-origin', '*'); // 모든 출처(orogin)을 허용
    response.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE'); // 모든 HTTP 메서드 허용
    response.setHeader('Access-Control-Allow-Credentials', 'true'); // 클라이언트와 서버 간에 쿠키 주고받기 허용

    // ...

    response.writeHead(200, { 'Content-Type': 'text/plain' });
    response.end('ok');
});

httpServer.listen(PORT, () => {
    console.log('Server is running at port 3000...');
});
```

#### Express.js 세팅
```shell
> npm i cors
```

```js
const express = require('express')
const cors = require("cors"); // cors 설정을 편안하게 하는 패키지
const app = express();

// ...

app.use(cors({
    origin: "https://naver.com", // 접근 권한을 부여하는 도메인
    credentials: true, // 응답 헤더에 Access-Control-Allow-Credentials 추가
    optionsSuccessStatus: 200, // 응답 상태 200으로 설정
}));

// ...
```

#### JSP / Servlet 세팅
```java
import javax.servlet.*;

public class CORSInterceptor implements Filter {

    private static final String[] allowedOrigins = {
            "http://localhost:3000", "http://localhost:5500", "http://localhost:5501",
            "http://127.0.0.1:3000", "http://127.0.0.1:5500", "http://127.0.0.1:5501"
    };

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) servletRequest;

        String requestOrigin = request.getHeader("Origin");
        if(isAllowedOrigin(requestOrigin)) {
            // Authorize the origin, all headers, and all methods
            ((HttpServletResponse) servletResponse).addHeader("Access-Control-Allow-Origin", requestOrigin);
            ((HttpServletResponse) servletResponse).addHeader("Access-Control-Allow-Headers", "*");
            ((HttpServletResponse) servletResponse).addHeader("Access-Control-Allow-Methods",
                    "GET, OPTIONS, HEAD, PUT, POST, DELETE");

            HttpServletResponse resp = (HttpServletResponse) servletResponse;

            // CORS handshake (pre-flight request)
            if (request.getMethod().equals("OPTIONS")) {
                resp.setStatus(HttpServletResponse.SC_ACCEPTED);
                return;
            }
        }
        // pass the request along the filter chain
        filterChain.doFilter(request, servletResponse);
    }

    private boolean isAllowedOrigin(String origin){
        for (String allowedOrigin : allowedOrigins) {
            if(origin.equals(allowedOrigin)) return true;
        }
        return false;
    }
}
```

#### Spring 세팅
```java
// 스프링 서버 전역적으로 CORS 설정
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
        	.allowedOrigins("http://localhost:8080", "http://localhost:8081") // 허용할 출처
            .allowedMethods("GET", "POST") // 허용할 HTTP method
            .allowCredentials(true) // 쿠키 인증 요청 허용
            .maxAge(3000) // 원하는 시간만큼 pre-flight 리퀘스트를 캐싱
    }
}
```

```java
// 특정 컨트롤러에만 CORS 적용하고 싶을때.
@Controller
@CrossOrigin(origins = "*", methods = RequestMethod.GET) 
public class customController {

	// 특정 메소드에만 CORS 적용 가능
    @GetMapping("/url")  
    @CrossOrigin(origins = "*", methods = RequestMethod.GET) 
    @ResponseBody
    public List<Object> findAll(){
        return service.getAll();
    }
}
```

#### Apache 세팅
httpd.conf에서 \<IfModule mod_headers.c> 태그 안에 헤더 설정을 넣어준다. 또는 VirualHost 부분에 넣어도 된다.

```xml
<IfModule mod_headers.c>
	Header set Access-Control-Allow-Origin "*"
</IfModule>
```

#### Tomcat
톰캣 폴더 경로의 conf/web.xml 혹은 webapps 내의 프로젝트 폴더 내 WEB-INF/web.xml 파일에 아래 헤더 설정을 추가

```xml
<filter>
    <filter-name>CorsFilter</filter-name>
    <filter-class>org.apache.catalina.filters.CorsFilter</filter-class>
    <init-param>
        <param-name>cors.allowed.origins</param-name>
        <param-value>*</param-value>
    </init-param>
    <init-param>
        <param-name>cors.allowed.methods</param-name>
        <param-value>GET,POST,HEAD,OPTIONS,PUT,DELETE</param-value>
    </init-param>
    <init-param>
        <param-name>cors.allowed.headers</param-name>
        <param-value>Content-Type,X-Requested-With,accept,Origin,Access-Control-Request-Method,Access-Control-Request-Headers</param-value>
    </init-param>
    <init-param>
        <param-name>cors.exposed.headers</param-name>
        <param-value>Access-Control-Allow-Origin,Access-Control-Allow-Credentials</param-value>
    </init-param>
    <init-param>
    	<!-- 쿠키 통신을 안하는데 이걸 true로 하면 4XX 서버 에러가 뜬다 -->
        <param-name>cors.support.credentials</param-name>
        <param-value>false</param-value> 
    </init-param>
    <init-param>
        <param-name>cors.preflight.maxage</param-name>
        <param-value>10</param-value>
    </init-param>
</filter>
```

#### Nginx
nginx.conf 파일 안에 ~~location /~~ 부분에 add_header 값으로 헤더 설정을 추가

```json
location / {
    root html;
    add_header 'Access-Control-Allow-Origin' '*';
    index  index.html index.htm;
}
```

#### AWS (S3 호스팅)
1. S3 콘솔 메뉴에 들어가 버킷을 선택한다.
2. 권한(Permissions) 탭을 선택한다.
3. 교차 출처 리소스 공유 창에서 \[편집] 선택한다.
4. 텍스트 상자에 아래 JSON CORS 규칙을 입력한다.

[![s3-cors](https://blog.kakaocdn.net/dn/cyXIRR/btrZzawiBkH/bsEZhz8d7SB7YpkSgLPN90/img.png)](https://blog.kakaocdn.net/dn/cyXIRR/btrZzawiBkH/bsEZhz8d7SB7YpkSgLPN90/img.png)
```json
[
  {
    "AllowedHeaders": [
      "Authorization"
    ],
    "AllowedMethods": [
      "GET",
      "HEAD"
    ],
    "AllowedOrigins": [
      "http://www.example.com"
    ],
    "ExposeHeaders": [
      "Access-Control-Allow-Origin"
    ]
  }
]
```

---
출처
[CORS란 무엇인가?](https://escapefromcoding.tistory.com/724)
[악명 높은 CORS 개념 & 해결법 - 정리 끝판왕](https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-CORS-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95-%F0%9F%91%8F)
