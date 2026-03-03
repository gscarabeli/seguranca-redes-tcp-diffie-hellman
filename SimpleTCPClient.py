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
# Conexão com servidor
# ==============================
serverName = "10.1.70.22"  # Altere para o IP correto
serverPort = 1300

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# 1️⃣ Gera segredo privado aleatório
private_b = random.randint(2, P-2)
public_B = pow(G, private_b, P)

# 2️⃣ Envia chave pública B
clientSocket.send(bytes(str(public_B), "utf-8"))

# 3️⃣ Recebe chave pública A
data_A = clientSocket.recv(1024)
public_A = int(str(data_A, "utf-8"))

# 4️⃣ Calcula chave compartilhada
shared_key = pow(public_A, private_b, P)
print("Chave Simétrica estabelecida:", shared_key)

# 5️⃣ Envia mensagem criptografada
sentence = input("Digite a frase: ")
msg_to_send = encrypt(sentence, shared_key)
clientSocket.send(bytes(msg_to_send, "utf-8"))

# 6️⃣ Recebe resposta e decripta
resp_bytes = clientSocket.recv(65000)
resp_text = str(resp_bytes, "utf-8")

print("Resposta do Servidor:", decrypt(resp_text, shared_key))

clientSocket.close()