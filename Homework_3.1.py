#common calculator
number1 = int(input("enter first number"))
number2 = int(input("enter second number"))
plusminus = input("enter +, -, * or /")

match plusminus:
    case "+":
        print(number1+number2)
    case "-":
        print(number1-number2)
    case "*":
        print(number1*number2)
    case "/":
        if number2 == 0:
            print("error, you cant divide on zero")
        else:
            print(number1/number2)
    case _:
        print("error, invalid type of symbol")
