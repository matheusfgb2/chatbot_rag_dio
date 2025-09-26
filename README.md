# 🏠 Assistente Técnico Minha Casa Minha Vida

> **Este projeto foi desenvolvido como parte do bootcamp da DIO: Microsoft Certification Challenge #4 - DP 100.**

Este projeto desenvolve um assistente inteligente da **Caixa Econômica Federal** capaz de responder dúvidas sobre financiamento habitacional, uso do FGTS, contratos, etapas do programa e regras operacionais do Minha Casa Minha Vida. O sistema utiliza **Recuperação Aumentada por Geração (RAG)** para garantir respostas fundamentadas em documentos oficiais.

---

## 📌 Objetivo

Oferecer uma solução institucional que torne o acesso à informação mais ágil e confiável, especialmente em contextos operacionais e sociais. A técnica de RAG garante que as respostas estejam sempre baseadas em documentos oficiais da Caixa.

---

## 🧩 Estrutura do Projeto

    ├── app/                 # Pasta principal do projeto
    │   ├── app.py           # Interface Streamlit
    │   ├── rag_core.py      # Núcleo RAG: embeddings, FAISS, LLM e cadeia de resposta
    │   ├── config.py        # Configurações centrais
    │   ├── index_mcmv/      # Índice FAISS já construído
    │   ├── documentos/      # Base de conhecimento (PDFs e DOCXs)
    │   └── requirements.txt # Lista de dependências

---

## ⚙️ Tecnologias Utilizadas

| Ferramenta/Biblioteca     | Finalidade                                     |
| ------------------------- | ---------------------------------------------- |
| **LangChain**             | Pipeline RAG e integração com o modelo         |
| **FAISS**                 | Indexação vetorial e busca semântica           |
| **Sentence Transformers** | Geração de embeddings semânticos               |
| **Ollama**                | Execução local do modelo de linguagem          |
| **Streamlit**             | Interface web interativa para o usuário        |
| **Python**                | Linguagem base para desenvolvimento do sistema |

---

## 🚀 Instalação e Execução

### 1. Clone o repositório

    git clone https://github.com/matheusfgb2/chatbot_rag_dio.git
    cd chatbot_rag_dio/app

---

### 2. Instale o Ollama

**Windows**: [https://ollama.com/download](https://ollama.com/download)  
**Linux/macOS**:

    curl -fsSL https://ollama.com/install.sh | sh

Depois:

    ollama pull llama3.1
    ollama serve

> O Ollama deve estar rodando em segundo plano para que o assistente funcione.

---

### 3. Crie e ative o ambiente virtual

**Windows**:

    python -m venv .venv
    .venv\Scripts\activate

**Linux/macOS**:

    python3 -m venv .venv
    source .venv/bin/activate

---

### 4. Instale as dependências

    pip install -r requirements.txt

> O processo pode levar alguns minutos. O tamanho total dos pacotes pode ultrapassar 2GB.

---

### 5. Execute o assistente

    streamlit run app.py

A interface estará disponível em:

    http://localhost:8501

> Na primeira execução, o carregamento pode demorar alguns segundos.  
> Se aparecer o erro `WinError 10061`, certifique-se de que o Ollama está rodando com `ollama serve`.

---

### 6. Desativar o ambiente virtual

    deactivate

---

## 📁 Documentação Técnica da Indexação

- Os documentos foram segmentados e vetorizados com `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.
- O índice FAISS foi gerado e salvo na pasta `index_mcmv/`.
- O sistema utiliza busca semântica com `search_type="mmr"` para equilibrar relevância e diversidade.

> O índice já está pronto e incluído no repositório. Não é necessário reindexar os documentos.

---

## ⏱️ Considerações Finais

- O tempo médio de resposta é de aproximadamente 1 minuto, dependendo da pergunta e dos recursos da máquina.
- A execução fora do Docker elimina overhead e melhora o desempenho local.
- Mantenha o modelo previamente baixado e o ambiente virtual ativo para garantir inicialização rápida e respostas consistentes.
