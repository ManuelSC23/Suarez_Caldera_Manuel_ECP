import subprocess
import sys
import os
import pytest

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "ex5.py")
PROMPT = "Introduce unha frase: "

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

# ---------- Casos válidos básicos ----------

def test_ola_devuelve_saudos():
    assert executar("ola") == "Saúdos"

def test_ver_mazda_devuelve_buscando_mazda():
    assert executar("ver mazda") == "Buscando Mazda"

def test_ver_toyota_devuelve_buscando_toyota():
    assert executar("ver Toyota") == "Buscando Toyota"

# ---------- Calquera marca é válida ----------

def test_ver_ford_devuelve_buscando_ford():
    assert executar("ver ford") == "Buscando Ford"

def test_ver_honda_devuelve_buscando_honda():
    assert executar("ver honda") == "Buscando Honda"

def test_ver_bmw_devuelve_buscando_bmw():
    assert executar("ver bmw") == "Buscando Bmw"

def test_ver_renault_devuelve_buscando_renault():
    assert executar("ver renault") == "Buscando Renault"

def test_ver_marca_desconocida():
    assert executar("ver ferrari") == "Buscando Ferrari"

# ---------- Casos con maiúsculas/minúsculas ----------

def test_ola_mayusculas():
    assert executar("OLA") == "Saúdos"

def test_ola_mixto():
    assert executar("ola") == "Saúdos"

def test_ver_mazda_mayusculas():
    assert executar("VER MAZDA") == "Buscando Mazda"

def test_ver_toyota_minusculas():
    assert executar("ver toyota") == "Buscando Toyota"

def test_ver_ford_mayusculas():
    assert executar("VER FORD") == "Buscando Ford"

# ---------- Casos con espacios extra ----------

def test_ola_con_espacios_alrededor():
    assert executar("  ola  ") == "Saúdos"

def test_ver_mazda_con_espacios_multiples():
    assert executar("ver   mazda") == "Buscando Mazda"

def test_ver_toyota_con_tabulador():
    assert executar("ver\tToyota") == "Buscando Toyota"

def test_ver_ford_con_espacios_multiples():
    assert executar("ver   ford") == "Buscando Ford"

# ---------- Casos non recoñecidos ----------

def test_frase_desconocida():
    assert executar("adeus") == "Non entendo"

def test_solo_ver():
    assert executar("ver") == "Non entendo"

def test_frase_vacia():
    assert executar("") == "Non entendo"

def test_solo_espacios():
    assert executar("   ") == "Non entendo"

def test_palabras_extra():
    assert executar("ola que tal") == "Non entendo"

def test_ver_mazda_con_palabra_extra():
    assert executar("ver mazda agora") == "Non entendo"

def test_ver_con_tres_palabras():
    assert executar("ver ford focus") == "Non entendo"

# ---------- Casos límite / robustez ----------

def test_entrada_no_string():
    with pytest.raises((TypeError, AttributeError)):
        executar(None)

def test_entrada_numerica():
    with pytest.raises((TypeError, AttributeError)):
        executar(123)

# ---------- Parametrización para reducir duplicación ----------

@pytest.mark.parametrize("frase,esperado", [
    ("ola", "Saúdos"),
    ("OLA", "Saúdos"),
    ("  ola  ", "Saúdos"),
    ("ver mazda", "Buscando Mazda"),
    ("VER MAZDA", "Buscando Mazda"),
    ("ver   mazda", "Buscando Mazda"),
    ("ver Toyota", "Buscando Toyota"),
    ("ver toyota", "Buscando Toyota"),
    ("ver\tToyota", "Buscando Toyota"),
    ("ver ford", "Buscando Ford"),
    ("ver honda", "Buscando Honda"),
    ("ver bmw", "Buscando Bmw"),
    ("ver renault", "Buscando Renault"),
    ("ver ferrari", "Buscando Ferrari"),
    ("adeus", "Non entendo"),
    ("ver", "Non entendo"),
    ("", "Non entendo"),
    ("   ", "Non entendo"),
    ("ola que tal", "Non entendo"),
    ("ver ford focus", "Non entendo"),
])
def test_tabla_de_casos(frase, esperado):
    assert executar(frase) == esperado