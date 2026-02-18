import os
from planner import create_research_plan

def main():
    print("--- 🤖 Autonomous Research Agent (OpenRouter Mode) ---")
    goal = input("What is your research goal? ")
    
    if not goal:
        print("Goal cannot be empty.")
        return

    print(f"\n[1] Planning strategy for: {goal}...")
    plan = create_research_plan(goal)
    queries = plan.get("search_queries", [])
    
    memory = []
    
    print(f"\n[2] Execution: Found {len(queries)} tasks.")
    for i, query in enumerate(queries, 1):
        print(f"\n🚀 Running Task {i}/{len(queries)}: {query}")
        result = f"Captured data for '{query}'" 
        memory.append({"query": query, "result": result})
        print(f"✅ Saved to memory.")

    print("\n--- 🏁 Research Complete ---")
    for entry in memory:
        print(f"- {entry['query']}")

if __name__ == "__main__":
    main()
