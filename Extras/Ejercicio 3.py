import re

pattern = re.compile(r"^[a-zA-Z][a-zA-Z0-9]*$")

def belongLanguage(cadena):
    return bool(pattern.fullmatch(cadena))

cadenas = ["variable1", "2variable", "var123", "a", "b1234", "_var"]
for cadena in cadenas:
    print(f"La cadena '{cadena}' {'es válido' if belongLanguage(cadena) else 'no es válido'} en el lenguaje.")
