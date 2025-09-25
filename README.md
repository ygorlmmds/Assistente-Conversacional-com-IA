# Assistente Conversacional com IA

Este projeto é um **chat web interativo** que utiliza Flask no backend e OpenAI (GPT) para respostas inteligentes. O frontend é simples, com HTML, CSS e JavaScript, exibindo mensagens do usuário e respostas da IA em tempo real.

---

## Funcionalidades

- Chat web em tempo real
- Respostas da IA via OpenAI API
- Interface limpa e responsiva
- Tratamento de erros básico (cota de API, mensagens vazias)

---

## Pré-requisitos

- Python 3.10 ou superior
- Biblioteca Flask
- Biblioteca OpenAI (`pip install openai`)
- Bibliotecas adicionais: `python-dotenv` (opcional, para variáveis de ambiente)
- Key API da Openai própria 

---

## Como rodar

1. Clone o projeto:

git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto

2. Instale as dependências:

Copiar código:
pip install -r requirements.txt

3. Adicione sua chave openai api dentro do arquivo .env

 OPENAI_API_KEY = (sua chave)

4. Rode o "main.py"
