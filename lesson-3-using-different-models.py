# Using different models with LangChain
import os

os.environ["OPENAI_API_KEY"] = "..."

from langchain import HuggingFaceHub

llm = HuggingFaceHub(
    repo_id="google/flan-t5-base", model_kwargs={"temperature": 0, "max_length": 64}
)
prompt = "What are good fitness tips?"

print(llm(prompt))
