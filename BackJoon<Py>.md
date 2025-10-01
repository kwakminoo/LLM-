입출력과 사칙연산
==

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

조건문
=
### 두 수 비교하기
~~~
a, b = map(int, input().split())

if a < b:
  print("<)
//파이썬은 else if가 아니라 elif다
elif a > b:
  print(">")
//파이썬에는 ==는 문법은 존재하지 않는다.
else:
  print(==)
~~~

### 시험 성적
~~~
value = int(input())

if 90 <= value <= 100:
    print("A")
elif 80 <= value <= 89:
    print("B")
elif 70 <= value <= 79:
    print("C")
elif 60 <= value <= 69:
    print("D")
else:
    print("F")
~~~

### 윤년
~~~
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("1")
else:
    print("0")
~~~

### 사분면
~~~
x = int(input())
y = int(input())

if(0 < x and 0 < y):
    print("1")
elif(x < 0 and 0 < y):
    print("2")
elif(x < 0 and y < 0):
    print("3")
elif(0 < x and y < 0):
    print("4")
~~~

### 알림시계
~~~
h, m = map(int, input().split())

if m < 45:         # 45분보다 작으면 시(hour)를 줄여야 함
    h -= 1
    m += 15        # (m + 60) - 45 와 같음
    if h < 0:      # 0시에서 1시간 줄이면 23시로
        h = 23
else:              # 45분 이상이면 그냥 분만 줄이면 됨
    m -= 45

print(h, m)
~~~

### 오븐 시계
~~~
a, b = map(int, input().split())
c = int(input())

// a * 60으로 시간인 a를 분으로 변환해서 총 분을 구함
total = a * 60 + b
//거기다가 c를 더해서 최종 걸리는 시간을 구하고
total += c

//그 값에서 60으로 나눈 몫을 24로 나눠 나머지 값이 곧 시간이 되고
a = (total // 60) % 24
//총 값에서 60으로 나눈 나머지 값이 분이 됨
b = (total % 60)

print(a, b)
~~~

### 세개의 주사위
~~~
a, b, c = map(int, input().split())

//모두 같을 때
if a == b == c:
    print(10000 + a * 1000)

//두개만 같을 때, 처음은 a를 기준으로 그러면 다음은 남은 b=c만 구현하면 됨
elif a == b or a ==c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
//마지막으로 위 조건이 다 아니면 세 수가 다 다른거니까 max를 이용해 세 수 중 가장 큰 값에 곱함
else:
    print(max(a, b, c) * 100)
~~~

반복문
=

### 구구단
~~~
n = int(input())

// 파이썬에서는 range를 씀
for i in range(1, 10):
    //f는 format의 최신버전 사용법으로 f"내용" 이런식으로 적으면 안에 따로 선언을 안해도 자동적으로 {}안에 변수의 값이 출력됨
    print(f"{n} * {i} = { n * i}")
~~~

### 테스트 출력
~~~
t = int(input())

// 파이썬에서 for문을 사용할 때는 i등의 변수가 들어가는데 그 변수가 필요 없을 경우 관습적으로 _를 넣는다
for _ in range(t)
    a, b = map(int, input().split())
    print(a + b)
~~~

### 합
~~~
n = int(input())
total = 0

//파이썬은 0 < i < 10형식이 아니라 10, 10이런 형식임 
for i in range(1, n+1):
    total += i

//total 바로 밑에 출력하면 for문이라 계속 출력되서 한번만 출력되기 위해 따로 출력
print(total)

or

n = int(input())
//이런 수학 공식을 이용해서도 가능
print(n * (n+1) // 2)
~~~

### 영수증
~~~
x = int(input())
n = int(input())
total = 0

for _ in range(n):
    a, b = map(int, input().split())
    total += a * b

// 정수값을 비교할 때는 == 를 써야한다
if total == x:
    print("Yes")
else:
    print("No")
~~~

### 코딩은 체육과목 입니다
~~~
n = int(input())

//그냥 /를 쓰면 값이 실수(float)으로 나온다 정수로 나올려면 //를 써야한다.
longN = n // 4
print("long " * longN + "int")
~~~

### 빠른 A + B
~~~
//파이썬 표준 라이브러리를 가져옴
import sys
input = sys.stdin.readline

t = int(input())
out_lines = []

for _ in range(t):
    a, b = map(int, input().split())
    out_lines.append(str(a + b))
    
sys.stdout.write("\n".join(out_lines))

~~~
