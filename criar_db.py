# Banco de dados vetorizado 
# definir uma funçao para: carregar o documento , dividir os documentos em pedaços de textos (chunks) e Vetorizar os chunks com processo de embedding

from langchain_community.document_loaders import PyPDFDirectoryLoader # Carregar os documentos pdf e retrnos os textos
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

pasta_base = "base"

def criar_db():
    documentos = carregar_documentos()
    chunks = dividir_chunks(documentos)
    vetorizar_chunks(chunks)


def carregar_documentos():
    carregar = PyPDFDirectoryLoader(pasta_base, glob="*.pdf")
    documentos = carregar.load()
    return documentos

def dividir_chunks(documentos):
    separar_documentos= RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )
    chunks = separar_documentos.split_documents(documentos)
    print(len(chunks))
    return chunks

def vetorizar_chunks(chunks):
    db = Chroma.from_documents(chunks,OpenAIEmbeddings(), persist_directory="db")

criar_db()