from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunker(profile_string):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 100)
    chunks = text_splitter.split_text(profile_string)
    return chunks

