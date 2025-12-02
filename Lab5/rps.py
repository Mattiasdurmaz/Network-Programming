#rps.py
#Lab 5 - Sockets: Rock-Paper-Scissors

import socket

PORT = 60003 # Port to use
ENC = "ascii"
VALID = {"R", "P", "S"}


def serversideGetPlaySocket():
    """Start server on Port and accept one connection. Return the connected socket."""
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP-socket
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("", PORT ))  # bind till alla lokala adresser, vald port
    srv.listen(1) 
    conn, _addr = srv.accept() # blockera tills en klient ansluter
    srv.close() 
    return conn

def clientsideGetPlaySocket(host):
    """Connect to server (host, PORT). Return the connecterd socket."""
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect((host, PORT)) # anslut till server
    return cli

def read_move() -> str:
    """Ask user for valid move (R/P/S). Re-promt until valid."""
    while True:
        mv = input().strip().upper()  # ta bort whitespace 
        if mv in VALID:
            return mv
        print("Invalid move, try again (R/P/S): ")


def decide_round(my, op) -> int:
    """return +1 if I win, -1 if I lose, 0 if tie
    R>S, S>P, P>R
    """

    if my == op:
        return 0
    wins = {("R", "S"), ("S", "P"), ("P", "R")}
    return 1 if (my, op) in wins else -1


def main():
    ans = "?"
    while ans not in {"C", "S"}:
        ans = input("Client or Server? (C/S): ").strip().upper()

    if ans == "S":
        sock = serversideGetPlaySocket()
    else:
        host = input("Enter server hostname or IP: ").strip()
        sock = clientsideGetPlaySocket(host)

    my_score = 0
    op_score = 0

    try:
        while my_score < 10 and op_score < 10:
            # print game stat and ask for move (player's points first)
            print(f"({my_score},{op_score}) Your move: ", end="", flush=True)

            # read/validate player's move
            my_move = read_move()

            # send player's move to opponent
            sock.sendall(my_move.encode(ENC))

            # receive opponent's move
            op_move = sock.recv(1024).decode(ENC).strip().upper()

            # decide round winner
            res = decide_round(my_move, op_move)

            # update scores
            res = decide_round(my_move, op_move)
            if res > 0:
                my_score += 1
            elif res < 0:
                op_score += 1
            
            # announce round result

            if my_score > op_score:
                print(f"You won this round! ({my_move} beats {op_move})")
            else:
                print(f"You lost this round! ({op_move} beats {my_move})")

    finally:
        # close socket
        try:
            sock.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        sock.close()

if __name__ == "__main__":
    main()