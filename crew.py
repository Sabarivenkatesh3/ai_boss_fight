from crewai import Task, Crew
from agents import create_optimist, create_skeptic, create_judge

def create_debate_crew(topic: str):

    optimist = create_optimist()
    skeptic = create_skeptic()
    judge = create_judge()

    optimist_task = Task(
        description=(
            f"Debate Topic: {topic}\n\n"
            "Provide 5–7 strong bullet points arguing FOR the topic."
        ),
        agent=optimist,
        expected_output="5–7 bullet points supporting the topic"
    )

    skeptic_task = Task(
        description=(
            f"Debate Topic: {topic}\n\n"
            "Provide 5–7 strong bullet points arguing AGAINST the topic."
        ),
        agent=skeptic,
        expected_output="5–7 bullet points opposing the topic"
    )

    judge_task = Task(
        description=(
            "You have received arguments from both the Optimist and Skeptic.\n\n"
            "Decide who wins the debate.\n"
            "Explain your reasoning clearly.\n"
            "Assign a score between 0 and 10."
        ),
        agent=judge,
        expected_output=(
            "Winner, reasoning, and numeric score"
        )
    )

    crew = Crew(
        agents=[optimist, skeptic, judge],
        tasks=[optimist_task, skeptic_task, judge_task],
        verbose=True
    )

    return crew
