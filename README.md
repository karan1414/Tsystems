
# Rag solution for telecom press release data

This project demonstrates a Retrieval-Augmented Generation (RAG) workflow using OpenAI's GPT-3.5-turbo model and Chroma for document storage and retrieval.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [How to Use the .ipynb File](#how-to-use-the-ipynb-file)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**:
    ```bash
    git clone git@github.com:karan1414/Tsystems.git
    cd yourproject
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the `.env` file**:
    - Create a file named `.env` in the root directory of your project.
    - Add your OpenAI API key to the `.env` file:
        ```plaintext
        OPENAI_API_KEY=your_openai_api_key_here
        ```

## Usage

1. **Run the main script**:
    ```bash
    python main.py
    ```

2. **Interact with the script**:
    - The script will load documents, save them to a Chroma database, and use the OpenAI API to generate responses based on queries.

## Files

- `main.py`: The main script containing the RAG workflow.
- `requirements.txt`: Lists all the dependencies required for the project.
- `.env`: Contains environment variables, such as API keys.
- `data/`: Directory containing text files to be loaded and processed.

## How to Use the .ipynb File

### In Jupyter Notebook

1. **Open Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```

2. **Navigate to the project directory** and open the `.ipynb` file.

3. **Run the cells**:
    - Click on each cell and press `Shift + Enter` to execute the code.

### In Visual Studio Code

1. **Install VS Code**: Download and install [Visual Studio Code](https://code.visualstudio.com/).

2. **Install the Python and Jupyter extensions**:
    - Open VS Code.
    - Go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
    - Search for "Python" and "Jupyter" and install them.

3. **Open the .ipynb file**:
    - Open the project folder in VS Code.
    - Click on the `.ipynb` file to open it in the editor.

4. **Select the Python interpreter**:
    - Click on the Python version in the bottom left corner of the window.
    - Select the interpreter from the virtual environment you created earlier.

5. **Run the cells**:
    - Click on each cell and press `Shift + Enter` to execute the code.


### `.env`

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
```
