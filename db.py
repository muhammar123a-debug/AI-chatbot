import sqlite3
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase

# 🔹 Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found! Add it to .env file.")

# 🔹 Connect Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=api_key)

# 🔹 Connect to SQLite DB
db = SQLDatabase.from_uri("sqlite:///qa_bot.db")

# 🔹 Toolkit (LangChain SQL Agent)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# 🔹 Agent
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

def run_query_with_ai(query: str):
    """AI se query karna aur jawab lana"""
    result = agent_executor.run(query)
    return result

if __name__ == "__main__":
    # Example test
    question = "What is stored in the database?"
    print("User:", question)
    answer = run_query_with_ai(question)
    print("AI:", answer)
