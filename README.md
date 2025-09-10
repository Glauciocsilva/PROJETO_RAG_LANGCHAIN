# 📘 Documentação do Projeto – LLM com  Banco de Dados Vetorial

Este projeto implementa um **Banco de Dados Vetorial** utilizando a biblioteca LangChain,
com suporte a embeddings da OpenAI e armazenamento no ChromaDB. O objetivo usuários façam pperguntas ao banco de conhecimento em arquivos pdf e LLM retorna 
a resposta . O fluxo é dividido em dois módulos principais:

1. **Criardb.py** – Responsável por:
   - Carregar documentos PDF da pasta `base/`
   - Dividir textos em pedaços menores (chunks)
   - Converter chunks em embeddings vetoriais
   - Salvar no banco vetorial `db/`

2. **main.py** – Responsável por:
   - Receber perguntas do usuário
   - Gerar embedding da pergunta
   - Buscar chunks relevantes no banco vetorial
   - Enviar para um modelo de linguagem (OpenAI) responder

---

## 🔹 Conceitos-Chave
- **Banco Vetorial**: armazena vetores (representações numéricas) de textos.
- **Embeddings**: transformam textos em vetores para comparação semântica.
- **Chunks**: divisão de textos longos em pedaços menores para melhor desempenho.
- **LangChain + ChromaDB + OpenAI**: integração para criar, armazenar e consultar embeddings.

---

## 🚀 Fluxo do Sistema
1. Criar DB → carregar PDFs → dividir → gerar embeddings → salvar.
2. Main → receber pergunta → gerar embedding da pergunta → buscar no banco → IA responde.

---

## 📦 Dependências
Instalar pacotes necessários:
```bash
pip install python-dotenv langchain langchain-openai langchain-community langchain-chroma chromadb openai pypdf
```

---

## 💡 Exemplo de Uso
1. Coloque seus arquivos PDF na pasta `base/`
2. Crie um arquivo .env e digite OPENAI_API_KEY = cole sua chave api da openai. 
3. Execute `Criardb.py` para criar o banco
4. Execute `main.py` e faça perguntas no terminal
