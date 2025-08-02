# from crewai import Agent, Task, Crew, Process
# from chat.rag_service import get_rag_chain
# from langchain_ollama import OllamaLLM

# local_llm = OllamaLLM(model="phi3", temperature=0.1)

# def run_crew_chatbot(query):
#     rag_chain = get_rag_chain()

#     def rag_tool(input_text):
#         return rag_chain.run(input_text)

#     retriever_agent = Agent(
#         role="RetrieverAgent",
#         goal="Retrieve relevant KB info",
#         backstory="Expert in semantic search from the IT knowledge base.",
#         llm=local_llm,
#         tools=[rag_tool],
#         verbose=True
#     )

#     responder_agent = Agent(
#         role="ResponderAgent",
#         goal="Generate helpful answers",
#         backstory="IT assistant trained to solve user issues",
#         tools=[rag_tool],
#         llm=local_llm,
#         verbose=True
#     )

#     retrieval_task = Task(description=f"Find docs for query: {query}", agent=retriever_agent, expected_output="Relevant info")
#     response_task = Task(description=f"Answer the question: {query}", agent=responder_agent, expected_output="Helpful answer")

#     crew = Crew(
#         agents=[retriever_agent, responder_agent],
#         tasks=[retrieval_task, response_task],
#         process=Process.sequential,
#         verbose=True
#     )

#     # result = crew.run()
#     return crew.kickoff()
    # return result



# from crewai import Agent, Task, Crew, Process
# from langchain.agents import Tool
# from langchain_ollama import OllamaLLM
# from chat.rag_service import get_rag_chain

# # Load the LangChain RAG chain
# rag_chain = get_rag_chain()

# # Define the Ollama LLM
# local_llm = OllamaLLM(model="phi3", temperature=0.1)

# # Wrap your RAG tool into a proper Tool object
# rag_search_tool = Tool(
#     name="RAGSearch",
#     func=rag_chain.run,
#     description="Retrieves relevant context from the IT support knowledge base using LangChain + ChromaDB."
# )

# def run_crew_chatbot(query):
#     # Define agents with tools
#     retriever_agent = Agent(
#         role="RetrieverAgent",
#         goal="Retrieve relevant KB info",
#         backstory="Expert in semantic search from the IT knowledge base.",
#         tools=[rag_search_tool],  # ✅ proper Tool object
#         llm=local_llm,
#         verbose=True
#     )

#     responder_agent = Agent(
#         role="ResponderAgent",
#         goal="Generate helpful answers using retrieved info",
#         backstory="IT assistant trained to solve user issues based on search results.",
#         tools=[rag_search_tool],  # ✅ reused tool
#         llm=local_llm,
#         verbose=True
#     )

#     # Define tasks
#     retrieval_task = Task(
#         description=f"Search the knowledge base and find relevant content for: {query}",
#         agent=retriever_agent,
#         expected_output="Relevant context or data"
#     )

#     response_task = Task(
#         description=f"Use the retrieved context to answer this query: {query}",
#         agent=responder_agent,
#         expected_output="Helpful and detailed answer"
#     )

#     # Create the crew
#     crew = Crew(
#         agents=[retriever_agent, responder_agent],
#         tasks=[retrieval_task, response_task],
#         process=Process.sequential,
#         verbose=True
#     )

#     return crew.kickoff()  # ✅ Launch the multi-agent process



# from crewai import Agent, Task, Crew, Process
# from crewai.tools import tool
# from langchain_community.llms import Ollama
# from chat.rag_service import get_rag_chain

# # ✅ Get RAG chain
# rag_chain = get_rag_chain()

# # ✅ Use correct Ollama LLM compatible with LangChain and CrewAI
# local_llm = Ollama(model="phi3", temperature=0.1)

# # ✅ Define as CrewAI tool
# @tool
# def rag_search_tool(query: str) -> str:
#     """Search IT knowledge base using LangChain + ChromaDB"""
#     return rag_chain.run(query)

# # ✅ CrewAI chatbot with agents
# def run_crew_chatbot(query):
#     retriever_agent = Agent(
#         role="RetrieverAgent",
#         goal="Retrieve relevant KB info",
#         backstory="Expert in searching IT support documents.",
#         tools=[rag_search_tool],
#         llm=local_llm,
#         verbose=True
#     )

#     responder_agent = Agent(
#         role="ResponderAgent",
#         goal="Give clear and helpful answers",
#         backstory="IT helpdesk assistant with domain expertise.",
#         tools=[rag_search_tool],
#         llm=local_llm,
#         verbose=True
#     )

#     retrieval_task = Task(
#         description=f"Find the most relevant information for: {query}",
#         agent=retriever_agent,
#         expected_output="Relevant content from knowledge base"
#     )

#     response_task = Task(
#         description=f"Answer the user question using retrieved information: {query}",
#         agent=responder_agent,
#         expected_output="Helpful response to the user"
#     )

#     crew = Crew(
#         agents=[retriever_agent, responder_agent],
#         tasks=[retrieval_task, response_task],
#         process=Process.sequential,
#         verbose=True
#     )

#     return crew.kickoff()



# from crewai import Agent, Task, Crew, Process
# from crewai.tools import tool
# from chat.rag_service import get_rag_chain  # your RAG function with phi3 + Chroma

# # ✅ Load your RAG chain using LangChain + Ollama
# rag_chain = get_rag_chain()

# # ✅ Define a CrewAI-compatible tool
# @tool
# def rag_search_tool(query: str) -> str:
#     """Search IT knowledge base using LangChain RAG + Ollama phi3"""
#     return rag_chain.run(query)

# # ✅ Main function that CrewAI will run
# def run_crew_chatbot(query):
#     # Only use tools — do NOT pass LLM here to avoid OpenAI fallback
#     responder_agent = Agent(
#         role="ITSupportAgent",
#         goal="Answer user questions using the IT knowledge base",
#         backstory="A reliable IT assistant that searches and responds using internal documentation.",
#         tools=[rag_search_tool],  # This will trigger your RAG pipeline
#         verbose=True
#     )

#     response_task = Task(
#         description=f"Answer the following IT support question: {query}",
#         agent=responder_agent,
#         expected_output="A clear and helpful support response."
#     )

#     crew = Crew(
#         agents=[responder_agent],
#         tasks=[response_task],
#         process=Process.sequential,
#         verbose=True
#     )

#     # ✅ Trigger the tool, which uses LangChain RAG + Ollama phi3
#     return crew.kickoff(inputs={"query": query})

