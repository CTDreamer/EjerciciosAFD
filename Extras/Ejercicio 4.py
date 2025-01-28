import re

# Expresión regular para declaraciones de funciones en C
pattern = re.compile(r"^(int|float|double|char|void)\s+[a-zA-Z_]\w*\s*\(\s*((int|float|double|char|void)\s+[a-zA-Z_]\w*(\s*,\s*(int|float|double|char|void)\s+[a-zA-Z_]\w*)*)?\s*\)$")

def belongLanguage(cadena):
    return bool(pattern.fullmatch(cadena))

# Casos de prueba
cadenas = [
    "int main()",
    "void foo(int a, float b)",
    "char function_name(char c, double d, int x)",
    "double computeArea()",
    "int 2invalid()",
    "float missing_params(",
    "void valid(int a, char b, double c)"
]

for cadena in cadenas:
    print(f"La declaración '{cadena}' {'es válida' if belongLanguage(cadena) else 'no es válida'} en el lenguaje.")
