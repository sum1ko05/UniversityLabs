from typing import Protocol
import socket
from datetime import datetime


class LogHandlerProtocol(Protocol):
    def handle(self, message: str):
        ...

class FileLogHandler(LogHandlerProtocol):
    def __init__(self, path: str):
        self.path = path

    def handle(self, message: str):
        with open(self.path, 'a') as file:  # File will be created if we don't find it
            file.write(f'{datetime.now().isoformat()}: \t {message}\n')

class SocketLogHandler(LogHandlerProtocol):
    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port

    def handle(self, message: str):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))
                sock.sendall(f'{str(datetime.now().isoformat())}: \t {message}\n'.encode('utf-8'))
        except Exception as error:
            print(f'Socket error: {error}')

class ConsoleLogHandler(LogHandlerProtocol):
    def __init__(self):
        pass  # No properties needed

    def handle(self, message: str):
        print(f'{datetime.now().isoformat()}: \t {message}')

class SysLogHandler(LogHandlerProtocol):
    # Not implemented
    pass
        