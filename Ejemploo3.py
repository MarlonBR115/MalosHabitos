def areaRectangulo(baseRectangulo, alturaRectangulo):
    rectangulo_area = baseRectangulo * alturaRectangulo
    return rectangulo_area

# Función para calcular el área de un triángulo
def areaTriangulo(baseTriangulo, alturaTriangulo):
    triangulo_area = 0.5 * baseTriangulo * alturaTriangulo
    return triangulo_area
def Menu(opcionMenu):
    if(opcionMenu==1):
        rectanguloBase = float(input("Ingrese el valor de la base del rectángulo: "))
        rectanguloAltura = float(input("Ingrese el valor de la altura del rectángulo: "))
        resultadoRectangulo = areaRectangulo(rectanguloBase, rectanguloAltura)
        print("Área del rectángulo:", resultadoRectangulo)
        validarRectangulo=input("Desea realizar otra operación(Y/N): ")
        if(validarRectangulo=='y' or validarRectangulo=='Y'):
            main()
        if(validarRectangulo=='n' or validarRectangulo=='N'):
            exit()
    if(opcionMenu==2):
        trianguloBase = float(input("Ingrese el valor de la base del triángulo: "))
        trianguloAltura = float(input("Ingrese el valor de la altura del triángulo: "))
        resultadoTriangulo = areaTriangulo(trianguloBase, trianguloAltura)
        print("Área del triángulo:", resultadoTriangulo)
        validarTriangulo = input("Desea realizar otra operación(Y/N): ")
        if (validarTriangulo == 'y' or validarTriangulo == 'Y'):
            main()
        if (validarTriangulo == 'n' or validarTriangulo == 'N'):
            exit()
    if(opcionMenu==3):
        exit()
# Función principal
def main():

    print("---------------Menú---------------")
    print("[1.] Hallar área del rectángulo.")
    print("[2.] Hallar área del triángulo.")
    print("[3.] Salir.")
    print("----------------------------------")
    Opcion = int(input("Ingrese la opción: "))
    Menu(Opcion)

main()