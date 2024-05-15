print ("Welcome to the CalcProject\n")

while True:
    n1 = input("Insert first number:\n")
    try: 
        if float(n1):
            break
    except ValueError:
        print("Please insert a valid value>")
while True:
    n2 = input("Insert second number:\n>")
    try: 
        if float(n2):
            break
    except ValueError:
        print("Please insert a valid value")

while True:
    op = input("\nSelect Operation:\n+\n-\n*\n%\n")
    if op=="+":
        print(float(n1)+float(n2))
        break
    if op=="-":
        print(float(n1)-float(n2))
        break
    if op=="*":
        print(float(n1)*float(n2))
        break
    if op=="%":
        print(float(n1)%float(n2))
        break
    else:
        print("Please enter a valid operation")
