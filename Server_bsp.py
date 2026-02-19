import socket

# Server konfigurieren
HOST = '127.0.0.1'  # Lokale IP-Adresse
PORT = 65432  # Port für die Verbindung

# Server-Socket erstellen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # IP und Port binden
    server_socket.listen()  # Auf Verbindungen warten
    print(f"Server läuft auf {HOST}:{PORT} und wartet auf Verbindungen...")

    conn, addr = server_socket.accept()  # Verbindung akzeptieren
    with conn:
        print(f"Verbunden mit {addr}")
        while True:
            data = conn.recv(1024)  # Daten empfangen (maximal 1024 Bytes)
            if not data:
                break
            print(f"Empfangen: {data.decode()}")
            conn.sendall(b"Nachricht vom Server erhalten!")  # Antwort senden
