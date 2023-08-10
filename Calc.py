print ("Welcome to the CalcProject")

while True:
    n1 = input("Insert first number:\n")
    try: 
        if float(n1):
            break
    except ValueError:
        print("Please insert a valid value")
while True:
    n2 = input("Insert second number:\n")
    try: float(n2)
    except ValueError:
        print("Please insert a valid value")

input("Select Operation:\n+\n-\n*\n%")