from crew import debate_crew

if __name__ == "__main__":
    topic = "Should companies allow AI to write production code?"
    
    result = debate_crew.kickoff(inputs={"topic": topic})
    
    print("\n=== AI Boss Fight Result ===\n")
    print(result)
