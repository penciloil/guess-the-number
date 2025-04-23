import random  # 匯入 random 模組，用來產生隨機數字

# 顯示 ASCII 藝術字與歡迎訊息
print("""
  __                                                         
 /__      _   _  _   _|_ |_   _    |\ |     ._ _  |_   _  ._ 
 \_| |_| (/_ _> _>    |_ | | (/_   | \| |_| | | | |_) (/_ |  

""")
print("Welcome to the Number Guessing Game!")  # 顯示歡迎訊息
print("I'm thinking of a number between 1 and 100.")  # 提示數字範圍

number = random.randint(1, 100)  # 隨機產生 1 到 100 的整數作為答案

level = input("Choose a difficulty. Type 'easy' or 'hard': ")  # 讓玩家選擇難度

# 遊戲主程式
def play_game():
    if level == "easy":
        attempts = 10  # easy 模式有 10 次機會
        print("You have 10 attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        while attempts > 0:
            guess = int(guess)
            if guess == number:
                print(f"You got it! The answer was {number}.")  # 猜對了
                break
            elif guess > number:
                print("Too high.")  # 猜太大
            else:
                print("Too low.")  # 猜太小

            attempts -= 1  # 次數減少
            if attempts > 0:
                print(f"You have {attempts} attempts remaining.")  # 顯示剩餘次數
                guess = input("Make a guess: ")
            else:
                print(f"You've run out of guesses. The number was {number}.")  # 猜完了還沒中

    elif level == "hard":
        attempts = 5  # hard 模式有 5 次機會
        print("You have 5 attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        while attempts > 0:
            guess = int(guess)
            if guess == number:
                print(f"You got it! The answer was {number}.")  # 猜對了
                break
            elif guess > number:
                print("Too high.")  # 猜太大
            else:
                print("Too low.")  # 猜太小

            attempts -= 1  # 次數減少
            if attempts > 0:
                print(f"You have {attempts} attempts remaining.")  # 顯示剩餘次數
                guess = input("Make a guess: ")
            else:
                print(f"You've run out of guesses. The number was {number}.")  # 猜完了還沒中

play_game()  # 呼叫主遊戲函式