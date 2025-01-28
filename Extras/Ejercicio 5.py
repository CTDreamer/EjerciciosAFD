import re

# Expresión regular para números binarios que no contienen "11"
pattern = re.compile(r"^(0|1|10)*$")

def belongLanguage(cadena):
    return bool(pattern.fullmatch(cadena))

# Casos de prueba
cadenas = [
    "0",       
    "1",       
    "10",      
    "101",     
    "1010",   
    "110",     
    "111",     
    "10101"    
]

for cadena in cadenas:
    print(f"La cadena '{cadena}' {'es válida' if belongLanguage(cadena) else 'no es válida'} en el lenguaje.")
