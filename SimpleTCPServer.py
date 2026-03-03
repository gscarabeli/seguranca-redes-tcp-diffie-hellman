from socket import *
import random

# ==============================
# Função para testar número primo
# ==============================
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# ==============================
# Parâmetros Diffie-Hellman
# ==============================
P = 23
G = 5

if not is_prime(P):
    print("P não é primo! Encerrando...")
    exit()

# ==============================
# Cifra de César
# ==============================
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# ==============================
# Configuração do Servidor
# ==============================
serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print("Servidor TCP aguardando conexão...")

while True:
    conn, addr = serverSocket.accept()
    print("Conectado por:", addr)

    # Gera segredo privado aleatório
    private_a = random.randint(2, P-2)
    public_A = pow(G, private_a, P)

    # Recebe chave pública do cliente
    data_B = conn.recv(1024)
    public_B = int(str(data_B, "utf-8"))

    # Envia chave pública do servidor
    conn.send(bytes(str(public_A), "utf-8"))

    # Calcula chave compartilhada
    shared_key = pow(public_B, private_a, P)
    print("Chave Simétrica estabelecida:", shared_key)

    # Recebe mensagem criptografada
    received_bytes = conn.recv(65000)
    msg_encrypted = str(received_bytes, "utf-8")

    msg_decrypted = decrypt(msg_encrypted, shared_key)
    print("Mensagem recebida (decifrada):", msg_decrypted)

    # Responde ao cliente
    resposta = encrypt(msg_decrypted.upper(), shared_key)
    conn.send(bytes(resposta, "utf-8"))

    conn.close()