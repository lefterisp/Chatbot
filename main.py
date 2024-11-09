from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation(): 
    context = ""
    print("Welcome to AI ChatBot! Type 'exit' to quit")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Generate response using the chain
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)

        # Update the conversation context with the latest exchange
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
