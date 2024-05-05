print("program gives you ratings of valorant agents rated best to worst")

valorant_agents = [
    {"name": "Jett", "rating": "S"},
    {"name": "Sova", "rating": "S"},
    {"name": "Viper", "rating": "A"},
    {"name": "Omen", "rating": "A"},
    {"name": "Breach", "rating": "B"},
    {"name": "Phoenix", "rating": "B"},
    {"name": "Yoru", "rating": "C"},
    {"name": "Skye", "rating": "A"},
    {"name": "Killjoy", "rating": "A"},
    {"name": "Reyna", "rating": "S"},
    {"name": "Cypher", "rating": "B"},
    {"name": "Brimstone", "rating": "C"},
    {"name": "Sage", "rating": "A"},
    {"name": "KAY/O", "rating": "B"},
    {"name": "Astra", "rating": "A"},
    {"name": "Neon", "rating": "C"},
    {"name": "Chamber", "rating": "S"},
    {"name": "Raze", "rating": "B"},
    {"name": "Fade", "rating": "A"},
    {"name": "Harbor", "rating": "B"}
]
valorant_agents.append({"name": "Zoro", "rating": "A"}
)
a=len(valorant_agents)
print(f"We have total {a} no of agents.")
n=int(input(f"Which position agent do you wanna see? starting from 0 to {(a-1)} \n"))

print(valorant_agents[n])