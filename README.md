# 🧠 AI Boss Fight – Multi-Agent Debate System

AI Boss Fight is a multi-agent AI system built using **CrewAI** that simulates structured debates between autonomous agents and produces a fair, reasoned verdict.

This project demonstrates **agent collaboration, conflict resolution, and decision-making**, inspired by real-world AI governance and product discussions.

---

## 🎯 Objective

To build a system where:
- One AI agent argues **for** a topic
- One AI agent argues **against** the topic
- A neutral judge agent evaluates both sides and decides a winner

---

## 🧩 System Architecture

User Topic
↓
Optimist Agent (Pros)
↓
Skeptic Agent (Cons)
↓
Judge Agent (Evaluation + Verdict)


---

## 🤖 Agents

### 1️⃣ Optimist Agent
- Focuses only on **benefits and positive outcomes**
- Uses logical, factual reasoning
- Produces concise bullet-point arguments

### 2️⃣ Skeptic Agent
- Focuses only on **risks, failures, and worst-case scenarios**
- Opposes the Optimist’s arguments
- Maintains ethical and educational tone

### 3️⃣ Judge Agent
- Receives outputs from both agents
- Evaluates objectively using real-world practicality
- Declares a **winner and score (0–10)**

---

## 🛠 Tech Stack

- **Language:** Python
- **Framework:** CrewAI
- **LLM Provider:** Groq (via LiteLLM)
- **Execution:** CLI-based
- **Secrets Management:** `.env` file

---

## 📁 Project Structure

ai_boss_fight/
│
├── agents.py # Agent roles, goals, backstories
├── crew.py # Tasks and execution order
├── run.py # Entry point (CLI execution)
├── .env # API keys (not committed)
└── README.md

---

## ▶️ How to Run

1. Create a virtual environment and install dependencies
2. Add your Groq API key in `.env`:
GROQ_API_KEY=your_api_key_here
3. Run the system:
```bash
python run.py

---

## 📤 Sample Output

Optimist Agent:
• AI increases development speed and productivity.
• Developers can focus on higher-level design and strategy.

Skeptic Agent:
• AI-generated code may introduce security vulnerabilities.
• Lack of transparency can reduce accountability.

Judge Verdict:
Winner: Skeptic Agent
Reasoning: Risks outweigh benefits in high-stakes environments.
Score: 8 / 10


---

## 🌱 Future Enhancements

Custom topic input via CLI arguments

Multi-round debates with rebuttals

JSON-structured outputs

Debate history logging

Token usage tracking

## 💡 Key Learnings

Agent role separation

Prompt engineering & output control

Sequential agent workflows

Real-world LLM integration

AI system debugging and reliability