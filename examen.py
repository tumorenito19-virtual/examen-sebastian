productos_almacen = {
    "EstanteríaA": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5}, 
                     {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}],
    "EstanteríaB": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5},
                     {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}],
    "EstanteríaC": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0},
                     {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "EstanteríaD": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8},
                     {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}]
}

def agregar_producto(productos_almacen):
    # Solicitar al usuario los detalles del nuevo producto
    nombre = input("Introduce el nombre del producto: ")
    cantidad = int(input("Introduce la cantidad del producto: "))
    precio = float(input("Introduce el precio del producto: "))
    estanteria = input("Introduce la estantería donde se guardará el producto: ")
    
    # Verificar si la estantería existe en el almacén
    if estanteria in productos_almacen:
        # Crear el diccionario del nuevo producto
        nuevo_producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        
        # Agregar el producto a la lista de esa estantería
        productos_almacen[estanteria].append(nuevo_producto)
        
        # Mensaje de confirmación
        print(f"Producto '{nombre}' agregado correctamente en la {estanteria}.")
    else:
        # Mostrar un mensaje de error si la estantería no existe
        print(f"Error: La estantería '{estanteria}' no existe en el almacén.")

# Llamada a la función para agregar un nuevo producto
#agregar_producto(productos_almacen)

def retirar_producto(productos_almacen):
    # Solicitar al usuario los detalles del producto a retirar
    nombre = input("Introduce el nombre del producto a retirar: ")
    cantidad_retirar = int(input("Introduce la cantidad a retirar: "))
    
    # Variable para rastrear si el producto fue encontrado
    producto_encontrado = False
    
    # Buscar el producto en todas las estanterías
    for estanteria, productos in productos_almacen.items():
        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():
                producto_encontrado = True
                if producto["cantidad"] >= cantidad_retirar:
                    # Retirar la cantidad especificada
                    producto["cantidad"] -= cantidad_retirar
                    print(f"Se han retirado {cantidad_retirar} unidades de '{nombre}' de la {estanteria}.")
                    if producto["cantidad"] == 0:
                        # Eliminar el producto de la lista si la cantidad es 0
                        productos.remove(producto)
                    return  # Salir de la función después de retirar el producto
                else:
                    # Si la cantidad es insuficiente, mostrar un mensaje de error
                    print(f"Error: No hay suficiente cantidad de '{nombre}'. Disponible: {producto['cantidad']}.")
                    return

    # Si el producto no fue encontrado en ninguna estantería
    if not producto_encontrado:
        print(f"Error: El producto '{nombre}' no se encuentra en el almacén.")

# Llamada a la función para retirar un producto
#retirar_producto(productos_almacen)

def buscar_producto(productos_almacen):
    # Solicitar al usuario el nombre del producto a buscar
    nombre = input("Introduce el nombre del producto a buscar: ")
    
    # Variable para rastrear si el producto fue encontrado
    producto_encontrado = False
    
    # Búsqueda lineal en el almacén
    for estanteria, productos in productos_almacen.items():
        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():
                # Si el producto se encuentra, mostrar la cantidad y ubicación
                print(f"Producto '{nombre}' encontrado en {estanteria}. Cantidad disponible: {producto['cantidad']}.")
                producto_encontrado = True
    
    # Si el producto no se encontró en ninguna estantería
    if not producto_encontrado:
        print(f"El producto '{nombre}' no se encuentra en el almacén.")

# Llamada a la función para buscar un producto
#buscar_producto(productos_almacen)
def estado_almacen(productos_almacen):
    # Variable para llevar el valor total de todo el almacén
    valor_total_almacen = 0
    
    # Recorrer cada estantería en el almacén
    for estanteria, productos in productos_almacen.items():
        print(f"\n{estanteria}:")
        print(f"  Número de productos: {len(productos)}")
        
        # Variable para llevar el valor total de cada estantería
        valor_total_estanteria = 0
        
        # Recorrer cada producto en la estantería
        for producto in productos:
            cantidad = producto["cantidad"]
            precio = producto["precio"]
            valor_total_producto = cantidad * precio
            valor_total_estanteria += valor_total_producto
            
            print(f"    - {producto['nombre']}:")
            print(f"      Cantidad: {cantidad}")
            print(f"      Precio por unidad: {precio}")
            print(f"      Valor total del producto: {valor_total_producto}")
        
        # Sumar el valor total de la estantería al valor total del almacén
        valor_total_almacen += valor_total_estanteria
        print(f"  Valor total de la {estanteria}: {valor_total_estanteria}")
    
    # Mostrar el valor total del almacén
    print(f"\nValor total de todos los productos en el almacén: {valor_total_almacen}")

