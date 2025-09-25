# Documentação Técnica do Processo de Indexação Vetorial

## 1. Objetivo

Este documento descreve o processo técnico de indexação utilizado para estruturar a base de conhecimento do **Assistente Técnico Minha Casa Minha Vida**, agente inteligente da **Caixa Econômica Federal**. A indexação foi realizada com foco em viabilizar a recuperação semântica de informações contidas em documentos institucionais, por meio da técnica de **Recuperação Aumentada por Geração (RAG)**.

---

## 2. Etapas do Processo

### a) Pré-processamento

- Os documentos foram lidos em formato PDF e segmentados em trechos curtos para facilitar a vetorização.
- Utilizou-se `PyPDFLoader` e `RecursiveCharacterTextSplitter` com parâmetros ajustados para preservar o contexto.

### b) Geração de Embeddings

- Os trechos foram convertidos em vetores semânticos utilizando o modelo `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.
- A integração foi feita via `HuggingFaceEmbeddings` com LangChain.

### c) Criação do Índice FAISS

- Os vetores foram armazenados em um índice FAISS local, salvo na pasta `index_mcmv/`:

```
vectorstore.save_local("index_mcmv")
```

---

## 3. Recuperação no Sistema RAG

Durante a execução do assistente, o índice é carregado e utilizado para buscar os trechos mais relevantes com base na pergunta do usuário:

```
retriever = vectorstore.as_retriever(search_type="mmr", k=5)
```

- O método `mmr` equilibra relevância e diversidade nos resultados.
- Os trechos recuperados são usados como contexto para gerar respostas fundamentadas.

---

## 4. Considerações Finais

O índice vetorial permite que o assistente funcione de forma rápida e independente dos documentos originais em tempo de execução. Essa abordagem garante consistência nas respostas e facilita a distribuição do sistema.

> **Observação:**  
> Mantenha a pasta `index_mcmv/` no diretório do projeto ao implantar o assistente.
