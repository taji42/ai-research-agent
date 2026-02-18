# 🤖 Autonomous AI Research Agent

An agentic Python system that takes a high-level research goal, breaks it into a multi-step execution plan, and stores findings in a stateful memory.

## 🚀 The Mission
This project demonstrates **Agentic Design Patterns**—moving beyond simple chatbots to systems that can plan and execute tasks autonomously.

## 🧠 Features
- **The Planner:** Uses an LLM (Gemini/DeepSeek via OpenRouter) to decompose complex goals into search queries.
- **Resilient Logic:** Built-in "Fallback Mode" that ensures the agent continues working even if API limits or regional blocks occur.
- **Stateful Memory:** Tracks task execution history in a structured format.

## 🛠️ Tech Stack
- **Python 3.12+**
- **OpenRouter API** (Accessing Gemini 2.0/2.5 & DeepSeek R1)
- **Git/GitHub** for version control
- **Dotenv** for secure credential management

## 🔧 Installation & Usage
1. Clone the repo: `git clone https://github.com/taji42/ai-research-agent.git`
2. Install dependencies: `pip install python-dotenv requests`
3. Add your `OPENROUTER_API_KEY` to a `.env` file.
4. Run the agent: `python3 main.py`

---
*Note: This project was built to navigate real-world engineering hurdles, including regional API blocks and model deprecations, showcasing a focus on fault-tolerant AI development.*
