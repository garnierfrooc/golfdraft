import pandas as pd
import json
import streamlit as st
import time
from datetime import datetime, timedelta
import pytz
import math

A1 = "Bryson DeChambeau"
A2 = "Jon Rahm"
A3 = "Rory McIlroy"
A4 = "Scottie Scheffler"
A5 = "Xander Schauffele"
B1 = "Cameron Young"
B2 = "Collin Morikawa"
B3 = "Hideki Matsuyama"
B4 = "Justin Rose"
B5 = "Ludvig Åberg"
B6 = "Matt Fitzpatrick"
B7 = "Min Woo Lee"
B8 = "Patrick Reed"
B9 = "Robert MacIntyre"
B10 = "Tommy Fleetwood"
C1 = "Adam Scott"
C2 = "Akshay Bhatia"
C3 = "Brooks Koepka"
C4 = "Chris Gotterup"
C5 = "Jake Knapp"
C6 = "Jason Day"
C7 = "Jordan Spieth"
C8 = "Justin Thomas"
C9 = "Maverick McNealy"
C10 = "Nicolai Højgaard"
C11 = "Patrick Cantlay"
C12 = "Russell Henley"
C13 = "Shane Lowry"
C14 = "Si Woo Kim"
C15 = "Viktor Hovland"
D1 = "Aldrich Potgieter"
D2 = "Alex Noren"
D3 = "Ben Griffin"
D4 = "Cameron Smith"
D5 = "Casey Jarvis"
D6 = "Corey Conners"
D7 = "Daniel Berger"
D8 = "Gary Woodland"
D9 = "Harris English"
D10 = "Harry Hall"
D11 = "J.J. Spaun"
D12 = "Jacob Bridgeman"
D13 = "Keegan Bradley"
D14 = "Kristoffer Reitan"
D15 = "Kurt Kitayama"
D16 = "Marco Penge"
D17 = "Max Homa"
D18 = "Rasmus Højgaard"
D19 = "Ryan Fox"
D20 = "Ryan Gerard"
D21 = "Sam Burns"
D22 = "Sam Stevens"
D23 = "Sepp Straka"
D24 = "Sungjae Im"
D25 = "Tyrrell Hatton"
E1 = "Aaron Rai"
E2 = "Andrew Novak"
E3 = "Angel Cabrera"
E4 = "Brandon Holtz"
E5 = "Brian Campbell"
E6 = "Brian Harman"
E7 = "Bubba Watson"
E8 = "Carlos Ortiz"
E9 = "Charl Schwartzel"
E10 = "Danny Willett"
E11 = "Davis Riley"
E12 = "Dustin Johnson"
E13 = "Ethan Fang"
E14 = "Fifa Laopakdee"
E15 = "Fred Couples"
E16 = "Haotong Li"
E17 = "Jackson Herrington"
E18 = "John Keefer"
E19 = "Jose Maria Olazabal"
E20 = "Mason Howell"
E21 = "Mateo Pulcini"
E22 = "Matt McCarty"
E23 = "Max Greyserman"
E24 = "Michael Brennan"
E25 = "Michael Kim"
E26 = "Mike Weir"
E27 = "Naoyuki Kataoka"
E28 = "Nick Taylor"
E29 = "Nicolas Echavarria"
E30 = "Rasmus Neergaard-Petersen"
E31 = "Sami Valimaki"
E32 = "Sergio Garcia"
E33 = "Tom McKibbin"
E34 = "Vijay Singh"
E35 = "Wyndham Clark"
E36 = "Zach Johnson"

# Assuming the JSON data is stored in a variable called 'data'
with open('ukopen2024.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Jonty - 18/20": [
        A3, B10, C7, D11, E35
    ],
    "Nick - 19/21": [
        A3, B6, C2, D4, E1
    ],
    "Stu - 16/15": [
        A3, B10, C13, D11, E25
    ],
    "Stef - 21/22": [
        A3, B6, C2, D11, E2
    ],
    "Phil - 25/25": [
        A3, B6, C13, D25, E10
    ],
    "Marc - 23/23": [
        A2, B4, C15, D16, E6
    ],
    "Gary - 18/19": [
        A3, B4, C7, D4, E7
    ],
    "Graeme - 22/18": [
        A4, B6, C8, D25, E1
    ],
    "Bean - 19/18": [
        A4, B6, C15, D11, E6
    ],
    "Ian - 13/15": [
        A2, B7, C3, D4, E4
    ],
    "Mark - 21/22": [
        A3, B4, C13, D9, E6
    ],
    "Pye - 17/19": [
        A4, B4, C1, D19, E28
    ],
    "Lewis - 17/16": [
        A5, B6, C7, D1, E3
    ],
    "Jamie - 21/21": [
        A4, B6, C12, D11, E28
    ],
    "Barry - 18/21": [
        A3, B4, C7, D25, E34
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
