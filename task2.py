def divided_squares():
    try:
        a = float(input('Please provide the first number: '))
        b = float(input('Please provide the second number: '))
        return a**2 / b**2
    except ValueError:
        raise ValueError("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")

try:
    res = divided_squares()
    print(res)
except (ValueError, ZeroDivisionError) as e:
    print(e)

        
    
    