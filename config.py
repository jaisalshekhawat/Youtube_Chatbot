# config.py

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# HuggingFace LLM
LLM_MODEL = "Qwen/Qwen2.5-1.5B"

# Text Splitter
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retriever
SEARCH_TYPE = "mmr"
TOP_K = 2

# Generation
MAX_NEW_TOKENS = 256
TEMPERATURE = 0.7