

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from chromadb import PersistentClient


embedding = OllamaEmbeddings(model="nomic-embed-text")
llm = OllamaLLM(model="phi3", temperature=0.1)


prompt_template = PromptTemplate.from_template("""
You are an experienced IT support assistant. Use the following context to answer the user question clearly.

Context: {context}

Question: {question}
""")

def get_rag_chain():
    
    client = PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection("it_support_kb")
    db = Chroma(persist_directory="./chroma_db", embedding_function=embedding)

    retriever = db.as_retriever(search_kwargs={"k": 3})

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt_template}
        
    )
    return chain
