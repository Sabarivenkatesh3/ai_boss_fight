import sys
from crew import debate_crew

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please provide a debate topic.")
        print('Example: python run.py "Should AI write production code?"')
        sys.exit(1)

    topic = " ".join(sys.argv[1:])


    result = debate_crew.kickoff(inputs={"topic": topic})

    print("\n=== AI Boss Fight Result ===\n")
    print(result)
