# Projeto: Assistente Técnico Minha Casa Minha Vida (Chatbot com RAG)

## 1. Objetivo

Este projeto tem como finalidade desenvolver o **Assistente Técnico Minha Casa Minha Vida**, um agente inteligente da **Caixa Econômica Federal** capaz de responder dúvidas sobre financiamento habitacional, uso do FGTS, contratos, etapas do programa e regras operacionais da instituição. O sistema utiliza técnicas de **Recuperação Aumentada por Geração (RAG)** para garantir respostas fundamentadas em documentos oficiais.

> **Observação:**  
> Para informações sobre como preparar o ambiente e executar o chatbot, verificar o `Guia de Instalação e Execução do Assistente com Ollama`.  
> Para informações sobre como foi feito o processo de indexação vetorial, verificar a `Documentação Técnica do Processo de Indexação Vetorial`.  
> Ambos os documentos se encontram nesta pasta.

---

## 2. Problema Proposto

A complexidade dos processos de financiamento e a diversidade de documentos técnicos dificultam o acesso rápido às informações por parte dos beneficiários e operadores do programa.

**Problema:**  
Como oferecer respostas precisas e contextualizadas sobre o programa Minha Casa Minha Vida com base em documentos oficiais da Caixa?

**Solução proposta:**  
Desenvolver um chatbot institucional que utiliza RAG para buscar trechos relevantes em documentos técnicos e gerar respostas confiáveis por meio de um modelo de linguagem local.

---

## 3. Documentos Utilizados no RAG

A base de conhecimento do assistente foi construída a partir de um conjunto de documentos institucionais da Caixa Econômica Federal relacionados ao programa Minha Casa Minha Vida.

Esses materiais incluem cartilhas operacionais, guias do beneficiário, convenções condominiais, regimentos internos, declarações, checklists e orientações sobre etapas de financiamento, uso do FGTS, amortização e direitos e deveres dos participantes.

Todos os documentos foram convertidos para texto, segmentados em trechos curtos e vetorizados para permitir busca semântica eficiente.
Essa estrutura permite que o assistente recupere informações relevantes com precisão e gere respostas fundamentadas diretamente a partir do conteúdo oficial da Caixa.

---

## 4. Tecnologias Utilizadas

| Ferramenta/Biblioteca     | Finalidade                                     |
| ------------------------- | ---------------------------------------------- |
| **LangChain**             | Pipeline RAG e integração com o modelo         |
| **FAISS**                 | Indexação vetorial e busca semântica           |
| **Sentence Transformers** | Geração de embeddings semânticos               |
| **Ollama**                | Execução local do modelo de linguagem          |
| **Streamlit**             | Interface web interativa para o usuário        |
| **Python**                | Linguagem base para desenvolvimento do sistema |

---

## 5. Funcionamento do Sistema

1. Os documentos são carregados e divididos em trechos menores.
2. Cada trecho é convertido em vetor semântico via embeddings.
3. Os vetores são armazenados em um índice FAISS.
4. O usuário faz uma pergunta via interface Streamlit.
5. O sistema busca os trechos mais relevantes no índice.
6. O modelo de linguagem gera uma resposta com base nos trechos recuperados.

---

## 6. Considerações Finais

O projeto oferece uma solução prática e institucional para tornar o acesso à informação mais ágil e confiável, especialmente em contextos operacionais e sociais. A técnica de RAG garante que as respostas estejam sempre fundamentadas em documentos oficiais da Caixa.

> **Observação final:**  
> O tempo médio de resposta do assistente é de aproximadamente 1 minuto, mesmo após a inicialização. Esse tempo pode variar conforme a complexidade da pergunta e os recursos disponíveis na máquina.
