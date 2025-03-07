# 주민등록번호 입력을 받아서 다음을 출력합니다.
# 성별(남자, 여자)
# 생년월일(00년 00월 00일생)
# 뒷자리 숫자 첫글자는 그대로 나머지는 *로 변경해서 출력
# 입력시 글자 앞,뒤로 공백이 포함될 수 있습니다. 공백에 대한 처리도 하세요


# 1. 주민번호 등록

# 주민등록번호는 "******-*******"의 형식으로 입력
# 입력받은 값을 .strip() 로 공백 처리
# input()으로 "주민등록번호를 입력하세요 >>>" 프롬프트 입력 후 받은 값은 number 변수로 저장
# 하이픈이 없으면 오류 -> print('값 1인지 확인', number.count('-'))


# 2. 성별 확인

# index[8]를 활용해서 도출한 값 gender 변수로 저장. -> X
# gender 변수값은 ‘1,2,3,4’만 가능
# print('값이1,3이면 남자 2,4이면 여자',gender)

# +쳇지피티 
# 성별을 나타내는 7번째 자리 숫자 추출
# gender_number = int(a[7])  # 7번째 자리 숫자를 추출하여 정수로 변환

# 성별을 인덱스로 판단 (0 -> 여자, 1 -> 남자)
# gender = ["여자", "남자"]

# gender_digit이 1 또는 3이면 남자, 2 또는 4이면 여자
# print(gender[gender_number % 2])


# 3. 생년월일 

# number[:6]로 생년월일 슬라이싱하여 birth_data 이름으로 변수 저장
# 생년월일 추출 (number[:6]에서 년, 월, 일 구하기) -> birth_data = number[:6]  # 주민등록번호 앞 6자리 (년, 월, 일)
# a = birth_data[:2] 
# b = birth_data[2:4] 
# c = birth_data[4:6]
# 생년월일 출력하기 print(birth_date = f"{a}년 {b}월 {c}일생")


# 4. 뒷자리 * 변경

# *로 변경할 뒷자리 변수를  back_number로 저장 
# back_number = print(number[8:])
# privacy = number.replace(“back_number”, “******”)
# privacy 값을 print()를 이용하여 출력


# number=input('주민등록번호를 입력하세요 >>> ')
# number.strip()
# print(number.count('-'))
# birth_data = number[:6]
# a = birth_data[:2] 
# b = birth_data[2:4] 
# c = birth_data[4:6]
# print(f"birth_data: {a}년 {b}월 {c}일생")
# gender_number = int(a[7])
# gender = ["여자", "남자"]
# print(gender[gender_number % 2])


# number=input('주민등록번호를 입력하세요 >>> ')
# number.strip()
# print(number.count('-'))
# gender = int(number[7])
# gender = ["여자", "남자"]
# print(gender[gender_number % 2])
# birth_data = number[:6]
# a = birth_data[:2] 
# b = birth_data[2:4] 
# c = birth_data[4:6]
# print(f"birth_data: {a}년 {b}월 {c}일생")
# print(birth_date)
# back_number = number[8:]
# masked = number.replace(back_number, "******")
# print(masked)

number =input('주민등록번호를 입력하세요 >>> ')
number.strip()
print(number.count('-'))
gender = number[7]
print(gender)
gender_int = int(gender)
print("남자는 '1', 여자는 '0' >>>", gender_int %2)
birth_data = number[:6]
print(birth_data)
a = birth_data[:2]
b = birth_data[2:4]
c = birth_data[4:6]
birth = f"{a}년 {b}월 {c}일생"
print(birth)
back = number[8:]
print(back)
masked = number.replace(back, '*******')
print(masked)