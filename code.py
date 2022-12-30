#coded by JRay 2022/12/30 

# 函數導入區
import random

# 變數宣告區
i = 0 
j = 0
diff = 0 
number_of_A = 0
number_of_B = 0

# 亂數產生系統
system = list(random.sample(range(0,9),4))
system = list(map(int, system))

while number_of_A != 4 :
    # 重新整理宣告區
    i = 0 
    j = 0
    number_of_A = 0
    number_of_B = 0


    # 輸入系統
    user = list(input("plz enter 4 number :"))
    #防叛逆子系統
    while len(user) != 4 :
        user = list(input("plz enter 4 number :"))
    while len(set(user)) != 4:
        user = list(input("plz enter 4 number :"))
    user = list(map(int, user))


    # number_of_A 計算
    while i < 4 : 
        diff = system[i] - user[i]
        i = i + 1
        if diff == 0 :
           number_of_A = number_of_A + 1

    # number_of_B 計算
    for i in user:
       for j in system:
          if(i==j):
              number_of_B = number_of_B + 1
              break

    
    # debug system
    print()
    print("debug system\n------------------------" )
    print('system :', system)
    print('user :', user)
    

    # A&B數量公布系統
    print()
    print("A :", number_of_A)
    print("B :", number_of_B - number_of_A)
print('congret !!')




