from sentence_transformers import SentenceTransformer
import faiss

model = None
index = None
chunks = []

def create_embeddings(text_chunks):
    global model, index, chunks
    model = SentenceTransformer('all-MiniLM-L6-v2')
    chunks = text_chunks
    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    # noinspection PyArgumentList
    index.add(embeddings.astype('float32'))

    return index

def search(query, c = 3):
    global model, index, chunks
    model = SentenceTransformer('all-MiniLM-L6-v2')
    if index is None:
        raise ValueError("No index created")
    query_embedding =  model.encode([query])
    distances, indices = index.search(query_embedding.astype('float32'), c)
    results = [(chunks[idx], float(dist)) for idx, dist in zip(indices[0], distances[0])]
    return results


