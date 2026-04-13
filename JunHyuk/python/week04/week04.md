# 1. 문자열 (String)

## 핵심 정리

- `' '` 또는 `" "` 사용
- 여러 줄: `''' '''` 또는 `""" """`
- 문자열은 **불변(immutable)**

---

## 예제 코드

```python
s1 = "hello"
s2 = 'world'
s3 = """multi
line"""

print(s1 + s2)
```

---

## 문제

1. 문자열 여러 줄 표현 방법은?
2. 문자열 수정 가능한가?
3. 다음 결과는?

```python
"hi" * 3
```

---

# 2. 문자열 기본 함수 (str, len, ord, chr)

## 핵심 정리

- `str()` → 문자열 변환
- `len()` → 길이
- `ord()` → 문자 → 숫자
- `chr()` → 숫자 → 문자

---

## 예제 코드

```python
print(len("python"))   # 6
print(ord('A'))        # 65
print(chr(65))         # A
```

---

## 문제

1. `"abc"` 길이는?
2. `ord('a')` 값은?
3. `chr(97)` 결과는?

---

# 3. 이스케이프 시퀀스

## 핵심 정리

- `\n` 줄바꿈
- `\t` 탭
- `\\` 백슬래시

---

## 예제 코드

```python
print("Hello\nWorld")
print("A\tB")
```

---

## 문제

1. 줄바꿈 기호는?
2. 탭 기호는?

---

# 4. 문자열 메서드 (핵심)

## 핵심 정리

- `split()` → 나누기
- `join()` → 합치기
- `replace()` → 바꾸기
- `count()` → 개수
- `find()` → 위치

---

## 예제 코드

```python
s = "a b c"

print(s.split())
print("-".join(["a", "b", "c"]))
print("hello".replace("l", "x"))
```

---

## 문제

1. 문자열 나누는 함수는?
2. `"a,b,c".split(",")` 결과는?
3. `"hello".count("l")` 결과는?

---

# 5. 문자열 변환 메서드

## 핵심 정리

- `upper()` / `lower()`
- `swapcase()`
- `title()`

---

## 예제 코드

```python
s = "PyThOn"

print(s.upper())
print(s.lower())
print(s.swapcase())
```

---

## 문제

1. 모두 대문자로 바꾸는 함수는?
2. `"abc".upper()` 결과는?

---

# 6. 문자열 정렬/정리

## 핵심 정리

- `strip()` → 공백 제거
- `center()`, `ljust()`, `rjust()`

---

## 예제 코드

```python
s = "  hello  "

print(s.strip())
print("hi".center(10, "-"))
```

---

## 문제

1. 양쪽 공백 제거 함수는?
2. `"hi".center(6,"*")` 결과는?

---

# 7. 리스트 (List)

## 핵심 정리

- 순서 O, 중복 O
- 수정 가능 (mutable)

---

## 예제 코드

```python
lst = [1, 2, 3]

lst.append(4)
lst.insert(1, 10)

print(lst)
```

---

## 문제

1. 리스트는 수정 가능한가?
2. 마지막에 추가하는 함수는?

---

# 8. 리스트 삭제

## 핵심 정리

- `remove()` → 값 삭제
- `pop()` → 인덱스 삭제
- `del` → 직접 삭제

---

## 예제 코드

```python
lst = [1, 2, 3]

lst.remove(2)
lst.pop()
del lst[0]

print(lst)
```

---

## 문제

1. 값 기준 삭제 함수는?
2. 마지막 요소 삭제 함수는?

---

# 9. 튜플 (Tuple)

## 핵심 정리

- 수정 불가능 (immutable)
- 빠름
- dict key로 사용 가능

---

## 예제 코드

```python
tpl = (1, 2, 3)

# tpl[0] = 10 → 오류
```

---

## 문제

1. 튜플은 수정 가능한가?
2. 튜플과 리스트 차이 1개

---

# 10. 튜플 패킹 / 언패킹

## 핵심 정리

- 패킹: 여러 값 → 하나
- 언패킹: 하나 → 여러 변수

---

## 예제 코드

```python
a = (1, 2, 3)   # 패킹

x, y, z = a     # 언패킹
print(x, y, z)
```

---

## 문제

1. 언패킹이란?
2. 다음 결과는?

```python
a, b = (10, 20)
print(a)
```

---

# 11. 인덱싱 (Indexing)

## 핵심 정리

- 0부터 시작
- 음수 가능 (`-1` 마지막)

---

## 예제 코드

```python
s = "python"

print(s[0])
print(s[-1])
```

---

## 문제

1. 첫 번째 인덱스는?
2. 마지막 인덱스는?

---

# 12. 슬라이싱 (Slicing)

## 핵심 정리

- `start:stop:step`
- stop은 포함 안됨

---

## 예제 코드

```python
s = "python"

print(s[1:4])   # yth
print(s[:3])    # pyt
print(s[::2])   # pto
```

---

## 문제

1. `"python"[1:4]` 결과는?
2. `"python"[::2]` 결과는?

---

# 13. 리스트 슬라이싱 수정

## 핵심 정리

- 슬라이싱으로 값 변경 가능

---

## 예제 코드

```python
lst = [1, 2, 3, 4]

lst[1:3] = [10, 20]
print(lst)
```

---

## 문제

1. 리스트 슬라이싱으로 수정 가능한가?
2. 위 코드 결과는?

---

# 14. bytes / bytearray (심화)

## 핵심 정리

- bytes → 불변
- bytearray → 가변

---

## 예제 코드

```python
b = bytearray(b"abc")
b[0] = ord('A')

print(b)
```

---

## 문제

1. bytes는 수정 가능한가?
2. bytearray 특징은?

---

# 전체 핵심 요약

- 문자열 → 불변
- 리스트 → 수정 가능
- 튜플 → 수정 불가
- 인덱스 → 하나 접근
- 슬라이싱 → 여러 개 접근
