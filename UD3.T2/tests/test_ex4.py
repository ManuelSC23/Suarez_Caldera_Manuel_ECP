import subprocess
import sys
import os
import pytest

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "ex4.py")
PROMPT = "Introduce unha lista: "

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

# --- Casos básicos ---

def test_baleira():
    assert executar("[]") == "Baleira"

def test_un():
    assert executar("[5]") == "Un"

def test_dous():
    assert executar("[2, 3]") == "Dous"

def test_moitos():
    assert executar("[1, 2, 3]") == "Moitos"

# --- Casos con espazos ---

def test_baleira_con_espazos():
    assert executar("[ ]") == "Baleira"

def test_un_con_espazos():
    assert executar("[ 5 ]") == "Un"

def test_dous_con_espazos():
    assert executar("[ 2 , 3 ]") == "Dous"

# --- Casos con outros tipos ---

def test_un_string():
    assert executar('["a"]') == "Un"

def test_dous_strings():
    assert executar('["a", "b"]') == "Dous"

def test_moitos_mixtos():
    assert executar('[1, "a", True]') == "Moitos"

# --- Tests parametrizados ---

@pytest.mark.parametrize("entrada, esperado", [
    ("[]", "Baleira"),
    ("[ ]", "Baleira"),
    ("[5]", "Un"),
    ("[ 5 ]", "Un"),
    ('["a"]', "Un"),
    ("[2, 3]", "Dous"),
    ("[ 2 , 3 ]", "Dous"),
    ('["a", "b"]', "Dous"),
    ("[1, 2, 3]", "Moitos"),
    ("[1, 2, 3, 4, 5]", "Moitos"),
    ('[1, "a", True]', "Moitos"),
])
def test_clasificacion_lista_parametrizado(entrada, esperado):
    assert executar(entrada) == esperado