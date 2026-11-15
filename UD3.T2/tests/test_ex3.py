import subprocess
import sys
import os
import pytest

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "ex3.py")
PROMPT = "Introduce x e y (separados por espazo): "

def executar(entrada):
    resultado = subprocess.run(
        [sys.executable, SCRIPT],
        input=entrada + "\n",
        capture_output=True,
        text=True,
    )
    saida = resultado.stdout.strip()
    if saida.startswith(PROMPT):
        saida = saida[len(PROMPT):]
    return saida.strip()

def test_orixe():
    assert executar("0 0") == "Orixe"

def test_eixo_y():
    assert executar("0 5") == "Eixo Y"

def test_eixo_x():
    assert executar("3 0") == "Eixo X"

def test_cuadrante():
    assert executar("2 4") == "Cuadrante"

def test_cuadrante_negativo():
    assert executar("-2 -4") == "Cuadrante"

def test_eixo_x_negativo():
    assert executar("-3 0") == "Eixo X"

def test_eixo_y_negativo():
    assert executar("0 -5") == "Eixo Y"

def test_con_espazos_multiples():
    assert executar("2   4") == "Cuadrante"

@pytest.mark.parametrize("entrada, esperado", [
    ("0 0", "Orixe"),
    ("0 5", "Eixo Y"),
    ("0 -3", "Eixo Y"),
    ("3 0", "Eixo X"),
    ("-2 0", "Eixo X"),
    ("2 4", "Cuadrante"),
    ("-1 5", "Cuadrante"),
    ("-1 -5", "Cuadrante"),
    ("1 -5", "Cuadrante"),
])

def test_clasificacion_punto_parametrizado(entrada, esperado):
    assert executar(entrada) == esperado