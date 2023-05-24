## `Future` 객체의미
파이썬 3.4 표준 라이브러리에서 `Future`라는 이름을 가진 클래스는 `concurrent.futures.Future`와 `asyncio.Future` 다. 이 두 `Future` 클래스의 객체는 완료되었을 수도 있고 아닐 수도 있는 지연된 계산을 표현하기 위해 사용된다. `Future` 클래스는 Twisted의 `Deffered` 클래스, Tornado의 `Future` 클래스, 자바스크립트 라이브러리의 `Promise` 객체와 비슷하다

## `Future`에 대해 알아야 할점
일반적으로 `Future`에 대해 알아야 할 중요한 점은 여러분이나 나 같은 사람이 직접 객체를 생성하면 안 된다는 것이다. `Future` 객체는 `concurrent.futures` 나 asyncio 같은 동시성 프레임워크에서만 배타적으로 생성해야 한다. 이유는 간단하다. `Future` 는 앞으로 일어난 일을 나타내고, `Future`의 실행을 스케줄링하는 프레임워크만이 어떤 일이 일어날지 확실히 알  수 있기 때문이다.