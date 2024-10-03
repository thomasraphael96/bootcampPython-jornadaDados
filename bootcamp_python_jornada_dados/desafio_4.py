# define lista de histórico de calculos
historico_calculos: list = []

VALOR_BONUS_ANO: float = 1000.00

def capturar_informacoes() -> str | float:
    # receber nome, salario e % do bonus
    # retorna o valor do bonus
    # 1000 + (salario * bonus)

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

    return nome, salario, mult_bonus

def calcular_bonus(salario: float, mult_bonus: float, valor_bonus_ano: float) -> float:

    # calcula o bonus
    bonus_base: float = salario * mult_bonus
    bonus_final: float = valor_bonus_ano + bonus_base

    return bonus_final

def criar_historico(nome: str, salario: float, mult_bonus: float, valor_bonus_ano: float, bonus: float):
    calculo_atual: dict = {}

    # adiciona calculo atual no histórico
    calculo_atual = {
        "nome": nome,
        "salario": salario,
        "mult_bonus": mult_bonus,
        "adicional_bonus_ano": valor_bonus_ano,
        "bonus": bonus
    }

    # edita a lista de histórico
    historico_calculos.append(calculo_atual)

def mostrar_historico(ver_historico):
    if ver_historico == "s":
        for calculo in historico_calculos:
            i = historico_calculos.index(calculo)
            print('=' * 35)
            print(f"Calculo de número {i + 1}:")
            print(f"- Nome: {calculo['nome']}")
            print(f"- Salário: {calculo['salario']:,.2f}")
            print(f"- Multiplicador do Bônus: {calculo['mult_bonus']}")
            print(f"- Adicional de Bônus do Ano: {calculo['adicional_bonus_ano']:,.2f}")
            print(f"- Bônus: {calculo['bonus']:,.2f}")

continuar: str = "s"
while continuar == "s":

    # chama a função que captura as informações
    nome, salario, mult_bonus = capturar_informacoes()

    # chama a função de calcular o bonus
    bonus = calcular_bonus(salario, mult_bonus, VALOR_BONUS_ANO)

    # retorna o resultado para o usuario
    print(f"Olá {nome}. Seu bônus será de {bonus:,.2f} reais.")
    
    criar_historico(nome, salario, mult_bonus, VALOR_BONUS_ANO, bonus)

    ver_historico: str = input("Deseja ver o histórico de calculos? (s/n) ").lower()
    mostrar_historico(ver_historico)

    continuar = input("Você deseja fazer um novo calculo? (s/n) ").lower()

print("Tudo bem. Volte em breve :)")