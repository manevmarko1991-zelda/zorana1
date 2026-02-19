import socket

# Server-Konfiguration
HOST = '127.0.0.1'  # IP-Adresse des Servers
PORT = 65432  # Port des Servers

# Client-Socket erstellen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # Verbindung herstellen
    client_socket.sendall(b"Hallo, Server!")  # Nachricht senden
    data = client_socket.recv(1024)  # Antwort empfangen

print(f"Antwort vom Server: {data.decode()}")
