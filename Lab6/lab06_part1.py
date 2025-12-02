# Lab 6 - HTTP Request part 1

import socket


HOST =""
PORT = 8080
ENC = "ascii"


def main():

    #skapa socket (ipv4, tcp)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #återanvänd adress
    server.bind((HOST, PORT)) #binda till adress och port
    server.listen(5) #lyssna efter anslutningar, max 5 i kö
    print(f"Server runnig on port {PORT}...(open http://localhost:{PORT}/)")

    #server loop
    while True:
        conn, addr = server.accept()
        print(f"\nConnection from {addr}")
        data = conn.recv(1024).decode(ENC, errors="ignore")
        if data:
           print("----Client Request Start----")
           print(data)
           print("----Client Request End----")
           conn.close()


if __name__ == "__main__":
    main()

