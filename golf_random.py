import json
import random

def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def select_random_golfers(json_file, rankings_file):
    open_data = load_json(json_file)
    leaderboard = open_data.get('leaderboard', [])
    rankings_data = load_json(rankings_file)
    ranked_players = rankings_data.get('players', [])

    first_fifteen_players = [player for player in ranked_players if 1 <= player['rank'] <= 15]
    sixteen_thirty_players = [player for player in ranked_players if 16 <= player['rank'] <= 30]
    thirtyone_fortyfive_players = [player for player in ranked_players if 31 <= player['rank'] <= 45]
    seventyfive_ninety_players = [player for player in ranked_players if 75 <= player['rank'] <= 90]

    selected_golfers = []

    # Select 1 player from ranks 1-15
    selected_golfers.append(random.choice(first_fifteen_players))

    # Select 1 player from ranks 16-30
    selected_golfers.append(random.choice(sixteen_thirty_players))

    # Select 1 player from ranks 31-45
    selected_golfers.append(random.choice(thirtyone_fortyfive_players))

    # Select 1 player from ranks 75-90
    selected_golfers.append(random.choice(seventyfive_ninety_players))

    # Get the corresponding first_name, last_name, and rank for each selected golfer
    selected_golfers_info = []
    for golfer in selected_golfers:
        first_name = golfer['first_name']
        last_name = golfer['last_name']
        rank = golfer['rank']
        selected_golfers_info.append((first_name, last_name, rank))

    return selected_golfers_info

if __name__ == "__main__":
    open_json_file = "open-leaderboard.json"
    rankings_json_file = "rankings.json"

    selected_golfers = select_random_golfers(open_json_file, rankings_json_file)

    print("Randomly selected golfers:")
    for idx, (first_name, last_name, rank) in enumerate(selected_golfers, start=1):
        print(f"{idx}. {first_name} {last_name} (Rank: {rank})")
