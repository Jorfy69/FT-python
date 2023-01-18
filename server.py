#MyServer server
import socket
from packet import Packet
from time import sleep

ip = "127.0.0.1"
port = 22222

print(f"This is the Ip {ip} and this is the port {port}")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.bind((ip,port))                                         
    stream.listen()                                                 
    conn, addr = stream.accept()   
    with conn:
        print(f'{addr} connected')
        print('Reciving...')
        
        buffer = conn.recv(2)
        if not buffer:
            print("this failed")
        size = int(Packet.extract_size(buffer)[0])        
        buffer = conn.recv(size+2)
        s = Packet.extract_pack(buffer, size)
        PacketLists = [s, s]
        print(PacketLists[0] + PacketLists[1])