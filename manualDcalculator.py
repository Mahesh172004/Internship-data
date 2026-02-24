def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):    
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")        
    print("4. Divide")

    ch=int(input("Enter choice(1/2/3/4): "))

    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    if ch == 1:
        print(num1,"+",num2,"=", add(num1,num2))
    elif ch == 2:
        print(num1,"-",num2,"=", subtract(num1,num2))
    elif ch == 3:
        print(num1,"*",num2,"=", multiply(num1,num2))
    elif ch == 4:
        print(num1,"/",num2,"=", divide(num1,num2))
    else:
        print("Invalid choice")

    again = input("Do you want to perform another calculation? (yes/no): ").lower()

    if again != 'yes':
        print("fuck off")
        break

