## 1부터 10까지 출력한다.

#for i in range(10):
#    print(i+1)

#print("################")

#for i in range(1,11):
#    print(i)

#print("################")
#print(list(range(1,11)))

## 여기서부터는 조건도 같이
# 369게임
# 1, 2, 짝(3)
# 1 ~100
# .include()

#for i in range(1,10):
#    if i//10 == 3 or i//10 == 6 or i//10 == 9:
#        print("짝")
#    else:
#        if i%10 == 3 or i %10 == 6 or i%10 == 9:
#            print("짝")
#        else:
#            print(i)


#for i in range(1,101):
#    clap = ""
#    if i // 10 == 3 or i // 10 == 6 or i // 10 ==9:
#        clap = clap+"짝"



#사용자한테 숫자 하나 입력
#해당 숫자의 구구단을 출력
#2를입력받으면
#2*1=2





num = int(input('숫자 하나를 입력하세요'))
for n in range(1,10):
    print(num, " * ", n, " = ", num*n)





#10개의 랜덤 알파벳을 배열로 생성
#[Q,W,A,F,S,C,G,D,E,T]
#하나씩 출력되며, 사용자가 해당 알파벳을 빠르게 입력하는 게임
#출력:Q
#사용자입력:z <-넘어가지 않음
#사용자입력:q<-다음 문제 w가 출력됨


