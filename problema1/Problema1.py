import re

def analizar_expresion():
    print("--- Problema 1 ---")

    expresion = input("Ingresa la expresión aritmética (ejemplo 12+3*(4)): ")

    # definimos los patrones de busqueda
    patrones = [
        ('NUMERO', r'\d+(?:\.\d+)?'),          # numeros enteros o decimales con punto
        ('OPERANDO', r'[a-zA-Z][a-zA-Z0-9]*'), # letras seguidas de letras o numeros
        ('OPERADOR', r'[\+\-\*\/]'),           # simbolos +, -, *, /
        ('PAREN_IZQ', r'\('),                  # parentesis de apertura
        ('PAREN_DER', r'\)')                   # parentesis de cierre
    ]
    
    # Unimos todas las reglas en un solo patron
    patron_general = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in patrones)
    
    resultado = []
    balance_parentesis = 0
    
    # escaneamos la expresion buscando coincidencias
    for match in re.finditer(patron_general, expresion):
        tipo = match.lastgroup  # La clasificacion (ejemplo: NUMERO)
        valor = match.group()   # el texto extraido (ejemplo: 12)
        
        resultado.append(f"{tipo} {valor}")
        
        # Verificamos el balance de los parentesis
        if tipo == 'PAREN_IZQ':
            balance_parentesis += 1
        elif tipo == 'PAREN_DER':
            balance_parentesis -= 1
            
    # Formateamos y mostramos la salida
    salida = " ".join(resultado)
    if balance_parentesis == 0:
        salida += " PARENTESIS BALANCEADOS."
    else:
        salida += " ERROR: PARENTESIS NO BALANCEADOS."
        
    print("\nSalida:")
    print(salida)

if __name__ == "__main__":
    analizar_expresion()
