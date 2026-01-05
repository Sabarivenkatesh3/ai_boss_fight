from crewai import Task
from crewai import Crew
from agents import optimist_agent, skeptic_agent, judge_agent

optimist_task = Task(
    description="Generate arguments highlighting the positive aspects and benefits of the given topic.",
    expected_output="A short list of bullet-point arguments describing the benefits and positive impacts of the topic.",
    agent=optimist_agent
)

skeptic_task = Task(
    description="Generate arguments highlighting the worst-case aspects, risks, and drawbacks of the given topic.",
    expected_output="A short list of bullet-point arguments describing risks, limitations, and potential failures related to the topic.",
    agent=skeptic_agent
)

judge_task = Task(
    description="Evaluate and compare the arguments produced by the Optimist and Skeptic agents.",
    expected_output=(
        "A final verdict that includes the winning side, a clear reasoning for the decision, "
        "and a numerical score representing the strength of the winning argument."
    ),
    agent=judge_agent
)


debate_crew = Crew(
    agents=[optimist_agent, skeptic_agent, judge_agent],
    tasks=[optimist_task, skeptic_task, judge_task],
    verbose=True
)
