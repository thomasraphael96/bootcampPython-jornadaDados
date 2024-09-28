# receber nome, salario e % do bonus
# retorna o valor do bonus
# 1000 + (salario * bonus)

VALOR_BONUS_ANO = 1000

# recebe informações do usuário
try:
    nome = input("Qual seu nome? (Sem abreviações) ")
    if nome.isdigit() == True:
        print("Notamos que tem digito(s) no nome informado.")
        exit()
    elif len(nome) < 3:
        print("O nome informado é muito curto (menos que 3 caracteres).")
        exit()
    else:
        try:
            salario = float(input("Qual seu salário? "))
            if salario <= 0:
                print("O salário informado é menor ou igual a 0, portanto inválido.")
                exit()
            else:
                try:
                    mult_bonus = float(input("Qual o percentual do seu bônus? "))
                    if mult_bonus <= 0:
                        print("O multiplicador de bonus informado é menor ou igual a 0, portanto inválido.")
                        exit()
                except ValueError:
                    print("O multiplicador de bonus informado não é um número.")
                    exit()
        except ValueError:
            print("O salário informado não é um número.")
            exit()
except:
    print("O programa abortou por erro ao digitar informações. Favor executar novamente.")

else:
    # calcula o bonus
    bonus_base = salario * mult_bonus
    bonus_final = VALOR_BONUS_ANO + bonus_base

    # retorna o resultado para o usuario
    print(f"Olá {nome}. Seu bônus será de {bonus_final:,.2f} reais.")