# Prompts and LLMs
import os

os.environ["OPENAI_API_KEY"] = "..."

from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

template = "You are a naming consultant for new companies. What is a good name for a {company} that makes {product}?"

prompt = PromptTemplate.from_template(template)
llm = OpenAI(temperature=0.9)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run({"company": "ABC Startup", "product": "colorful socks"}))
