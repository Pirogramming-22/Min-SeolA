num=0
player="playerA"
def switchPlayer():
    global player
    if (player=="playerA"):
        return ("playerB")
    else:
        return("playerA")

def gameResult(player):
    print(player, "win!")

while True:
    try:
        addNum=int(input("�θ� ������ ������ �Է��ϼ���.(1, 2, 3�� �Է� ����) :"))
        if (addNum<1 or addNum>3):
            print("1, 2, 3 �� �ϳ��� �Է��ϼ���.\n")
            continue
    except Exception:
        print("������ �Է��ϼ���.\n")
        continue
    
    for i in range(addNum):
        print(player,":",num+1+i)
    num+=addNum
    if (num>=31):
        player=switchPlayer()
        gameResult(player)
        break
    player=switchPlayer() 
    