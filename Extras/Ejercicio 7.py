import re

# Expresión regular para números reales con parte entera par y parte fraccionaria impar
pattern = re.compile(r"^(0|[2468]|[0-9]*[02468])\.\d*[13579]$")

def belongLanguage(cadena):
    return bool(pattern.fullmatch(cadena))

# Casos de prueba
cadenas = [
    "2.3",      
    "4.135",    
    "1.3",      
    "20.2",     
    "0.1",      
    "2468.246", 
    ".5",       
]

for cadena in cadenas:
    print(f"La cadena '{cadena}' {'es válida' if belongLanguage(cadena) else 'no es válida'} en el lenguaje.")
