#coded by JRay 2022/12/30 

# ��ƾɤJ��
import random

# �ܼƫŧi��
i = 0 
j = 0
diff = 0 
number_of_A = 0
number_of_B = 0

# �üƲ��ͨt��
system = list(random.sample(range(0,9),4))
system = list(map(int, system))

while number_of_A != 4 :
    # ���s��z�ŧi��
    i = 0 
    j = 0
    number_of_A = 0
    number_of_B = 0


    # ��J�t��
    user = list(input("plz enter 4 number :"))
    #���q�f�l�t��
    while len(user) != 4 :
        user = list(input("plz enter 4 number :"))
    while len(set(user)) != 4:
        user = list(input("plz enter 4 number :"))
    user = list(map(int, user))


    # number_of_A �p��
    while i < 4 : 
        diff = system[i] - user[i]
        i = i + 1
        if diff == 0 :
           number_of_A = number_of_A + 1

    # number_of_B �p��
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
    

    # A&B�ƶq�����t��
    print()
    print("A :", number_of_A)
    print("B :", number_of_B - number_of_A)





