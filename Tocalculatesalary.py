sal = float(input("enter amount"))

if sal>1000000:
    print(int(sal*0.04))
elif sal > 500000 and sal<= 1000000 :
    print(int(sal*0.02))
elif sal<= 500000 :
    print(int('0'))
