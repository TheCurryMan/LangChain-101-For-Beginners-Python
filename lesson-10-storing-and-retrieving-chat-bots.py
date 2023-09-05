# Storing and Retrieving Chat History
import os

os.environ["OPENAI_API_KEY"] = "..."

from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain import OpenAI, ConversationChain

history = ChatMessageHistory()
history.add_user_message("hello! let's talk about giraffes")
history.add_ai_message("hi! i'm down to talk about giraffes")
dicts = messages_to_dict(history.messages)
new_messages = messages_from_dict(dicts)

llm = OpenAI(temperature=0)
history = ChatMessageHistory(messages=new_messages)
buffer = ConversationBufferMemory(chat_memory=history)
conversation = ConversationChain(llm=llm, memory=buffer, verbose=True)

print(conversation.predict(input="what are they?"))