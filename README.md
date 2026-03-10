# 🔐 TCP Secure Chat com RSA, Diffie-Hellman e Cifra de César

Projeto desenvolvido para a disciplina de **Segurança da Informação**.

---

# 📌 Objetivo

Implementar uma comunicação **cliente-servidor segura** utilizando:

* **Socket TCP em Python**
* **RSA (implementação autoral)** para proteção da troca de chaves
* **Diffie-Hellman** para geração de chave simétrica
* **Cifra de César (implementação autoral)** para criptografia das mensagens
* **primo_hyper** para geração eficiente de números primos de **4096 bits**
* **Análise de tráfego com Wireshark**

---

# 🏗️ Estrutura do Projeto

```
.
├── SimpleTCPServer.py
├── SimpleTCPClient.py
└── README.md
```

---

# 🔄 Funcionamento do Sistema

A comunicação segura ocorre em **três etapas principais**.

---

# 1️⃣ Proteção da troca de chaves com RSA

Cada lado gera um par de chaves RSA:

* **Chave pública**
* **Chave privada**

As chaves públicas do **Diffie-Hellman** são **criptografadas usando RSA** antes de serem enviadas pela rede.

Isso impede que um atacante obtenha as chaves públicas diretamente ao analisar o tráfego.

Fluxo:

```
Cliente gera B (Diffie-Hellman)
↓
Cliente cifra B com RSA
↓
Servidor recebe B criptografado
↓
Servidor decifra usando RSA
```

---

# 2️⃣ Troca de Chaves (Diffie-Hellman)

Após a proteção com RSA, ocorre o **processo Diffie-Hellman**.

Cliente e servidor:

1. Geram um segredo privado
2. Calculam suas chaves públicas
3. Trocam as chaves públicas protegidas por RSA
4. Calculam a **mesma chave simétrica compartilhada**

Essa chave é utilizada para cifrar as mensagens.

---

# 3️⃣ Criptografia das Mensagens (Cifra de César)

A **chave simétrica gerada pelo Diffie-Hellman** é utilizada como deslocamento na **Cifra de César**.

Fluxo da comunicação:

```
Cliente cifra mensagem
↓
Mensagem enviada ao servidor
↓
Servidor decifra mensagem
↓
Servidor responde cifrando novamente
↓
Cliente decifra a resposta
```

---

# 🔢 Geração de Números Primos (4096 bits)

Para atender aos requisitos de segurança do projeto, o algoritmo **RSA utiliza números primos de 4096 bits**.

A geração desses primos é realizada utilizando o módulo:

```
primo_hyper.py
```

Esse módulo fornece um gerador eficiente de números primos grandes, permitindo a criação das chaves RSA.

---

# 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Socket TCP**
* **RSA (implementação autoral)**
* **Diffie-Hellman**
* **Cifra de César**
* **primo_hyper (geração de primos 4096 bits)**
* **Wireshark**

---

# ▶️ Como Executar

## 1️⃣ Executar o servidor

```bash
python SimpleTCPServer.py
```

O servidor ficará aguardando conexões.

---

## 2️⃣ Configurar o cliente

Editar o IP do servidor no arquivo:

```python
serverName = "IP_DO_SERVIDOR"
```

---

## 3️⃣ Executar o cliente

```bash
python SimpleTCPClient.py
```

---

# 📊 Teste com Wireshark

Durante a execução é possível observar no Wireshark:

* **Handshake TCP**

  * SYN
  * SYN-ACK
  * ACK

* **Troca de chaves Diffie-Hellman protegidas com RSA**

* **Mensagens cifradas utilizando Cifra de César**

Filtro recomendado:

```
tcp.port == 1300
```

---

# 🔒 Camadas de Segurança Implementadas

| Camada | Algoritmo      | Função                      |
| ------ | -------------- | --------------------------- |
| 1      | RSA            | Proteção da troca de chaves |
| 2      | Diffie-Hellman | Geração de chave simétrica  |
| 3      | Cifra de César | Criptografia das mensagens  |

---

# 👨‍💻 Autores

**Gustavo Correia Scarabeli**
**Matheus Andrade de Oliveira**
**Artur Rossi Júnior**
**Gustavo Correa Pedro de Carvalho**
