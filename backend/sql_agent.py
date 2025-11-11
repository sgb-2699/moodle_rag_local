from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from backend.config import MYSQL_CONFIG

def get_database():
    uri = (
        f"mysql+mysqlconnector://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}"
        f"@{MYSQL_CONFIG['host']}/{MYSQL_CONFIG['database']}"
    )
    return SQLDatabase.from_uri(uri)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

custom_prompt = PromptTemplate(
    input_variables=["input", "agent_scratchpad", "tools", "tool_names"],
    template="""
You are an agent designed to interact with a MySQL database.

You have access to the following tools:
{tools}

Tool names: {tool_names}

IMPORTANT:
- Don't limit queries by default, only do it if it is explicitly mentioned by the user.

Question: {input}
{agent_scratchpad}
"""
)


local = False

if(local):
    def build_sql_agent(model_name="mistral"):
        db = get_database()
        llm = Ollama(model=model_name)
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)
        return create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True,
            handle_parsing_errors=True
        )
else:
    def build_sql_agent(model_name="gemini-2.0-flash"):
        db = get_database()
        llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.2)
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)

        return create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True,
            #prompt = custom_prompt,
            handle_parsing_errors=True
        )