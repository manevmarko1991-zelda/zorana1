import socket

# Client-Konfiguration
HOST = '127.0.0.1'
PORT = 12345


# Hauptfunktion des Clients
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))

        while True:
            choice = input('Enter seat number to reserve (e.g., A1) or type "LIST" to see available seats: ')
            client_socket.sendall(choice.encode('utf-8'))
            response = client_socket.recv(1024)
            print(response.decode('utf-8'))

    except Exception as e:
        print("Fehler:", e)

    finally:
        # Socket schließen, egal was passiert
        client_socket.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()

