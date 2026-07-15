import pandas as pd
import json
import streamlit as st
import time
from datetime import datetime, timedelta
import pytz
import math

A1 = "Jon Rahm"
A2 = "Matt Fitzpatrick"
A3 = "Rory McIlroy"
A4 = "Scottie Scheffler"
A5 = "Tommy Fleetwood"
B1 = "Cameron Young"
B2 = "Chris Gotterup"
B3 = "Collin Morikawa"
B4 = "Justin Rose"
B5 = "Ludvig Åberg"
B6 = "Robert MacIntyre"
B7 = "Tyrrell Hatton"
B8 = "Viktor Hovland"
B9 = "Wyndham Clark"
B10 = "Xander Schauffele"
C1 = "Aaron Rai"
C2 = "Alex Fitzpatrick"
C3 = "Brooks Koepka"
C4 = "Bryson DeChambeau"
C5 = "Joaquin Niemann"
C6 = "Jordan Spieth"
C7 = "Justin Thomas"
C8 = "Min Woo Lee"
C9 = "Patrick Cantlay"
C10 = "Patrick Reed"
C11 = "Russell Henley"
C12 = "Sam Burns"
C13 = "Shane Lowry"
C14 = "Si Woo Kim"
C15 = "Tom Kim"
D1 = "Adam Scott"
D2 = "Akshay Bhatia"
D3 = "Ben Griffin"
D4 = "Brian Harman"
D5 = "Cameron Smith"
D6 = "Corey Conners"
D7 = "David Puig"
D8 = "Harris English"
D9 = "Hideki Matsuyama"
D10 = "Jake Knapp"
D11 = "Jason Day"
D12 = "J.J. Spaun"
D13 = "Kristoffer Reitan"
D14 = "Kurt Kitayama"
D15 = "Marco Penge"
D16 = "Maverick McNealy"
D17 = "Nicolai Højgaard"
D18 = "Rasmus Højgaard"
D19 = "Rickie Fowler"
D20 = "Sepp Straka"
D21 = "Victor Perez"
D22 = "Michael Thorbjornsen"
E1 = "Alex Noren"
E2 = "Angel Ayora"
E3 = "Bud Cauley"
E4 = "Eric Cole"
E5 = "Eugenio Chacarra"
E6 = "Gary Woodland"
E7 = "Haotong Li"
E8 = "Harry Hall"
E9 = "J.T. Poston"
E10 = "Jacob Bridgeman"
E11 = "Jayden Schaper"
E12 = "Jordan L. Smith"
E13 = "Lucas Herbert"
E14 = "Max Homa"
E15 = "Rasmus Neergaard-Petersen"
E16 = "Ryan Fox"
E17 = "Ryan Gerard"
E18 = "Ryo Hisatsune"
E19 = "Sahith Theegala"
E20 = "Sungjae Im"
F1 = "Alex Smalley"
F2 = "Andrew Novak"
F3 = "Bernd Wiesberger"
F4 = "Billy Horschel"
F5 = "Casey Jarvis"
F6 = "Daniel Berger"
F7 = "Daniel Brown"
F8 = "Daniel Hillier"
F9 = "Francesco Laporta"
F10 = "Hennie du Plessis"
F11 = "Jackson Suber"
F12 = "Jesper Svensson"
F13 = "John Parry"
F14 = "Keegan Bradley"
F15 = "Keita Nakajima"
F16 = "Keith Mitchell"
F17 = "Laurie Canter"
F18 = "Louis Oosthuizen"
F19 = "Matt McCarty"
F20 = "Matt Wallace"
F21 = "Matthew Jordan"
F22 = "Max Greyserman"
F23 = "Michael Brennan"
F24 = "Michael Kim"
F25 = "Nick Taylor"
F26 = "Pierceson Coody"
F27 = "Sam Stevens"
F28 = "Scott Vincent"
F29 = "Thomas Detry"
F30 = "Tom McKibbin"

# Assuming the JSON data is stored in a variable called 'data'
with open('ukopen2024.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Stef - 15/18": [
        A2, B2, C14, D22, E12, F15
    ],
    "Marc - 16/17": [
        A2, B4, C13, D2, E12, F22
    ],
    "Jonty - 17/19": [
        A3, B2, C15, D12, E10, F19
    ],
    "Graeme - 14/18": [
        A2, B4, C6, D9, E7, F4
    ],
    "Gary - 17/16": [
        A2, B4, C2, D3, E14, F4
    ],
    "Tom - 17/17": [
        A3, B9, C8, D22, E15, F15
    ],
    "Phil - 18/18": [
        A3, B10, C13, D6, E20, F6
    ],
    "Mark - 17/18": [
        A3, B4, C3, D4, E1, F14
    ],
    "Stu - 15/14": [
        A3, B4, C1, D6, E12, F20
    ],
    "Chris - 16/20": [
        A5, B7, C10, D21, E17, F30
    ],
    "Bean - 17/16": [
        A4, B10, C10, D16, E19, F25
    ],
    "Nick - 20/22": [
        A2, B2, C2, D2, E2, F2
    ],
    "Ian - 13/16": [
        A5, B7, C12, D4, E15, F24
    ],
    "Pye - 17/19": [
        A3, B4, C6, D1, E12, F25
    ],
    "Lewis - 19/17": [
        A4, B3, C13, D6, E20, F6
    ],
    "Jamie - 17/17": [
        A4, B9, C15, D14, E17, F25
    ],
    "Barry - 19/22": [
        A3, B4, C13, D18, E14, F14
    ]
}

