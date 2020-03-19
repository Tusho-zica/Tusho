# Dado o salário fixo, o valor das vendas efetuadas pelo vendedor de uma empresa e sabendo-se que ele recebe uma 
# comissão de 3% sobre o total das vendas até R$ 1.500,00 e 5% sobre o que ultrapassar este valor, calcular e 
# escrever o seu salário total.

vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo mensal: "))
vendas = float(input(f"Digite o valor das vendas mensais do {vendedor}: "))
comissao = 0

if vendas <= 1500 : comissao = vendas * 0.03
else : comissao = (1500 * 0.03) + ((vendas - 1500) * 0.05)

salario_total = salario_fixo + comissao

print(salario_total)
