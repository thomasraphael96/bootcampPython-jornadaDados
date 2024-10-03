# receber nome, salario e % do bonus
# retorna o valor do bonus
# 1000 + (salario * bonus)

VALOR_BONUS_ANO = 1000

continuar: str = "s"

while continuar == "s":
    # variáveis de controle do while
    nome_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False

    # recebe informações do usuário
    while nome_valido is not True:
        try:
            nome: str = input("Qual seu nome? (Sem abreviações) ")
            if any(char.isdigit() for char in nome):
                print("Notamos que tem digito(s) no nome informado.")
            elif len(nome) < 3:
                print("O nome informado é muito curto (menos que 3 caracteres).")
            else:
                print('Nome válido.')
                nome_valido = True
        except ValueError:
            print("O multiplicador de bonus informado não é um número.")

    while salario_valido is not True:
        try:
            salario: float = float(input("Qual seu salário? "))
            if salario <= 0:
                print("O salário informado é menor ou igual a 0, portanto inválido.")
            else:
                print('Salário válido.')
                salario_valido = True
        except ValueError:
            print("O multiplicador de bonus informado não é um número.")

    while bonus_valido is not True:
        try:
            mult_bonus: float = float(input("Qual o percentual do seu bônus? "))
            if mult_bonus <= 0:
                print("O multiplicador de bonus informado é menor ou igual a 0, portanto inválido.")
            else:
                print('Multiplicador de bônus válido.')
                bonus_valido = True
        except ValueError:
            print("O multiplicador de bonus informado não é um número.")

    # calcula o bonus
    bonus_base: float = salario * mult_bonus
    bonus_final: float = VALOR_BONUS_ANO + bonus_base

    # retorna o resultado para o usuario
    print(f"Olá {nome}. Seu bônus será de {bonus_final:,.2f} reais.")

    continuar = input("Você deseja fazer um novo calculo? (s/n) ").lower()

print("Tudo bem. Volte em breve :)")