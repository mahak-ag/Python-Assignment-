age=int(input("Enter your age= "))
if(age>=18):
    print("You are eligible for vote")
    print("Select your Govt:")
    print("1. BJP")
    print("2. INC")
    print("3. AITC")
    print("4. BSP")

    choice=input("Now enter 'B' to vote BJP; enter 'I' to vote INC: enter 'A' to vote AITC; enter 'P' to vote BSP: ")
    if(choice=='B'):
        print("YOU VOTED BJP")
        print("THANK YOU")
    
    elif(choice=='I'):
        print("YOU VOTED INC")
        print("THANK YOU")
    
    elif(choice=='A'):
        print("YOU VOTED AITC")
        print("THANK YOU")
    
    elif(choice=='P'):
        print("YOU VOTED BSP")
        print("THANK YOU")
        
else:
    print("You are not eligible for vote")
