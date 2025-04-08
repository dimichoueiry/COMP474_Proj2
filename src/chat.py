from langchain_ollama import OllamaLLM

def main():
    # Initialize the chat model
    llm = OllamaLLM(model="llama3.2")
    
    # Example chat
    query = "What is the admission process for Computer Science at Concordia?"
    response = llm.invoke(query)
    print(f"Response: {response}")

if __name__ == "__main__":
    main() 