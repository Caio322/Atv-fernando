numero = int(input("Digite um número decimal: "))
resultado_hex = ""

if numero == 0:
    resultado_hex = "0"
else:
    numero_decimal = numero
    while numero_decimal > 0:
        resto = numero_decimal % 16
        numero_decimal = numero_decimal // 16

        if resto < 10:
            resultado_hex = str(resto) + resultado_hex
        elif resto == 10:
            resultado_hex = "A" + resultado_hex
        elif resto == 11:
            resultado_hex = "B" + resultado_hex
        elif resto == 12:
            resultado_hex = "C" + resultado_hex
        elif resto == 13:
            resultado_hex = "D" + resultado_hex
        elif resto == 14:
            resultado_hex = "E" + resultado_hex
        elif resto == 15:
            resultado_hex = "F" + resultado_hex 
        else: 
            resultado_hex = ""
           
print(f"O número {numero} em hexadecimal é: {resultado_hex}") 