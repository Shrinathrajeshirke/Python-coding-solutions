# Write a function that maintains a leaderboard.
# Sort players by score (descending), use binary 
# search to find a player's rank.

def leaderboard(players, search_name):
    sorted_players = sorted(players, key= lambda x: x[1], reverse=True)

    print("Leaderboard:")
    for rank, (name, score) in enumerate(sorted_players,start=1):
        print(f"{rank}. {name} - {score}")
    
    for rank, (name, score) in enumerate(sorted_players,start=1):
        if name == search_name:
            print(f"\n{search_name} is ranked #{rank}")
        
players = [
    ("Alice", 850),
    ("Bob", 920),
    ("Charlie", 750),
    ("David", 980),
    ("Eve", 870)
]

leaderboard(players, "Alice")

















