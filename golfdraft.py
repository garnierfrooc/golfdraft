import pandas as pd
import json
import streamlit as st


# Assuming the JSON data is stored in a variable called 'data'
with open('leaderboard.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Daniel": [
        "Jon Rahm",
        "Russell Henley",
        "Sam Burns",
        "Victor Perez"
    ],
    "Sean": [
        "Justin Thomas",
        "Cameron Young",
        "Patrick Reed",
        "Denny McCarthy"
    ],
    "Andy": [
        "Tony Finau",
        "Keegan Bradley",
        "Sahith Theegala",
        "Webb Simpson"
    ],
    "Marcus": [
        "Jason Day",
        "Jordan Spieth",
        "Rickie Fowler",
        "Nick Taylor"
    ],
    "Lewis": [
        "Scottie Scheffler",
        "Viktor Hovland",
        "Dustin Johnson",
        "Talor Gooch"
    ],
    "Jonty": [
        "Brooks Koepka",
        "Tyrrell Hatton",
        "Shane Lowry",
        "Thomas Pieters"
    ],
    "Bean": [
        "Rory McIlroy",
        "Cameron Smith",
        "Adam Scott",
        "Gary Woodland"
    ],
    "Phil": [
        "Collin Morikawa",
        "Patrick Cantlay",
        "Hideki Matsuyama",
        "Joel Dahmen"
    ],
    "Gary": [
        "Max Homa",
        "Matt Fitzpatrick",
        "Justin Rose",
        "Phil Mickelson"
    ],
    "Jamie": [
        "Xander Schauffele",
        "Sungjae Im",
        "Wyndham Clark",
        "Mito Pereira"
    ]
}

# Create a dictionary to store the separate tables for each player
player_tables = {}

# Iterate over each player's selection
for player, selections in players.items():
    # Create an empty dictionary to store player data
    player_data = {"Name": [], "Overall Score": []}

    # Filter the leaderboard based on the player's selections
    filtered_data = [player_info for player_info in leaderboard if
                     player_info["first_name"] + " " + player_info["last_name"] in selections]

    # Sort the filtered data by score in ascending order
    sorted_data = sorted(filtered_data, key=lambda x: x["score"])

    # Iterate over the sorted data to populate player_data
    for player_info in sorted_data:
        player_data["Name"].append(
            player_info["first_name"] + " " + player_info["last_name"])
        player_data["Overall Score"].append(player_info["score"])

        rounds = player_info["rounds"]
        for i, round_info in enumerate(rounds, start=1):
            player_data[f"Round {i} Sequence"] = player_data.get(
                f"Round {i} Sequence", [])
            player_data[f"Round {i} Thru"] = player_data.get(
                f"Round {i} Thru", [])

            player_data[f"Round {i} Sequence"].append(round_info["sequence"])
            player_data[f"Round {i} Thru"].append(round_info["thru"])

    # Create a DataFrame from the player_data dictionary
    df = pd.DataFrame(player_data)

    # Add the DataFrame to the player_tables dictionary
    player_tables[player] = df

# Sort the player_tables dictionary by the combined score in ascending order
sorted_player_tables = sorted(
    player_tables.items(), key=lambda x: x[1]["Overall Score"].sum())

# Determine the range of table positions for emoji sentiment mapping
min_position = 0
max_position = len(sorted_player_tables) - 1

# Display the sorted tables for each player using Streamlit
for position, (player, df) in enumerate(sorted_player_tables):
    overall_score = df["Overall Score"].sum()

    # Calculate the position range percentage for emoji sentiment mapping
    range_percentage = position / max_position

    # Map the range percentage to emoji sentiment (flipped scale)
    if range_percentage <= 0.1:
        emoji = "😄"  # Big smile
    elif range_percentage <= 0.5:
        emoji = "🙂"  # Slight smile
    elif range_percentage <= 0.9:
        emoji = "😐"  # Neutral
    else:
        emoji = "💩"  # Turd

    st.subheader(f"{player}'s Table (Overall Score: {overall_score}) {emoji}")
    st.write(df.drop("Overall Score", axis=1))
    st.write("\n")
