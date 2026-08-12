import streamlit as st
from rag import YouTubeRAG

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="YouTube Transcript Chatbot",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YouTube Transcript Chatbot")
st.write("Ask questions about any YouTube video's transcript using RAG.")

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "rag" not in st.session_state:
    st.session_state.rag = YouTubeRAG()

if "video_loaded" not in st.session_state:
    st.session_state.video_loaded = False

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("Video")

    video_url = st.text_input(
        "Enter YouTube URL"
    )

    if st.button("Load Transcript"):

        if video_url.strip() == "":
            st.warning("Please enter a YouTube URL.")

        else:

            with st.spinner("Fetching transcript..."):

                try:

                    chunks = st.session_state.rag.load_video(video_url)

                    st.session_state.video_loaded = True

                    st.success(
                        f"Transcript Loaded Successfully!\n\nChunks Created : {chunks}"
                    )

                except Exception as e:
                    st.error(str(e))

    st.divider()

    if st.button("Summarize Video"):

        if not st.session_state.video_loaded:

            st.warning("Load a video first.")

        else:

            with st.spinner("Generating summary..."):

                summary = st.session_state.rag.summarize()

                st.subheader("Summary")

                st.write(summary)

# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask something about the transcript..."
)

if question:

    if not st.session_state.video_loaded:

        st.warning("Please load a YouTube transcript first.")

    else:

        # Show user message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Get answer

        with st.spinner("Thinking..."):

            answer, docs = st.session_state.rag.ask(question)

        # Show assistant answer

        with st.chat_message("assistant"):

            st.markdown(answer)

            with st.expander("Retrieved Context"):

                for i, doc in enumerate(docs):

                    st.markdown(f"### Chunk {i+1}")
                    st.write(doc.page_content)
                    st.divider()

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )