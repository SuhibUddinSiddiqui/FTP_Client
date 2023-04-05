import socket

class get_ip:
    def get_current_ip(a):
        ip =socket.gethostbyname(socket.gethostname())
        print(ip)



