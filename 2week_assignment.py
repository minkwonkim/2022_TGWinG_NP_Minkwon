# 문제 1번
def sum(a,b):
    # your code
    return a+b

# 문제 2번
def sub(a,b):
    # your code
    return a-b

# 문제 3번
def mul(a,b):
    # your code
    return a*b

# 문제 4번
def div(a,b):
    # your code
    return a/b

# 문제 5번
def distance(x1,y1,x2,y2):
    # your code
    return ((x1-x2)**2+(y1-y2)**2)**0.5

# 문제 6번
def short():
    lylic = "life is short art is long"
    # your code
    return lylic[0:24]

# 문제 7번
def myReverse(string):
    
    String = "kimminkwon";
    print(String[::-1])

    return 

# 문제 8번
def letMeIntroduceMyself():
a=input("이름을 입력하시오: ")
b=input("취미를 입력하시오: ")
c=input("재학 중인 대학을 입력하시오: ")
d=input("생일을 입력하시오(예시: 981224): ")

e=d[2:4]
f=d[4:6]

introduce = "제 이름은 {0}입니다. 제 취미는 {1}이구요. 저는 {2}를 다니고 있습니다. 제 생일은 {3}월 {4}일 입니다.".format(a,b,c,e,f)
print(introduce)

    return 

# 문제 9번
# def calcAI():
   a=int(input("첫 번째 숫자를 입력하시오: "))
   b=int(input("두 번째 숫자를 입력하시오: "))
   c=a+b
   sum = "두수의 합은 {0}입니다.".format(c)
   print(sum)

   return 