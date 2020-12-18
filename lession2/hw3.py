print("You may want to use this calculator to perform basic arithmetics, such as addition: '+';\n"
      "substraction: '-'; multiplication: '*' or division: '/'.\n"
      "Please be aware that all operations are performed according to the input order,\n"
      "so you wont have much practical benefits of using it."
      "For your convenience, you are welcome to add as much numeric data and operands as you need.\n"
      "I am at your disposal! ;)\n"
      "The result of calculations will be displayed after inputting '=' as an operand.")
result = 0
operand = None
while operand != "=":
    try:
        userNumber1 = input("Please enter a number: ")
        number1 = float(userNumber1)
    except ValueError:
        print("Hey, is not a numeric value, please try again ((")
        continue
    if operand == None:
        result = number1
    elif operand == "+":
        result += number1
    elif operand == "-":
        result -= number1
    elif operand == "*":
        result *= number1
    elif operand == "/":
        try:
            result /= number1
        except ZeroDivisionError:
            print("Oops! It's zero division... try again ((")
            continue
    operand = input("Please enter an operand: ")
    while operand not in ('+', "-", '*', '/', '='):
        print("Hey, we had a deal! I expect only +,-,*,/ or =...")
        operand = input("Please enter an operand: ")
    if operand == "=":
        continue
print(f'You result is {result} ')
