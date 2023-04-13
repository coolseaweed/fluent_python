## 내장 시퀀스 (Sequence) 개요
### `컨테이너 시퀀스` vs `균일 시퀀스` (`Container Sequence` vs `Flat Sequence`)
> 컨테이너 시퀀스: 서로다른 자료형의 항목들을 담을 수 있는 `list`, `tuple`, `collections.deque` 형

> 균일 시퀀스: 단 하나의 자료형만 담을 수 있는 `str`, `bytes`, `bytearray`, `memoryview`, `array.array` 형


### `가변 시퀀스` vs `불변 시퀀스` (`Mutable Sequence` vs `Immutable Sequence`)
> 가변 시퀀스: 생성 후 값이 바뀔 수 있는 `list`, `bytearray`, `array.array`, `collections.deque`, `memoryview` 형

> 불변 시퀀스: 생성 후 값이 바뀔 수 없는 `tuple`, `str`, `bytes` 형

## 명명된 튜플 (Named Tuple)
> `collections.namedtuple()` 함수는 필드명과 클래스명을 추가한 튜플의 서브클래스를 생성하는 팩토리 함수로서, 디버깅할 때 유용하다.