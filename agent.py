from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
class XMLSearchAgent:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
        self.setup_agent()

    def setup_agent(self):
        """Set up the agent using LangGraph."""
        retriever = self.vector_store.as_retriever()
        prompt = ChatPromptTemplate.from_template(
            "You are an assistant that searches through recall data. Please list all the relevant recalls with their brand, company, date, product description, reason, and URL in a table in markdown based on the context.\n\nContext:\n{context}\n\nQuestion:\n{question}"
        )

        self.chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )

        @tool
        def recall_search(query: str) -> str:
            """Search through recall data."""
            return self.chain.invoke(query)

        tools = [recall_search]

        checkpointer = MemorySaver()

        self.app = create_react_agent(self.llm, tools, checkpointer=checkpointer)

    def run(self, query):
        """Run the agent with a user query."""
        final_state = self.app.invoke({"messages": [{"role": "user", "content": query}]},
        config={"configurable": {"thread_id": 42}})
        return final_state["messages"][-1].content

if __name__ == "__main__":
    from embedding import embed_database
    vector_store = embed_database("./data")
    agent = XMLSearchAgent(vector_store)
    response = agent.run("Find recalls related to defective products.")
    print(response)