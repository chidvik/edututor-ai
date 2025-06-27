from pinecone import Pinecone, ServerlessSpec

# Replace with your actual API key
PINECONE_API_KEY = "pcsk_3nE6XJ_3y2kd7ynvJ5jPHCdDCUBMmm9YmbStGUe57XoKYQ9KgzT9DCNwFEpRkkt8KxyPHQ"

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Index name
index_name = "edututor-index"

# Check and create index
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
    print(f"✅ Created index: {index_name}")
else:
    print(f"✅ Index '{index_name}' already exists.")
