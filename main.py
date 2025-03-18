from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize FastAPI app
app = FastAPI()

# Initialize LLM
llm = ChatGroq(api_key=GROQ_API_KEY, model="gemma2-9b-it")

# Define prompt template
prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=(
        "You are an AI-powered Data Science tutor with expertise in machine learning, "
        "statistics, data analysis, and AI concepts. Your goal is to teach users in a "
        "structured, clear, and engaging way.\n\n"
        "Conversation history:\n{history}\n"
        "User: {input}\n\n"
        "Provide a well-structured response following this format:\n\n"
        "1️⃣ **Introduction:** Briefly explain the concept.\n"
        "2️⃣ **Core Explanation:** Dive deeper into details with clarity.\n"
        "3️⃣ **Example:** Provide a real-world analogy or practical example.\n"
        "4️⃣ **Code (if applicable):** Share a relevant Python snippet with comments.\n"
        "5️⃣ **Conclusion:** Summarize key takeaways and encourage follow-up questions.\n\n"
        "Ensure clarity, engagement, and depth based on the user’s expertise level."
    )
)

# Dictionary to store user session histories
user_histories = {}

# Function to get session history
def get_session_history(session_id: str) -> ChatMessageHistory:
    """Retrieves or initializes a chat history for a session."""
    if session_id not in user_histories:
        user_histories[session_id] = ChatMessageHistory()
    return user_histories[session_id]

# Create conversation chain using RunnableWithMessageHistory
conversation = RunnableWithMessageHistory(
    llm,
    get_session_history=get_session_history,  # Fixes missing argument
    input_key="input",
    history_key="history",
)

# Define request model
class QueryRequest(BaseModel):
    user_input: str
    session_id: str  # Unique session identifier

@app.post("/ask")
async def ask_tutor(request: QueryRequest):
    """Handles user queries and returns AI responses."""
    response = conversation.invoke(
        {"input": request.user_input}, config={"configurable": {"session_id": request.session_id}}
    )
    return {"response": {"content": response}}  # Ensure consistent JSON format

