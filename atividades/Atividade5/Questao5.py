num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, * ou /): ")

match operador:
    case "+":
        print(f"Resultado: {num1 + num2}")
    case "-":
        print(f"Resultado: {num1 - num2}")
    case "*":
        print(f"Resultado: {num1 * num2}")
    case "/":
        print(f"Resultado: {num1 / num2}")
    case _:
        print("Operação inválida!")