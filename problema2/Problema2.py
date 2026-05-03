import re

def validar_fen(cadena_fen):
    print(f"\nAnalizando cadena: '{cadena_fen}'")
    
    # Verificar que haya exactamente 6 bloques separados por espacio
    partes = cadena_fen.split(" ")
    if len(partes) != 6:
        return "ERROR: La cadena no tiene los 6 bloques requeridos por FEN."
        
    tablero, turno, enroque, peon_paso, medios_mov, mov_completos = partes
    
    # validar el Tablero 
    filas = tablero.split("/")
    if len(filas) != 8:
        return "ERROR: El tablero no tiene 8 filas separadas por '/'."
        
    for i, fila in enumerate(filas):
        casillas = 0
        for caracter in fila:
            if caracter.isdigit():
                casillas += int(caracter) # si es numero, suma casillas vacías
            elif caracter in "pnbrqkPNBRQK":
                casillas += 1             # si es letra (pieza), suma 1 casilla
            else:
                return f"ERROR: Caracter no reconocido '{caracter}' en la fila {i+1}."
        
        if casillas != 8:
            return f"ERROR: La fila {i+1} no suma exactamente 8 casillas."

    # validar el Turno
    if turno not in ['w', 'b']:
        return "ERROR: El turno debe ser 'w' (blancas) o 'b' (negras)."

    # validar el Enroque
    if enroque != "-" and not all(c in "KQkq" for c in enroque):
        return "ERROR: Formato de enroque invalido."

    # validar el Peón al paso - Usamos una expresion regular simple
    if not re.match(r'^([a-h][36]|-)$', peon_paso):
        return "ERROR: Casilla de peon al paso invalida."

    # validar los contadores de movimiento 
    if not (medios_mov.isdigit() and mov_completos.isdigit()):
        return "ERROR: Los contadores de movimientos deben ser números enteros."

    # Si pasa todas las validaciones:
    return "La cadena FEN es valida."

def iniciar_validador():
    print("--- Validador de Notacion FEN ---")
    fen_usuario = input("Ingresa la cadena FEN a evaluar: ")
    resultado = validar_fen(fen_usuario)
    print(resultado)

if __name__ == "__main__":
    iniciar_validador()
