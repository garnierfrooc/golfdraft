import pandas as pd
import json
import streamlit as st
import time
from datetime import datetime, timedelta
import pytz


# Assuming the JSON data is stored in a variable called 'data'
with open('masters2024-new.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Aaron": [
        "Si Woo Kim",
        "Russell Henley",
        "Byeong Hun An"
    ],
    "Richard": [
        "Bryson DeChambeau",
        "Patrick Cantlay",
        "Taylor Moore"
    ],
    "Andy": [
        "Hideki Matsuyama",
        "Jason Day",
        "Grayson Murray"
    ],
    "Marcus": [
        "Ludvig Aberg",
        "Rickie Fowler",
        "Nicolai Hojgaard"
    ],
    "Lewis": [
        "Shane Lowry",
        "Sergio Garcia",
        "Keegan Bradley"
    ],
    "Jonty": [
        "Viktor Hovland",
        "Phil Mickelson",
        "Chris Kirk"
    ],
    "Bean": [
        "Collin Morikawa",
        "Sahith Theegala",
        "Emiliano Grillo"
    ],
    "Phil": [
        "Dustin Johnson",
        "Cameron Young",
        "Sepp Straka"
    ],
    "Gary": [
        "Rory McIlroy",
        "Min Woo Lee",
        "Christo Lamprecht"
    ],
    "Jamie": [
        "Will Zalatoris",
        "Patrick Reed",
        "Denny McCarthy"
    ],
    "Beeton": [
        "Joaquin Niemann",
        "Tony Finau",
        "Jake Knapp"
    ],
    "Ben": [
        "Jon Rahm",
        "Tom Kim",
        "Gary Woodland"
    ],
    "Sean": [
        "Scottie Scheffler",
        "Sungjae Im",
        "Vijay Singh"
    ],
    "Ian": [
        "Jordan Spieth",
        "Adam Schenk",
        "Cameron Davis"
    ],
    "Bradley": [
        "Brooks Koepka",
        "Justin Rose",
        "Danny Willett"
    ],
    "Ben Powis-D": [
        "Wyndham Clark",
        "Adam Scott",
        "Ryan Fox"
    ],
    "Nick": [
        "Xander Schauffele",
        "Akshay Bhatia",
        "Harris English"
    ],
    "Dutty": [
        "Justin Thomas",
        "Max Homa",
        "Kurt Kitayama"
    ],
    "Chris": [
        "Sam Burns",
        "Corey Conners",
        "Erik Van Rooyen"
    ],
    "Dean": [
        "Cameron Smith",
        "Tiger Woods",
        "Bubba Watson"
    ],
    "Stu": [
        "Tommy Fleetwood",
        "Tyrrell Hatton",
        "Adrian Meronk"
    ],
    "Dave": [
        "Brian Harman",
        "Matt Fitzpatrick",
        "Adam Hadwin"
    ]
}

# Create a dictionary to store the separate tables for each player
player_tables = {}

