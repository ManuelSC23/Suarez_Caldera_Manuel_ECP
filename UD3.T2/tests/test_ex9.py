import subprocess
import sys
import os
import pytest

SCRIPT = os.path.join(os.path.dirname(__file__), "..", "ex9.py")
PROMPT = "Introduce unha orde: "

def executar(entrada):
    resultado = subprocess.run(
        [sys.executable, SCRIPT],
        input=str(entrada) + "\n",
        capture_output=True,
        text=True,
    )
    saida = resultado.stdout
    if saida.startswith(PROMPT):
        saida = saida[len(PROMPT):]
    return saida.rstrip("\n")

# ---------- Casos válidos ----------

def test_start():
    assert executar("start") == "Iniciando sistema..."

def test_stop():
    assert executar("stop") == "Detendo sistema..."

def test_axuda():
    assert executar("axuda") == "Lista de comandos: start, stop, restart"

def test_help():
    assert executar("help") == "Lista de comandos: start, stop, restart"

def test_restart():
    assert executar("restart") == "Reiniciando..."

# ---------- Mayúsculas/minúsculas ----------

def test_start_mayusculas():
    assert executar("START") == "Iniciando sistema..."

def test_stop_mixto():
    assert executar("Stop") == "Detendo sistema..."

def test_axuda_mayusculas():
    assert executar("AXUDA") == "Lista de comandos: start, stop, restart"

def test_help_mixto():
    assert executar("Help") == "Lista de comandos: start, stop, restart"

def test_restart_mayusculas():
    assert executar("RESTART") == "Reiniciando..."

# ---------- Espacios extra ----------

def test_start_con_espacios():
    assert executar("  start  ") == "Iniciando sistema..."

def test_stop_con_tabulador():
    assert executar("\tstop\t") == "Detendo sistema..."

def test_axuda_con_espacios():
    assert executar("  axuda  ") == "Lista de comandos: start, stop, restart"

# ---------- Comandos no reconocidos ----------

def test_comando_desconocido():
    assert executar("ola") == "Comando ola non recoñecido"

def test_comando_desconocido_con_espacios():
    assert executar("  ola  ") == "Comando ola non recoñecido"

def test_comando_desconocido_numerico():
    assert executar("123") == "Comando 123 non recoñecido"

def test_comando_desconocido_frase():
    assert executar("start now") == "Comando start now non recoñecido"

def test_comando_vacio():
    assert executar("") == "Comando  non recoñecido"

def test_solo_espacios():
    assert executar("   ") == "Comando  non recoñecido"

# ---------- Parametrización completa ----------

@pytest.mark.parametrize("entrada,esperado", [
    ("start", "Iniciando sistema..."),
    ("stop", "Detendo sistema..."),
    ("axuda", "Lista de comandos: start, stop, restart"),
    ("help", "Lista de comandos: start, stop, restart"),
    ("restart", "Reiniciando..."),
    ("START", "Iniciando sistema..."),
    ("Stop", "Detendo sistema..."),
    ("AXUDA", "Lista de comandos: start, stop, restart"),
    ("Help", "Lista de comandos: start, stop, restart"),
    ("RESTART", "Reiniciando..."),
    ("  start  ", "Iniciando sistema..."),
    ("\tstop\t", "Detendo sistema..."),
    ("  axuda  ", "Lista de comandos: start, stop, restart"),
    ("hola", "Comando hola non recoñecido"),
    ("  hola  ", "Comando hola non recoñecido"),
    ("123", "Comando 123 non recoñecido"),
    ("start now", "Comando start now non recoñecido"),
    ("", "Comando  non recoñecido"),
    ("   ", "Comando  non recoñecido"),
])
def test_tabla_de_casos(entrada, esperado):
    assert executar(entrada) == esperado