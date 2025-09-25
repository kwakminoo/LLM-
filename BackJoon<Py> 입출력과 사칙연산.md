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
    // 나누기에서 /는 실수로 출력하고 //는 정수로 출력한다.
    print(a // b)
else:
    print("수를 다시 입력하세요")
~~~

### ??!
~~~
webId = ["joonas", "kwakmw12", "baekbalgui1212", "baekjoon"]

//split은 두 개 이상의 변수를 할 때 사용, 지금처럼 하나만 있는 단독으로 있는 변수에 인풋할 때는 스플릿 사용 안함.
//예 a, b = input().split() or 숫자가 필요하면 map을 같이 씀
jsId = input()

//파이썬에선 한 값이 다른 변수안에 있는지 확인할려면 in을 써야함     
if jsId in webId:
    print(jsId + "??!")
else:
    print("사용가능한 아이디 입니다.")
~~~

### 불기연도가 주어질 때 서기 연도
~~~
일단 그러니까 543년의차이가 남.
불기 연도가 주어지면 거기서 543을 빼면 됨

bAge = int(input())
diffrence = 543
print(bAge - diffence)
~~~

### 나머지 출력
~~~
a, b, c = map(int, input().split())
   
print((a+b)%c)
print(((a%c) * (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)
~~~

### 곱셈
~~~
//num1은 정수로 받고 num2는 문자형으로 받음
num1 = int(input())
num2 = input()

// 리스트 컴프리엑션 기법으로 num2를 리스트로 바꾸면서 역순으로 진행.
result = [num1 * int(x) for x in reversed(num2)]

// for문을 통해서 r이 리스트안에 모든 값을 다 사용할 때 까지 반복
for r in result:
    print(r)

//마지막은 단순하니까 그냥 num2를 인트로 변환해서 처리.
print(num1 * int(num2))
~~~

