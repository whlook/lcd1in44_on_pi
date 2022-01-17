#!/usr/bin/env python
import socket
def get_local_ip():
    try :
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(( '8.8.8.8' , 80 ))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        return "127.0.0.1"

if __name__ == "__main__" :
    local_IP = get_local_ip() 
    print(local_IP)
