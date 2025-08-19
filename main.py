import streamlit as st
import asyncio  # <-- 1. Tambahkan import asyncio

# 2. Tambahkan blok kode ini untuk mengatasi error event loop
try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from dotenv import load_dotenv
load_dotenv()
from RAG_Chatbot import show_rag_chatbot


def main():
    st.title('RAG Chatbot')
    show_rag_chatbot()

if __name__ == '__main__':
    main()