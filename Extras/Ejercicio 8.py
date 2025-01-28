import re

# Expresión regular para números reales con signo y notación exponencial
pattern = re.compile(r"^[+-]?\d+(\.\d+)?([eE][+-]?\d+)?$")

def belongLanguage(cadena):
    return bool(pattern.fullmatch(cadena))

# Casos de prueba
cadenas = [
    "+32.475E+3",  
    "-0.5e-2",     
    "3.14E10",     
    "42",          
    "-42",         
    "0.001",       
    "+0.5",        
    "E5",          
    "3.14E",       
    "3.14E-2.3",   
    "-.5",         
    "32E+3.1",     
]

for cadena in cadenas:
    print(f"La cadena '{cadena}' {'es válida' if belongLanguage(cadena) else 'no es válida'} en el lenguaje.")
