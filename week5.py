# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 입력을 요구하는 문제가 없습니다.
# result 변수를 사용하여 문제를 풀이하세요. 반환값은 result 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 12일 23시 59분.
# 지각 제출 기한: 2022년 4월 13일 23시 59분. 주차 점수에서 20% 감점

import math

def calcCircleArea(r):
    result = float(math.pi*math.pow(float(r),2))
    return round(result,2)
def calcLog(a, b):
    result = float(math.log(float(b),float(a)))
    return round(result,2)
def calcSin(x):
    result = float(math.sin(float(x)))
    return round(result,2)
def calcFactorial(x):
    result = int(math.factorial(int(x)))
    return round(result,2)
def calcCombination(n, r):
    result = int(math.comb(int(n),int(r)))
    return result

def calculator(order):
    command=order.split(" ")
    if(command[0]=="원넓이:"):
        answer=calcCircleArea(command[1])
    elif(command[0]=="로그:"):
        if(command[1]=="e"):
            answer=round(math.log(float(command[2])),2)
        else:
            answer=calcLog(command[1], command[2])
    elif(command[0]=="사인:"):
        answer=calcSin(command[1])
    elif(command[0]=="팩토리얼:"):
        answer=calcFactorial(command[1])
    elif(command[0]=="조합:"):
        answer=calcCombination(command[1], command[2])
    
    return answer

print(calculator("원넓이: 10"))
print(calculator("로그: e 10"))
print(calculator("사인: 100"))
print(calculator("팩토리얼: 5"))
print(calculator("조합: 3 2"))