import socket

# Server-Konfiguration
HOST = '127.0.0.1'
PORT = 12345
SEATS = {'A1': False, 'A2': False, 'A3': False, 'B1': False, 'B2': False, 'B3': False}  # Datenzugriffsschicht


# Funktion zum Bearbeiten eingehender Nachrichten (Logikschicht)
def handle_message(client_socket, message):
    # [('A1', False), ('A2', True), ('A3', False), ('B1', False), ('B2', True), ('B3', False)]
    # ['A1', 'A3', 'B1', 'B3']
    # Alternative:
    # available_seats = []
    # for seat, reserved in SEATS.items():
    #     if not reserved:
    #         available_seats.append(seat)
    if message == "LIST":
        available_seats = [seat for seat, reserved in SEATS.items() if not reserved]  # List Comprehension
        response = "Available seats: " + ", ".join(available_seats) if available_seats else "No seats available!"
        client_socket.sendall(response.encode('utf-8'))
    elif message in SEATS:
        if not SEATS[message]:
            SEATS[message] = True  # Reservierung des Sitzplatzes (Datenzugriffsschicht)
            client_socket.sendall(b'Seat reserved successfully!')
        else:
            client_socket.sendall(b'Seat already reserved!')
    else:
        client_socket.sendall(b'Invalid seat number!')


# Hauptfunktion des Servers
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print('Server started. Waiting for connections...')

    while True:
        client_socket, addr = server_socket.accept()
        print('Connected to', addr)

        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8').strip()
                handle_message(client_socket, message)


if __name__ == "__main__":
    main()
