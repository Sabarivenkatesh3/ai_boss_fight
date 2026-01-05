from crewai import Task
from crewai import Crew
from agents import optimist_agent, skeptic_agent, judge_agent

optimist_task = Task(
    description="Analyze the debate topic: “{topic}”.Generate only positive arguments that support allowing this idea in real-world usage.Focus strictly on benefits, advantages, opportunities, and positive outcomes related to the topic.Do not mention risks, drawbacks, or negative impacts.All statements must be factually reasonable and logically sound.",
    expected_output="Output ONLY in bullet points.Output EXACTLY 2 bullet points.Each bullet point must be 1–2 sentences only.Do NOT add introductions, conclusions, headings, or explanations.Do NOT repeat the topic text",
    agent=optimist_agent
)

skeptic_task = Task(
    description="Analyze the same debate topic: “{topic}”.Generate only critical arguments that oppose the idea by examining worst-case scenarios, risks, and failures.Focus on real-world limitations, negative consequences, and potential harm.Do not mention benefits or positive outcomes.Arguments must remain educational, ethical, and non-offensive.",
    expected_output="Output ONLY in bullet points.Output EXACTLY 2 bullet points.Each bullet point must be 1–2 sentences only.Use realistic, non-offensive, educational language.Do NOT add introductions, conclusions, or extra commentary",
    agent=skeptic_agent
)


judge_task = Task(
    description="Evaluate the arguments produced by the Optimist Agent and Skeptic Agent for the topic: “{topic}”.Compare both sides objectively using real-world practicality, impact, and reasoning quality.Do not introduce new arguments or personal opinions.Your responsibility is to decide which argument is stronger overall.",
    expected_output=(
        "Winner: Optimist Agent / Skeptic Agent"
        "Reasoning: 2–3 sentences maximum"
        "Score: X / 10"
        
    ),
    agent=judge_agent
)


debate_crew = Crew(
    agents=[optimist_agent, skeptic_agent, judge_agent],
    tasks=[optimist_task, skeptic_task, judge_task],
    verbose=True
)
