# Faça uma função chamada somaImposto. A função possui dois parâmetros: taxa_imposto, que é 
# a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item 
# antes do imposto. A função retorna o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxa_imposto, custo):
    valor_custo = custo * taxa_imposto
    return valor_custo

taxa_imposto = 0.15
custo = 1000

print(somaImposto(taxa_imposto, custo))
