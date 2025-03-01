# Socket-Based Remote Command Executor

This project implements a **remote shell** using Python's **socket** library, where a server can accept commands from a client, execute those commands, and return the output. Additionally, it supports **file transfer** between the server and client.

The system is composed of two components:
1. **Server**: A Python-based TCP server that listens for incoming connections from the client. It sends commands (like `ls`, `cd`, etc.), and handles receiving the output or downloaded files
2. **Client**: A Python-based TCP client that connects to the server, and receive shell commands from the server. 

## Features
- **Remote Command Execution**: The server can send shell commands (such as `pwd`, `ls`, `cd`, etc.) to the client, and the client will execute the commands and return the results.
- **File Transfer**: The server can download files from the client using the `download` command.
- **Cross-Platform Support**: Works on both **Windows** and **Linux** systems.
- **Simple Communication Protocol**: The server and client communicate using TCP sockets, with a basic protocol for sending messages and receiving responses.

## Requirements
- Python 3.x
- No additional libraries are required (uses standard Python libraries like `socket`, `os`, `subprocess`, `pickle`)

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/zafarfast/remotecodeexecution.git
    ```

2. Change to the project directory:
    ```bash
    cd remotecodeexecution
    ```

3. No dependencies need to be installed, as this project only uses the Python standard library.

## Usage

### 1. Run the Server

To start the server, run the following command in your terminal:

```bash
python server.py
```
To start the server, run the following command in your terminal:


### Run the Client

In a separate terminal, run the following command to start the client:

```bash
python client.py
```

The client will automatically connect to the server. Once connected, you can send commands such as:

- **pwd: Get the current working directory of the server.
- **ls: List the files in the current directory of the server.
- **cd <directory>: Change the server's directory to <directory>.
- **download <file_path>: Download a file from the server.

### Example Interaction
## Server:

``` bash
[+] Server listening on port 7878...
[+] Connection established with ('127.0.0.1', 12345)
```

## Client connects to server:
```
bash
b'0000000136'
```



## Server Output:

```bash
received message length: 100
```

## Client sends back:

```bash
data: List of files in the current directory
```

### 3. Exiting the Server and Client
To exit the connection and shut down the servre, simply type exit at the server's prompt.

## Code Structure

- server.py: The main server script that handles incoming client connections, sends commands, and receives output.
- client.py: The main client script that connects to the server, sends output, and handles incoming commands.
- README.md: This file, explaining the project and its usage.

##How It Works

### Client:
- The client connects to the server and sends serialized data using the pickle library. Data is wrapped in a dictionary format to ensure structured communication.
- File transfers are handled by reading the file content and sending it to the servre in chunks.

### Server:
- The server sends commands, and receives the output from client
- The server uses the pickle library to deserialize received data.


## Example of Commands
Here are a few example commands that can be sent from the client:

- **ls**: List files in the current working directory on the server.
- **pwd**: Show the current directory on the server.
- **cd <directory>**: Change directory on the server (e.g., cd /home/user).
- **download <file_path>**: Download a file from the server (e.g., download /home/user/file.txt).
- **exit**: Close the connection between the client and server.

## Contributing
Contributions are welcome! If you want to improve the functionality or report a bug, please feel free to fork the repository, make changes, and create a pull request.

## License
This project is open-source and available under the MIT License.





