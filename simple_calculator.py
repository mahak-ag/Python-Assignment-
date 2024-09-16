a=int(input("enter a number= "))
b=int(input("enter a number= "))
choice=input("enter a choice(+ , - , / , * , % , // , **)= ")
if(choice=='+'):
    print(a+b)
elif(choice=='-'):
    print(a-b)
elif(choice=='/'):
    print(a/b);
elif(choice=='*'):
    print(a*b)
elif(choice=='%'):
    print(a%b)
elif(choice=='//'):
    print(a//b)
elif(choice==''):
    print(a**b)
else:
    print("INVALID CHOICE")
