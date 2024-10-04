Introduction

Welcome to the repository!

This project is built upon several libraries and technologies, such as ZeroMQ (ZMQ), JSON, SymPy, and asyncio, designed to facilitate asynchronous client-server communication for executing operating system commands and mathematical expressions.
Project Overview

The primary libraries utilized in this project include:

  ZeroMQ (ZMQ): A high-performance asynchronous messaging library. It provides the foundation for message passing between the client and server, operating in a brokerless      architecture.
    JSON: Handles structured data by encoding and decoding JSON, the format in which commands are transmitted.
    SymPy: A symbolic computation library, utilized to evaluate mathematical expressions.
    asyncio: A core Python library that enables asynchronous programming, allowing the server to handle concurrent client requests using non-blocking IO operations via async and await.

Project Structure

This project consists of four core components:


  Server: Responsible for handling incoming commands and returning the appropriate response.
  Client: Sends JSON commands to the server and displays the results.
  Operation Files: Handle specific tasks, such as OS command execution and math computations.
  client_task_test:Handle a test and run project
  

Server Implementation

The server facilitates the ZeroMQ communication and processes two types of commands: OS commands and math expressions. It listens on the default localhost (127.0.0.1) at port 4000. Configuration options, including the port, are defined in config.py.

The server is implemented in an Object-Oriented Programming (OOP) approach, broken into the following key parts:

  Class AsyncServer: This class encapsulates the server functionality. The __init__ method initializes the server, setting up a ZMQ context and a REP (reply) socket to receive and respond to client requests.

  handle_request method: Continuously listens for incoming client requests, leveraging a while True loop to maintain responsiveness.

  process_command method: Parses the incoming JSON, determines the command type (OS or math), and processes it accordingly. This method also includes error handling to manage malformed requests or execution failures.

  Server Execution: Finally, an instance of AsyncServer is created, and the server starts its main loop.

Client Implementation

The client interacts with the server using ZMQ’s REQ (request) socket pattern.

  Class AsyncClient: The client functionality mirrors that of the server, with the exception that it uses a REQ socket for sending requests.

  send_command method: Sends a JSON-encoded command to the server and awaits a response. This method abstracts the client-server communication.

Operation Files

The project includes two primary operation files:

  Math Operations: Implemented using SymPy for symbolic and numeric evaluation of mathematical expressions.
  OS Operations: Utilizes Python's subprocess module to execute system-level commands (currently tailored for Windows environments).

client_task_test

  FunctionForSendAsynchronousCommand: Used for testing, this function generates sample commands and sends them to the server.

  Concurrency Handling: The client employs asyncio.gather to handle multiple concurrent commands, making use of Python's asynchronous capabilities for high efficiency.


Additional Features

This project leverages asynchronous programming to efficiently manage multiple client requests simultaneously. The server operates in non-blocking mode, ensuring responsiveness under load. For configuration adjustments, such as port changes, modifications can be made easily in the corresponding config.py file.
Getting Started

To set up the project:

   Start the server by running:


    python server.py

To run the client test and send commands, use:


    python client_task_test.py

Test commands can be written directly into the client_task_test.py file.
Programming Language and Dependencies

This project requires Python 3.8 or higher. Below are the dependencies:

    Python 3.8+: Ensure you have Python version 3.8 or later installed.

   Required Libraries:
    pyzmq: Python bindings for ZeroMQ. Install via:


    pip install pyzmq

sympy: For symbolic mathematics. Install via:

    pip install sympy

asyncio: Built into Python 3.3+; no separate installation required.
json: Built-in to Python for handling JSON data.
