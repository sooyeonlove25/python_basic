text01 = "문자열"
print(text01)
text02 = '문자열'
print(text02)
text03 = " sunny's "
print(text03)
text04 = '"sunny" is '
print(text04)
text05 = '''첫번째 줄
두번째줄'''
print(text05)

'''
첫번째 줄
두번째 줄
세번째 줄
'''

text06 = '첫줄 \n두번째'
print(text06)

print(text01 + text03)
# print(text04 + 3)
# str 숫자는 + 안됨

print(text04 * 2)
# 문자를 몇번 곱할 것인지

print(len(text01))

a = "Life is too short, You need Python"
print(a[0])
print(a[33])
print(a[-1])
print(a[19:22])
# a = "Pithon"
# a[1] = 'y'
# print(a)

data1 = "I eat %d apples. %s"
print(data1 % (3,"ggg"))

num01 = 1
text01 = "I eat {0} apples {1}"
# text01 = "I eat {} apples {}" -> 생략하면 순서대로 도출출
print(text01.format(3, 'ggg'))

num01 = 1
text01 = "I eat {0} apples {1}"
print(text01.format(3, text03))

num01 = 1
text01 = "I eat {:<20} apples {}"
print(text01.format(3, text03))

num01 = 1
text01 = "I eat {:0.2f} apples {}"
print(text01.format(3, text03))

num01 = 1
txt02 = "I eat {:,.2f} apples {}"
print(txt02.format(300000, text03))

# name = "홍길동"
# age = 24
# txt03 = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
# print(txt03)

name = "홍길동"
age = 24
txt03 = f'나의 이름은 {name:^20}입니다. 나이는 {age:.2f}입니다.'
print(txt03)
