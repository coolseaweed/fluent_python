## 내장 자료형 상속
> CAUTION_ dict나 list, str 등의 내장 자료형은 사용자가 정의한 오버라드된 메서드를 무시하므로, 이 클래스들을 직접 상속하면 에러가 발생하기 쉽다. 내장 자료형보다는 쉽게 확장할 수 있도록 설계된 UserDict, UserList, UserString 등을 사용하는 collections 모듈에서 클래스를 상속하는 것이 좋다.

## Mixin 클래스
'is-a' 관계를 나타내지 않고 서로 관련 없는 여러 서브클래스에서 코드를 재사용하기 위해 설계된 클새스는 명시적으로 믹스인 클래스로 만들어야 한다. 개념적으로 믹스인 클래스느 새로운 자료형을 정의하지 않고, 단지 재사용할 메서드들을 묶어놓을 뿐이다. 믹스인 클래스로 객체를 생성하면 안 되며, 믹스인 클래스를 상속하는 구상 클래스는 다른 클래스도 상속해야 한다. 각가의 믹스인 클래스는 밀접히 연관된 메서드 몇 개를 구현해서 하나의 구체적인 행위를 제공해야 한다.

## ABC가 믹스인이 될 수는 있지만, 믹스인이라고 해서 ABC인 것은 아니다
ABC는 구상 메서드를 구현할 수 있으므로 믹스인으로 사용할 수도 있다. 그리고 ABC는 자료형을 정의하지만, 믹스인은 자료형을 정의하지 않는다. 게다가 ABC는 다른 클래스의 유일한 기저 클래스가 될 수 있는 반면, 믹스인 하나만 사용해서 서브클래스를 정의하면 안 된다 (물론 특화된 믹스인을 정의하는 경우는 예외지만, 실제 코드에서 이런 구조는 보기 드물다).

믹스인에는 적용되지 않고 ABC에만 적용되는 제한이 하나 있다. ABC에서 구현된 구상 메서드는 해당 ABC나 슈퍼클래스의 메서드만 사용할 수 있다. 즉, ABC에 정의된 구상 메서드는 일종의 편의를 위한 것일 뿐이다. 구상 메서드가 수행하는 모든 것은 ABC의 다른 메서드를 호출해서 동일하게 수행할 수 있기 때문이다.

## 두 개 이상의 구상 클래스에서 상속받지 않는다.
구상 클래스는 0개 또는 많아야 하나의 구상 슈퍼클래스를 가져야 한다. 즉, 구상 클래스의 슈퍼클래스 중 하나를 제외한 나머지 클래스는 ABC나 믹스인이어야 한다. 예를 들어 다음코드에서 `Alpha`가 구상클래스면, `Beta`와 `Gamma`는 ABC이거나 믹스인이어야 한다.
```Python
class MyConcreteClass(Alpha, Beta, Gamma):
    """구상 클래스: 객체를 생성할 수 있다."""
```

## 클래스 상속보다 객체 구성을 사용하라.
일단 상속에 익숙해지면 과도하게 사용하기 쉬워진다. 객체를 계층구조로 깔끔하게 정리하면 보기 좋아지며, 프로그래머는 이 일을 즐기게 된다. 그러나 구성을 더 좋아하게 되면 설계의 융통성이 향상된다.

## 읽을거리
- [PyPy와 CPython의 차이점](http://bit.ly/1JHNmhX)