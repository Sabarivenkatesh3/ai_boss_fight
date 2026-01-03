from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192"
)

def create_optimist():
    return Agent(
        role="Optimist AI Engineer",
        goal="Strongly argue in favor of the debate topic",
        backstory="You believe AI accelerates innovation and productivity.",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

def create_skeptic():
    return Agent(
        role="Skeptic Software Architect",
        goal="Strongly argue against the debate topic",
        backstory="You prioritize stability, security, and reliability.",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

def create_judge():
    return Agent(
        role="Neutral AI Judge",
        goal="Evaluate both arguments fairly and decide a winner",
        backstory="You are unbiased and logic-driven.",
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
