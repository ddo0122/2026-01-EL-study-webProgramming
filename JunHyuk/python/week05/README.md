# 1. 시퀀스 연산자 (+, \*)

## 핵심 정리

- `+` → 이어붙이기
- `*` → 반복
- 문자열 / 리스트 / 튜플 모두 적용 가능

---

## 예제 코드

```python
print("hi" + "bye")      # hibye
print("py" * 3)          # pypypy

a = [1, 2]
b = [3, 4]
print(a + b)             # [1,2,3,4]
```

---

## 문제

1. `"a" * 4` 결과는?
2. `[1,2] + [3]` 결과는?
3. 튜플도 + 연산 가능한가?

---

# 2. += 동작 차이

## 핵심 정리

- 리스트: **원본 수정**
- 문자열/튜플: **새 객체 생성**

---

## 예제 코드

```python
lst = [1, 2]
lst += [3]
print(lst)   # [1,2,3]

s = "hi"
s += "!"
print(s)     # hi!
```

---

## 문제

1. 리스트는 += 시 새로운 객체인가?
2. 문자열은 += 시 어떻게 되는가?

---

# 3. 멤버십 연산자 (in, not in)

## 핵심 정리

- 포함 여부 확인
- dict는 **key 기준**

---

## 예제 코드

```python
print(3 in [1,2,3])      # True
print("a" in "apple")    # True

d = {"a": 1}
print("a" in d)          # True
```

---

## 문제

1. dict에서 in은 key 기준인가 value 기준인가?
2. `5 in range(5)` 결과는?

---

# 4. 얕은 복사 vs 깊은 복사

## 핵심 정리

- `=` → 같은 객체 (얕은 복사 느낌)
- `[:]`, `list()` → 새로운 객체 (깊은 복사)

---

## 예제 코드

```python
a = [1,2,3]
b = a

a.pop()
print(b)  # 같이 바뀜

c = a[:]
a.append(10)
print(c)  # 영향 없음
```

---

## 문제

1. `a = b`는 복사인가 공유인가?
2. 깊은 복사 방법 2개

---

# 5. is 연산자

## 핵심 정리

- 같은 객체인지 확인 (메모리 기준)

---

## 예제 코드

```python
a = [1,2]
b = a

print(a is b)  # True
```

---

## 문제

1. is는 무엇을 비교하는가?
2. 값 비교는 어떤 연산자?

---

# 6. 딕셔너리 기본

## 핵심 정리

- key : value 구조
- key는 중복 불가
- value는 중복 가능
- key는 불변 타입만 가능

---

## 예제 코드

```python
d = {"name": "Tom", "age": 20}

print(d["name"])
d["age"] = 21
```

---

## 문제

1. key로 list 사용 가능한가?
2. key 중복 가능?

---

# 7. 딕셔너리 생성

## 핵심 정리

- `{}` 또는 `dict()`
- `dict.fromkeys()` 사용 가능

---

## 예제 코드

```python
d = dict(a=1, b=2)
d2 = dict.fromkeys(["x","y"], 0)

print(d2)
```

---

## 문제

1. 빈 딕셔너리 만드는 방법 2개
2. fromkeys 역할은?

---

# 8. 딕셔너리 순회

## 핵심 정리

- `keys()`, `values()`, `items()`

---

## 예제 코드

```python
d = {"a":1, "b":2}

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)
```

---

## 문제

1. key+value 동시에 가져오는 메서드는?
2. values()는 무엇 반환?

---

# 9. 딕셔너리 조회/삭제

## 핵심 정리

- `get()` → 안전 조회
- `pop()` → 삭제 + 반환
- `clear()` → 전체 삭제

---

## 예제 코드

```python
d = {"a":1}

print(d.get("b"))      # None
d.pop("a")
```

---

## 문제

1. 없는 key 접근 시 안전한 함수는?
2. pop의 역할은?

---

# 10. 딕셔너리 추가/병합

## 핵심 정리

- `update()` → 병합
- 동일 key는 덮어쓰기

---

## 예제 코드

```python
a = {"x":1}
b = {"x":2, "y":3}

a.update(b)
print(a)
```

---

## 문제

1. update 시 key 겹치면?
2. 딕셔너리 길이 구하는 함수?

---

# 11. 집합 (set)

## 핵심 정리

- 중복 X, 순서 X
- mutable
- 요소는 immutable만 가능

---

## 예제 코드

```python
s = {1,2,2,3}
print(s)  # {1,2,3}
```

---

## 문제

1. set은 순서 있는가?
2. list를 set 요소로 넣을 수 있는가?

---

# 12. 집합 생성

## 핵심 정리

- `set()` 사용
- `{}`는 dict임 (주의)

---

## 예제 코드

```python
s = set([1,2,2,3])
print(s)
```

---

## 문제

1. 공집합 만드는 방법은?
2. `{}`는 무엇인가?

---

# 13. 집합 연산

## 핵심 정리

- 합집합: `|`
- 교집합: `&`
- 차집합: `-`
- 대칭차: `^`

---

## 예제 코드

```python
A = {1,2,3}
B = {3,4}

print(A | B)
print(A & B)
print(A - B)
```

---

## 문제

1. 교집합 연산자는?
2. `A ^ B` 의미는?

---

# 14. 집합 메서드

## 핵심 정리

- `add`, `remove`, `discard`
- `remove` → 에러 발생
- `discard` → 에러 없음

---

## 예제 코드

```python
s = {1,2}

s.add(3)
s.remove(2)
s.discard(10)
```

---

## 문제

1. remove vs discard 차이
2. pop()은 무엇 삭제?

---

# 15. frozenset

## 핵심 정리

- set의 **불변 버전**
- dict key로 사용 가능

---

## 예제 코드

```python
fs = frozenset([1,2,3])
```

---

## 문제

1. frozenset 특징 1개
2. 왜 dict key로 사용 가능한가?

---

# 전체 핵심 요약

- +, \* → 시퀀스 연산
- 복사 → 얕은 vs 깊은
- dict → key-value 핵심
- set → 중복 제거 + 집합 연산
