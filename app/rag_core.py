# rag_core.py
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from config import faiss_path, embedding_model_name, ollama_model_name

# Função para carregar componentes do RAG
def load_rag_components():
    # Carrega índice FAISS e modelo de embeddings
    print("🔄 Carregando modelo de embeddings...")
    embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)
    print("✅ Embeddings carregados.")
    print("📦 Carregando índice FAISS...")
    vectorstore = FAISS.load_local(faiss_path, embedding_model, allow_dangerous_deserialization=True)
    print("✅ Índice FAISS carregado.")
    retriever = vectorstore.as_retriever(search_type="mmr", k=5)

    # Prompt especializado
    prompt = PromptTemplate(
        template="""
Você é um assistente técnico especializado nos programas de habitação social e financiamento imobiliário promovidos pela Caixa Econômica Federal, com foco no Minha Casa Minha Vida.
Utilize os documentos abaixo como base para responder perguntas sobre direitos e deveres dos beneficiários, etapas do financiamento, uso do FGTS, reforma e ampliação de unidades, gestão condominial, documentação necessária e orientações operacionais fornecidas pela Caixa.

Se a resposta não estiver nos documentos, diga que não sabe.
Se a pergunta for genérica demais, peça mais detalhes.
Seja claro, objetivo e tecnicamente preciso. Use o nível de detalhe necessário para responder com completude, sem exagerar.

Pergunta: {question}
Documentos: {documents}
Resposta:
""",
        input_variables=["question", "documents"],
    )

    # Configuração do modelo LLM
    llm = ChatOllama(model=ollama_model_name, temperature=0)
    parser = StrOutputParser()
    rag_chain = prompt | llm | parser

    return RAGApplication(retriever=retriever, rag_chain=rag_chain)


# Classe principal
class RAGApplication:
    def __init__(self, retriever, rag_chain):
        self.retriever = retriever
        self.rag_chain = rag_chain

    # Método para processar perguntas
    def run(self, question):
        retrieved_docs = self.retriever.invoke(question)

        # Formata os trechos com a fonte (nome do arquivo)
        trechos_formatados = []
        for doc in retrieved_docs:
            origem = os.path.basename(doc.metadata.get("source", "Documento desconhecido"))
            trecho = doc.page_content
            trechos_formatados.append(f"📄 **Fonte**: {origem}\n\n{trecho}")

        doc_texts = "\n\n".join(trechos_formatados)
        return self.rag_chain.invoke({"question": question, "documents": doc_texts})
