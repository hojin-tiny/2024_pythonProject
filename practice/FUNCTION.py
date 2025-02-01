## 함수 사용방법


def warm_up():
    print("음료를 데웁니다.")


def add_ice():
    print("얼음을 넣습니다.")


def add_esspresso():
    print("espresso를 넣습니다.")


def add_water():
    print("물을 넣습니다.")


def add_milk():
    print("우유를 넣습니다.")


def add_cocoa():
    print("코코아를 넣습니다")


user_input = input("주문을 입력하세요:")

if user_input == "에스프레소":
    add_esspresso()

if user_input == "아이스 아메리카노":
    add_ice()
    add_water()
    add_esspresso()

if user_input == "핫 모카라떼":
    add_milk()
    warm_up()
    add_esspresso()
    add_cocoa()

if user_input == "아이스 라떼":
    add_ice()
    add_milk()
    add_esspresso()
    add_cocoa()

if user_input == "아이스 코코아":
    add_ice()
    add_milk()
    add_cocoa()\


    X = 0
    Y = 0

    '''
    X가 2고, Y가 0일때 예상 출력 결과:
    ############
    #**********#
    #**********#
    #**********#
    #**********#
    #**********#
    #**********#
    #**********#
    #**********#
    #**********#
    #**@*******#
    ############
    '''


    def print_map():
        for i in range(1, 10):
            print("")


    user_input = ""

    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    valid_inputs = ["EXIT"] + directions

    while user_input != "EXIT":
        user_input = ""  # user_input 초기화
        while user_input not in valid_inputs:
            user_input = input("움직일 방향을 입력하세요 (종료는 EXIT) :: ")

        if user_input in directions:
            index = directions.index(user_input)

            tmpX = X + dx[index]
            if tmpX > 10 or tmpX < 0:
                print("map의 범위를 벗어날 수 없습니다.")
            else:
                X = tmpX

            tmpY = Y + dy[index]
            if tmpY > 10 or tmpY < 0:
                print("map의 범위를 벗어날 수 없습니다.")
            else:
                Y = tmpY

        print_map()

    print("프로그램을 종료합니다.")