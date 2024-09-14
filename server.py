import socket # Permite comunicación cliente - servidor
import threading # Permite manejar varios clientes al tiempo

customers = [] # Lista para almacenar clientes
services = [ # Lista para almacenar servicios (en este caso están pre-definidos porque el cliente no tiene porqué añadir servicios)
    {'nombre_servicio': 'Baño', 'precio': 20},
    {'nombre_servicio': 'Corte', 'precio': 30}
]

def handle_client(client_socket): # Manejar conexiones de clientes de forma individual
    while True: # Iniciar ciclo de interacción cliente - servidor
        try:
            request = client_socket.recv(1024).decode('utf-8') # Recibir mensaje de cliente
            if request == 'VER_CLIENTES':
                response = '\n'.join([f"Cliente: {c['nombre']}, Mascota: {c['nombre_mascota']}" for c in customers]) or "No hay clientes todavía." # Ver todos los clientes al tiempo en un solo mensaje atravesando la lista de clientes
            elif request.startswith('AGREGAR_CLIENTE'):
                _, name, pet_name = request.split(',') # Separar el mensaje para extraer datos del cliente y mascota
                customers.append({'nombre': name, 'nombre_mascota': pet_name}) # Añadir datos de cliente a la lista
                response = f"{name} y {pet_name} han sido añadidos exitosamente." # Notificación de proceso exitoso
            elif request == 'VER_SERVICIOS':
                response = '\n'.join([f"Servicio: {s['nombre_servicio']}, Precio: ${s['precio']}" for s in services]) # Ver todos los servicios al tiempo en un solo mensaje atravesando la lista de servicios
            else:
                response = "Solicitud errada."

            client_socket.send(response.encode('utf-8')) # Enviar respuesta al cliente
        except:
            break # Romper el ciclo en caso de que ocurra algún error

    client_socket.close() # Cerrar la conexión

def start_server(): # Inicializar el servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creación objeto socket
    server.bind(('localhost', 9999)) # Usamos localhost para habilitar conexiones únicamente desde la misma máquina
    server.listen(5) # Limitamos el número de conexiones a 5
    print("Servidor escuchando en el puerto 9999") # Notificar que el puerto está abierto

    while True: # Ciclo para aceptar las conexiones de los clientes
        client_socket, addr = server.accept() # Aceptar la conexión
        print(f"Conexión aceptada desde {addr}") # Notificar conexión aceptada desde qué dirección IP y qué puerto
        client_handler = threading.Thread(target=handle_client, args=(client_socket,)) # Crear hilo para manejar conexión del cliente de forma independiente
        client_handler.start() # Inicializar hilo

if __name__ == "__main__": # Main, punto de entrada del programa
    start_server()
