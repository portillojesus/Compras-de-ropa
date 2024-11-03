# Clase base Prenda
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")

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

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


# Clase RopaMujer que hereda de Prenda
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


# Clase Carrito para gestionar los productos seleccionados por el usuario
class Carrito:
    def __init__(self):
        self.items = []

    def agregar_al_carrito(self, prenda, cantidad):
        self.items.append((prenda, cantidad))
        print(f"Agregado al carrito: {prenda.nombre} x {cantidad}")

    def mostrar_resumen(self):
        print("\nResumen del Carrito:")
        total = 0
        for prenda, cantidad in self.items:
            subtotal = prenda.precio * cantidad
            total += subtotal
            print(f"{prenda.nombre} x {cantidad} - Subtotal: ${subtotal:.2f}")
        print(f"Total a pagar: ${total:.2f}")


# Clase Inventario para gestionar las prendas
class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        print("Inventario de Ropa:")
        for prenda in self.prendas:
            prenda.mostrar_info()
            print("---")

    def mostrar_prendas_disponibles(self):
        print("\nPrendas disponibles para agregar al carrito:")
        for prenda in self.prendas:
            print(f"- {prenda.nombre} (Stock: {prenda.cantidad}, Precio: ${prenda.precio})")

    def buscar_prenda(self, nombre_prenda):
        for prenda in self.prendas:
            if prenda.nombre == nombre_prenda:
                return prenda
        return None


# Ejecución principal del programa
if __name__ == "__main__":
    inventario = Inventario()
    carrito = Carrito()

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

    # Mostrar inventario general
    inventario.mostrar_inventario()

    # Permitir al usuario agregar productos al carrito
    while True:
        # Mostrar las prendas disponibles para facilitar la selección
        inventario.mostrar_prendas_disponibles()

        print("\nSeleccione una prenda por su nombre para agregar al carrito (o escriba 'fin' para terminar):")
        nombre_prenda = input("Nombre de la prenda: ").strip()
        
        if nombre_prenda.lower() == "fin":
            break

        prenda = inventario.buscar_prenda(nombre_prenda)
        if prenda:
            cantidad = int(input("Cantidad: "))
            if prenda.reducir_stock(cantidad):
                carrito.agregar_al_carrito(prenda, cantidad)
            else:
                print("Cantidad no disponible en stock.")
        else:
            print("Prenda no encontrada en el inventario.")

    # Mostrar resumen final del carrito
    carrito.mostrar_resumen()
