def greatest(num1,num2,num3):
    if(num1>num2):
        f1 = num1
    else:
        f1 = num2

    if(f1>num3):
        print(str(f1) +" is greatest")
    else:
        print(str(num3) +" is greatest")

a = 3
b = 5
c = 1


d = greatest(a,b,c)
