from src.agent import RealityChecker

agent = RealityChecker()
graph = agent.build_graph()

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    state = {"messages": [{"role": "user", "content": user_input}]}
    result = graph.invoke(state)
    print("Agent:\n", result["messages"][-1].content)