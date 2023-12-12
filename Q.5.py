#Q.5 리스트 안의 숫자 조합해서 가장 큰 수 만들기
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    #numbers 의 길이와 원소의 크기를 제한함
    if not (1 <= len(numbers) <= 100000):
        return 'numbers의 길이가 올바르지 않습니다.'
    elif any(not (0 <= i <= 1000) for i in numbers):
        return 'numbers 원소의 크기가 올바르지 않습니다.'
    else:
        answer = ''
        mapped_numbers = list(map(str, numbers)) #입력된 값 문자형으로 변환 및 list화
        mapped_numbers = sorted(mapped_numbers,key=lambda x : x*3, reverse=True) # 역순으로 정렬 (원소를 세번 반복하여 두 번째로 오는 숫자를 제대로 비교)
        answer = ''.join(mapped_numbers) # 리스트에 정렬된 값을 빈틈없이 연결해줌
        return answer
    

numbers_list = [8, 30, 17, 2, 23] # 입력 값


result = solution(numbers_list) #결과 반환
print(result) #결과 출력

