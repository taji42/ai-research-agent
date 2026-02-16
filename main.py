import os
from planner import create_research_plan

def main():
    print("--- 🤖 Autonomous Research Agent ---")
    goal = input("What is your research goal? ")
    
    print(f"\n[1] Planning strategy for: {goal}...")
    plan = create_research_plan(goal)
    queries = plan.get("search_queries", [])
    
    memory = []
    
    print(f"\n[2] Execution: Found {len(queries)} tasks.")
    for i, query in enumerate(queries, 1):
        print(f"\n🚀 Running Task {i}/{len(queries)}: {query}")
        
        # This simulates a tool/web search
        result = f"Summary data for '{query}'" 
        
        # Store in memory
        memory.append({"query": query, "result": result})
        print(f"✅ Saved to memory.")

    print("\n--- 🏁 Research Complete ---")
    print(f"The agent processed {len(memory)} tasks successfully.")
    for entry in memory:
        print(f"- {entry['query']}")

if __name__ == "__main__":
    main()
