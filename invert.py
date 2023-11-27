from reportlab.pdfgen import canvas

def guardar_datos_en_pdf(nombre, edad, direccion, archivo_salida='datos_personales.pdf'):
    # Crear un archivo PDF
    pdf = canvas.Canvas(archivo_salida)

    # Agregar contenido al PDF
    pdf.drawString(100, 800, "Datos Personales:")
    pdf.drawString(100, 780, f"Nombre: {nombre}")
    pdf.drawString(100, 760, f"Edad: {edad}")
    pdf.drawString(100, 740, f"Dirección: {direccion}")

    # Guardar el PDF
    pdf.save()

    print(f"Los datos se han guardado en {archivo_salida}")

# Solicitar al usuario que ingrese sus datos
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")

# Llamar a la función para guardar los datos en un PDF
guardar_datos_en_pdf(nombre, edad, direccion)
