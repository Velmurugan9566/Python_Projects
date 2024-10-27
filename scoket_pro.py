import pyqrcode
from pyqrcode import QRCode
site="facebook.com"
getqr=pyqrcode.create(site)
getqr.svg("qrcode.svg",scale=10)
import socket
host=socket.gethostname()
ipadd=socket.gethostbyname(host)
print(host)
print(ipadd)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('server_ip', server_port)
client_socket.connect(server_address)
while True:
    # Send a message to the server
    message_to_send = input("Enter your message: ")
    client_socket.send(message_to_send.encode())

    # Receive a message from the server
    received_message = client_socket.recv(1024).decode()
    print("Server:", received_message)

