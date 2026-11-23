# 🎥 YouTube Transcript Chatbot using RAG

A Retrieval-Augmented Generation (RAG) application that lets you chat with any YouTube video. Paste a link, and the app fetches the transcript, indexes it in a FAISS vector store, retrieves the most relevant passages for your question, and generates a grounded answer using Google Gemini.

---

## Features

- Fetches transcripts from YouTube videos automatically
- Splits transcripts into overlapping chunks
- Generates embeddings with Gemini embeddings
- Stores embeddings in a FAISS vector database
- Retrieves relevant chunks using MMR (Maximal Marginal Relevance) for diverse context
- Answers questions with Gemini, strictly grounded in the transcript
- Replies "I don't know based on the provided transcript." when the answer isn't in the video
- Video summarization in bullet points
- Interactive Streamlit chat interface
- Shows the retrieved context behind each answer

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Orchestration | LangChain |
| Embeddings | Gemini (`gemini-embedding-2`) |
| LLM | Gemini (`gemini-3.6-flash`) |
| Vector Database | FAISS |
| Transcript Source | `youtube-transcript-api` |
| Config | `python-dotenv` |

---

## Project Structure

```
youtube-rag-chatbot/
├── app.py              # Streamlit UI
├── rag.py              # RAG pipeline (YouTubeRAG class)
├── config.py           # Model names and tunable parameters
├── test.py             # Quick check that your Gemini API key works
├── requirements.txt
├── .env.example        # Template for your API key
├── .gitignore
└── README.md
```

---

## Workflow

1. User enters a YouTube URL.
2. The transcript is fetched with `youtube-transcript-api`.
3. The transcript is split into overlapping chunks.
4. Each chunk is embedded using Gemini embeddings.
5. Embeddings are stored in a FAISS vector database.
6. User asks a question.
7. The retriever finds the most relevant chunks using MMR.
8. The retrieved context and question are inserted into a prompt template.
9. Gemini generates an answer based only on that context.

---

## Architecture

```
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
Gemini Embeddings
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
Gemini LLM
      │
      ▼
Final Answer
```

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/youtube-rag-chatbot.git
cd youtube-rag-chatbot
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Add your Gemini API key**

Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey), then create a `.env` file in the project root:

```bash
cp .env.example .env
```

Open `.env` and set your key:

```
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file. Make sure `.env` is listed in `.gitignore`.

**5. (Optional) Verify your API key**

```bash
python test.py
```

If everything is set up correctly, this prints a short explanation of RAG from Gemini.

---

## Run the Application

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

---

## Usage

1. Paste a YouTube URL in the sidebar and click **Load Transcript**.
2. Wait for the success message showing how many chunks were created.
3. Ask questions in the chat box, or click **Summarize Video** for a bullet-point summary.
4. Expand **Retrieved Context** under any answer to see which transcript passages were used.

---

## Configuration

All tunable settings live in `config.py`:

| Setting | Default | Description |
|---|---|---|
| `EMBEDDING_MODEL` | `gemini-embedding-2` | Gemini embedding model |
| `LLM_MODEL` | `gemini-3.6-flash` | Gemini chat model |
| `CHUNK_SIZE` | `1000` | Characters per chunk |
| `CHUNK_OVERLAP` | `200` | Overlap between chunks |
| `SEARCH_TYPE` | `mmr` | Retrieval strategy |
| `TOP_K` | `2` | Chunks passed to the LLM |
| `MAX_NEW_TOKENS` | `256` | Max length of generated answers |
| `TEMPERATURE` | `0.7` | Sampling temperature |

Increase `TOP_K` for questions that need broader context, and `MAX_NEW_TOKENS` for longer answers or summaries.

---

## Example Questions

- Summarize this video.
- What are the speaker's main arguments?
- What advice does the speaker give?
- What was said about [topic]?
- Who is [person mentioned in the video]?

---

## Limitations

- Works only for videos that have an **English** transcript available.
- Supports standard `youtube.com/watch?v=` and `youtu.be/` links.
- Uses transcript text only (does not analyze video frames or audio).
- Answer quality depends on how well retrieval surfaces the right chunks.
- Summaries are built from the top retrieved chunks, so they may not cover an entire long video.
- Requires an internet connection and a valid Gemini API key. Usage is subject to Google's API quotas.

---

## Future Improvements

- Source citations with timestamps
- Conversational memory
- Hybrid search (BM25 + vector search)
- Full-video summarization (map-reduce over all chunks)
- Multi-language transcript support
- Multi-video support
- PDF and DOCX ingestion
- Streaming responses
- Support for additional LLM providers (OpenAI, Hugging Face)
- Docker deployment

---

## Requirements

- Python 3.10+
- A Gemini API key
- Internet connection

---

## Author

**Jaisal Shekhawat**
