import inventario

opcion = ""

while opcion != "6":
    print("""
    === Gestor de Inventario ===

    1. Agregar producto
    2. Ver inventario
    3. Buscar producto
    4. Eliminar producto
    5. Actualizar producto
    6. Salir
    """)
    opcion = input("Elija una opcion: ")
    if opcion == "1":
        inventario.agregar_producto()
    elif opcion == "2":
        inventario.ver_inventario()
    elif opcion == "3":
        inventario.buscar_producto()
    elif opcion == "4":
        inventario.eliminar_producto()
    elif opcion == "5":
        inventario.actualizar_producto()
    elif opcion == "6":
        pass
    else:
        print("Opcion no valida")
print("Hasta luego!")
