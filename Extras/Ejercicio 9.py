import re

# Expresión regular para validar declaraciones de variables en Pascal
pattern = re.compile(
    r"^VAR\s+(([a-zA-Z_][a-zA-Z0-9_]*(\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*)*)\s*:\s*(integer|real|char|boolean);\s*)+BEGIN$",
    re.IGNORECASE
)

def belongLanguage(cadena):
    return bool(pattern.fullmatch(cadena))

# Casos de prueba
cadenas = [
    "VAR\na, b : integer;\nx : real\nBEGIN",         
    "VAR\nx : integer;\nBEGIN",                     
    "VAR\nx, y, z : real;\nBEGIN",                 
    "VAR\nx : integer; y : real\nBEGIN",            
    "VAR\nx : integer;",                            
    "VAR\nx : ;\nBEGIN",                            
    "VAR\na, b : boolean;\nc : char;\nBEGIN",       
    "var\na, b : integer;\nBEGIN",                 
]

for cadena in cadenas:
    print(f"La declaración:\n'{cadena}'\n{'es válida' if belongLanguage(cadena) else 'no es válida'}\n")
