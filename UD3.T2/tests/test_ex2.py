import subprocess
import sys
import os
import pytest

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "ex2.py")
PROMPT = "Introduce un código HTTP: "

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

# --- Casos representativos de cada rango ---

def test_informativa_100():
    assert executar("100") == "Info"

def test_informativa_199():
    assert executar("199") == "Info"

def test_correcta_200():
    assert executar("200") == "Éxito"

def test_correcta_299():
    assert executar("299") == "Éxito"

def test_redireccion_300():
    assert executar("300") == "Redireccións"

def test_redireccion_399():
    assert executar("399") == "Redireccións"

def test_error_cliente_400():
    assert executar("400") == "Erro Cliente"

def test_error_cliente_499():
    assert executar("499") == "Erro Cliente"

def test_error_servidor_500():
    assert executar("500") == "Erro Servidor"

def test_error_servidor_599():
    assert executar("599") == "Erro Servidor"

# --- Casos fuera de rango ---

def test_codigo_negativo():
    assert executar("-1") == "Descoñecido"

def test_codigo_cero():
    assert executar("0") == "Descoñecido"

def test_codigo_600():
    assert executar("600") == "Descoñecido"

def test_codigo_moi_alto():
    assert executar("999") == "Descoñecido"

# --- Tests parametrizados (máis compactos) ---

@pytest.mark.parametrize("entrada, esperado", [
    ("100", "Info"),
    ("150", "Info"),
    ("199", "Info"),
    ("200", "Éxito"),
    ("250", "Éxito"),
    ("299", "Éxito"),
    ("300", "Redireccións"),
    ("350", "Redireccións"),
    ("399", "Redireccións"),
    ("400", "Erro Cliente"),
    ("450", "Erro Cliente"),
    ("499", "Erro Cliente"),
    ("500", "Erro Servidor"),
    ("550", "Erro Servidor"),
    ("599", "Erro Servidor"),
    ("0", "Descoñecido"),
    ("-1", "Descoñecido"),
    ("600", "Descoñecido"),
    ("999", "Descoñecido"),
])
def test_clasificacion_http_parametrizado(entrada, esperado):
    assert executar(entrada) == esperado