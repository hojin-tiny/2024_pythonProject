size = int(input("수학 시험 점수를 입력해주쇼"))
print(size)

if size <= 100:
    if size >= 90:
        print("당신은 상반입니다")
    elif size >= 70:\
        print("당신은 중반입니다")
    else:
        print("당신은 하반입니다")
else:
    print("잘못된 점수입니다")

