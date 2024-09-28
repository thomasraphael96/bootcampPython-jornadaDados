# receber nome, salario e % do bonus
# retorna o valor do bonus
# 1000 + (salario * bonus)

VALOR_BONUS_ANO = 1000

# recebe informações do usuário
nome = input("Qual seu nome? ")
salario = float(input("Qual seu salário? "))
mult_bonus = float(input("Qual o percentual do seu bônus? "))

# calcula o bonus
bonus_base = salario * mult_bonus
bonus_final = VALOR_BONUS_ANO + bonus_base

# retorna o resultado para o usuario
print(f"Olá {nome}. Seu bônus será de {bonus_final:,.2f} reais.")