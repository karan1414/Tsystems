
# Document Retrieval and Response Generation

This project demonstrates how to use OpenAI's embeddings and language models to create a document retrieval and response generation system. The system saves documents to a Chroma database, retrieves relevant documents based on a query, and generates responses using a language model.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Running in VS Code](#running-in-vs-code)

## Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:karan1414/Tsystems.git
    cd document-retrieval
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

5. Set up your OpenAI API key:
    ```sh
    export OPENAI_API_KEY='your_openai_api_key'
    ```

## Usage

1. Place your text files in the `data` directory.

2. Run the main script:
    ```sh
    python main.py
    ```


## Running in VS Code

1. **Open the project in VS Code**:
    - Open VS Code.
    - Click on `File` > `Open Folder` and select the project directory.

2. **Set up the virtual environment in VS Code**:
    - Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS).
    - Type `Python: Select Interpreter` and select the virtual environment you created (`venv`).

3. **Install the required extensions**:
    - Install the Python extension for VS Code if you haven't already.

4. **Run the script in an IPython notebook**:
    - Create a new Jupyter notebook file (`.ipynb`) in the project directory.

5. **Run the notebook cells**:
    - Execute each cell in the notebook to run the code and see the output.

6. **Running interactive version i.e main.py**
    - Go to the directory containing main.py and run `streamlit run main.py`
