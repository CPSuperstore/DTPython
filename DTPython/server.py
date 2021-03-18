from socket import *
import DTPython
import typing
import DTPython.coder as coder
import DTPython.message as message


class DTPServer:
    def __init__(self, port: int = None):
        self.port = DTPython.PORT if port is None else port

        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.bind(('', DTPython.PORT))

    def listen(self) -> typing.Tuple[message.Message, typing.Tuple[str, int]]:
        m = self.listen_raw()
        msg = coder.decode_message(m[0]).split("|")
        msg = message.Message(msg[0], msg[1])

        return msg, m[1]

    def listen_raw(self) -> typing.Tuple[bytes, typing.Tuple[str, int]]:
        m = self.s.recvfrom(1024)
        self.s.sendto(b'received', m[1])

        return m

    def close(self):
        self.s.close()
