# Document Loading and Analysis
import os

os.environ["OPENAI_API_KEY"] = "..."

from langchain import OpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

loader = TextLoader("./state-of-the-union-23.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
store = Chroma.from_documents(texts, embeddings, collection_name="state-of-union")

llm = OpenAI(temperature=0)
chain = RetrievalQA.from_chain_type(llm, retriever=store.as_retriever())
print(chain.run("What did biden talk about Ohio?"))
