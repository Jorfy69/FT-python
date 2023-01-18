#MyServer client
import socket
from packet import Packet
import os
import sys

ip ='127.0.0.1'
port = 22222
filename = sys.argv[1]
file = open(filename, 'rb')
FileSize = os.path.getsize(filename)
filenamebytes = len(filename).to_bytes(len(filename), 'big')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.connect((ip, port))
    print(f"Connected to {ip, port}") 
    
    testpacket = Packet.construct(14, 1, b"this is a test")
    stream.send(testpacket)
    
    #NamePacket = Packet.construct(len(filename), 1, filenamebytes)
    #ContentsPacket = Packet.construct(FileSize, 2, file.read())
    #tream.send(NamePacket)
    #stream.send(ContentsPacket)
    