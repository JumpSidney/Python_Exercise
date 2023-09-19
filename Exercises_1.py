def exibir_menu():
    print("Escolha um exercício:")
    print("1 - Exibir um número")
    print("2 - Somar dois números")
    print("3 - Calcular média de 4 notas")
    print("4 - Converter metros para centímetros")
    print("5 - Calcular área de um círculo")
    print("6 - Calcular área de um quadrado e seu dobro")
    print("7 - Calcular salário mensal")
    print("8 - Converter Fahrenheit para Celsius")
    print("9 - Converter Celsius para Fahrenheit")
    print("10 - Calcular operações com números inteiros e reais")
    print("11 - Calcular peso ideal (homens)")
    print("12 - Calcular peso ideal (homens e mulheres)")
    print("13 - Calcular excesso de peso de peixes e multa")
    print("14 - Calcular salário líquido")
    print("15 - Calcular quantidade de latas de tinta")
    print("16 - Calcular quantidade de tinta em latas e galões")
    print("0 - Sair")

def numero_informado():
    numero = float(input("Digite um número: "))
    print(f"O número informado foi {numero}")

def somar_dois_numeros():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    soma = numero1 + numero2
    print(f"A soma dos números é: {soma}")

def calcular_media_notas():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A média das notas é: {media}")

def converter_metros_para_centimetros():
    metros = float(input("Digite a quantidade de metros: "))
    centimetros = metros * 100
    print(f"{metros} metros é igual a {centimetros} centímetros")

def calcular_area_circulo():
    raio = float(input("Digite o raio do círculo: "))
    area = 3.14 * raio ** 2
    print(f"A área do círculo é: {area}")

def calcular_area_quadrado_dobro():
    lado = float(input("Digite o tamanho do lado do quadrado: "))
    area = lado ** 2
    dobro_area = 2 * area
    print(f"A área do quadrado é: {area}")
    print(f"O dobro da área é: {dobro_area}")

def calcular_salario_mensal():
    valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    salario = valor_por_hora * horas_trabalhadas
    print(f"O total do seu salário no mês é: {salario}")

def converter_fahrenheit_para_celsius():
    fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} graus Fahrenheit é igual a {celsius:.2f} graus Celsius")

def converter_celsius_para_fahrenheit():
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} graus Celsius é igual a {fahrenheit:.2f} graus Fahrenheit")

def operacoes_com_numeros():
    numero1 = int(input("Digite um número inteiro: "))
    numero2 = int(input("Digite outro número inteiro: "))
    numero3 = float(input("Digite um número real: "))
    
    resultado_a = (numero1 * 2) * (numero2 / 2)
    resultado_b = (numero1 * 3) + numero3
    resultado_c = numero3 ** 3
    
    print(f"Resultado a: {resultado_a}")
    print(f"Resultado b: {resultado_b}")
    print(f"Resultado c: {resultado_c}")

def calcular_peso_ideal_homens():
    altura = float(input("Digite sua altura (em metros): "))
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")

def calcular_peso_ideal_homens_mulheres():
    altura = float(input("Digite sua altura (em metros): "))
    peso_ideal_homem = (72.7 * altura) - 58
    peso_ideal_mulher = (62.1 * altura) - 44.7
    print(f"Peso ideal para homem: {peso_ideal_homem:.2f} kg")
    print(f"Peso ideal para mulher: {peso_ideal_mulher:.2f} kg")

def calcular_excesso_peso_peixes():
    peso_peixes = float(input("Digite o peso dos peixes (em kg): "))
    limite = 50
    if peso_peixes <= limite:
        print("Você não excedeu o limite de peso de peixes.")
        excesso = 0
        multa = 0
    else:
        excesso = peso_peixes - limite
        multa = excesso * 4.00
        print(f"Excesso de peso: {excesso} kg")
        print(f"Multa a ser paga: R$ {multa:.2f}")

def calcular_salario_liquido():
    valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    salario_bruto = valor_por_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - ir - inss - sindicato
    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"IR (11%): R$ {ir:.2f}")
    print(f"INSS (8%): R$ {inss:.2f}")
    print(f"Sindicato (5%): R$ {sindicato:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")

def calcular_quantidade_latas_tinta():
    area_pintada = float(input("Digite a área a ser pintada em metros quadrados: "))
    litros_necessarios = area_pintada / 3
    latas_necessarias = litros_necessarios / 18
    if litros_necessarios % 18 != 0:
        latas_necessarias += 1
    preco_total = latas_necessarias * 80.00
    print(f"Quantidade de latas de tinta necessárias: {int(latas_necessarias)}")
    print(f"Preço total: R$ {preco_total:.2f}")

def calcular_quantidade_tinta_latas_galoes():
    area_pintada = float(input("Digite a área a ser pintada em metros quadrados: "))
    litros_necessarios = area_pintada / 3
    latas_18l = int(litros_necessarios / 18)
    galoes_36l = int((litros_necessarios % 18) / 3.6)
    
    if (litros_necessarios % 18) % 3.6 != 0:
        galoes_36l += 1
    
    preco_total_latas = latas_18l * 80.00
    preco_total_galoes = galoes_36l * 25.00
    
    print(f"Quantidade de latas de tinta necessárias: {latas_18l}")
    print(f"Quantidade de galões de tinta necessários: {galoes_36l}")
    print(f"Preço total com latas: R$ {preco_total_latas:.2f}")
    print(f"Preço total com galões: R$ {preco_total_galoes:.2f}")

while True:
    exibir_menu()
    opcao = int(input("Digite o número do exercício que deseja executar (ou 0 para sair): "))
    
    if opcao == 0:
        print("Programa encerrado. Até mais!")
        break
    elif opcao == 1:
        numero_informado()
    elif opcao == 2:
        somar_dois_numeros()
    elif opcao == 3:
        calcular_media_notas()
    elif opcao == 4:
        converter_metros_para_centimetros()
    elif opcao == 5:
        calcular_area_circulo()
    elif opcao == 6:
        calcular_area_quadrado_dobro()
    elif opcao == 7:
        calcular_salario_mensal()
    elif opcao == 8:
        converter_fahrenheit_para_celsius()
    elif opcao == 9:
        converter_celsius_para_fahrenheit()
    elif opcao == 10:
        operacoes_com_numeros()
    elif opcao == 11:
        calcular_peso_ideal_homens()
    elif opcao == 12:
        calcular_peso_ideal_homens_mulheres()
    elif opcao == 13:
        calcular_excesso_peso_peixes()
    elif opcao == 14:
        calcular_salario_liquido()
    elif opcao == 15:
        calcular_quantidade_latas_tinta()
    elif opcao == 16:
        calcular_quantidade_tinta_latas_galoes()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    
    input("Pressione Enter para continuar...")
