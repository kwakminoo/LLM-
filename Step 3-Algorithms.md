CS50 X 2025 - Week 3 정리: 알고리즘(Algorithms)
===

## 주요 학습 내용

### 검색 알고리즘
#### 선형검색(Linear Serch)
- 배열을 왼쪽에서 오른쪽으로 순차적으로 탐색
- 최악의 경우, n개의 항목을 모두 확인해야 함
- 시간복잡도: **O(n)**

#### 이진 검색(Binary Serch)
- 배열이 정렬된 상태일 때만 가능
- 중간 값을 기준으로 반씩 줄여가며 검색
- 시간복잡도: **O(log n)**

### 정렬 알고리즘
#### 선택 정렬(Selection Sort)
- 가장 작은 값을 찾아 앞쪽과 교환하는 방식
- 전체 배열을 순차적으로 정렬
- 시간복잡도: **O(n²)**

#### 버블 정렬(Bubble Sort)
- 인접한 두 값을 비교하여 더 큰 값을 오른쪽으로 밀어냄
- 한 회전마다 가장 큰 값이 맨 뒤로 "버블"처럼 올라감
- 시간복잡도: **O(n²)**

#### 병합 정렬(Merge Sort)
- 배열을 반으로 계속 나눈 뒤, 다시 정렬하며 병합
- 재귀적 방식으로 작동
- 시간복잡도: **O(n log n)**
~~~C
#include <stdio.h>

void merge(int arr[], int left, int mid, int right)
{
  int n1 = mid - left + 1;
  int n2 = right - mid;

  int L[n1], R[n2];

  for(int i = 0; i < n1; i++)
  {
    L[i] = arr[left + i];
  }

  for(int j = 0; j < n2; j++)
  {
    arr[mid + 1 + j];
  }

  int i = 0;
  int j = 0;
  k = left;
  while(i < n1 && j < n2)
  {
    if(L[i] <= R[i])
    {
      arr[k++] = L[i++];
    }
    else{
      arr[k++] = R[j++];
    }
  }

  while(i < n1)
  {
    arr[k++] = L[i++];
  }
  while(j < n2)
  {
    arr[k++] = R[j++]
  }
}

void mergeSort(int arr[], int left, int right)
{
  if(left < right)
  {
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);         // 왼쪽 정렬
    mergeSort(arr, mid + 1, right);    //오른쪽 정렬
    mergeSort(arr, left, mid, right);  //병합
  }
}
~~~

### 재귀(Recursion)
- 함수가 자기 자신을 다시 호출하는 방식
- 종료 조건(base case)을 반드시 명시해야 함
  ~~~C
  void countdown(int n)
  {
    if(n <= 0)
      return;
    printf("%i\n", n);
    countdown(n - 1);
  }
  ~~~

### 빅오 표기법(Big O Notation)
| 표기       | 설명                      |
| -------- | ----------------------- |
| O(1)     | 상수 시간 - 입력 크기와 무관       |
| O(log n) | 로그 시간 - 이진 탐색처럼 절반씩 줄이기 |
| O(n)     | 선형 시간 - 입력 크기만큼 반복      |
| O(n²)    | 제곱 시간 - 중첩 반복문 구조       |

- **Ω(오메가)**: 최선의 경우
- **Θ(세타)**: 평균적인 경우
- **O(빅오)**: 최악의 경우

### 문자열 비교
- 문자열은 배열이므로 직접 비교 불가
- **strcmp()** 함수를 사용해 비교
  ~~~C
  if (strcmp(s1, s2) == 0)
  {
    // 문자열이 같다
  }
  ~~~

### 구조체(Struct)
~~~C
typedef struct
{
  string name;
  string number;
} person;
~~~
- 연관된 데이터(name, number)를 하나의 타입으로 묶어 처리할 수 있음
- 데이터베이스의 하나의 row와 비슷한 구조

### 기타 개념
- **return 0**: 프로그램 정상 종료
- **return 1**: 오류 등 비정상 종료
- 문자열은 **"HI!"** -> 실제 메모리에는 **'H', 'I', '!', '\0' (4칸)**
- 배열 전달 시 포인터(주소)만 넘겨지므로 크기 정보를 함께 전달해야 함

### 오늘의 핵심 이해
- 이진 검색은 정렬되어 있어야 하고, 로그형태로 빠르게 줄어듦
- 재귀는 코드가 간결하지만, 종료 조건이 명확 해야 함
- 정렬 알고리즘 중 병합 정렬이 가장 빠름(n log n)

## CS50 Week 3 퀴즈 복습
### 문제 1. 선형 검색과 이진 검색의 시간 복잡도는?
- 나의 답: 선형 검색 O(n) / 이진 검색 O(n²)  ❌
- 정답: 선형 검색 O(n) / 이진 검색 O(log n)
- 해설:
    1. 선형 검색은 모든 항목을 순차적으로 확인하므로 O(n)
    2. 이진 검색은 절반씩 줄여가며 탐색하므로 O(log n)
    3. O(n²)은 버블/선택 정렬의 시간복잡도
 
### 문제 2. 다음 중 정렬된 배열에서만 사용 가능한 검색 알고르짐은?
- 나의 답: 버블 정렬 ❌
- 정답: 이진 검색
- 해설:
    1. 버블 정렬은 검색이 아니라 정렬 알고리즘
    2. 이진 검색은 배열이 정렬되어 있을 때만 작동 가능
 
### 문제 3. 아래 코드를 실행했을 때 출력되는 결과는?
~~~C
int numbers[] = {1, 2, 3, 4, 5};
int n = 3;
for (int i = 0; i < 5; i++)
{
    if (numbers[i] == n)
    {
        printf("Found\n");
        break;
    }
}
~~~
- 나의 답: 4 ❌
- 정답: Found
- 해설:
    1. n == 3일 때 numbers[2] == 3이므로 Found가 출력
    2. 숫자 "4"는 결과가 아님(코드엔 printf("4)가 없음)
 
### 문제 4. 다음 중 빅오 표기법이 설명하는 것은
* A. 메모리 크기

* B. 코드 길이

* ✅ C. 알고리즘 수행 시간

- 너의 답: ✅ C
- 정답: ✅ C
- 해설:
    1. Big-O는 알고리즘의 시간/공간 복잡도를 설명하는 표기법이야.
    2. O(n), O(log n) 등으로 성능 예측 가능
