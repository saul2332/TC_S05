# inventario.py

class Inventario:
    def __init__(self):
        self.productos = []

    # Sobrecarga de métodos mediante parámetros opcionales
    def agregar_producto(self, nombre, cantidad=1, precio=0.0):
        producto = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        self.productos.append(producto)
        print(f"Producto '{nombre}' agregado exitosamente.")

    # Manejo de errores en la búsqueda
    def buscar_producto(self, nombre):
        try:
            for producto in self.productos:
                if producto["nombre"].lower() == nombre.lower():
                    return producto
            raise ValueError(f"Producto '{nombre}' no encontrado.")
        except ValueError as e:
            print(e)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("\nInventario actual:")
            for producto in self.productos:
                print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']:.2f}")

# ------------------ PROGRAMA PRINCIPAL ------------------

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad (opcional, default 1): ") or 1)
                precio = float(input("Ingrese el precio (opcional, default 0.0): ") or 0.0)
                inventario.agregar_producto(nombre, cantidad, precio)
            except ValueError:
                print("Error: cantidad y precio deben ser numéricos.")
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(f"Producto encontrado: {producto}")
        
        elif opcion == '3':
            inventario.mostrar_productos()
        
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor ingrese un número entre 1 y 4.")

if __name__ == "__main__":
    menu()