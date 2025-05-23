while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
        break  

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("Division by zero is not allowed. Please enter a non-zero second number.")
