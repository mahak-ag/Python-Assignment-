s = int(input("Enter starting point= "))
e = int(input("Enter ending point= "))
u = int(input("Enter updation= "))
choice = input("Enter 'r' to print the series in reverse order or 'f' to print the series in forward order= ")
choice1 = input("Enter 'h' for horizontal or 'v' for vertical= ")

if choice == 'r':
    if choice1 == 'h':
        for i in range(e, s - 1, -u):
            print(i, end=" ")
    elif choice1 == 'v':
        for i in range(e, s - 1, -u):
            print(i)
    else:
        print("INVALID CHOICE")
elif choice == 'f':
    if choice1 == 'h':
        for i in range(s, e + 1, u):
            print(i, end=" ")
    elif choice1 == 'v':
        for i in range(s, e + 1, u):
            print(i)
    else:
        print("INVALID CHOICE")
else:
    print("INVALID INPUT")
