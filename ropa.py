# Clase base Prenda
class Prenda:
    # Constructor para inicializar atributos básicos de una prenda
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre       
        self.precio = precio       
        self.cantidad = cantidad 
          
    # Método para mostrar la información de la prenda
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")

    # Método para reducir el stock de la prenda, verificando disponibilidad
    def reducir_stock(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        else:
            print("Stock insuficiente")
            return False


# Clase RopaHombre que hereda de Prenda
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad) 
        self.talla = talla                          

    # Sobreescritura del método para mostrar información con detalles adicionales
    def mostrar_info(self):
        super().mostrar_info()                      
        print(f"Talla: {self.talla}")


# Clase RopaMujer que hereda de Prenda
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  
        self.talla = talla                          

    # Sobreescritura del método para mostrar información con detalles adicionales
    def mostrar_info(self):
        super().mostrar_info()                     
        print(f"Talla: {self.talla}")


# Clase Inventario para gestionar las prendas y sus operaciones
class Inventario:
    def __init__(self):
        self.prendas = []                          

    # Método para agregar una prenda al inventario
    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    # Método para mostrar todas las prendas del inventario
    def mostrar_inventario(self):
        print("Inventario de Ropa:")
        for prenda in self.prendas:
            prenda.mostrar_info()
            print("---")

    # Método para procesar una compra, reduciendo el stock y calculando el total
    def procesar_compra(self, nombre_prenda, cantidad):
        for prenda in self.prendas:
            if prenda.nombre == nombre_prenda:
                if prenda.reducir_stock(cantidad):          # Verifica si hay stock suficiente
                    total = prenda.precio * cantidad        # Calcula el total de la compra
                    print(f"Compra realizada: {nombre_prenda} x {cantidad} - Total: ${total}")
                    return total
        print("Producto no disponible o stock insuficiente")
        return 0

    # Método interactivo para agregar prendas desde la consola
    def agregar_prenda_desde_input(self):
        tipo = input("Tipo de prenda (hombre/mujer): ").strip().lower()
        nombre = input("Nombre de la prenda: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad en stock: "))
        talla = input("Talla: ")

        if tipo == "hombre":
            prenda = RopaHombre(nombre, precio, cantidad, talla)
        elif tipo == "mujer":
            prenda = RopaMujer(nombre, precio, cantidad, talla)
        else:
            print("Tipo de prenda no válido")
            return

        self.agregar_prenda(prenda)
        print("Prenda agregada al inventario.")


# Ejecución principal
if __name__ == "__main__":
    inventario = Inventario()

    # Ejemplos de ropa de hombre
    inventario.agregar_prenda(RopaHombre("Camisa de Hombre", 25.00, 50, "M"))
    inventario.agregar_prenda(RopaHombre("Pantalón de Hombre", 30.00, 30, "L"))
    inventario.agregar_prenda(RopaHombre("Chaqueta de Hombre", 55.00, 20, "XL"))
    inventario.agregar_prenda(RopaHombre("Zapatos de Hombre", 60.00, 25, "42"))

    # Ejemplos de ropa de mujer
    inventario.agregar_prenda(RopaMujer("Falda de Mujer", 28.00, 15, "S"))
    inventario.agregar_prenda(RopaMujer("Blusa de Mujer", 22.00, 40, "M"))
    inventario.agregar_prenda(RopaMujer("Vestido de Mujer", 45.00, 10, "L"))
    inventario.agregar_prenda(RopaMujer("Zapatos de Mujer", 50.00, 20, "38"))

    # Mostrar inventario y procesar una compra
    inventario.mostrar_inventario()
    print("\nRealizando una compra:")
    inventario.procesar_compra("Camisa de Hombre", 2)
    inventario.procesar_compra("Vestido de Mujer", 1)

    # Se agrego la linea de codigo de abajo para poder agregar desde consola las prendas (Se puede comentar)
    inventario.agregar_prenda_desde_input()
