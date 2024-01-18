import random

# variables
difficulty = 4
num_A = 0
num_B = 0

#functions
def difficulty_set():
    global difficulty
    difficulty = int(input("請輸入難度(3~7) :"))
    while difficulty < 3 or difficulty > 7:
        print("!! 輸入異常 !!")
        difficulty = int(input("請輸入難度(3~7) :"))
        return difficulty
    
def answer():
    user_ans = input("請輸入"+str(difficulty)+"位不重複數字 :")
    while len(user_ans) != difficulty or len(set(user_ans)) != difficulty:
        print("!! 輸入異常 !!")
        user_ans = input("請輸入"+str(difficulty)+"位不重複數字 :")
    user_ans = list(map(int,user_ans[:]))
    return user_ans

def number_of_A(user_ans,question):
    num_A = sum(1 for q,a in zip(question,user_ans) if q == a)
    return num_A

def number_of_B(user_ans,question,num_A):
    num_B = len(set(user_ans).intersection(question)) - num_A
    return num_B

def debug():
    print('Question :', question)
    print('Answer :', user_ans)

# Create question
difficulty_set()
question = list(map(int,(random.sample(range(0,9),difficulty))))

while num_A != difficulty:
    user_ans = answer()
    num_A = number_of_A(user_ans,question)
    num_B = number_of_B(user_ans,question,num_A)
    print('A :', num_A)
    print('B :', num_B)
    #debug()
print("恭喜答對了！")