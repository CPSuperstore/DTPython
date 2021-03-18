from socket import *

import DTPython
import DTPython.coder as coder


class DTPClient:
    def __init__(self, identifier: int, broadcast_address: str = "255.255.255.255", port: int = None):
        self.port = DTPython.PORT if port is None else port
        self.identifier = identifier
        self.broadcast_address = broadcast_address

        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    def broadcast_raw(self, message: bytes):
        self.s.sendto(message, (self.broadcast_address, self.port))

    def broadcast(self, message: str):
        message = "{}|{}".format(str(self.identifier), message)

        message = coder.encode_message(message)
        self.broadcast_raw(message)

    def await_response(self):
        return self.s.recvfrom(1024)

    def broadcast_await(self, message: str):
        self.broadcast(message)
        return self.await_response()
