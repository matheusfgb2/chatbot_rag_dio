# app.py
import streamlit as st
import time
from rag_core import load_rag_components

# 🚀 Inicializa o sistema completo
if "app" not in st.session_state:
    inicio = time.time()
    st.session_state.app = load_rag_components()
    fim = time.time()
    st.session_state.tempo_carregamento = fim - inicio
    st.session_state.carregamento_exibido = False

app = st.session_state.app

# 💬 Interface fixa
st.title("🏠 Assistente Técnico Minha Casa Minha Vida")

# 📝 Campo de entrada
pergunta = st.text_input("📝 Sua pergunta:")

# ⏱️ Tempo de carregamento — só uma vez, e só se não estiver processando pergunta
if (
    "tempo_carregamento" in st.session_state
    and not st.session_state.carregamento_exibido
    and pergunta == ""
):
    st.markdown(f"🕒 Tempo de carregamento do assistente: **{st.session_state.tempo_carregamento:.2f} segundos**")
    st.session_state.carregamento_exibido = True

# 🔎 Descrição sempre visível
st.markdown("""
Este assistente responde dúvidas sobre **financiamento habitacional**, uso do **FGTS**, **contratos**, etapas do programa e regras operacionais da Caixa Econômica Federal.

Exemplos de perguntas:
- Como usar o FGTS para amortizar o financiamento?
- Quais despesas não podem ser pagas com FGTS?
- Quais documentos são exigidos para formalizar o contrato?
- O que acontece se houver atraso na obra?
""")

# 🤖 Processa pergunta
if pergunta and len(pergunta.strip()) > 3:
    with st.spinner("🤖 Gerando resposta..."):
        try:
            inicio = time.time()
            resposta = app.run(pergunta)
            fim = time.time()
            duracao = fim - inicio
        except Exception as e:
            st.error(f"❌ Erro ao gerar resposta: {e}")
            resposta = "Desculpe, ocorreu um erro ao processar sua pergunta."
            duracao = 0

    st.markdown("### 💬 Resposta:")
    st.write(resposta)
    st.markdown(f"⏱️ Tempo de resposta: **{duracao:.2f} segundos**")

    # 📚 Exibe trechos utilizados
    if hasattr(app, "doc_texts"):
        with st.expander("📚 Trechos utilizados na resposta"):
            st.markdown(app.doc_texts)
else:
    if pergunta:
        st.warning("❗ Por favor, insira uma pergunta mais específica.")
