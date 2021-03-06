# -*- coding:utf-8 -*- 

def coffee(cups, money):
    # 잔돈 계산
    # prn 호출(커피 잔 수, 잔돈)
    change = money - cups * 300
    if change >= 0:
        prn(cups, change)
    else:
        prn()
        
    
def prn(cups=0, change=0):      #기본값을 지정해줄 수 있다.
    # 출력
    # 커피 x 잔이 나왓습니다. 잔돈은 y원 입니다.
    # 돈이 부족합니다.
    if cups == 0 & change == 0:
        print('돈이 부족합니다')
    else:
        print('커피 {}잔이 나왔습니다. 잔돈은 {}원 입니다'.format(cups, change))
    
def start():
    # 커피 잔 수 입력
    # 돈 입력
    # coffee함수에 잔수와 돈 전달하면서 호출
    cups = int(input('주문할 커피 개수를 입력해주세요'))
    money = int(input('지불할 금액을 입력해주세요 (1잔에 300원)'))
    coffee(cups, money)

if __name__ == '__main__':
    start()