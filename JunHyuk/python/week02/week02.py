# 예제 코드
a = 10          # int
b = 3.14        # float
c = "hello"     # str
d = True        # bool

lst = [1, 2, 3]
tpl = (1, 2, 3)
st = {1, 2, 3}
dic = {"name": "Tom", "age": 20}

print('자료형 모음')
print(type(a), type(b), type(c), type(d),'\n', type(lst), type(tpl), type(st), type(dic))
print()

print('2진수, 8진수, 16진수 예제')
print('2진수', 0b1010)  # 10
print('8진수', 0o11)    # 9
print('16진수', 0xff)    # 255
print()

num = 1_000_000
print(num)
print()

print('변수의 대입 방법')
print('name = \"홍길동\" \n age = 20')
name = "홍길동"
age = 20
print('이름: ', name, ' 나이: ', age)

print('x, y = 5, 10')
x, y = 5, 10
print(x, y)
print()

print('리스트와 튜플')
lst = [1, 2, 3]
print(lst)
lst.append(4)
lst[0] = 10
print(lst)

tpl = (1, 2, 3)
print(tpl)
# tpl[0] = 10  # 오류
print(tpl)
print()

print('딕셔너리')
mart = {"라면": 1200, "과자": 1000}
print(mart["라면"], mart["과자"])

mart["과자"] += 100
mart["과일"] = 2000

print(mart.keys())
print(mart.values())
print()

print('집합')
s = {1, 2, 2, 3}
print(s)  # {1,2,3}

s.add(4)
print(s)
print()

print('입력')
age = int(input("나이 입력: "))
print(age)
print()

print('출력 포맷')
name = "Tom"
age = 20

print("이름: {}, 나이: {}".format(name, age))
print(f"이름: {name}, 나이: {age}")
print("이름: %s, 나이: %d" % (name, age))
print()

print('math 모듈')
import math
print(math.sqrt(16))
print(math.pow(2, 3))
print(math.pi)