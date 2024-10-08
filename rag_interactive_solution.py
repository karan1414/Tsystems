import logging
import os

import openai
import streamlit as st
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

DB_PATH = "chroma_db"
PERSIS_DIR = "./chroma_langchain_db"

def save_documents(release_data: list[str], embeddings: OpenAIEmbeddings) -> Chroma:
    """
    Save documents to a Chroma database with embeddings.

    Args:
        release_data (List[str]): List of text data to be saved.
        embeddings (OpenAIEmbeddings): Embedding model to use for creating document embeddings.

    Returns:
        Chroma: The Chroma database object with the saved documents.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
    docs = []
    for data in release_data:   
        docs.extend(text_splitter.create_documents([data]))
    
    db = Chroma.from_documents(docs, embeddings, persist_directory=PERSIS_DIR)
    db.persist()
    return db


def load_text_files(directory_path: str) -> list[str]:
    """
    Load all text files from a specified directory using LangChain's DirectoryLoader.

    Args:
        directory_path (str): The path to the directory containing text files.

    Returns:
        List[str]: A list of text data loaded from the files.
    """
    loader = DirectoryLoader(directory_path, glob="**/*.txt", loader_cls=TextLoader)
    documents = loader.load()
    return [doc.page_content for doc in documents]


def retrive_docs(chroma_db: Chroma, llm: ChatOpenAI, query: str) -> list[str]:
    """
    Retrieve documents from a Chroma database using a language model.

    Args:
        chroma_db (Chroma): The Chroma database object.
        llm (ChatOpenAI): The language model to use for retrieval.
        query (str): The query string to search for.

    Returns:
        List[str]: A list of unique documents retrieved based on the query.
    """
    retriever_from_llm = MultiQueryRetriever.from_llm(
        retriever=chroma_db.as_retriever(), llm=llm
    )

    unique_docs = retriever_from_llm.invoke(query)
    return unique_docs


def get_response(llm: ChatOpenAI, docs: list[str], query: str) -> str:
    """
    Get a response from the language model based on the provided documents and query.

    Args:
        llm (ChatOpenAI): The language model to use for generating the response.
        docs (List[str]): The list of documents to use as context.
        query (str): The query string to ask the language model.

    Returns:
        str: The response generated by the language model.
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You have to answer question based on context given:\n\n{context}"),
            ("user", "Question:\n\n{query}")
            ]
    )

    chain = create_stuff_documents_chain(llm=llm, prompt=prompt)

    llm_response = chain.invoke({"context": docs, "query": query})
    return llm_response

def main():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    if os.path.exists(PERSIS_DIR):
        chroma_db = Chroma(persist_directory=PERSIS_DIR, embedding_function=embeddings)
    else:
        release_data_list = load_text_files('data')
        chroma_db = save_documents(release_data_list, embeddings)

    # title of app
    st.title("T-systems Q&A")

    # sidebar for settings
    st.sidebar.title("Settings")
    api_key = st.sidebar.text_input("Enter you openAI Api key: ", type="password")

    # response param
    temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5)

    # main interface for user input
    st.write("Go ahead and ask question related to Tsystem press release")
    query = st.text_input("Search")

    llm = ChatOpenAI(temperature=temperature, api_key=api_key)
    docs = retrive_docs(chroma_db, llm, query)

    if not api_key:
        st.write("Please provide the open ai api key !")
    
    if query:
        llm_response = get_response(llm, docs, query)
        if llm_response:
            st.write(llm_response)
        else:
            st.write("No response from LLM !")
    else:
        st.write("Please provide the search query !")

if __name__ == "__main__":
    main()
