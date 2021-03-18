import DTPython

client = DTPython.DTPClient(DTPython.get_formatted_mac_address())

print(client.broadcast_await("1.3, 2.2, 3.1\n4.6, 5.5, 6.4"))
