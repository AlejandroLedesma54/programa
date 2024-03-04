
print("\nHola, bienvenido al inventario")
name = input("\nPor favor, ingrese su nombre: ")
base = {'papas':500,'manzana':3000}
cantidad = {'papas':1,'manzana':2}
start = ''

#Funcion para mostrar los productos
def mostrar_productos():
    print("\nInventario")
    for productos, valor in base.items():
        print(f"\nProducto: {productos.capitalize()} /// Precio: ${valor:.2f}")

#Funcion para mostrar la cantidad de productos
def mostrar_productos2():
    print("\nCantidad de productos")
    for productos, cant in cantidad.items():
        print(f"\nProducto: {productos.capitalize()} /// Cantidad: {cant}")

#Funcion para verificar si el producto esta en el inventario
def verificar_productos():
    producto = input("Ingrese el producto que desea verificar si esta en el inventario: ").lower()
    for productos, valor in base.items():
        if producto in base.keys():
            print(f"El producto {producto.capitalize()} se encuentra en el inventario con un valor de {valor}")
        else:
            print(f"El producto {producto.capitalize()} no se encuentra en el inventario")

#Funcion para verificar eliminar el producto
def eliminar_producto():
    producto = input(f"\nIngrese el nombre del producto que desea eliminar del inventario: ").lower()
    if producto in base.keys():
            del base[producto]
            del cantidad[producto]
            print("\nEl producto ha sido eliminado correctamente del inventario ")
    else:
            print("\nEl producto a eliminar no se encuentra en el inventario. ")

#Funcion para actualizar la cantidad del producto
def actualizar_cantidad():
    producto = input(f"\nIngrese el nombre del producto del cual desea actualizar la cantidad en el inventario: ")
    if producto in cantidad.keys():
        numero = int(input(f"\nIngrese la cantidad a agregar al producto en el inventario: "))
        cantidad[producto] += numero
        print("La cantidad del producto ha sido actualizada exitosamente")
    else:
        print("El producto no se encuentra en el inventario. ")

#Funcion para agregar productos
def agregar_productos():
    num_productos = int(input("Ingrese el número de productos que va a ingresar: "))
    for i in range(num_productos):
        producto = input(f"\nIngrese el nombre del producto: ")
        valor = float(input(f"Ingrese el valor del producto: "))
        base[producto] = valor
        numero = int(input(f"Ingrese la cantidad del producto: "))
        cantidad[producto]= numero
        print("\nEl producto ha sido agregado correctamente al inventario!")

def menu_inicial():
    start1 = input(f"\nBienvenido al inventario {name}.\nSeleccione una opcion a continuacion: \n\na. Agregar un nuevo producto al inventario. \nb. Actualizar la cantidad de un producto existente en el inventario. \nc. Eliminar un producto del inventario. \nd. Listar todos los productos en el inventario. \ne. Verificar si un producto esta en el inventario. \nf. Finalizar el programa. \n\nPor favor ingrese una opcion: ").lower()
    return start1

#Ciclo While para Menu
while True:
    start = menu_inicial()
    if start == "a":
        agregar_productos()
    elif start == "b": 
        actualizar_cantidad()
    elif start == "c":
        eliminar_producto()
    elif start == "d":
        if not base:
            print("No hay articulos en el inventario")
        else:
            mostrar_productos()
            mostrar_productos2()
    elif start == "e":
        verificar_productos()
    
    elif start == "f":
        print("\nEl programa ha finalizado.")
        break
        

