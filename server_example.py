import DTPython

server = DTPython.DTPServer()

while True:
    message = server.listen()
    print(message)
