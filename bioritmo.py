#!/usr/bin/python3
#
import math
from datetime import datetime

def calcula_bioritmo(date):
    fisico      = math.sin(2 * math.pi * date / 23) * 100
    emocional   = math.sin(2 * math.pi * date / 28) * 100
    intelectual = math.sin(2 * math.pi * date / 33) * 100
    return fisico, emocional, intelectual

# Data de nascimento
data_nascimento = datetime(1900, 1, 1)

# Data atual
data_atual = datetime.now()

# Diferença em dias
data = (data_atual - data_nascimento).days

# Calcular o biorritmo com a data obtida
fisico, emocional, intelectual = calcula_bioritmo(data)

# Imprimir os resultados
print(f"Biorritmo físico      : {fisico:.2f}")
print(f"Biorritmo emocional   : {emocional:.2f}")
print(f"Biorritmo intelectual : {intelectual:.2f}")
