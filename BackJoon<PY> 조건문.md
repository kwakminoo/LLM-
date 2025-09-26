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
~~~1

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
