import re

pattern = re.compile(r"^(0|1)*0$")

def belongLanguage(cadena):
    return bool(pattern.fullmatch(cadena))

cadenas = ["0", "10", "110", "111", "1010", "1111"]
for cadena in cadenas:
    print(f"La cadena '{cadena}' {'es válido' if belongLanguage(cadena) else 'no es válido'} en el lenguaje.")
