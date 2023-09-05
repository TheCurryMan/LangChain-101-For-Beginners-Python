# Action Agents
import os

os.environ["OPENAI_API_KEY"] = "..."

from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent

prompt = "When was the 3rd president of the United States born? What is that year raised to the power of 3?"

llm = OpenAI(temperature=0)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent.run(prompt)
