import re

# Definir el patrón usando una expresión regular
# 0(0|1)*1 => comienza con 0 y termina con 1
# 1(0|1)*0 => comienza con 1 y termina con 0
pattern = re.compile(r"^(0(0|1)*1|1(0|1)*0)$")

# Función para verificar si una cadena pertenece al lenguaje
def belongLanguage(cadena):
    if pattern.fullmatch(cadena):
        return True
    else:
        return False

# Pruebas
cadenas = ["01", "10", "011", "100", "0", "1", "111100", "000"]
for cadena in cadenas:
    resultado = "es válido" if belongLanguage(cadena) else "no es válido"
    print(f"La cadena '{cadena}' {resultado} en el lenguaje.")
