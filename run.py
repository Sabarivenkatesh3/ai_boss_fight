from crew import create_debate_crew

def main():
    topic = "Should companies allow AI to write production code?"

    crew = create_debate_crew(topic)
    result = crew.kickoff()

    print("\n" + "="*60)
    print("🧠 AI BOSS FIGHT RESULT")
    print("="*60)
    print(result)

if __name__ == "__main__":
    main()
