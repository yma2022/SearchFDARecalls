from embedding import embed_database
from agent import XMLSearchAgent

def main():
    vector_store = embed_database("./data")
    agent = XMLSearchAgent(vector_store)
    while True:
        query = input("Enter your query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break
        response = agent.run(query)
        print(f"Response: {response}")

if __name__ == "__main__":
    main()