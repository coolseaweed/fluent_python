## if문 이외에서의 else 블록(이것 다음에 저것)
- for: for 루프가 완전히 실행된 후에(break 문으로 중간에 멈추지 않고) else 블록이 실행된다.
```Python
for item in my_list:
    if item.flaver == 'banana':
        break
else:
    raise ValueError('No banana flaver found!')
```

- try/except: try 블록에서 예외가 발생하지 않을 때만 else 블록이 실행된다. 그리고 else 블록에서 발생한 예외는 else블록 앞에 나오는 except 블록에서 처리되지 않는다.
```Python
try:
    dangerous_call()
except OSError:
    log('OSError...')
else:
    after_call()
```

- while: 조건식이 거짓이 되어 while 루프를 빠져나온 후에(break 문으로 중간에 멈추지 않고) else 블록이 실행된다.


## 제너레이터? 코루틴?
`@contextmanager` 데코레이터와 함께 사용되는 제너레이터 안의 `yield` 문은 반복과 상관없음을 주의하자. 이 절에서 보여준 예제에서 제너레이터는 코루틴과 비슷하게 동작한다. 코루틴은 어떤 지점까지 실행한 후 호출자가 실행할 수 있도록 멈춘 후, 호출자가 원하면 나머지 작업을 진행한다.


## 읽을 거리
- [@contextmanager examples:in-place file rewriting context manager](http://bit.ly/1MM96aR)
- [Compound Statements](http://bit.ly/1MMa1YB)
- [Is it a good practice to use try-except-else in python?](http://bit.ly/1MMa2Mp)