# 1. 자료형 (Data Types)

## 핵심 정리

- 숫자: `int`, `float`, `complex`
- 문자열: `str`
- 논리: `bool`
- 시퀀스: `list`, `tuple`
- 매핑: `dict`
- 집합: `set`

---

## 예제 코드

```python
a = 10          # int
b = 3.14        # float
c = "hello"     # str
d = True        # bool

lst = [1, 2, 3]
tpl = (1, 2, 3)
st = {1, 2, 3}
dic = {"name": "Tom", "age": 20}

print(type(a), type(c), type(lst))
```

---

## 문제

1. 다음 중 집합형은?
   - (1) list (2) tuple (3) set (4) dict

2. 문자열 타입은 무엇인가?

3. 다음 코드 결과는?

```python
type(3.14)
```

---

# 2. 리터럴 & 진수 표현

## 핵심 정리

- 리터럴 = 코드에 직접 쓰는 값
- 진수:
  - 2진수: `0b`
  - 8진수: `0o`
  - 16진수: `0x`

---

## 예제 코드

```python
print(0b1010)  # 10
print(0o11)    # 9
print(0xff)    # 255

num = 1_000_000
print(num)
```

---

## 문제

1. `0b1001`의 10진수 값은?
2. `0xff`는 몇인가?
3. 숫자 가독성을 위해 사용하는 기호는?

---

# 3. 변수 (Variables)

## 핵심 정리

- 변수 = 값을 저장하는 공간
- 대입: `=`
- 여러 변수 동시 할당 가능

---

## 예제 코드

```python
name = "홍길동"
age = 20

x, y = 5, 10
print(x, y)
```

---

## 문제

1. 변수에 값을 넣는 연산자는?
2. 다음 코드 결과는?

```python
a, b = 1, 2
print(a + b)
```

---

# 4. 리스트 vs 튜플

## 핵심 정리

- 리스트: 수정 가능 (mutable)
- 튜플: 수정 불가능 (immutable)

---

## 예제 코드

```python
lst = [1, 2, 3]
lst.append(4)
lst[0] = 10

tpl = (1, 2, 3)
# tpl[0] = 10  # 오류
```

---

## 문제

1. 수정 가능한 자료형은?
2. 다음 코드에서 오류 발생하는 줄은?

```python
t = (1, 2, 3)
t[1] = 5
```

---

# 5. 딕셔너리 (dict)

## 핵심 정리

- key : value 구조
- key는 변경 불가능한 타입만 가능

---

## 예제 코드

```python
mart = {"라면": 1200, "과자": 1000}

print(mart["라면"])
mart["과자"] += 100

print(mart.keys())
print(mart.values())
```

---

## 문제

1. 딕셔너리에서 값을 꺼낼 때 사용하는 것은?
2. key로 사용할 수 없는 타입은?
   - (1) int (2) str (3) list (4) tuple

---

# 6. 집합 (set)

## 핵심 정리

- 중복 없음
- 순서 없음
- 인덱스 사용 불가

---

## 예제 코드

```python
s = {1, 2, 2, 3}
print(s)  # {1,2,3}

s.add(4)
```

---

## 문제

1. set에서 중복 값은 어떻게 되는가?
2. set에서 인덱스로 접근 가능한가?

---

# 7. 가변 vs 불변

## 핵심 정리

- 가변: list, dict, set
- 불변: int, str, tuple

---

## 예제 코드

```python
a = 10
b = a
a = a + 1

print(a, b)  # 11, 10
```

---

## 문제

1. int는 가변인가 불변인가?
2. 리스트는 수정 가능한가?

---

# 8. 입력 (input)

## 핵심 정리

- input() → 항상 문자열 반환
- 숫자는 변환 필요

---

## 예제 코드

```python
age = int(input("나이 입력: "))
print(age + 1)
```

---

## 문제

1. input()의 기본 반환 타입은?
2. 숫자로 바꾸는 함수는?

---

# 9. 출력 포맷

## 핵심 정리

- format()
- f-string (가장 많이 사용)
- % 방식 (구버전)

---

## 예제 코드

```python
name = "Tom"
age = 20

print("이름: {}, 나이: {}".format(name, age))
print(f"이름: {name}, 나이: {age}")
print("이름: %s, 나이: %d" % (name, age))
```

---

## 문제

1. 가장 최신 문자열 포맷 방식은?
2. 다음 코드 결과는?

```python
x = 3.14159
print(f"{x:.2f}")
```

---

# 10. math 모듈

## 핵심 정리

- 수학 계산 함수 제공
- import 필요

---

## 예제 코드

```python
import math

print(math.sqrt(16))
print(math.pow(2, 3))
print(math.pi)
```

---

## 문제

1. 제곱근 함수는?
2. 원주율 상수 이름은?

---

# 한 줄 총정리

- 자료형 → 데이터 종류
- 변수 → 값 저장
- list/dict/set → 자주 쓰임
- input → 문자열 반환
- 출력 → f-string 추천
