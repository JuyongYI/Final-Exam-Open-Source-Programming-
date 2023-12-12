#Q.1 부분 문자열인지 아닌지 확인하기
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.


 #'strung'을 'string'으로 수정, 두 매개변수는 소문자만 받음 이외의 값은 다음과 같이 리턴, 문자열 길이 제한도 둠

def solution(my_string, target):
    if any(char.isupper() for char in my_string):
        return '영소문자만 입력해주세요.' 
    if any(char.isupper() for char in target):
        return '영소문자만 입력해주세요.'
    answer = 1 if target in my_string and  1<=len(my_string)<=100 and 1<=len(target)<=100  else 0 
    return answer



# 매개변수에 입력을 받고, .lower() 함수 사용 및 입력값 할당 및 출력

my_string= input("소문자를 입력해주세요.:\n")
target = input("소문자를 입력해주세요.:\n") 
result = solution(my_string, target) 
print(result)
