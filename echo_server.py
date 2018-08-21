import socket


def setup_server():
    """

    :return:
    """
    # Instantiate a socket instant
    echo_server = socket.socket(
        socket.AF_INET,  # family
        socket.SOCK_STREAM,  # type
        socket.IPPROTO_TCP,  # proto
    )
    # Bind an endpoint (HOST, PORT) to the socket
    echo_server.bind(('127.0.0.1', '8000'))  # Expects a Tuples(immutable), Find an Endpoint
    # Activates a listener on the SOCKET!
    echo_server.listen(1)  # Acting like a while loop. Arg is listening for errors in any 1 client connection before break
    return echo_server, echo_server.accept()  # Return the server itself and Accept starts the server.


if __name__ == '__main__':
    server, (conn, addr) = setup_server()  # Tuple is the return of the Accept method.
    print('Received a client connections for {}'.format(addr))

    buffer_length = 16
    message_complete = False

    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode())
        if len(part) < buffer_length:
            break
    message = 'The server received your message!'
    conn.sendall(message.encode())

    conn.close()
    server.close()
