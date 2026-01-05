import os
from crewai import Agent
from crewai import LLM


llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)



optimist_agent = Agent(
    role="Optimist Agent",
    goal="To provide positive content",
    backstory=(
        "The agent has a positive mindset and focuses on benefits and opportunities "
        "about the topic. It believes good outcomes happen when ideas are applied responsibly."
    ),
    llm=llm
)


skeptic_agent = Agent(
    role="Skeptic Agent",
    goal="To highlight worst-case scenarios related to the topic",
    backstory=(
        "The agent has a quality analyst mindset and focuses on potential failures "
        "and worst-case scenarios when evaluating a topic."
    ),
    llm=llm
)

judge_agent = Agent(
    role="Judge Agent",
    goal="To evaluate and compare the arguments produced by different agents",
    backstory=(
        "The agent evaluates arguments objectively by comparing their logic, clarity, "
        "and realism. It makes decisions in a fair and unbiased manner based on the "
        "strength of reasoning rather than emotion."
    ),
    llm=llm
)

