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
    add_cocoa()