# Function to load and process the data
def load_data():
    # Iterate over each player's selection
    for player, selections in players.items():
        # Create an empty dictionary to store player data
        player_data = {"Name": [], "Score": []}

        # Filter the leaderboard based on the player's selections
        filtered_data = [player_info for player_info in leaderboard if
                         player_info["first_name"] + " " + player_info["last_name"] in selections]

        # Sort the filtered data by score in ascending order
        sorted_data = sorted(filtered_data, key=lambda x: x["score"])

        # Iterate over the sorted data to populate player_data
        num_rounds = 0
        for player_info in sorted_data:
            player_data["Name"].append(
                player_info["first_name"] + " " + player_info["last_name"])
            player_data["Score"].append(player_info["score"])

            rounds = player_info["rounds"]
            # Update the maximum number of rounds played
            num_rounds = max(num_rounds, len(rounds))

            for i, round_info in enumerate(rounds, start=1):
                player_data[f"{i} Thru"] = player_data.get(f"{i} Thru", [])
                player_data[f"{i} Score"] = player_data.get(f"{i} Score", [])

                player_data[f"{i} Thru"].append(round_info["thru"])
                if round_info["thru"] == 18:
                    player_data[f"{i} Score"].append(round_info["strokes"])
                else:
                    # None if the round is not completed yet
                    player_data[f"{i} Score"].append(None)

        # Create a DataFrame from the player_data dictionary
        df = pd.DataFrame.from_dict(player_data)

        # Drop rows where any "Thru" column hasn't reached 18
        df_completed_rounds = df.dropna(
            subset=[f"{i} Thru" for i in range(1, num_rounds + 1)], how="any")

        # Hide the scores for incomplete rounds
        for i in range(1, num_rounds + 1):
            if not all(df_completed_rounds[f"{i} Thru"] == 18):
                df_completed_rounds[f"{i} Score"] = None

        # Remove the "Thru" column for completed rounds
        for i in range(1, num_rounds + 1):
            if all(df_completed_rounds[f"{i} Thru"] == 18):
                df_completed_rounds = df_completed_rounds.drop(
                    columns=[f"{i} Thru"])

        # Add the DataFrame to the player_tables dictionary
        player_tables[player] = df_completed_rounds

    # Concatenate all tables into a single DataFrame
    combined_df = pd.concat(player_tables.values())

    # Sort the player_tables dictionary by the combined score in ascending order
    sorted_player_tables = sorted(
        player_tables.items(), key=lambda x: x[1]["Score"].sum())

    return sorted_player_tables


# Function to display the tables in Streamlit
def display_tables(sorted_player_tables):
    # Determine the range of table positions for emoji sentiment mapping
    min_position = 0
    max_position = len(sorted_player_tables) - 1

    # CSS class definition for static table
    static_table_css = """
    .static-table th {
        background-color: #f4f4f4;
        color: black;
        font-weight: bold;
        text-align: left;
    }

    .static-table td {
        background-color: #ffffff;
        color: black;
        text-align: left;
    }

    .static-table-dark-mode th {
        background-color: #303030;
        color: white;
        font-weight: bold;
        text-align: left;
    }

    .static-table-dark-mode td {
        background-color: #424242;
        color: white;
        text-align: left;
    }

    .static-table {
        border-collapse: collapse;
        border: 1px solid #ccc;
        width: 100%;
    }
    """

    # Display the CSS class definition
    st.markdown(f'<style>{static_table_css}</style>', unsafe_allow_html=True)

    # Toggle between light and dark mode
    dark_mode = st.checkbox("Dark Mode")

    # Determine the appropriate table class based on the mode
    table_class = "static-table-dark-mode" if dark_mode else "static-table"

    # Display the sorted tables for each player using Streamlit
    for position, (player, df) in enumerate(sorted_player_tables):
        overall_score = df["Score"].sum()

        # Calculate the position range percentage for emoji sentiment mapping
        range_percentage = position / max_position

        # Map the range percentage to emoji sentiment (flipped scale)
        if range_percentage <= 0.1:
            emoji = "🏆"  # Big smile
        elif range_percentage <= 0.5:
            emoji = "🙂"  # Slight smile
        elif range_percentage <= 0.9:
            emoji = "😐"  # Neutral
        else:
            emoji = "💩"  # Turd

        st.subheader(f"{player} | Total: {overall_score} {emoji}")

        # Apply CSS class to make the table static
        styled_table = df.style.set_table_attributes(f'class="{table_class}"')

        # Convert styled table to HTML
        styled_table_html = styled_table.to_html(escape=False)

        # Display the styled table using write()
        st.write(styled_table_html, unsafe_allow_html=True)
        st.write("\n")


# Load and display the initial data
sorted_tables = load_data()

# Function to refresh the app
def refresh_app():
    # Load and display the updated data
    st.experimental_rerun()

# Refresh button
if st.button("Refresh", key="refresh_button"):
    st.experimental_rerun()

# Refresh button
if st.button("Add Complaint", key="complaint_button"):
    st.warning("Fuck off")

# Load and display the initial data
sorted_tables = load_data()
current_time = datetime.now(pytz.timezone('Europe/London')).strftime("%d-%m-%Y %H:%M")
st.title(f"Last Updated: {current_time}")
display_tables(sorted_tables)

# Auto-refresh the app every 1 minute
while True:
    time.sleep(60)
    refresh_app()
