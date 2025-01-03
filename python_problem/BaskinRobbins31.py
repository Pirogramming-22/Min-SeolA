num=0
player="playerA"

def switchPlayer():
    if (player=="playerA"):
        return ("playerB")
    else:
        return("playerA")

def gameResult(player):
    print(player, "win!")
    
def brGame():
    global num, player
    while True:
        try:
            addNum=int(input("부를 숫자의 개수를 입력하세요.(1, 2, 3만 입력 가능) :"))
            if (addNum<1 or addNum>3):
                print("1, 2, 3 중 하나를 입력하세요.\n")
                continue
        except Exception:
            print("정수를 입력하세요.\n")
            continue
        
        for i in range(addNum):
            if num+1+i>31:
                player=switchPlayer()
                gameResult(player)
                return
            print (player,":",num+1+i)
        num+=addNum
        player=switchPlayer()
        
brGame()
    
