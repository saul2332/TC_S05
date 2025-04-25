class Inventario:
    def __init__(self):
        self.productos = []

    # Sobrecarga por parámetros opcionales
    def agregar_producto(self, nombre, cantidad=1, precio=0.0):
        producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        self.productos.append(producto)
        print(f"Producto agregado: {producto}")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return

        for i, prod in enumerate(self.productos, 1):
            print(f"{i}. {prod['nombre']} - Cantidad: {prod['cantidad']} - Precio: ${prod['precio']}")

    def buscar_producto(self, nombre):
        try:
            resultados = [p for p in self.productos if p["nombre"].lower() == nombre.lower()]
            if resultados:
                print("Producto encontrado:", resultados[0])
            else:
                raise ValueError("Producto no encontrado.")
        except ValueError as e:
            print("Error:", e)


# Ejemplo de uso
inv = Inventario()
inv.agregar_producto("Lapicero")
inv.agregar_producto("Cuaderno", 3)
inv.agregar_producto("Regla", 2, 1.5)
inv.mostrar_productos()
inv.buscar_producto("Cuaderno")
inv.buscar_producto("Borrador")  # genera un error controlado