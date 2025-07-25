# 📘 CS50 2025 Week 1 학습 정리

> 작성일: 2025-07-03  
> 학습자: (나의 GitHub ID)

---

## 🎯 오늘의 학습 개요

- [CS50 Week 1 강의](https://cs50.harvard.edu/x/2025/weeks/1/) 수강 완료
- Visual Studio Code(코드 에디터) 사용법 습득
- 터미널 명령어 실습
- C 언어 기초 문법 학습 (데이터 타입, 변수, 함수, 헤더 등)
- `get_string`, `printf`, `int`, `string` 등 기본 함수 및 자료형 활용

---

## 🧠 내가 기억하는 핵심 요약

- `string name = get_string("What's your name?");`  
  사용자 입력을 받아 문자열 변수에 저장
- `printf()` 함수는 출력 함수로, 문자열과 변수 값을 함께 출력 가능
- `#include <stdio.h>`, `#include <cs50.h>`는 각각의 함수 정의를 가져오는 헤더파일
- C는 함수형 언어이며, 프로그램의 시작점은 반드시 `int main(void)` 함수
- Visual Studio Code에서 파일 작성 후 `make`로 컴파일, `./프로그램명`으로 실행
- `int`, `float`, `char`, `string` 등 다양한 타입이 있으며 변수 선언 시 타입 지정이 필요

---

## 📘 CS50 Week 1 공식 요약

### 🖥️ Visual Studio Code & 터미널

- `code hello.c`: VS Code로 파일 열기
- `make hello`: hello.c를 컴파일하여 실행 파일 생성
- `./hello`: 프로그램 실행
- `ls`, `cd`, `pwd`, `mkdir`, `rm`, `cp`, `mv`: 기본 명령어 숙지

# 📘 CS50 2025 Week 1 학습 정리

## 💻 C 언어 기초 문법

- 프로그램은 `main` 함수에서 시작
```c
int main(void) {
    // 코드
}

printf("Hello, %s\n", name);

string name = get_string("Name? "); // cs50.h 필요
```

# 📘 CS50 Week 1 실습 문제 풀이

이 문서는 CS50 2025 1주차 강의 내용을 바탕으로  
기본 C 문법을 연습한 실습 문제(입출력, 변수, 함수 등)의 풀이 내용을 정리한 문서입니다.

---

## ✅ 문제 1: 사용자 이름을 입력받고 인사 출력

### 🔴 원래 코드
```c
string name = get_string("What your name?");

void main()
{
    printf("Hello,", "%s|n", name);
}

```
### 수정된 코드
```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
  string name = get_string("What your name?");
  printf("Hello, %s", name);
}
```

## ✅ 문제 2: 두 정수를 입력받아 합 출력

### 원래 코드
```c
int x = get_int("x의 값");
int y = get_int("y의 값);
int value = x + y;

void main()
{
    printf("x + y =", "%i|n", value);
}
```

### 수정된 코드
```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
  int x = get_int("x의 값: ");
  int y = get_int("y의 값: ");
  int value = x + y;

  printf("x + y = %i", value);
}
```

## ✅ 문제 3: 초기화되지 않은 변수 출력

### 원래 코드
```c
int main(void) {
    int x;
    printf("x의 값은",  "%i입니다.\n", x);
}

```

### 수정된 코드
```c
#include <stdio.h>

int main(void) {
    int x = 5;
    printf("x의 값은 %i입니다.\n", x);
}

or

#include <cs50.h>
#include <stdio.h>

int main(void)
{
  int x = get_int("x의 값: ");

  printf("x의 값은 %i입니다", x);
}
```

## 문제 4: 첫 번째 C 프로그램 출력

### 원래 코드
```c
printf("나의 첫 번째 C 프로그램입니다.");
```

### 수정된 코드
```c
#include <stdio.h>

int main(void)
{
  printf("나의 첫 번째 C 프로그램입니다.\n");
}
```
