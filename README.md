# 🔐 TCP Secure Chat com Diffie-Hellman e Cifra de César

Projeto desenvolvido para a disciplina de Segurança da Informação.

## 📌 Objetivo

Implementar uma comunicação cliente-servidor utilizando:

- Socket TCP em Python
- Cifra de César (implementação autoral)
- Algoritmo de Diffie-Hellman para troca de chave simétrica
- Teste de número primo para validação do parâmetro P
- Análise de tráfego com Wireshark

---

## 🏗️ Estrutura do Projeto

```
.
├── SimpleTCPServer.py
├── SimpleTCPClient.py
└── README.md
```

---

## 🔄 Funcionamento

### 1️⃣ Troca de Chaves (Diffie-Hellman)

- Cliente e servidor geram chaves privadas aleatórias
- Trocam chaves públicas
- Calculam independentemente a mesma chave simétrica

### 2️⃣ Criptografia

A chave compartilhada é utilizada como deslocamento (shift) na Cifra de César.

Fluxo:

1. Cliente cifra a mensagem
2. Servidor decifra
3. Servidor responde cifrando novamente
4. Cliente decifra a resposta

---

## 🔢 Validação de Número Primo

Foi implementada função para teste de primalidade:

- Garante que o número P utilizado no Diffie-Hellman é primo
- Condição necessária para funcionamento correto do algoritmo

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Socket TCP
- Wireshark

---

## ▶️ Como Executar

### 1. No servidor:

```bash
python SimpleTCPServer.py
```

### 2. No cliente:

Editar o IP do servidor no arquivo:

```python
serverName = "IP_DO_SERVIDOR"
```

Executar:

```bash
python SimpleTCPClient.py
```

---

## 📊 Teste no Wireshark

Durante a execução é possível observar:

- Handshake TCP (SYN, SYN-ACK, ACK)
- Troca de chaves públicas
- Mensagens cifradas trafegando na rede

---

## 🎥 Demonstração

Link do vídeo demonstrando o funcionamento:

https://youtu.be/ljKbw0VP-0I
---

## 👨‍💻 Autor

Gustavo Correia Scarabeli  
Matheus Andrade de Oliveira
Artur Rossi Júnior
Gustavo Correa Pedro de Carvalho
