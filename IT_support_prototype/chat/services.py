
from chromadb import PersistentClient
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from chat.models import KnowledgeBase
from chat.utils.extractor import extract_paragraphs_from_docx

client = PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("it_support_kb")

def build_knowledge_base(docx_path):
    paragraphs = extract_paragraphs_from_docx(docx_path)
    full_text = "\n".join(paragraphs)

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(full_text)

    embedding_model = OllamaEmbeddings(model="nomic-embed-text")

    KnowledgeBase.objects.all().delete()

    
    client.delete_collection("it_support_kb")
    collection = client.get_or_create_collection("it_support_kb")

    for i, chunk in enumerate(chunks):
        embedding = embedding_model.embed_query(chunk)
        doc_id = f"chunk_{i}"

        collection.add(documents=[chunk], ids=[doc_id], embeddings=[embedding])
        KnowledgeBase.objects.create(title="IT Support KB", content=chunk, chunk_index=i)

    # Remove this:
    # client.persist()
