# Lab 6 - HTTP Request part 2


import socket

HOST =""
PORT = 8080
ENC = "ascii"


def main():
    #Skapa och starta servern (IPv4, TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server runnig on port {PORT}...(open http://localhost:{PORT}/)")

    #Server loop
    while True:
        #Vänta på klientanslutningar
        conn, addr = server.accept()
        print(f"\nConnection from {addr}")

        request = conn.recv(1024).decode(ENC, errors="ignore")
        if not request:
            conn.close()
            continue
        
        print("----Client Request Start----")
        print(request)
        print("----Client Request End----")

        #simple HTTP responseC
        html = f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<html>
<head><title>Lab 6 HTTP request</title></head>
<body>
<h2>Client Request: </h2>
<pre>{request}</pre>
</body>
</html>
"""
        conn.sendall(html.encode(ENC))
        conn.close()

if __name__ == "__main__":
    main()