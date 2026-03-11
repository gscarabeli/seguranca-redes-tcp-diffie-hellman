# 🔐 Secure TCP Communication – RSA + Diffie-Hellman + Caesar Cipher

Este projeto implementa um **sistema de comunicação segura cliente-servidor em Python utilizando sockets TCP**.

A segurança da comunicação é construída em **três camadas criptográficas**:

1. **RSA (4096 bits)** – protege a troca de chaves do Diffie-Hellman
2. **Diffie-Hellman** – gera uma chave simétrica compartilhada
3. **Cifra de César em bytes UTF-8** – criptografa as mensagens trocadas

---

# 📁 Estrutura do Projeto

```text
.
├── SimpleTCPServer.py
├── SimpleTCPClient.py
└── README.md
```

### SimpleTCPServer.py

Responsável por:

* iniciar o servidor TCP
* realizar a troca segura de chaves
* descriptografar a mensagem do cliente
* responder ao cliente

### SimpleTCPClient.py

Responsável por:

* conectar ao servidor
* participar do handshake criptográfico
* criptografar a mensagem
* enviar e receber respostas

---

# 🔐 Arquitetura de Segurança

O projeto utiliza um modelo de **criptografia híbrida**, combinando criptografia assimétrica e simétrica.

## 1️⃣ Proteção com RSA (4096 bits)

O RSA é utilizado **somente para proteger a troca das chaves públicas do Diffie-Hellman**.

As chaves são geradas a partir de dois primos grandes:

```text
p (4096 bits)
q (4096 bits)
```

A partir deles são calculados:

```text
n = p × q
φ(n) = (p − 1)(q − 1)
e = 65537
d = e⁻¹ mod φ(n)
```

Fluxo:

```text
Cliente → RSA(public_B)
Servidor → RSA(public_A)
```

Isso impede ataques **Man-in-the-Middle** durante a troca de chaves.

---

## 2️⃣ Diffie-Hellman – Geração da chave compartilhada

Após a proteção com RSA, cliente e servidor executam o protocolo Diffie-Hellman.

Parâmetros utilizados:

```text
P = 23
G = 5
```

Cada lado gera um número secreto usando o módulo seguro do Python:

```python
secrets.randbelow()
```

Cálculo das chaves públicas:

```text
public_A = G^a mod P
public_B = G^b mod P
```

Chave compartilhada:

```text
shared_key = public_key^private_key mod P
```

Essa chave é usada como **shift da cifra de César**.

---

## 3️⃣ Cifra de César em bytes (UTF-8)

Após a geração da chave simétrica, as mensagens são criptografadas usando uma **variação da cifra de César aplicada diretamente aos bytes UTF-8**.

Processo:

1. A mensagem é convertida para bytes UTF-8
2. Cada byte recebe um deslocamento (`shift`)
3. O resultado é transmitido pela rede

Exemplo conceitual:

```text
byte_original + shared_key mod 256
```

Isso permite suportar qualquer caractere UTF-8, incluindo:

```text
ç ã é ê ó ü etc
```

---

# 🔄 Fluxo da Comunicação

```text
CLIENTE                          SERVIDOR
   │                                 │
   │ RSA(public_B) ─────────────────►│
   │                                 │
   │◄──────────────── RSA(public_A)  │
   │                                 │
   │   Diffie-Hellman handshake      │
   │   shared_key gerada             │
   │                                 │
   │ César(msg) ────────────────────►│
   │                                 │
   │◄──────────────── César(resp)    │
```

---

# 🖥️ Como Executar

## 1️⃣ Iniciar o servidor

```bash
python SimpleTCPServer.py
```

Saída esperada:

```text
Servidor aguardando conexão...
```

---

## 2️⃣ Executar o cliente

```bash
python SimpleTCPClient.py
```

Exemplo de execução:

```text
Chave simétrica: 17
Digite a mensagem: ola servidor
Resposta do servidor: OLA SERVIDOR
```

---

# ⚙️ Tecnologias Utilizadas

* Python 3
* TCP Sockets
* RSA (4096 bits)
* Diffie-Hellman
* Cifra de César em bytes
* Biblioteca `secrets` para geração de números aleatórios criptograficamente seguros

---

# 👨‍💻 Autores

* **Gustavo Correia Scarabeli**
* **Matheus Andrade de Oliveira**
* **Artur Rossi Júnior**
* **Gustavo Correa Pedro de Carvalho**
