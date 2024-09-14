# client.py
import socket # Permite comunicación cliente- servidor

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creación objeto socket
    client.connect(('localhost', 9999)) # Conexión del socket cliente al servidor, especificando dirección IP y puerto

    while True: # Ciclo de menú principal
        print("Bienvenido a la guardería")
        print("\n1. Ver clientes")
        print("2. Agregar cliente")
        print("3. Ver servicios")
        print("4. Salir")

        choice = input("Elija una opción: ") # Guarda elección del usuario

        if choice == "1":
            client.send("VER_CLIENTES".encode('utf-8')) # Enviar solicitud
            response = client.recv(1024).decode('utf-8') # Recibir respuesta de servidor
            print(response) # Mostrar respuesta de servidor
        elif choice == "2":
            name = input("Ingrese nombre del cliente: ") # Pedir nombre cliente
            pet_name = input("Ingrese nombre de mascota: ") # Pedir nombre mascota
            client.send(f"AGREGAR_CLIENTE,{name},{pet_name}".encode('utf-8')) # Enviar solicitud
            response = client.recv(1024).decode('utf-8') # Recibir respuesta de servidor
            print(response) # Mostrar respuesta de servidor
        elif choice == "3":
            client.send("VER_SERVICIOS".encode('utf-8')) # Enviar solicitud
            response = client.recv(1024).decode('utf-8') # Recibir respuesta de servidor
            print(response) # Mostrar respuesta de servidor # Mostrar respuesta de servidor
        elif choice == "4":
            print("Hasta pronto!")
            client.close() # Cerrar conexión
            break # Romper ciclo
        else:
            print("Opción errada. Por favor intente nuevamente.")

if __name__ == "__main__": # Main, punto de entrada del programa
    start_client()
