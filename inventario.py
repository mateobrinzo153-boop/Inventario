inventario = []

def agregar_producto():
    nombre = input("Inserte nombre del producto: ")

    if not nombre.strip():
        print("Campo obligatorio.")
        return

    try:  
        precio = float(input("Inserte precio del producto: "))
        cantidad = int(input("Inserte cantidad del producto: "))
        encontrado = False
    except ValueError:
        print("Insertar numero:")
        return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero")
        return
    if precio <= 0:
        print("El precio debe ser mayor a cero")
        return
    for producto_existente in inventario:
        if producto_existente["nombre"].lower().strip() == nombre.lower().strip():
            print(f"El producto {nombre} ya existe. Desea actualizar el precio? (s/n)")
            respuesta = input().lower().strip()

            producto_existente["cantidad"] += cantidad
            encontrado = True
    if encontrado == False:
        inventario.append(producto)
        print("Producto agregado")

def ver_inventario():
    valor_inventario = 0
    for producto in inventario:
        valor_stock = producto['precio'] * producto['cantidad']
        valor_inventario += valor_stock
        print(f"{producto['nombre']} - ${producto['precio']} - Cantidad: {producto['cantidad']} - Valor del stock: {valor_stock}")
    if not inventario:
        print("El inventario está vacío")
    print(f"Valor total del inventario: {valor_inventario}")

def eliminar_producto():
    nombre = input("Inserte nombre del producto a eliminar: ")
    encontrado = False
    if not nombre.strip():
        print("Campo obligatorio.")
        return
    for producto in inventario:
        if producto["nombre"].lower().strip() == nombre.lower().strip():
            print(f"Esta seguro de que quiere eliminar {nombre} del inventario? (s/n)")
            respuesta = input().lower().strip()
            while respuesta not in ["s","n"]: 
                print("Respuesta no valida. Ingrese 's' para sí o 'n' para no.")
                respuesta = input().lower().strip()
            if respuesta == "s":
                inventario.remove(producto)
                print("Producto eliminado")
            elif respuesta == "n":
                print("Eliminacion cancelada")
                return
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado")

def buscar_producto():
    nombre = input("Inserte nombre del producto a buscar: ")
    if not nombre.strip():
        print("Campo obligatorio.")
        return
    for producto in inventario:
        if producto["nombre"].lower().strip() == nombre.lower().strip():
            print(f"{producto['nombre']} - ${producto['precio']} - Cantidad: {producto['cantidad']}")
            return
    print("Producto no encontrado")

def actualizar_producto():
    nombre = input("inserte su nombre del producto: ")
    if not nombre.strip():
        print("campo obligatorio")
        return
    encontrado = False   
    for producto in inventario:
        if producto["nombre"].lower().strip() == nombre.lower().strip():
            encontrado = True
            print(f"Desea actualizar la informacion de {nombre}? (s/n)")
            respuesta = input().lower().strip()
            while respuesta not in ["s", "n"]:
                    print("Respuesta no valida. Ingrese 's' para sí o 'n' para no.")
                    respuesta = input().lower().strip()
            if respuesta == "s":    
                    try:  
                        precio = float(input("Inserte precio del producto: "))
                        cantidad = int(input("Inserte cantidad del producto: "))
                    except ValueError:
                        print("Insertar numero:")
                        return
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor a cero")
                        return
                    if precio <= 0:
                        print("El precio debe ser mayor a cero")
                        return                    
                    producto["precio"] = precio
                    producto["cantidad"] = cantidad
            elif respuesta== "n":
                    return
    if not encontrado:
        print("Producto no encontrado")         

