# 🎥 YouTube Transcript Chatbot using RAG

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about a YouTube video's transcript. The application fetches the transcript, converts it into vector embeddings, stores them in a FAISS vector database, retrieves relevant context, and generates answers using a Hugging Face Large Language Model.

---

## Features

- Extracts transcripts from YouTube videos
- Splits transcripts into semantic chunks
- Generates embeddings using Sentence Transformers
- Stores embeddings in a FAISS vector database
- Retrieves relevant transcript chunks using MMR
- Answers questions using a Hugging Face LLM
- Interactive Streamlit interface
- Video transcript summarization
- Displays retrieved context used for answering

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python
- LangChain

### Embedding Model
- sentence-transformers/all-MiniLM-L6-v2

### Vector Database
- FAISS

### LLM
- Qwen2.5-1.5B (Hugging Face)

### Transcript Source
- youtube-transcript-api

---

## Project Structure

youtube-rag-chatbot/

├── app.py

├── rag.py

├── config.py

├── requirements.txt

├── README.md

└── .gitignore

---

## Workflow

1. User enters a YouTube URL.
2. Transcript is fetched using YouTube Transcript API.
3. Transcript is split into chunks.
4. Embeddings are generated using Sentence Transformers.
5. Embeddings are stored in a FAISS vector database.
6. User asks a question.
7. Retriever searches for relevant chunks.
8. Retrieved context is passed to the LLM.
9. LLM generates an answer based only on the retrieved context.

---

## Architecture

YouTube Video
        │
        ▼
Transcript API
        │
        ▼
Transcript Text
        │
        ▼
Text Splitter
        │
        ▼
Embeddings
        │
        ▼
FAISS Vector Store
        │
        ▼
Retriever (MMR)
        │
        ▼
Prompt Template
        │
        ▼
Hugging Face LLM
        │
        ▼
Final Answer

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/youtube-rag-chatbot.git
```

Move into the project

```bash
cd youtube-rag-chatbot
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Example Questions

- Summarize this video.
- What is income tax?
- Who is Demis?
- What are the speaker's main arguments?
- What advice does the speaker give?
- What was discussed about the government?

---

## Limitations

- Works only for videos that have transcripts available.
- Uses transcript text only (does not analyze video frames or audio).
- Answers depend on the quality of transcript retrieval.
- Small language models may occasionally hallucinate despite prompt constraints.

---

## Future Improvements

- Multi-video support
- PDF and DOCX ingestion
- Conversational memory
- Hybrid search (BM25 + Vector Search)
- Source citations with timestamps
- Streaming responses
- Multiple embedding model selection
- Support for OpenAI and Gemini APIs
- Docker deployment

---

## Requirements

- Python 3.10+
- Internet connection (for downloading models the first time)

---

## Author

## Jaisal Shekhawat

