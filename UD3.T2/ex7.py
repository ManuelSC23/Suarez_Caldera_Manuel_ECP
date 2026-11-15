import ast

entrada = input("Introduce un valor: ")

try:
    valor = ast.literal_eval(entrada)
except (ValueError, SyntaxError):
    valor = entrada

if isinstance(valor, bool):
    print("Outro")
elif isinstance(valor, int):
    print(f"Enteiro: {valor}")
elif isinstance(valor, str):
    print(f"Texto: {valor}")
elif isinstance(valor, list) and len(valor) > 0 and isinstance(valor[0], int) and not isinstance(valor[0], bool):
    print("Lista Enteiros")
else:
    print("Outro")
