### Hello world 출력
~~~
print("Hello World!")
~~~

### A + B
~~~
// 여기서 map은 a, b 두 개의 값을 인트로 만들고 그것을 인풋으로 받아오면서 스플릿으로 나눈다.
a, b = map(int, input().split())

//if문의 문법은 이런 형식이고 ()대신 끝에 : 가 붙는다
if a < 10 and b < 10:
    print(a * b)
else:
    print("수를 다시 입력하세요")
~~~
