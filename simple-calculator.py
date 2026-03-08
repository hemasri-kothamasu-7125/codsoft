num1=int(input("Enter Your Fisrt Number:"))
num2=int(input("Enter Your Second Number:"))
print("choices are +,-,*,/,//")
choice=input("Enter Your choice:")
if choice=='+':
    result=num1+num2
    print("Result:",result)
elif choice=='-':
    result=num1-num2
    print("Result:",result)
elif choice=='*':
    result=num1*num2
    print("Result:",result)
elif choice=='/':
    if num2==0:
        print("Error!!")
    else:
        result=num1/num2
        print("Result:",result)
elif choice=='//':
    if num2==0:
        print("Error!!")
    else:
        result=num1//num2
        print("Result:",result)
else:
    print("Invalid choice!!")