import subprocess
import sys
import os
import pytest

# Ruta ao script do alumno, relativa á carpeta de tests
SCRIPT = os.path.join(os.path.dirname(__file__), "..", "ex1.py")

PROMPT = "Introduce unha cor: "

def executar(entrada):
    resultado = subprocess.run(
        [sys.executable, SCRIPT],
        input=entrada + "\n",
        capture_output=True,
        text=True,
    )
    saida = resultado.stdout.strip()
    # Quitar o prompt se aparece ao comezo
    if saida.startswith(PROMPT):
        saida = saida[len(PROMPT):]
    return saida.strip()

# --- Casos válidos en minúsculas ---
def test_vermello():
    assert executar("vermello") == "Parar"

def test_amarelo():
    assert executar("amarelo") == "Precaución"

def test_verde():
    assert executar("verde") == "Pasar"

# --- Casos con maiúsculas ---
def test_verde_maiuscula():
    assert executar("Verde") == "Pasar"

def test_vermello_maiuscula():
    assert executar("Vermello") == "Parar"

def test_amarelo_maiuscula():
    assert executar("Amarelo") == "Precaución"

# --- Casos con mezcla de maiúsculas/minúsculas ---
def test_verde_mixto():
    assert executar("vErDe") == "Pasar"

# --- Caso de error ---
def test_cor_invalida():
    assert executar("azul") == "Erro"

def test_cor_baleira():
    assert executar("") == "Erro"

# --- Tests parametrizados (máis compactos) ---
@pytest.mark.parametrize("entrada, esperado", [
    ("vermello", "Parar"),
    ("amarelo", "Precaución"),
    ("verde", "Pasar"),
    ("Verde", "Pasar"),
    ("VERMELLO", "Parar"),
    ("azul", "Erro"),
    ("", "Erro"),
])
def test_semaforo_parametrizado(entrada, esperado):
    assert executar(entrada) == esperado