from parcial1a import Representante

def datos_representantes():
    print("\nIngrese los datos del reprensentante")

    codigoContinente = input("Código Continente: ")
    nombreContinente = input("Nombre Continente: ")
    codigoPais = input("Código País: ")
    nombrePais = input("Nombre País: ")
    codigoEmpresa = input("Código Empresa: ")
    nombreEmpresa = input("Nombre Empresa: ")
    telefonoEmpresa = input("Teléfono Empresa: ")
    codigoRepresentante = input("Código Representante: ")
    nombreRepresentante = input("Nombre Representante: ")

    return Representante(codigoContinente, nombreContinente, codigoPais, nombrePais, codigoEmpresa, nombreEmpresa, telefonoEmpresa, codigoRepresentante, nombreRepresentante)

def main():
    print("Registro de representantes")

    representante1 = datos_representantes()
    representante2 = datos_representantes()

    representante1.mostrar_datos()
    representante2.mostrar_datos()

if __name__ == "__main__":
    main()
