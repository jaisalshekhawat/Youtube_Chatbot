from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import (
    HuggingFaceEmbeddings,
    HuggingFacePipeline
)

from langchain_community.vectorstores import FAISS

from transformers import pipeline

from langchain_core.prompts import PromptTemplate

from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda
)

from langchain_core.output_parsers import StrOutputParser

import config


class YouTubeRAG:

    def __init__(self):

        self.vector_store = None
        self.retriever = None
        self.main_chain = None

        print("Loading Embedding Model...")

        self.embeddings = HuggingFaceEmbeddings(
            model_name=config.EMBEDDING_MODEL
        )

        print("Loading LLM...")

        pipe = pipeline(
            task="text-generation",
            model=config.LLM_MODEL,
            max_new_tokens=config.MAX_NEW_TOKENS,
            temperature=config.TEMPERATURE,
            do_sample=False,
            return_full_text=False,
        )

        self.llm = HuggingFacePipeline(pipeline=pipe)

        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
You are a helpful assistant.

Answer ONLY from the provided context.

If the answer is not present, reply:

"I don't know based on the provided context."

Context:
{context}

Question:
{question}

Answer:
"""
        )

    ###################################################################

    def extract_video_id(self, url):

        if "watch?v=" in url:
            return url.split("watch?v=")[1].split("&")[0]

        if "youtu.be/" in url:
            return url.split("youtu.be/")[1].split("?")[0]

        return url

    ###################################################################

    def load_video(self, url):

        video_id = self.extract_video_id(url)

        api = YouTubeTranscriptApi()

        transcript = api.fetch(
            video_id,
            languages=["en"]
        )

        transcript_text = " ".join(
            snippet.text
            for snippet in transcript
        )

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP
        )

        # Create a list of Document objects from a list of texts.
        chunks = splitter.create_documents([transcript_text])

        self.vector_store = FAISS.from_documents(
            chunks,
            self.embeddings
        )

        self.retriever = self.vector_store.as_retriever(
            search_type=config.SEARCH_TYPE,
            search_kwargs={"k": config.TOP_K}
        )

        def format_docs(docs):
            return "\n\n".join(
                doc.page_content
                for doc in docs
            )

        parallel_chain = RunnableParallel(
            {
                "context":
                self.retriever
                | RunnableLambda(format_docs),

                "question":
                RunnablePassthrough(),
            }
        )

        parser = StrOutputParser()

        self.main_chain = (
            parallel_chain
            | self.prompt
            | self.llm
            | parser
        )

        return len(chunks)

    ###################################################################

    def ask(self, question):

        retrieved_docs = self.retriever.invoke(question)

        answer = self.main_chain.invoke(question)

        return answer, retrieved_docs

    ###################################################################

    def summarize(self):

        summary_prompt = """
Summarize this video in bullet points.
"""

        return self.main_chain.invoke(summary_prompt)