# 1. 함수 (Function)

## 핵심 정리

- `def`로 정의
- 호출해야 실행됨
- return 없으면 `None`
- 매개변수 vs 인자 구분 중요

---

## 예제 코드

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

---

## 문제

1. 함수 정의 키워드는?
2. return이 없으면 반환값은?
3. 다음 결과는?

```python
def f(x):
    print(x)

print(f(10))
```

---

# 2. 람다 함수 (lambda)

## 핵심 정리

- 한 줄 함수
- 이름 없음
- 자동 return

---

## 예제 코드

```python
square = lambda x: x * x
print(square(5))
```

---

## 문제

1. 람다 함수 특징 2가지
2. 다음 결과는?

```python
(lambda x: x + 1)(10)
```

---

# 3. 내장 함수

## 핵심 정리

- 이미 만들어진 함수
- 자주 쓰는 것:
  - `abs`, `pow`, `round`, `divmod`
  - `min`, `max`, `sum`

---

## 예제 코드

```python
print(abs(-5))
print(pow(2, 3))
print(divmod(10, 3))
```

---

## 문제

1. 절댓값 함수는?
2. `divmod(9,2)` 결과는?

---

# 4. 정렬 & 반복 관련 함수

## 핵심 정리

- `sorted()` → 정렬
- `reversed()` → 뒤집기
- `key`로 기준 변경 가능

---

## 예제 코드

```python
words = ["apple", "kiwi", "banana"]

print(sorted(words))
print(sorted(words, key=len))
```

---

## 문제

1. 내림차순 정렬 방법은?
2. 길이 기준 정렬 시 사용하는 옵션은?

---

# 5. all / any

## 핵심 정리

- `all()` → 모두 True
- `any()` → 하나라도 True

---

## 예제 코드

```python
print(all([1, 2, 3]))     # True
print(any([0, 0, 1]))     # True
```

---

## 문제

1. `all([0,1])` 결과는?
2. `any([0,0])` 결과는?

---

# 6. 조건문 if

## 핵심 정리

- if / else / elif
- 조건은 True/False

---

## 예제 코드

```python
x = 10

if x > 0:
    print("양수")
elif x == 0:
    print("0")
else:
    print("음수")
```

---

## 문제

1. elif는 몇 개까지 가능?
2. 다음 결과는?

```python
x = -1
if x > 0:
    print("A")
else:
    print("B")
```

---

# 7. 한 줄 if (삼항 연산자)

## 핵심 정리

- `A if 조건 else B`

---

## 예제 코드

```python
x = 5
result = "짝수" if x % 2 == 0 else "홀수"
print(result)
```

---

## 문제

1. 다음 결과는?

```python
x = 4
print("YES" if x > 5 else "NO")
```

---

# 8. for 반복문

## 핵심 정리

- 컬렉션 순회
- 문자열, 리스트 등 가능

---

## 예제 코드

```python
for ch in "python":
    print(ch)
```

---

## 문제

1. for문에서 사용할 수 있는 자료형 2개
2. 위 코드 출력 순서는?

---

# 9. range()

## 핵심 정리

- `range(start, stop, step)`
- stop은 포함 안됨

---

## 예제 코드

```python
for i in range(1, 6):
    print(i)
```

---

## 문제

1. `range(3)` 결과 리스트는?
2. 다음 결과는?

```python
list(range(2, 10, 3))
```

---

# 10. while 반복문

## 핵심 정리

- 조건이 True 동안 반복
- 횟수 모를 때 사용

---

## 예제 코드

```python
i = 1
while i <= 3:
    print(i)
    i += 1
```

---

## 문제

1. while 종료 조건은?
2. 무한루프 조건은?

---

# 11. break / continue

## 핵심 정리

- break → 반복 종료
- continue → 다음 반복

---

## 예제 코드

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

---

## 문제

1. break 역할은?
2. continue는 무엇을 건너뛰는가?

---

# 12. 중첩 반복 (구구단)

## 핵심 정리

- 반복문 안에 반복문

---

## 예제 코드

```python
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
```

---

## 문제

1. 반복문 안에 반복문을 뭐라고 하나?
2. i, j 역할은?

---

# 전체 핵심 한 줄 요약

- 함수 → 코드 재사용
- if → 조건 분기
- for → 반복 (횟수 있음)
- while → 반복 (조건 기반)
- break/continue → 흐름 제어
