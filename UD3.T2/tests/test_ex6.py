import subprocess
import sys
import os
import pytest

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "ex6.py")
PROMPT = "Introduce un número enteiro: "

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
    return saida.strip()

# ---------- Casos válidos: negativos ----------

def test_negativo_uno():
    assert executar(-1) == "Negativo"

def test_negativo_grande():
    assert executar(-100) == "Negativo"

def test_negativo_muy_grande():
    assert executar(-999999) == "Negativo"

# ---------- Casos válidos: cero ----------

def test_cero():
    assert executar(0) == "Cero"

# ---------- Casos válidos: unidades (1-10) ----------

def test_unidad_uno():
    assert executar(1) == "Unidade"

def test_unidad_cinco():
    assert executar(5) == "Unidade"

def test_unidad_diez():
    assert executar(10) == "Unidade"

# ---------- Casos válidos: decenas (11-99) ----------

def test_decena_once():
    assert executar(11) == "Decena"

def test_decena_cincuenta():
    assert executar(50) == "Decena"

def test_decena_noventa_y_nueve():
    assert executar(99) == "Decena"

# ---------- Casos válidos: centenas (> 99) ----------

def test_centena_cien():
    assert executar(100) == "Centena"

def test_centena_mil():
    assert executar(1000) == "Centena"

def test_centena_muy_grande():
    assert executar(999999) == "Centena"

# ---------- Fronteras entre categorías ----------

def test_frontera_negativo_cero():
    assert executar(-1) == "Negativo"
    assert executar(0) == "Cero"

def test_frontera_cero_unidad():
    assert executar(0) == "Cero"
    assert executar(1) == "Unidade"

def test_frontera_unidad_decena():
    assert executar(10) == "Unidade"
    assert executar(11) == "Decena"

def test_frontera_decena_centena():
    assert executar(99) == "Decena"
    assert executar(100) == "Centena"

# ---------- Filtro básico de entrada: casos de error explícitos ----------

@pytest.mark.parametrize("entrada", ["abc", "a1b", ""])
def test_entrada_invalida_devuelve_erro(entrada):
    assert executar(entrada) == "Erro"

# ---------- Filtro básico de entrada: otros casos inválidos ----------

@pytest.mark.parametrize("entrada", ["12abc", "  ", "3.5", "1e3", None, [1], {"n": 1}])
def test_otras_entradas_invalidas(entrada):
    assert executar(entrada) == "Erro"

# ---------- Booleanos ----------

def test_booleano_true_es_error():
    assert executar(True) == "Erro"

def test_booleano_false_es_error():
    assert executar(False) == "Erro"

# ---------- Cadenas numéricas válidas ----------

def test_cadena_numerica_entero():
    assert executar("5") == "Unidade"

def test_cadena_numerica_negativa():
    assert executar("-3") == "Negativo"

def test_cadena_numerica_cero():
    assert executar("0") == "Cero"

def test_cadena_numerica_centena():
    assert executar("150") == "Centena"

# ---------- Parametrización completa de casos válidos ----------

@pytest.mark.parametrize("numero,esperado", [
    (-1000, "Negativo"),
    (-1, "Negativo"),
    (0, "Cero"),
    (1, "Unidade"),
    (5, "Unidade"),
    (10, "Unidade"),
    (11, "Decena"),
    (50, "Decena"),
    (99, "Decena"),
    (100, "Centena"),
    (1000, "Centena"),
    (999999, "Centena"),
])
def test_tabla_de_casos(numero, esperado):
    assert executar(numero) == esperado

# ---------- Parametrización completa de entradas inválidas ----------

@pytest.mark.parametrize("entrada", [
    "abc", "a1b", "", "12abc", "  ", "3.5", "1e3", None, [1], {"n": 1}, True, False,
])
def test_tabla_entradas_invalidas(entrada):
    assert executar(entrada) == "Erro"