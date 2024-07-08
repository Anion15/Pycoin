import math
import time

try:
    import numpy as np
except ModuleNotFoundError:
    print("모듈을 찾을 수 없습니다. 'numpy'가 설치되어 있는지 확인하세요.")
    while True:
        pass      

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("모듈을 찾을 수 없습니다. 'matplotlib.pyplot'가 설치되어 있는지 확인하세요.")
    while True:
        pass

턴수 = int(input('턴 수 : '))
turn = 0                          
시작주가 = int(input('시작 주가 : ')) 
stock = 시작주가
stock_record = [시작주가]
돈 = 1000000
처음시작한돈 = 돈
지금갖고있는주식 = 0

print("\n\n\nmade with python")
print("(pycoin_start!)\n")
print("그래프창을 닫으면 이어서 동작합니다.")

for _ in range(턴수):
    turn += 1
    up_down_range = np.random.rand()
    if up_down_range < 0.2:
        stock_up_down = np.random.randint(-30000, -6999)
    elif 0.2 <= up_down_range <= 0.78:
        stock_up_down = np.random.randint(-7000, 7001)
    elif 0.78 < up_down_range <= 0.79:
        stock_up_down = np.random.randint(stock * 0.2, stock * 0.4)
    elif 0.79 < up_down_range <= 0.8 and stock >= 120000:
        stock_up_down = np.random.randint(-stock * 0.4, -stock * 0.1)
    else:
        stock_up_down = np.random.randint(7001, 30001)

    if stock + stock_up_down <= 0:
        stock_up_down = abs(stock_up_down)
    stock = max(1, stock + stock_up_down)
    stock_record.append(stock)

    plt.plot(stock_record)
    plt.xlabel('turn')
    plt.ylabel('stock')
    plt.grid(True)
    plt.show()

    현재주가 = int(stock)
    print(f'\n{turn}번째 턴')
    print(f'주가 변동 : {stock_up_down}원')
    print(f'현재 주가 : {stock}원\n')

    질문 = input('이 주식을 사시겠습니까? : ')
    if 질문.lower() in ["y", "네", "yes", "ㅇ"]:
        질문 = int(input('얼마나 사시겠습니까? : '))
        if 질문 * 현재주가 <= 돈:
            지금갖고있는주식 += 질문
            돈 -= 질문 * 현재주가
            print(f"\n\n구매 후 남은 돈 : {돈}원")
            print(f"현재 가지고 있는 주식 : {지금갖고있는주식}개")
            time.sleep(2)
        else:
            print("현재 소지하고 있는 돈의 양보다 더 많이 선택하셨습니다. (결재 불가)")    

    print("")
  
    질문 = input('이 주식을 파시겠습니까? : ')
    if 질문.lower() in ["y", "네", "yes", "ㅇ"]:
        질문 = int(input('얼마나 파시겠습니까? : '))
        if 지금갖고있는주식 == 0:
            print("현재 소지하고 있는 주식이 없습니다. (판매 불가)")
        else:
            돈 += 질문 * 현재주가
            지금갖고있는주식 -= 질문
            print(f"\n\n정상적으로 판매가 되었습니다. (판매 완료)")
            print(f"판매 후 남은 돈 : {돈}원")
            print(f"현재 가지고 있는 주식 : {지금갖고있는주식}개")
            time.sleep(2)
    print("\n---------------------------------------------------------------------")

print(f"\n\n\n총 소지 금액: {돈}")
print(f"총 소지하고 있는 주식의 개수: {지금갖고있는주식}개")
print("pycoin이 종료 되었습니다.\n\n")

while True:
    pass
