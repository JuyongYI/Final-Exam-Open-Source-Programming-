#Q.4 두 원 사이의 공간에서 x,y 좌표가 모두 정수인 점의 개수 구하기
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    answer = 0
    #여러 개의 반환값을 받기 위해 변수 추가
    count1 = 0
    count2 = 0
    # 반지름 크기 조건
    if not (1 <= r1 < r2 <= 1000000):
        return '잘못된 숫자입니다.'
    
    # r1의 x,y좌표 범위 제한 및 조건에 만족하는 순서쌍 개수 구하기

    for x in range(1, r1 + 1):
        for y in range(1, r1 + 1):
            if x**2 + y**2 < r1**2:
                count1 += 1

    # r2의 x,y좌표 범위 제한 및 조건에 만족하는 순서쌍 개수 구하기

    for x2 in range(1, r2 + 1):
        for y2 in range(1, r2 + 1):
            if x2**2 + y2**2 <= r2**2:
                count2 += 1

    # 조건에 맞는 최종적인 값 반환

    answer = (count2 - count1) * 4 + ((r2 - r1 + 1) * 4)
    
    return answer

# 반지름 값 입력 및 결과 출력

r1_input = int(input("반지름 R1을 입력하세요: \n"))
r2_input = int(input("반지름 R2를 입력하세요: \n"))
result = solution(r1_input, r2_input)
print(result)
