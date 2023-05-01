- UML (Unified Modeling Language) - 소프트웨어 개발뿐만 아니라 많은 산업 전반의 비 소프트웨어 시스템에서도 중요한 역할을 담당합니다. UML이 시스템이나 프로세스의 동작 및 구조를 시각적으로 보여주는 방법이기 때문입니다. UML은 응용 프로그램 구조, 시스템 동작 및 기타 비즈니스 프로세스에서 잠재적인 오류를 찾아내는 데 도움을 줍니다. 

- 일급함수 (First Class Function) - 함수를 다른 변수와 동일하게 다루는 언어는 일급 함수를 가졌다고 표현한다. 예를 들어, 일급 함수를 가진 언어에서는 함수를 다른 함수에 인수로 제공하거나, 함수가 함수를 반환할 수 있으며, 변수에도 할당할 수 있다.

- 메타프로그래밍 (Meta Programming) - 자기 자신 혹은 다른 컴퓨터 프로그램을 데이터로 취급하며 프로그램을 작성·수정하는 것을 말한다. 넓은 의미에서, 런타임에 수행해야 할 작업의 일부를 컴파일 타임 동안 수행하는 프로그램을 말하기도 한다.

- 자유 변수 (free variable) - 자유 변수는 지역범위에 바인딩되어 있지 않은 변수를 의미하며, closure과 긴밀히 연결된 변수이다.
    ```Python
    def make_averager():
        # -------------- closure ------------- #
        seriese = [] # free variable
        def averager(new_value):
            seriese.append(new_value)
            total = sum(series)
            return total/len(series)
        # ------------------------------------ #
        return averager

    >>> avg = make_averager()
    >>> avg.__code__.co_varnames # ('new_value', 'total')
    >>> avg.__code__.co_freevars # ('series',)
    ```

