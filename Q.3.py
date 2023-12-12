#Q.3 행성의 나이 알파벳으로 표현하기
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    converted_age = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    if not (isinstance(age,int) and  0<age<=1000): # 자연수와 1000이하 조건 달성
        return '잘못된 입력입니다.'  
    age_str = str(age) #age를 문자형으로 저장

    answer = ''

    # 변환된 문자열을 딕셔너리의 값과 대응해서 나온 값을 모두 더해줌
    for i in age_str: 
        answer += converted_age.get(i,'') 
    return answer

planet_age= int(input ("행성의 나이를 입력해주세요: ")) # 값 입력(정수형으로 변환)
result = solution(planet_age) #PROGEAMMER-857식 나이로 변환해서 저장
print(result) #결과값 출력

