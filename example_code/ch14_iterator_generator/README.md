## 코루틴으로서의 제너레이터
- 제너레이터는 반복하기 위한 데이터를 생성한다.
- 코루틴은 데이터의 소비자다.
- 머리가 터지지 않으려면 이 두개념을 뒤섞지 마라.
- 코루틴은 반복과 상관없다.
- 주의: 코루틴 안에서 yield가 값을 생성하게 하는 것은 쓸모가 있지만, 이것은 반복과 상관없다.

## 표준 라이브러리의 제너레이터 함수 20가지
- **필터링 제너레이터 함수**
    |module|function|explain|
    |:---|:---|:---|
    |itertools|`compress(it, selector_it)`|두 개의 반복형을 병렬로 소비한다. selector_it의 해당 항목이 참된 값일 때마다 it에서 항목을 생성한다.|
    |itertools|`dropwhile(predicate, it)`|predicate가 참된 값인 동안 항목들을 지나가면서 it를 소비한 후, 추가 검사 없이 남아 있는 항목을 모두 생성한다.|
    |built-in|`filter(predicate, it)`|predicate를 it의 각 항목에 적용해서 predicated(it)가 참된 값이면 각 항목을 생성한다. predicate가 None이면 참된 항목을 모두 생성한다.|
    |itertools|`filter(predicate, it)`|filter()와 같지만 반대 논리를 적용한다. predicate로 거짓된 값이 나오는 항목을 모두 생성한다.|
    |itertools|`islice(it.stop)`이나 `islice(it, start, stop, step=1)`|s[:stop]이나 s[start:stop:step]과 비슷하게, 반복할 수 있는 모든 객체에 느긋하게 연산을 적용해서 it의 슬라이스 항목을 생성한다.|
    |itertools|`takewhile(predicate, it)`|predicate가 참된 값으로 계산되는 동안 모든 항목을 생서하고, 추가 검사 없이 멈춘다.|


- **맵핑 제너레이터 함수**
    |module|function|explain|
    |:---|:---|:---|
    |itertools|`accumulate(it, [func])`|누적된 합계를 구한다. func를 제공하면, 처음 두 개의 항목에 func를 적용한 결과를 첫 번째 값으로 생성하며 it를 반복한다.|
    |built-in|`enumerate(it, start=0)`|(인덱스, 항목) 형태의 튜플을 생성한다. 인덱스는 start부터 세며, 항목은 it에서 가져온다.|
    |built-in|`map(func, it1, [it2, ..., itN])`|func를 각 it에 적용해서 결과를 생성한다. N개의 반복형이 주어지는 경우, func는 N개의 인수를 받아야 하며, N개의 반복형을 병렬로 소비한다.|
    |itertools|`starmap(func, it)`|it의 각 항목에 func를 적용해서 결과를 생성한다. 입력된 it는 iit 항목을 생성하고 func는 func(*iit)형태로 호출된다.|


- **입력된 여러 입력 반복형을 병합하는 제너레이터 함수**
    |module|function|explain|
    |:---|:---|:---|
    |itertools|`chain(it1, ..., itN)`|it1의 모든 항목을 생성한 후, 나머지 반복형의 항목을 차례대로 생성한다.|
    |itertools|`chain.from_iterable(it)`|it에서 생성된 반복형 객체의 모든 항목을 생성한다. it가 생성한 항목은 반복할 수 있어야 한다 (예를 들면 반복형의 리스트)|
    |itertools|`product(it1, ...., itN, repeat=1)`|데카르트 곱을 계산한다. 각 it의 항목을 이용해서 중첩된 for 루프가 생성하듯이 N-튜플을 생성한다. repeat는 it가 두번 이상 소비되도록 허용한다.|
    |built-in|`zip(it1, ..., itN)`|각 it의 항목을 병렬로 소비해서 N-튜플을 생성한다. 어느 하나의 it가 소모되면 조용히 중단한다.|
    |itertools|`zip_longest(it1, ..., itN, fillvalue=None)`|각 it의 항목을 병렬로 소비해서 N-튜플을 생성한다. 최종 it가 소모될 때까지 빈 칸을 fillvalue로 채워가며 생성한다.|


