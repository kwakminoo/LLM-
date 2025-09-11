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

d = f"{one}까진 {t} {th}".format(one = 1, t = "까진", th = "할만한데?")
print(d)