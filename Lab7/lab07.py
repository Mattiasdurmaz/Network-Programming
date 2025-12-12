#Lab 7 - Multiple clients wiht select (single-threaded)




import socket
import select


PORT = 60003
ENC  = "ascii"


def ftm_addr(sock: socket.socket) -> str:
    ip, port = sock.getpeername()
    return f"[{ip}:{port}]"


def broadcast(targets, msg: str, exclude=None):
    data =(msg + "\n").encode(ENC)
    for s in list(targets):
        if s is exclude:
            continue
        try:
            s.sendall(data)
        except Exception:
            try:
                s.close()
            finally:
                targets.remove(s)




def main():
    # lyssnarsocket
    sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockL.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockL.bind(("", PORT))
    sockL.listen(50)
    print(f"Server listening on port {PORT}")


    sockets = {sockL}  # alla sockets vi bevakar (lyssnare + klienter)


    try:
        while True:
            readable, _, _ = select.select(list(sockets), [], [])
            for sock in readable:
                if sock is sockL:
                    # ny klient
                    cli, _addr = sockL.accept()
                    sockets.add(cli)
                    print(f"Connection from {ftm_addr(cli)}")
                    broadcast(sockets - {sockL, cli}, f"{ftm_addr(cli)} has connected.")
                else:
                    # data/nerkoppling befintlig klient
                    try:
                        data = sock.recv(2048)
                    except ConnectionResetError:
                        data = b""
                   
                    if not data:
                        # disconnect
                        try:
                            who = ftm_addr(sock)
                        except Exception:
                            who = "[?:?]"
                        print(f"Disconnect from {who}")
                        sockets.discard(sock)
                        try:
                            sock.close()
                        finally:
                            pass
                        broadcast(sockets - {sockL}, f"{who} has disconnected.")
                    else:
                        msg = data.decode(ENC, errors="ingore").rstrip("\n\r")
                        who = ftm_addr(sock)
                        print(f"{who} {msg}")
                        broadcast(sockets - {sockL, sock}, f"{who} {msg}")
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        try:
            sockL.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()



