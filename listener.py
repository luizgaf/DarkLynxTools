import socket

def start_server(host='127.0.0.1', port=65432):
    # Cria um socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Vincula o socket ao endereço e porta
        s.bind((host, port))
        # Habilita o servidor para aceitar conexões
        s.listen()
        print(f"Servidor escutando em {host}:{port}")
        
        while True:
            # Aceita uma nova conexão
            conn, addr = s.accept()
            with conn:
                print(f"Conexão estabelecida com {addr}")
                while True:
                    # Recebe dados do cliente
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Dados recebidos: {data.decode()}")
                    # Envia os dados de volta (eco)
                    conn.sendall(data)
                print(f"Conexão com {addr} encerrada")

if __name__ == "__main__":
    start_server()