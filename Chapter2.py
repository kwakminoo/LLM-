# 문자열 포맷팅 예제
number = 3
month = 12
day = "two"
# 파이썬에선 여러 문자열이 있지만 %s로 통일해서 사용할 수 있다.
# C#에서 %f, (대입할 값) 하는 것 처럼 여기선 "문자"  % (대입할 값)이런 형태로 %로 사용한다
a = "%s달 %s일 이벤트 당첨 번호는 %s입니다 담청 확률은 %%s입니다다" % (month, day, number)
print(a) 

# %f는 소수점을 나타내는 문자형이고 0.4는 4번째 자리까지 나타내는 것이다.
b = "%0.4f" % 3.42134234234
print(b)

# format 함수는 {}안에 넣을 값을 대입하는 함수이다.
c = "i eat {0} apples".format(3)
print(c)

d = "{one}까진 {t} {th}".format(one = 1, t = "까진", th = "할만한데?")
print(d)

# 문자열 슬라이싱 예제
e = "나는 생각한다, 고로 존재한다."
print(e[0:0:-1])
 
# {:>10}10칸을 만들고 그 칸 안에서 오른쪽 정렬
# {:<5}5칸을 만들고 그 칸 안에서 왼쪽 정렬
# {:^7}7칸을 만들고 그 칸 안에서 가운데 정렬
# .format()은 ()안에 있는 것을 대입한다
e = "{0:^10}".format("hi")
print(e)

name = "곽민우"
age = 23
# f''는 format의 최신문법으로 format과 같은 기능을 한다.
f = f'나의 이름은 {name}이고 나이는 {age}살이야.'
print(f)
 
g = "hobby"
#count는 숫자를 새는 것이고 밑은 b의 개수를 새는 것이다.
print(g.count('b'))

# 리스트 안에 또 다른 리스트를 만들 수 있다.
odd = [1,2,3,4,5, ['one', 'two', 'three', 'four','five']]
#type은 말 그대로 그것의 클래스 타입을 나타낸다.
print(type(odd))
# 리스트 안에 리스트의 값을 출력할 때는 몇번 리스트의 몇번인지 동일하게 연속해서 사용하면 된다.
print(odd[5][3])

a = [1,2,3,4,5]
# 밑은 a리스트의 [2]번 값을 변경하는 것이다.
a[2] = "fuck"
print(a)
# del은 그 부분을 삭제한다.
del a[2]
# len은 길이를 새는 것으로 안에 변수가 5개라면 5를 출력한다다
print(len(a))
# sort는 오름차순 정렬
a.sort()
print(a)
# reverse는 내림차순 정렬이다.
a.reverse()
print(a)

test = ["angly", "gold", "xe", "hi", "under"]
test.sort()
print(test)
test.reverse()
print(test)

a.insert(2, "fuck")
print(a)
a.pop(2)
print(a)

#  Mutable: 리스트, 딕셔너리, 집합 등 변경이 가능한 것.
# Immutable: 정수, 실수, 문자열, 튜플 등 변경이 불가능 한 것.
# 리스트: [] 튜플: ()

t = 1,2,3
print(t)
t1 = (1, 3)
print(t1[-1])
t2 = (1, 2, (3, 4, 5))
print(t2[1], t2[2][1])