#자판기 프로그램
#사용자모드/관리자모드
#사용자모드-물건 구매
#관리자모드-물건 추가, 물건 변경, 물건 삭제


'''
자판기에서 가져야할 내용들:
음료수 종류: 콜라,사이다, 초코우유, 딸기우유, 바나나 우유
가격과 결제방법 카드,현금,네이버 페이, 삼성페이 애플페이 유무등
1.사용자모드
원하는 음료수가 무엇인지 물어보기
사용자 입력 받기
입력값에 따라 음료수가 있으면 사용자에게 추가
남아있는 음료가 없으면 재고없음을 출력

2.관리자모드
음료수 종류 추가
음료수 개수 변경
음료수 가격변경

'''




# 각각의 dictionary
inventory = {'pepsi': 0, 'chill sung': 0, 'chocolate milk': 0, 'strewberry milk': 0, 'banana milk': 0}
price = {'pepsi': 1000, 'chill sung': 1000, 'chocolate milk': 2000, 'strewberry milk': 2000, 'banana milk': 2000}

mode = "manager"

def print_menu():
    print("menu를 출력합니다.")
    for i in inventory.keys():
        print(i, "가격:", price[i], " 잔여수량:", inventory[i])

def buy_drink():
    print("음료를 선택하고, 구매합니다.")

def switch_mode():
    print("모드를 전환합니다.")
    global mode
    if mode == "manager":
        mode = "user"
    else:
        mode = "manager"

def manager_login():
    print("관리자 모드 상태입니다.")
    print_function()

def print_function():
    print("관리자가 사용가능한 기능입니다.")
    print("1. 음료를 등록하기")
    print("2. 음료를 추가하기")
    print("3. 음료를 빼기")
    print("4. 음료를 삭제하기")
    print("5. 사용자 모드로 전환")
    print("6. 재고확인")

def change_price():
    print("음료의 가격을 변경합니다.")

def add_drink():
    print("음료를 추가합니다.")
    user_input =str(input("음료를 골라주세요  1:pepsi, 2:chill sung, 3:chocolate milk, 4:strewberry milk,  5:banana milk"))
    if user_input == 1:
        inventory['pepsi'] = inventory['pepsi'] + 1
    elif user_input == 2:
        inventory['chill sung'] = inventory['chill sung'] + 1
    elif user_input == 3:
        inventory['chocolate milk'] = inventory['chocolate milk'] + 1
    elif user_input == 4:
        inventory['strewberry milk'] = inventory['strewberry milk'] + 1
    elif user_input == 5:
        inventory['banana milk'] = inventory['banana milk'] + 1
#여기 애드 드링크 함수에서 딕셔너리값을 변경해도 재고확인했을때 다 0으로 뜹ㄴ디ㅏ


def register_drink():
    print("음료를 등록합니다.")

def show_menu():
    print_menu()

def delete_drink():
    print("음료를 삭제합니다.")

def extract_drink():
    print("음료를 뺍니다.")

while True:
    if mode == "manager":
        manager_login()
        user_input =int(input("메뉴를 선택하세요"))

        if user_input == 1:
            register_drink()
        elif user_input == 2:
            add_drink()
        elif user_input == 3:
            extract_drink()
        elif user_input == 4:
            delete_drink()
        elif user_input == 5:
            switch_mode()
        elif user_input == 6:
            show_menu()


    else:
        print_menu()
        user_input = input("메뉴를 선택하세요")