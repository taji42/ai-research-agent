# 🤖 Autonomous AI Research Agent

An intelligent agent built in Python that uses **Gemini 2.0 Flash** to autonomously plan, execute, and store research data.

## 🌟 How it Works
1. **Planner:** The agent analyzes your goal and creates a 3-step search strategy.
2. **Executor:** It iterates through the plan, performing (simulated) web searches.
3. **Memory:** Every finding is saved into a stateful memory class, preventing duplicate work.

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **LLM:** Google Gemini 2.0 Flash (via Google AI Studio)
* **Environment:** Managed with `python-dotenv` for security.

## 🚀 Setup
1. Clone this repository.
2. Create a `.env` file and add your API key:
   `GEMINI_API_KEY=your_key_here`
3. Run the agent:
   ```bash
   python3 main.py
