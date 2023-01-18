from struct import pack, unpack

class Packet:

    @staticmethod
    def construct(size, id, buffer):
        return pack(f'2h {size}s', size, id, buffer)
    
    @staticmethod
    def extract_size(incoming_packet):
        return unpack('h', incoming_packet)
    
    @staticmethod
    def extract_pack(incoming_packet, size):
        return unpack(f'h {size}s', incoming_packet)
    
   