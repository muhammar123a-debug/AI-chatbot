import sqlite3
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_sql_agent
from langchain.agent.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from dotenv import load_dotenv
import os

# load Api
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key():
    raise ValueError("GOOGLE_API_KEY not found! Add it to .env file.")

llm = ChatGoogleGenerativeAI(model="femini-1.5-flash", google_api_key=api_key)

# connect to sql db
db = SQLDatabase.from_url("sqlite:///database.db")

#  Toolkit (LangChain SQL Agent)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

