from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from data_loader import load_data
from prompts import SYSTEM_PROMPT
import os

load_dotenv()

df = load_data()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0
)

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=False,
    allow_dangerous_code=True,
    prefix=SYSTEM_PROMPT,
    agent_executor_kwargs={"handle_parsing_errors": True}
)

def ask_question(question):
    try:
        response = agent.invoke(question)
        return response["output"]
    except Exception as e:
        return f"Error processing query: {str(e)}"