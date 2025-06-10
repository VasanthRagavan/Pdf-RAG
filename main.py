from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
load_dotenv()
client = OpenAI()
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
pdf_path = Path(__file__).parent/"crime-and-punishment.pdf"
loader  = PyPDFLoader(file_path=pdf_path)
docs = loader.load()
#chunking 
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200 
    #understand the context
)
splitted_docs = text_splitter.split_documents(docs)

#create vector embeddings
embed_model = OpenAIEmbeddings(
    model="text-embedding-small"
)