# Llamada a la función para mostrar el estado del almacén
#estado_almacen(productos_almacen)
def transferir_producto(productos_almacen):
    # Pedir al usuario los datos necesarios
    nombre_producto = input("Introduce el nombre del producto a transferir: ")
    cantidad = int(input("Introduce la cantidad a transferir: "))
    estanteria_origen = input("Introduce la estantería de origen: ")
    estanteria_destino = input("Introduce la estantería de destino: ")
    
    # Verificar si las estanterías de origen y destino existen
    if estanteria_origen not in productos_almacen:
        print(f"Error: La estantería de origen '{estanteria_origen}' no existe.")
        return
    if estanteria_destino not in productos_almacen:
        print(f"Error: La estantería de destino '{estanteria_destino}' no existe.")
        return
    
    # Buscar el producto en la estantería de origen
    producto_encontrado = None
    for producto in productos_almacen[estanteria_origen]:
        if producto["nombre"] == nombre_producto:
            producto_encontrado = producto
            break
    
    # Verificar si el producto existe en la estantería de origen
    if not producto_encontrado:
        print(f"Error: El producto '{nombre_producto}' no se encuentra en la estantería de origen '{estanteria_origen}'.")
        return
    
    # Verificar si hay suficiente cantidad para transferir
    if producto_encontrado["cantidad"] < cantidad:
        print(f"Error: No hay suficiente cantidad de '{nombre_producto}' en la estantería de origen '{estanteria_origen}'.")
        return

    # Reducir la cantidad en la estantería de origen
    producto_encontrado["cantidad"] -= cantidad
    
    # Si la cantidad llega a cero, eliminar el producto de la estantería de origen
    if producto_encontrado["cantidad"] == 0:
        productos_almacen[estanteria_origen].remove(producto_encontrado)
    
    # Buscar o agregar el producto en la estantería de destino
    producto_destino = None
    for producto in productos_almacen[estanteria_destino]:
        if producto["nombre"] == nombre_producto:
            producto_destino = producto
            break
    
    if producto_destino:
        # Si el producto ya existe en la estantería de destino, aumentar la cantidad
        producto_destino["cantidad"] += cantidad
    else:
        # Si el producto no existe en la estantería de destino, agregarlo
        nuevo_producto = {
            "nombre": nombre_producto,
            "cantidad": cantidad,
            "precio": producto_encontrado["precio"]  # Mantener el mismo precio
        }
        productos_almacen[estanteria_destino].append(nuevo_producto)
    
    # Mensaje de confirmación
    print(f"Producto '{nombre_producto}' transferido exitosamente de '{estanteria_origen}' a '{estanteria_destino}'.")
    print("\nContenido actualizado del almacén:")
    for estanteria, productos in productos_almacen.items():
        print(f"{estanteria}: {productos}")
    

    

# Llamada a la función para transferir un producto
#transferir_producto(productos_almacen)

# Mostrar el contenido actualizado del almacén



def analizar_estanterias(productos_almacen):
    # Inicializar variables para almacenar resultados
    estanteria_mayor_valor = None
    valor_maximo = 0
    estanteria_menos_productos = None
    min_productos = float('inf')

    # Recorrer cada estantería
    for estanteria, productos in productos_almacen.items():
        # Calcular el valor total de los productos en la estantería actual
        valor_total_estanteria = sum(producto["cantidad"] * producto["precio"] for producto in productos)
        
        # Actualizar si encontramos una estantería con mayor valor acumulado
        if valor_total_estanteria > valor_maximo:
            valor_maximo = valor_total_estanteria
            estanteria_mayor_valor = estanteria

        # Contar el número de productos en la estantería actual
        total_productos = len(productos)
        
        # Actualizar si encontramos una estantería con menos productos
        if total_productos < min_productos:
            min_productos = total_productos
            estanteria_menos_productos = estanteria

    # Retornar los resultados
    return estanteria_mayor_valor, estanteria_menos_productos

# Llamada a la función con el diccionario productos_almacen
estanteria_valor, estanteria_menos_prod = analizar_estanterias(productos_almacen)
print("Estantería con mayor valor acumulado:", estanteria_valor)
print("Estantería con menos productos:", estanteria_menos_prod)
