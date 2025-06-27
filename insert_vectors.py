import numpy as np
from pinecone import Pinecone

# Replace with your actual API key
PINECONE_API_KEY = "pcsk_3nE6XJ_3y2kd7ynvJ5jPHCdDCUBMmm9YmbStGUe57XoKYQ9KgzT9DCNwFEpRkkt8KxyPHQ"
INDEX_NAME = "edututor-index"

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

# Create dummy data: 5 vectors of dimension 1536
dummy_vectors = [
    {
        "id": f"vec{i}",
        "values": np.random.rand(1536).tolist(),
        "metadata": {"title": f"Sample vector {i}", "type": "note"}
    }
    for i in range(5)
]

# Upload to Pinecone
index.upsert(dummy_vectors)

print("✅ Inserted 5 dummy vectors into Pinecone.")
