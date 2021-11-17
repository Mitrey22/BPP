import pytest
import pandas as pd


def test_gasto_mes():
    gasto = -23456
    resultado = True
    if gasto < 0:
        final = True
    else:
        final = False
    assert resultado == final


def test_ingreso_mes():
    gasto = 29463
    resultado = True
    if gasto > 0:
        final = True
    else:
        final = False
    assert resultado == final


def test_df_creator():
    ctn = 0
    df = pd.read_csv("finanzas2020.csv")
    lista = []
    data = df['Enero']
    while ctn < len(data):
        value = data.iloc[ctn]
        try:
            value = int(value)
        except ValueError:
            value = 0
        lista.insert(ctn, value)
        ctn += 1
        pass
    tipo_lista = type(lista)
    lista_prueva = [2, 3, 4, 65, 423, 3]
    tipo_lista_prueva = type(lista_prueva)
    assert tipo_lista == tipo_lista_prueva
