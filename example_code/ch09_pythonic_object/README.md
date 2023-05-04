## `classmethod` vs `staticmethod`
- `classmethod` 는 객체가 아닌 클래스에 연산을 수행하는 method 를 정의한다.
- `staticmethod` 는 method 가 특별한 첫 번째 인수를 받지 않도록 method 를 변경한다. 본질적으로 `staticmethod` 는 모듈 대신 클래스 본체 안에 정의된 평범한 함수 일 뿐이다.
```Python
class Demo:
    @classmethod
    def classmeth(*args):
        return args
    
    @staticmethod
    def statmeth(*args):
        return args

>>> Demo.classmeth()
(<class '__main__'.Demo>,)
>>> Demo.classmeth('spam')
(<class '__main__'.Demo>, 'spam')
>>> Demo.statmeth()
()
>>> Demo.statmeth('spam')
('spam',)
```

## `__slot__` 클래스 속성으로 공간 절약하기

`__slot__`속성은 파이썬 인터프리터가 객체 속성을 딕셔너리 대신 튜플에 저장하게 만든다.
> 주의점 1. 슈퍼클래스에서 상속받은 `__slot__` 속성은 서브를래스에 영향을 미치지 않는다. 파이썬은 각 클래스에서 개별적으로 정의된 `__slot__` 속성만 고려한다.

> 주의점 2. 클래스 안ㅇ `__slot__` 를 명시하는 경우, 객체는 `__slot__` 에 명시되지 않은 속성을 가질 수 없게 된다. 이는 `__slot__`가 존재하는 이유는 아니며, 실제로는 부작용이다. 그러나 단지 여러분이 만든 클래스의 사용자 객체에 새로운 속성을 추가할 수 없게 하기 위해 `__slot__`를 사용하는 것은 적절치 않다고 생각한다. `__slot__`는 최적화를 위해 사용하는 것이지, 프로그래머를 억압하기 위한 것은 아니다.

> 주의점 3. 객체가 약한 참조(GC)를 지원하려면 `__weakref__` 속성이 필요하다. 이 속성은 사용자 정의 클래스에 기본적으로 존재한다. 그러나 클래스가 `__slot__` 를 정의하고 이 클래스의 객체를 약한 참조의 대상이 되게 하려면 `__weakref__`를 `__slot__`리스트에 추가해야 한다.

다른 최적화 작업과 마찬가지로 필요성이 정당화되고 신중히 프로파일링해서 효과가 입증된 경우에만 `__slot__`을 사용해야한다.