- **입력된 항목 하나를 여러 개로 확장하는 제너레이터 함수**
    |module|function|explain|
    |:---|:---|:---|
    |itertools|`combinations(it, out_len)`|it로 생성된 항목에서 out_len 개의 조합을 생성한다.|
    |itertools|`combinations_with_replacement(it, out_len)`|반복된 항목들의 조합을 포함해서, it로 생성된 항목에서 out_len ro개의 조합을 생성한다.|
    |itertools|`count(start=0, step=1)`|start에서 시작해서 step만큼 증가시키며 숫자를 무한히 생성한다.|
    |itertools|`cycle(it)`|각 항목의 사본을 저장한 후, 항목을 무한히 반복한다.|
    |itertools|`permutations(it, out_len=None)`|it로 생성된 항목에서 out_len개 항목의 조합을 생성한다. 기본적으로 out_len은 len(list(it))다.|
    |itertools|`repeat(item, [times])`|times를 지정하면 times만큼, 아니면 주어진 item을 무한히 반복해서 생성한다.|

- **재배치 제너레이터 함수**
    |module|function|explain|
    |:---|:---|:---|
    |itertools|`groupby(it, key=None)`|(<키>,<그룹>)의 튜플을 생성한다. 이때 <키>는 그룹화 기준, <그룹>은 그룹 안의 항목을 생성하는 제너레이터다.|
    |built-in|`reversed(seq)`|seq 안의 항목을 뒤에서부터 역순으로 생성한다. seq는 시퀀스이거나 __reversed__() 특별 메서드를 구현해야 한다.|
    |itertools|`tee(it, n=2)`|n개의 제너레이터로 구성된 튜플을 하나 생성한다. 각 제너레이터는 입력된 it를 독립적으로 생성한다.|

## 반복형을 리듀스하는 함수
- **반복형을 읽어서 하나의 값을 반환하는 내장 함수**
    |module|function|explain|
    |:---|:---|:---|
    |built-in|`all(it)`|it의 모든 항목이 참된 값이면 True를, 아니면 False를 반환한다. all([])은 True를 반환한다.|
    |built-in|`any(it)`|it의 항목들 중 하나라도 참된 값이면 True를, 아니면 False를 반환한다. any([])는 False를 반환한다.|
    |built-in|`max(it, [key=,] [default=])`|it의 항목들 중 최댓값을 반환한다. key는 sorted()에서 사용하는 정렬 함수와 동일한 함수며, it가 비어 있을 때는 default가 반환된다. max(arg1, arg2, ..., [key=?])형태로 호출할 수도 있으며, 이때 인수들 중 최댓값이 반환된다.|
    |built-in|`min(it, [key=,] [default=])`|it의 항목들 중 최솟값을 반환한다. key는 sorted()에서 사용하는 정렬 함수와 동일한 함수며, it가 비어 있을 때는 default가 반환된다. min(arg1, arg2, ..., [key=?])형태로 호출할 수도 있으며, 이때 인수들 중 최솟값이 반환된다.|
    |functools|`reduce(func, it, [initial])`|처음 두 개의 항목에 func를 적용하고, 그 결과와 세 번째 항목에 또 func를 적용하는 과정을 반복한 결과를 반환한다. initial이 주어지면 initial과 첫 항목에 func를 적용하면서 시작한다.|
    |built-in|`sum(it, start=0)`|it 항목의 합계에 선택적인 start 값을 더한 값을 반환한다. 실수형의 경우 math.fsum()을 사용하면 정밀도가 향상된다.|

## 읽을 거리
- [itertools 예제](https://docs.python.org/3/library/itertools.html)
- [itertools recipes](http://bit.ly/1MM5YvA)
- [코루틴과 동시성에 대한 흥미로운 강좌 (#31 slide)](http://www.dabeaz.com/coroutines/Coroutines.pdf)