import re

# Expresión regular para validar una sentencia INSERT en SQL
pattern = re.compile(
    r"^INSERT\s+INTO\s+[a-zA-Z_][a-zA-Z0-9_]*\s+VALUES\s*\(\s*\d+\s*,\s*'[^']*'\s*\)\s*;$",
    re.IGNORECASE
)

def belongLanguage(cadena):
    return bool(pattern.fullmatch(cadena))

# Casos de prueba
cadenas = [
    "INSERT INTO tabla1 VALUES (32, 'abc');",
    "insert into tabla2 values (10, 'xyz');",
    "INSERT INTO tabla VALUES (123, 'hello');",
    "INSERT tabla1 VALUES (32, 'abc');",
    "INSERT INTO 123tabla VALUES (10, 'test');",
    "INSERT INTO tabla1 VALUES (32, 'abc')",
    "INSERT INTO tabla1 VALUES (32, abc);",
    "INSERT INTO tabla1 (column1, column2) VALUES (32, 'abc');"
]

for cadena in cadenas:
    print(f"La sentencia '{cadena}' {'es válida' if belongLanguage(cadena) else 'no es válida'}")
