
# ******  TABELA    ********
# |  A  |  C  |  T  |  G   |
# |  1  | 000 | 001 |  01  |
# --------------------------

A = '1'
C = '000'
T = '001'
G = '01'

ent = input()
entS = ent.replace('A', A).replace('C', C).replace('T', T ).replace('G', G)

print('{} {:.1f}'.format(entS, 100 - ((len(sn) * 100) / (len(ent) * 8 ))))  

# 100 - (((len(ns)*100)/(len(s)*8))

# Ex: ATC (24bits) - 1001000 (7bits)
# Fórmula:  100 - ((7x100)/24)
# Entrada: ATC
# Saída: 1001000 70.8

# Teste
# E ACTGACTGACTGACTGACTGACTG
# S 100000101100000101100000101100000101100000101100000101 71.9
