def invertir_numero(numero):
    # Convierte el número a cadena y luego invierte la cadena
    numero_str = str(numero)
    numero_invertido_str = numero_str[::-1]
    
    # Convierte la cadena invertida de nuevo a un número entero
    numero_invertido = int(numero_invertido_str)
    
    return numero_invertido

# Ejemplo de uso
numero_original = 54321
numero_invertido = invertir_numero(numero_original)

print(f"Número original: {numero_original}")
print(f"Número invertido: {numero_invertido}")