# Function to load and process the data
def load_data():
    player_tables = {}
    
    for player, selections in players.items():
        player_data = {"Name": [], "Score": []}
        filtered_data = [player_info for player_info in leaderboard if
                         player_info["first_name"] + " " + player_info["last_name"] in selections]
        
        for player_info in filtered_data:
            full_name = player_info["first_name"] + " " + player_info["last_name"]
            score = player_info["score"]
            if player_info.get("status") == "CUT":
                score *= 2
                score = math.ceil(score)
                full_name += "*"

            player_data["Name"].append(full_name)
            player_data["Score"].append(score)

            rounds = player_info["rounds"]
            num_rounds = len(rounds)
            for i, round_info in enumerate(rounds, start=1):
                player_data[f"{i} Thru"] = player_data.get(f"{i} Thru", [])
                player_data[f"{i} Score"] = player_data.get(f"{i} Score", [])

                player_data[f"{i} Thru"].append(round_info["thru"])
                if round_info["thru"] == 18:
                    player_data[f"{i} Score"].append(round_info["strokes"])
                else:
                    player_data[f"{i} Score"].append(None)

        df = pd.DataFrame.from_dict(player_data)
        df_completed_rounds = df.dropna(subset=[f"{i} Thru" for i in range(1, num_rounds + 1)], how="any")
        
        for i in range(1, num_rounds + 1):
            if not all(df_completed_rounds[f"{i} Thru"] == 18):
                df_completed_rounds[f"{i} Score"] = None
        for i in range(1, num_rounds + 1):
            if all(df_completed_rounds[f"{i} Thru"] == 18):
                df_completed_rounds = df_completed_rounds.drop(columns=[f"{i} Thru"])
        
        player_tables[player] = df_completed_rounds

    combined_df = pd.concat(player_tables.values())
    sorted_player_tables = sorted(player_tables.items(), key=lambda x: x[1]["Score"].sum())

    return sorted_player_tables

# Function to calculate total birdies or better for a player
def calculate_birdies_or_better(player_name):
    player_data = next((p for p in leaderboard if p["first_name"] + " " + p["last_name"] == player_name), None)
    if not player_data:
        return 0

    total_birdies_or_better = sum(
        round_info["birdies"] + round_info["eagles"] + round_info["holes_in_one"]
        for round_info in player_data["rounds"]
    )
    return total_birdies_or_better

# Function to display the tables in Streamlit
def display_tables(sorted_player_tables):
    min_position = 0
    max_position = len(sorted_player_tables) - 1
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
    st.markdown(f'<style>{static_table_css}</style>', unsafe_allow_html=True)
    dark_mode = st.checkbox("Dark Mode")
    table_class = "static-table-dark-mode" if dark_mode else "static-table"

    for position, (player, df) in enumerate(sorted_player_tables):
        overall_score = df["Score"].sum()
        range_percentage = position / max_position
        if range_percentage <= 0.1:
            emoji = "🏆"
        elif range_percentage <= 0.5:
            emoji = "🙂"
        elif range_percentage <= 0.9:
            emoji = "😐"
        else:
            emoji = "💩"

        st.subheader(f"{player} | Total: {overall_score} {emoji}")
        styled_table = df.style.set_table_attributes(f'class="{table_class}"')
        styled_table_html = styled_table.to_html(escape=False)
        st.write(styled_table_html, unsafe_allow_html=True)
        st.write("\n")

# Calculate birdies or better for Scottie Scheffler and Rory McIlroy
scottie_birdies_or_better = calculate_birdies_or_better("Scottie Scheffler")
rory_birdies_or_better = calculate_birdies_or_better("Rory McIlroy")

# Load and display the initial data
sorted_tables = load_data()

# Function to refresh the app
def refresh_app():
    st.experimental_rerun()

# Refresh button
if st.button("Refresh", key="refresh_button"):
    refresh_app()

current_time = datetime.now(pytz.timezone('Europe/London')).strftime("%d-%m-%Y %H:%M")
st.title(f"Last Updated: {current_time}")

# Display birdies or better
st.subheader(f"Scottie Scheffler Birdies or Better: {scottie_birdies_or_better}")
st.subheader(f"Rory McIlroy Birdies or Better: {rory_birdies_or_better}")

display_tables(sorted_tables)

# Auto-refresh the app every 1 minute
while True:
    time.sleep(60)
    refresh_app()
