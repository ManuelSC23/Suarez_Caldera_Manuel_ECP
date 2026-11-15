import subprocess
import sys
import os
import pytest

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "ex8.py")
PROMPT = "Introduce un diccionario: "

def executar(entrada):
    resultado = subprocess.run(
        [sys.executable, SCRIPT],
        input=str(entrada) + "\n",
        capture_output=True,
        text=True,
    )
    saida = resultado.stdout
    if saida.startswith(PROMPT):
        saida = saida[len(PROMPT):] # Slicing para coller só o do final, sen a mensaxe do input
    return saida.rstrip("\n") # Eliminamos o salto de liña da cadea de entrada

# ---------- Casos válidos: rango con varios elementos ----------

def test_rango_dos_elementos():
    assert executar('{"status": 200, "data": [1, 4]}') == "Rango: 1 a 4"

def test_rango_cuatro_elementos():
    assert executar('{"status": 200, "data": [1, 2, 3, 4]}') == "Rango: 1 a 4"

def test_rango_negativos():
    assert executar('{"status": 200, "data": [-5, 0, 10]}') == "Rango: -5 a 10"

def test_rango_texto():
    assert executar('{"status": 200, "data": ["a", "b", "c"]}') == "Rango: a a c"

def test_rango_mixto():
    assert executar('{"status": 200, "data": [1, "b", 3]}') == "Rango: 1 a 3"

# ---------- Casos válidos: un solo elemento ----------

def test_unico_entero():
    assert executar('{"status": 200, "data": [42]}') == "Rango: 42 a 42"

def test_unico_texto():
    assert executar('{"status": 200, "data": ["solo"]}') == "Rango: solo a solo"

def test_unico_negativo():
    assert executar('{"status": 200, "data": [-1]}') == "Rango: -1 a -1"

# ---------- Casos de error: status distinto de 200 ----------

def test_status_404():
    assert executar('{"status": 404, "data": []}') == "Erro"

def test_status_500():
    assert executar('{"status": 500, "data": [1, 2]}') == "Erro"

def test_status_201():
    assert executar('{"status": 201, "data": [1, 2]}') == "Erro"

def test_sin_status():
    assert executar('{"data": [1, 2]}') == "Erro"

# ---------- Casos de error: data no válida ----------

def test_data_baleira():
    assert executar('{"status": 200, "data": []}') == "Erro"

def test_data_texto():
    assert executar('{"status": 200, "data": "texto"}') == "Erro"

def test_data_entero():
    assert executar('{"status": 200, "data": 5}') == "Erro"

def test_data_none():
    assert executar('{"status": 200, "data": None}') == "Erro"

def test_data_diccionario():
    assert executar('{"status": 200, "data": {"a": 1}}') == "Erro"

def test_sin_data():
    assert executar('{"status": 200}') == "Erro"

# ---------- Casos de error: entrada no es diccionario ----------

def test_entrada_lista():
    assert executar('[1, 2, 3]') == "Erro"

def test_entrada_texto():
    assert executar('"hola"') == "Erro"

def test_entrada_entero():
    assert executar('42') == "Erro"

def test_entrada_none():
    assert executar('None') == "Erro"

def test_entrada_baleira():
    assert executar('') == "Baleira"

# ---------- Parametrización completa ----------

@pytest.mark.parametrize("entrada,esperado", [
    ('{"status": 200, "data": [1, 4]}', "Rango: 1 a 4"),
    ('{"status": 200, "data": [1, 2, 3, 4]}', "Rango: 1 a 4"),
    ('{"status": 200, "data": [-5, 0, 10]}', "Rango: -5 a 10"),
    ('{"status": 200, "data": ["a", "b", "c"]}', "Rango: a a c"),
    ('{"status": 200, "data": [1, "b", 3]}', "Rango: 1 a 3"),
    ('{"status": 200, "data": [42]}', "Rango: 42 a 42"),
    ('{"status": 200, "data": ["solo"]}', "Rango: solo a solo"),
    ('{"status": 200, "data": [-1]}', "Rango: -1 a -1"),
    ('{"status": 404, "data": []}', "Erro"),
    ('{"status": 500, "data": [1, 2]}', "Erro"),
    ('{"status": 201, "data": [1, 2]}', "Erro"),
    ('{"data": [1, 2]}', "Erro"),
    ('{"status": 200, "data": []}', "Erro"),
    ('{"status": 200, "data": "texto"}', "Erro"),
    ('{"status": 200, "data": 5}', "Erro"),
    ('{"status": 200, "data": None}', "Erro"),
    ('{"status": 200, "data": {"a": 1}}', "Erro"),
    ('{"status": 200}', "Erro"),
    ('[1, 2, 3]', "Erro"),
    ('"hola"', "Erro"),
    ('42', "Erro"),
    ('None', "Erro"),
    ('', "Baleira"),
])
def test_tabla_de_casos(entrada, esperado):
    assert executar(entrada) == esperado