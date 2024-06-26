while True:

    num = int(input("enter the num: "))
    digit = 0
    t1 = num
    while t1>0:
        t1//=10
        digit+=1

    t2 = num
    sum =0
    while t2>0:
        rem = t2%10
        sum += rem**digit
        t2//=10

    if sum==num:
        print("armstrong")

    else:
        print("not armstrong")       