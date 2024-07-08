import socket
from mockClick import DataHandler

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    print("Server is listening on port 8080...")
    data_handler = DataHandler()

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break

                # 使用 DataHandler 处理数据
                data_handler.process_data(data)
                # client_socket.send("successed received data from client".encode('utf-8'))

            except ConnectionResetError:
                print("Client disconnected.")
                break
        
        client_socket.close()

if __name__ == "__main__":
    start_server()