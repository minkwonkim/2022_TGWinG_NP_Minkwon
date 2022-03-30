# 이번 주차부터는 컴파일 에러 등으로 프로그램 자체가 실행되지 않을 시에는 과제 점수 0점 처리합니다.
# 문제에서 요구하는 입출력 외에는 절대 포함해서 제출하지 마세요. 0점 처리합니다.
# 문제에서 요구하는 출력 형식, 반환 형식을 "모두" 지켜주세요. 지키지 않으면 오답처리 됩니다.
# 한 파일에 모든 문제를 풀이해서 제출하세요. 분리 제출 시 채점자 PC기준 최상위에 정렬되는 파일만 채점합니다.
# 제출 마감일: 2022-03-29 23:59, 지각 제출 시 점수에서 20% 감점입니다.

# 문제 1번
def question1():
    return "next"

# 문제 2번
def leapYear(year):
    if(year%4==0):
        if(year%400==0):
            return print("윤년입니다.")
        elif(year%100==0):
            return print("윤년이 아닙니다.")
        else:
            return print("윤년이 입니다.")
    else:
        return print("윤년이 아닙니다.")

# 문제 3번
def alram(time):
    str_time=str(time)
    awake=int(time)-45
    str_awake=str(awake)
    if(int(str_time[-2:])<45):
        awakeminute=60+int(str_time[-2:])-45
    else:
        awakeminute=str_awake[-2:]

    if(awake<1200):
        if(awake<1000):
            print("오전 ",str_awake[:1],"시 ",awakeminute,"분",sep="")
        else:
            print("오전 ",str_awake[:2],"시 ",awakeminute,"분",sep="")
    else:
        print("오후",str_awake[:2],"시 ",awakeminute,"분",sep="")
alram(1610)

    

# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
    return
