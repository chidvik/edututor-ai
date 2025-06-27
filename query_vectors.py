import numpy as np
from pinecone import Pinecone

# Pinecone setup
PINECONE_API_KEY = "pcsk_3nE6XJ_3y2kd7ynvJ5jPHCdDCUBMmm9YmbStGUe57XoKYQ9KgzT9DCNwFEpRkkt8KxyPHQ"
INDEX_NAME = "edututor-index"

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

# Create a random query vector (same dimension: 1536)
query_vector = np.random.rand(1536).tolist()

# Query Pinecone
results = index.query(vector=query_vector, top_k=3, include_metadata=True)

# Print results
print("🔍 Query Results:")
for match in results["matches"]:
    print(f"ID: {match['id']}, Score: {match['score']:.4f}, Metadata: {match['metadata']}")
