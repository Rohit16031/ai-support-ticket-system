from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from data_loader import load_data

import os

# Load environment variables
load_dotenv()

# Load CSV data into dataframe
df = load_data()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0
)

# Create Pandas DataFrame Agent
agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=False,
    allow_dangerous_code=True,
    number_of_head_rows=5
)

# Function to process natural language queries
def ask_question(question):

    try:
        response = agent.invoke(question)

        return response["output"]

    except Exception as e:

        return f"Error processing query: {str(e)}"