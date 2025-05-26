while True:
    try:
        num = float(input("Enter a positive number: "))
        if num <= 0:
            raise Exception("Number must be positive. Try again.")
        print(f"Great! {num} is positive.")
        break
    except ValueError:
        print("Please enter a valid number.")
    except Exception:
        print("Number must be positive. Try again.")
    