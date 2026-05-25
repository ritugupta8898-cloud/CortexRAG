import os
from source.dataloader import pdf_loader
from source.splitter import text_split
from source.vectordb import vectordb
from source.splitter import clean_chunks
from dotenv import load_dotenv

load_dotenv()
def loadall_documents(folder_path: str):
    res = []
    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)
        docs = pdf_loader(path)
        for doc in docs:
            doc.metadata["paper_name"] = file
        res.extend(docs)

    return res


doc = loadall_documents("/Users/pratyushgupta/Documents/rag/data")

chunked = text_split(doc)
chunks = clean_chunks(chunks)
vectordb(chunked)



