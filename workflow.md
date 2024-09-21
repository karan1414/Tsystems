## Workflow

1. **Initialization**:
    - **Set up the environment**:
        - Ensure the required packages are installed.
        - Set the `OPENAI_API_KEY` environment variable with your OpenAI API key.
        - Define the `PERSIS_DIR` for persisting the Chroma database.

2. **Loading or Saving Documents**:
    - **Check if the persistence directory exists**:
        - If it exists, load the Chroma database from the persistence directory using the `OpenAIEmbeddings` model.
        - If it does not exist, load documents from the specified folder (`data`), save them to the Chroma database, and persist the database.

3. **Loading Documents**:
    - **Using LangChain's DirectoryLoader**:
        - Load all text files from the specified directory using `DirectoryLoader` and `TextLoader`.
        - Read the content of each text file and store it in a list.

4. **Saving Documents**:
    - **Split documents into chunks**:
        - Use `RecursiveCharacterTextSplitter` to split each document into smaller chunks of 1000 characters.
    - **Create a Chroma database**:
        - Use the `Chroma.from_documents` method to create a Chroma database from the document chunks and embeddings.
        - Persist the database to the specified directory.

5. **Retrieving Documents**:
    - **Create a retriever**:
        - Use `MultiQueryRetriever.from_llm` to create a retriever from the language model and Chroma database.
    - **Invoke the retriever**:
        - Use the retriever to search for documents based on the query and return a list of unique documents.

6. **Generating Responses**:
    - **Create a prompt template**:
        - Use `ChatPromptTemplate.from_messages` to create a prompt template for the language model.
    - **Create a chain**:
        - Use `create_stuff_documents_chain` to create a chain that processes the documents and generates a response.
    - **Invoke the chain**:
        - Use the chain to generate a response from the language model based on the provided documents and query.

7. **Main Function**:
    - **Initialize the embeddings model**:
        - Use `OpenAIEmbeddings` with the specified model.
    - **Load or save documents**:
        - Check if the persistence directory exists and load or save documents accordingly.
    - **Define the query**:
        - Specify the query to be used for document retrieval.
    - **Retrieve documents**:
        - Use the `retrive_docs` function to retrieve documents from the Chroma database based on the query.
    - **Generate and print the response**:
        - Use the `get_response` function to generate a response from the language model based on the retrieved documents and query.
        - Print the response if available, otherwise log an appropriate message.