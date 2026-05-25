from langchain_community.document_loaders import PyPDFLoader

def  pdf_loader(x):
    loader =  PyPDFLoader(x)
    doc =  loader.load()
    return doc
