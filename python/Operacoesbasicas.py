n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

operacao = input("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nEscolha o tipo de operação que deseja realizar:")

if operacao == "1":
    resultado = n1 + n2
    print(f"O resultado da operação é: {resultado}")
elif operacao == "2":
    resultado = n1 - n2
    print(f"O resultado da operação é: {resultado}")
elif operacao == "3":
    resultado = n1 * n2
    print(f"O resultado da operação é: {resultado}")
elif operacao == "4":
    resultado = n1 / n2
    print(f"O resultado da operação é: {resultado}")
else:
    print("Opção inválida.")
    resultado = None    