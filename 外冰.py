print("이번 미니로또 숫자 맞추기 게임의 숫자 범위는 1부터 20까지 입니다.")

import random



list_number = []



for i in range(1, 7) :
    match_val = random.randrange(1, 20)
    while match_val in list_number :
        match_val = random.randrange(1, 20)
    list_number.append(match_val)
list_mynum = []

count = 0
while count < 6 :
    v_input = int(input(f'{count+1}번째 숫자 입력 >>'))

    if count == 0 :
       list_mynum.append(v_input)
       count += 1
    else :
      if v_input in list_mynum :
         print(f'{v_input}은 이미 존재합니다.')
      else :
         list_mynum.append(v_input)
         count += 1

print(list_mynum)
SetNum = set(list_number) 
Setmynum = set(list_mynum)
SetAnd = SetNum & Setmynum


if SetNum == Setmynum : #추첨번호와 내 번호가 모두 같으면 1등 
   print('1등') 
elif len(SetAnd) == 5 :
   print('2등') 
elif len(SetAnd) == 5 : #추첨번호와 내 번호의 교집합이 5개이면 3등 
   print('3등') 
elif len(SetAnd) == 4 : #추첨번호와 내 번호의 교집합이 4개면 4등 
   print('4등') 
elif len(SetAnd) == 3 : #추첨번호와 내 번호의 교집합이 3개면 5등
   print('5등') 
else :                  #나머지 경우 꽝 
   print('꽝입니다') 

print("로또번호는", list_number, "이다.")
