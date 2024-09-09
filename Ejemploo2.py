def calcularFuncion(Factor01, Factor02, Factor03):
    Total = Factor01 * Factor02 + Factor03
    return Total

if __name__=="__main__":
    print("----------------------------------------------------------------------------")
    print("Teniendo en cuenta la siguiente operación: Multiplicando*Multiplicador+Sumando")
    print("----------------------------------------------------------------------------")
    Multiplicando = float(input("Ingrese el multiplicando: "))
    Multiplicador = float(input("Ingrese el multiplicador: "))
    Sumando = float(input("Ingrese el sumando: "))
    resultado = calcularFuncion(Multiplicando, Multiplicador, Sumando)
    print("#############################################################################")
    print("El resultado de: ",f"{Multiplicando}*{Multiplicador}+{Sumando} = {resultado}")
    print("##############################################################################")
