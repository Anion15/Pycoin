import numpy as np
import matplotlib.pyplot as plt
import math
import time
              
턴수 = int(input('턴 수 : '))
turn = 0                          
시작주가 = int(input('시작 주가 : ')) 
stock = 시작주가
stock_record = [시작주가]
돈 = 1000000
처음시작한돈 = 돈
처음갖고있는돈 = 돈
지금갖고있는주식 = 0
합 = 0
질문 = 0

print()
print()
print()
print("made whit python")
print("(pycoin_start!)")
print()

for a in range(턴수) :         
  turn = turn + 1              
  up_down_range = np.random.rand()
  if up_down_range < 0.2 :
    stock_up_down = np.random.randint(-30000, -6999)
  elif up_down_range >= 0.2 and up_down_range <= 0.78 :
    stock_up_down = np.random.randint(-7000, 7001)
  elif up_down_range > 0.78 and up_down_range <= 0.79 :
    stock_up_down = np.random.randint(stock * 0.2, stock * 0.4)
  elif up_down_range > 0.79 and up_down_range <= 0.8 and stock >= 120000 :
    stock_up_down = np.random.randint(-stock * 0.4 , -stock * 0.1)
  else :
    stock_up_down = np.random.randint(7001, 30001)
  if stock + stock_up_down <= 0 :
    stock_up_down = abs(stock_up_down)
    stock = stock + stock_up_down
  else :
    stock = max(1, stock + stock_up_down)
  stock_record.append(stock)


  plt.plot(stock_record)
  plt.xlabel('turn')
  plt.ylabel('stock')
  plt.grid(True)
  현재주가 = int(stock)
  print('')
  print(str(turn) + '번째 턴 ')
  plt.show()
  print('주가 변동 : ' + str(stock_up_down) + '원')
  print('현재 주가 : ' + str(stock) + '원')
  print('')
  
  질문 = input('이 주식을 사시겠습니까? : ')
  
  if 질문 == "y" or 질문 == "Y" or 질문 == "네" or 질문 == "yes" or 질문 == "Yes" or 질문 == "ㅇ" :
    
    질문 = input('얼마나 사시겠습니까? : ')

    
    if int(질문) * int(현재주가) <= 돈 :
    
          지금갖고있는주식 = 지금갖고있는주식 + int(질문)
          빼기 = int(질문) * 현재주가
          돈 -= int(질문) * 현재주가
          print("")
          print()
          print("구매 후 남은 돈 : " + str(돈) + "원")
          print("현재 가지고 있는 주식 : " + str(지금갖고있는주식) + "개")
          time.sleep(2)
    
    else:

      print("현재 소지하고 있는 돈의 양보다 더 많이 선택하셨습니다. (결재 불가)")    

  print("")
  
  
  질문 = input('이 주식을 파시겠습니까? : ')
  if 질문 == "y" or 질문 == "Y" or 질문 == "네" or 질문 == "yes" or 질문 == "Yes" or 질문 == "ㅇ" :
    
    질문 = int(input('얼마나 파시겠습니까? : '))

    
    if 지금갖고있는주식 == 0 :
      
      print("현재 소지하고 있는 주식이 없습니다. (판매 불가)")
          
    
    else:
 
      돈 += int(질문) * 현재주가
      지금갖고있는주식 = 지금갖고있는주식 - (질문)
      print("")
      print()
      print("정상적으로 판매가 되었습니다. (판매 완료)")
      print("판매 후 남은 돈 : " + str(돈) + "원")
      print("현재 가지고 있는 주식 : " + str(지금갖고있는주식) + "개")
      time.sleep(2)
  print("")
      





  print('---------------------------------------------------------------------')
print()
print()
print()
print()
print()
print("총 소지 금액: " + str(돈))
print("총 소지하고 있는 주식의 개 수 : " + str(지금갖고있는주식) + "개")
print("pycoin이 종료 되었습니다.")
#2023/4/13
print()
print()
