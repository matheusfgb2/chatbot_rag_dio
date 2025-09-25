# Guia de Instalação e Execução do Assistente com Ollama

## 1. Objetivo

Este guia tem como finalidade instruir a instalação e execução do assistente técnico com base em Ollama e Streamlit, sem o uso de contêineres Docker. A abordagem visa desempenho otimizado e maior controle sobre os recursos da máquina local.

---

## 2. Etapas de Instalação

### a) Instalação do Ollama

**Windows**  
Baixe e instale via: [https://ollama.com/download](https://ollama.com/download)

**Linux/macOS**  
Execute no terminal:

```
curl -fsSL https://ollama.com/install.sh | sh
```

Após a instalação, baixe o modelo de linguagem:

```
ollama pull llama3.1
```

> **Importante:**  
> O Ollama precisa estar rodando em segundo plano para que o assistente funcione corretamente.  
> Você pode iniciar o serviço manualmente com o comando abaixo, em um terminal separado:

```
ollama serve
```

---

### b) Criação e ativação do ambiente virtual

> **Observação:**  
> Os próximos passos devem ser feitos na pasta /app deste projeto (cd app).

**Windows (CMD)**

```
python -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell)**

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS**

```
python3 -m venv .venv
source .venv/bin/activate
```

---

### c) Instalação das dependências

```
pip install -r requirements.txt
```

> **Observação:**  
> A instalação dos pacotes pode demorar alguns minutos, especialmente em máquinas com conexão lenta ou sem cache local.  
> Isso ocorre porque o projeto depende de bibliotecas pesadas como `langchain`, `transformers`, `sentence-transformers`, `streamlit`, entre outras.  
> Algumas dessas bibliotecas também instalam subdependências como `torch`, que podem ultrapassar 500 MB e exigir compilação parcial dependendo do sistema.  
> O tamanho aproximado de todos os pacotes é de `2GB`.

---

## 3. Execução do Assistente

Para iniciar o sistema, execute:

```
streamlit run app.py
```

> **Observação:**  
> Ao acessar o endereço no navegador, é normal que a tela fique preta ou carregando por alguns segundos.
> Isso ocorre porque o modelo está sendo carregado na memória e inicializado em tempo real.
> Esse processo pode ser mais demorado em máquinas sem GPU ou com recursos limitados, especialmente na primeira execução.

> **Importante:**  
> Se o erro abaixo aparecer após o envio da pergunta é porque o o ollama não está sendo executado. Execute-o através do comando `ollama serve`, em um terminal separado.  
> `❌ Erro ao gerar resposta: [WinError 10061] Nenhuma conexão pôde ser feita porque a máquina de destino as recusou ativamente`

A interface estará disponível em:

```
http://localhost:8501
```

---

## 4. Desativação do Ambiente Virtual

Para encerrar o ambiente virtual:

```
deactivate
```

---

## 5. Considerações Finais

A execução fora do Docker elimina o overhead de contêineres e permite melhor aproveitamento dos recursos da máquina. Essa abordagem é recomendada para ambientes locais com foco em desempenho e controle.

> **Observação:**  
> Mantenha o modelo previamente baixado e o ambiente virtual ativo para garantir inicialização rápida e respostas consistentes.  
> Certifique-se de que o Ollama esteja rodando em segundo plano antes de iniciar o assistente.
