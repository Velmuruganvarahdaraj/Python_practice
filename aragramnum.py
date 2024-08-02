def aragramnum(num1,num2):
    return sorted(str(num1))== sorted (str(num2))
num1=int(input())
num2=int(input())
if aragramnum(num1,num2):
    print("It's Aragram")
else:
    print("Not Aragram")