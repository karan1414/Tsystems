import logging
import os

import openai
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

DB_PATH = "chroma_db"
PERSIS_DIR = "./chroma_langchain_db"

def save_documents(release_data, embeddings):
    """ 
        This method to save documents by splitting release data 
        in chunk size and saving the embedding db. 
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
    docs = []
    for data in release_data:   
        docs.extend(text_splitter.create_documents([data]))
    
    db = Chroma.from_documents(docs, embeddings, persist_directory=PERSIS_DIR)
    db.persist()
    return db

def load_documents(folder_name):
    """
        This methods loads all the text files from a folder
    """
    release_data = []
    
    files = os.listdir(folder_name)
    for file_name in files:
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_name, file_name)
            text_data = open(file_path, encoding="utf-8").read()
            release_data.append(text_data)              
    return release_data

def get_llm_response(context, query, temperature, openai_client):
    """
        This method gets the LLM response given the context, query, temperature and openapi client. 
    """
    prompt = f"Given the context: {context}, please answer the following question {query}."
    
    try :
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': 'system', 'content': "You have to answer question based on context given"},
                {'role': 'user', 'content': prompt}
            ],
            temperature=temperature
        )
    except ValueError as ve:
        logging.error(f"A Value Error {ve}")
        st.write(f"An error occured: {ve}")

    except Exception as e:
        logging.error(f'An error occured: {e}')
    return response.choices[0].message.content

def main():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    if os.path.exists(PERSIS_DIR):
        chroma_db = Chroma(persist_directory=PERSIS_DIR, embedding_function=embeddings)
    else:
        release_data_list = load_documents('data')
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

    retriver = chroma_db.as_retriever()
    relevant_docs = retriver.get_relevant_documents(query)[0].page_content
    context = " ".join(relevant_docs)
    if api_key:
        openai_client = openai.OpenAI(api_key=api_key)
    else:
        st.write("Please provide the open ai api key !")
    
    if query:
        llm_response = get_llm_response(context, query, temperature, openai_client)
        if llm_response:
            st.write(llm_response)
        else:
            st.write("No response from LLM !")
    else:
        st.write("Please provide the search query !")

if __name__ == "__main__":
    main()
