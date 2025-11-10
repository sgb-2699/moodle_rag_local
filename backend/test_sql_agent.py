# test_sql_agent.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.sql_agent import build_sql_agent

if __name__ == "__main__":
    agent = build_sql_agent()
    query = "How many different departments are in the students table?"
    result = agent.invoke(query)
    print(result)