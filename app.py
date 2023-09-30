import os
import sys
import logging
import openai
import pandas as pd
import nltk
from textblob import TextBlob
import PyPDF2
from termcolor import colored
from tqdm import tqdm
from prettytable import PrettyTable

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

import constants

# Set up logging
logging.basicConfig(filename='langchain.log', level=logging.INFO)

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Set persistence flag
PERSIST = False

# Get query from command line arguments
query = None
if len(sys.argv) > 1:
    query = sys.argv[1]

# ASCII Art for fun
print(colored("""
                          
 👋👋 Hello there! Welcome to                                                                                                                        

    Ask me anything about the files you place in the data folder! 
    
        We can do some basic analysis of data, 
        Or I can tell you how to do the setup and admin
                        
    I'm still reading your stuff, give me a sec                                                                                                                        
                                            
""", 'green'))

try:
    print(colored("Loading data...", 'green'))

    # Check if persistence is enabled and index already exists
    if PERSIST and os.path.exists("persist"):
        print(colored("Reusing index...\n", 'yellow'))
        vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
        index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
        # Load data from directory
        loader = DirectoryLoader("data/")
        if PERSIST:
            # Create index with persistence
            index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
        else:
            # Create index without persistence
            index = VectorstoreIndexCreator().from_loaders([loader])

    # Create a ConversationalRetrievalChain
    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-4"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    chat_history = []
    while True:
        # Get user input if query is not provided as command line argument
        if not query:
            query = input(colored("Prompt: ", 'cyan'))
        if query in ['quit', 'q', 'exit']:
            sys.exit()
        if query.lower().startswith('analyze '):
            # Perform analysis on a column in the dataset
            column_name = query.split(' ')[1]
            if column_name in df.columns:
                # Calculate statistics on the column
                stats = df[column_name].describe()
                result = {'answer': str(stats)}
                table = PrettyTable()
                table.field_names = ["Stat", "Value"]
                for key, value in stats.items():
                    table.add_row([key, value])
                print(colored(table, 'green'))
            else:
                print(colored('Column not found in the dataset.', 'red'))
        else:
            # Get response from the ConversationalRetrievalChain
            result = chain({"question": query, "chat_history": chat_history})
            print(colored(result['answer'], 'blue'))

        # Add query and response to chat history
        chat_history.append((query, result['answer']))
        query = None

except Exception as e:
    # Log and display error message
    logging.error(f"An error occurred: {e}", exc_info=True)
    print(colored("An error occurred. Please check the log for more information.", 'red'))
