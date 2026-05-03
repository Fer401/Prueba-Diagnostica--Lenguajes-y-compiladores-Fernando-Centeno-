def demostrar_collatz(p, q):
    # validar la regla exigida para la demostracion
    if q < 100 * p:
        return f"ERROR: No se cumple la regla q >= 100p. (Tu q es {q} y 100p es {100*p})"
    
    print(f"\nVerificando Conjetura de Collatz en el intervalo [{p}, {q}]:")
    print("-" * 50)

    # iterar sobre cada numero en el intervalo desde p hasta q (incluido)
    for n in range(p, q + 1):
        secuencia = [str(n)]  # lista que se usa para guardar el recorrido como texto
        actual = n
        
        # aplicar las reglas matematicas hasta que el numero sea 1
        while actual != 1:
            if actual % 2 == 0:
                # si el residuo de la division entre 2 es 0, es PAR
                actual = actual // 2
            else:
                # de lo contrario, es IMPAR
                actual = (3 * actual) + 1
                
            secuencia.append(str(actual))
            
        # imprimir la ruta completa del numero
        print(f"n={n}: {' -> '.join(secuencia)}")
        
    return "\nDemostrado..."

def iniciar_programa():
    print("--- Conjetura de Collatz ---")
    try:
        p = int(input("Ingresa el valor inicial (p): "))
        q = int(input("Ingresa el valor final (q): "))
        resultado = demostrar_collatz(p, q)
        print(resultado)
    except ValueError:
        print("ERROR: Por favor ingrese solo numeros enteros.")

if __name__ == "__main__":
    iniciar_programa()
