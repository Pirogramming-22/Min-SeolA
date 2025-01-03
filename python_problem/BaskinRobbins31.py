import random

num = 0
player = "player"

def switchPlayer():
    if player == "player":
        return "computer"
    else:
        return "player"

def gameResult(winner):
    print(winner, "win!")

def printNumbers(addNum):
    global num, player
    for i in range(addNum):
        if num + 1 + i > 31: 
            if player == "computer":
                player = switchPlayer()
                gameResult(player)
                return 
            else:
                player = switchPlayer()
                gameResult(player)
                return
        print(player, ":", num + 1 + i)
    num += addNum

def brGame():
    global num, player
    while num<31:
        if player == "player":
            try:
                addNum = int(input("부를 숫자의 개수를 입력하세요.(1, 2, 3만 입력 가능) :"))
                if addNum < 1 or addNum > 3:
                    print("1, 2, 3 중 하나를 입력하세요.\n")
                    continue
            except Exception:
                print("정수를 입력하세요.\n")
                continue
            printNumbers(addNum)
        else:
            addNum = random.randint(1, 3)
            if num + addNum > 31: 
                addNum = 31 - num
            printNumbers(addNum)

        if num >= 31:
            player = switchPlayer()
            gameResult(player)
            return
        player = switchPlayer()

brGame()
