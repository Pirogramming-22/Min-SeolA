num=0

while True:
    try:
        addNum=int(input("�θ� ������ ������ �Է��ϼ���.(1, 2, 3�� �Է� ����) :"))
        if (addNum<1 or addNum>3):
            print("1, 2, 3 �� �ϳ��� �Է��ϼ���.\n")
            continue
    except Exception:
        print("������ �Է��ϼ���.\n")