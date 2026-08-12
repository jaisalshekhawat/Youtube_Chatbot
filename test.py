from rag import YouTubeRAG

rag = YouTubeRAG()

rag.load_video("https://www.youtube.com/watch?v=jr0k_fOR1b0")

answer, docs = rag.ask("What is income tax?")

print(answer)