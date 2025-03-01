# Socket-Based Remote Command Executor

This project implements a **remote shell** using Python's **socket** library, where a server can accept commands from a client, execute those commands, and return the output. Additionally, it supports **file transfer** between the server and client.

The system is composed of two components:
1. **Server**: A Python-based TCP server that listens for incoming connections from the client. It can receive commands and execute them, then send the output or requested files back to the client.
2. **Client**: A Python-based TCP client that connects to the server, sends commands (like `ls`, `cd`, etc.), and handles receiving the output or downloaded files.

## Features
- **Remote Command Execution**: The client can send shell commands (such as `pwd`, `ls`, `cd`, etc.) to the server, and the server will execute the commands and return the results.
- **File Transfer**: The client can download files from the server using the `download` command.
- **Cross-Platform Support**: Works on both **Windows** and **Linux** systems.
- **Simple Communication Protocol**: The server and client communicate using TCP sockets, with a basic protocol for sending messages and receiving responses.

## Requirements
- Python 3.x
- No additional libraries are required (uses standard Python libraries like `socket`, `os`, `subprocess`, `pickle`)

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/remote-shell-server-client.git
    ```

2. Change to the project directory:
    ```bash
    cd remote-shell-server-client
    ```

3. No dependencies need to be installed, as this project only uses the Python standard library.

## Usage

### 1. Run the Server

To start the server, run the following command in your terminal:

```bash
python server.py
