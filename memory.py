class Memory:
    def __init__(self):
        self.notes = []

    def add_note(self, query: str, result: str):
        """
        Add a new note to memory.
        Each note tracks:
        - query
        - result
        - done: whether the agent considers this query fully processed
        """
        self.notes.append({
            "query": query,
            "result": result,
            "done": False  # initially not done
        })

    def mark_done(self, query: str):
        """
        Mark a query as done.
        """
        for note in self.notes:
            if note["query"] == query:
                note["done"] = True

    def get_pending_queries(self, all_queries: list):
        """
        Return queries that have not been processed yet.
        If a query is not in memory, it's pending.
        """
        pending = []
        for query in all_queries:
            # Check if query exists in memory and is done
            in_memory = next((note for note in self.notes if note["query"] == query), None)
            if not in_memory or not in_memory["done"]:
                pending.append(query)
        return pending

    def get_all_notes(self):
        return self.notes

