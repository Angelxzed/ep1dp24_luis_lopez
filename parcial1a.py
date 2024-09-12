class Continente:
    def __init__(self, codigoContinente, nombreContinente):
        self.codigoContinente = codigoContinente
        self.nombreContinente = nombreContinente

class Pais(Continente):
    def __init__(self, codigoContinente, nombreContinente, codigoPais, nombrePais):
        super().__init__(codigoContinente, nombreContinente)
        self.codigoPais = codigoPais
        self.nombrePais = nombrePais

class Empresa(Pais):
    def __init__(self, codigoContinente, nombreContinente, codigoPais, nombrePais, codigoEmpresa, nombreEmpresa, telefonoEmpresa):
        super().__init__(codigoContinente, nombreContinente, codigoPais, nombrePais)
        self.codigoEmpresa = codigoEmpresa
        self.nombreEmpresa = nombreEmpresa
        self.telefonoEmpresa = telefonoEmpresa

class Representante(Empresa):
    def __init__(self, codigoContinente, nombreContinente, codigoPais, nombrePais, codigoEmpresa, nombreEmpresa, telefonoEmpresa, codigoRepresentante, nombreRepresentante):
        super().__init__(codigoContinente, nombreContinente, codigoPais, nombrePais, codigoEmpresa, nombreEmpresa, telefonoEmpresa)
        self.codigoRepresentante = codigoRepresentante
        self.nombreRepresentante = nombreRepresentante

    def mostrar_datos(self):
        print("\nDatos del Representante")
        print(f"Código Continente: {self.codigoContinente}, Nombre Continente: {self.nombreContinente}")
        print(f"Código País: {self.codigoPais}, Nombre País: {self.nombrePais}")
        print(f"Código Empresa: {self.codigoEmpresa}, Nombre Empresa: {self.nombreEmpresa}, Teléfono Empresa: {self.telefonoEmpresa}")
        print(f"Código Representante: {self.codigoRepresentante}, Nombre Representante: {self.nombreRepresentante}")
