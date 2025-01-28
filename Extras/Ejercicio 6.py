import re

# Expresión regular corregida
pattern = re.compile(r"^(0(0|1){2})*0?$|^(1(0|1){2})*1$")

def belongLanguage(cadena):
    return bool(pattern.fullmatch(cadena))

# Casos de prueba
cadenas = [
    "0",       
    "10",      
    "11",      
    "0011",    
    "101",     
    "1001",    
    "00",      
    "1101"     
]

for cadena in cadenas:
    print(f"La cadena '{cadena}' {'es válida' if belongLanguage(cadena) else 'no es válida'} en el lenguaje.")
