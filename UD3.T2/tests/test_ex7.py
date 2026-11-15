import subprocess
import sys
import os
import pytest

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "ex7.py")
PROMPT = "Introduce un valor: "

def executar(entrada):
    resultado = subprocess.run(
        [sys.executable, SCRIPT],
        input=str(entrada) + "\n",
        capture_output=True,
        text=True,
    )
    saida = resultado.stdout.strip()
    if saida.startswith(PROMPT):
        saida = saida[len(PROMPT):]
    return saida.rstrip("\n")

# ---------- Casos válidos: enteros ----------

def test_entero_positivo():
    assert executar("42") == "Enteiro: 42"

def test_entero_negativo():
    assert executar("-7") == "Enteiro: -7"

def test_entero_cero():
    assert executar("0") == "Enteiro: 0"

def test_entero_grande():
    assert executar("999999") == "Enteiro: 999999"

# ---------- Casos válidos: texto ----------

def test_texto_simple():
    assert executar("ola") == "Texto: ola"

def test_texto_con_espacios():
    assert executar("ola mundo") == "Texto: ola mundo"

def test_texto_con_numeros():
    assert executar("abc123") == "Texto: abc123"

def test_texto_vacio():
    assert executar("") == "Texto:"

# ---------- Casos válidos: lista que comeza por enteiro ----------

def test_lista_entero_solo():
    assert executar("[1]") == "Lista Enteiros"

def test_lista_entero_y_texto():
    assert executar("[1, 'a', 'b']") == "Lista Enteiros"

def test_lista_entero_y_mas_enteros():
    assert executar("[5, 10, 15]") == "Lista Enteiros"

def test_lista_entero_negativo():
    assert executar("[-3, 'x']") == "Lista Enteiros"

def test_lista_entero_cero():
    assert executar("[0, 'a']") == "Lista Enteiros"

# ---------- Casos: listas que NO empiezan por entero ----------

def test_lista_vacia():
    assert executar("[]") == "Outro"

def test_lista_empieza_por_texto():
    assert executar("['a', 1]") == "Outro"

def test_lista_empieza_por_flotante():
    assert executar("[1.5, 'a']") == "Outro"

def test_lista_empieza_por_booleano():
    # True == 1 en Python; si el script usa type(x) is int, True no es int.
    assert executar("[True, 'a']") == "Outro"

# ---------- Casos: otros tipos ----------

def test_flotante():
    assert executar("3.14") == "Outro"

def test_booleano_true():
    assert executar("True") == "Outro"

def test_booleano_false():
    assert executar("False") == "Outro"

def test_diccionario():
    assert executar("{'a': 1}") == "Outro"

def test_tupla():
    assert executar("(1, 2)") == "Outro"

def test_none():
    assert executar("None") == "Outro"