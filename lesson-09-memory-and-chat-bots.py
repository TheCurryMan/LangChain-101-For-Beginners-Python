# Memory and Chat Bots
import os

os.environ["OPENAI_API_KEY"] = "..."

from langchain import OpenAI, ConversationChain

# Printing Predictions
llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

print(conversation.predict(input="Hi there!"))
print(conversation.predict(input="Can we talk about weather?"))
print(conversation.predict(input="It's a beautiful day today"))

# -------------------------------------------------------------
# Creating an interactive terminal Chat Bot
llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm)

print("Welcome to your AI chatbot! What's on your mind?")
for _ in range(0, 3):
    human_input = input("You: ")
    ai_response = conversation.predict(input=human_input)
    print(f"AI: {ai_response}")
