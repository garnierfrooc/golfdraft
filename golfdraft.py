import pandas as pd
import json
import streamlit as st
import time
from datetime import datetime, timedelta
import pytz

A1 = "Collin Morikawa"
A2 = "Jon Rahm"
A3 = "Ludvig Aberg"
A4 = "Rory McIlroy"
A5 = "Scottie Scheffler"
B1 = "Brooks Koepka"
B2 = "Bryson Dechambeau"
B3 = "Hideki Matsuyama"
B4 = "Joaquin Niemann"
B5 = "Jordan Spieth"
B6 = "Justin Thomas"
B7 = "Patrick Cantlay"
B8 = "Tommy Fleetwood"
B9 = "Viktor Hovland"
B10 = "Xander Schauffele"
C1 = "Akshay Bhatia"
C2 = "Cameron Smith"
C3 = "Corey Conners"
C4 = "Dustin Johnson"
C5 = "Jason Day"
C6 = "Justin Rose"
C7 = "Matt Fitzpatrick"
C8 = "Minwoo Lee"
C9 = "Patrick Reed"
C10 = "Robert MacIntyre"
C11 = "Russell Henley"
C12 = "Sahith Theegala"
C13 = "Sepp Straka"
C14 = "Sergio Garcia"
C15 = "Shane Lowry"
C16 = "Tom Kim"
C17 = "Tony Finau"
C18 = "Tyrrell Hatton"
C19 = "Will Zalatoris"
C20 = "Wyndham Clark"
D1 = "Aaron Rai"
D2 = "Adam Scott"
D3 = "Billy Horschel"
D4 = "Brian Harman"
D5 = "Byeong Hun An"
D6 = "Cam Davis"
D7 = "Cameron Young"
D8 = "Christiaan Bezuidenhout"
D9 = "Daniel Berger"
D10 = "Davis Thompson"
D11 = "Denny McCarthy"
D12 = "Harris English"
D13 = "J.J. Spaun"
D14 = "Keegan Bradley"
D15 = "Lucas Glover"
D16 = "Maverick McNealy"
D17 = "Max Homa"
D18 = "Michael Kim"
D19 = "Nicolai Hojgaard"
D20 = "Phil Mickelson"
D21 = "Rasmus Hojgaard"
D22 = "Sam Burns"
D23 = "Sungjae Im"
D24 = "Taylor Pendrith"
D25 = "Thomas Detry"
E1 = "Adam Schenk"
E2 = "Angel Cabrera"
E3 = "Austin Eckroat"
E4 = "Bernhard Langer"
E5 = "Brian Campbell"
E6 = "Bubba Watson"
E7 = "Charl Schwartzel"
E8 = "Chris Kirk"
E9 = "Danny Willett"
E10 = "Davis Riley"
E11 = "Evan Beck"
E12 = "Fred Couples"
E13 = "Hiroshi Tai"
E14 = "J.T. Poston"
E15 = "Jhonattan Vegas"
E16 = "Joe Highsmith"
E17 = "Jose Luis Ballester"
E18 = "Jose Maria Olazabal"
E19 = "Justin Hastings"
E20 = "Kevin Yu"
E21 = "Laurie Canter"
E22 = "Matt McCarty"
E23 = "Matthieu Pavon"
E24 = "Max Greyserman"
E25 = "Mike Weir"
E26 = "Nick Dunlap"
E27 = "Nick Taylor"
E28 = "Nico Echavarria"
E29 = "Noah Kent"
E30 = "Patton Kizzire"
E31 = "Rafael Campos"
E32 = "Stephan Jaeger"
E33 = "Thriston Lawrence"
E34 = "Tom Hoge"
E35 = "Vijay Singh"
E36 = "Zach Johnson"

# Assuming the JSON data is stored in a variable called 'data'
with open('ukopen2024.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Ian - 14/16": [
        A3, B3, C16, D20, E15, F37
    ],
    "Marc - 10/10": [
        A3, B6, C11, D20, E14, F25
    ],
    "Gary - 17/18": [
        A3, B8, C11, D10, E17, F9
    ],
    "Barry - 14/10": [
        A4, B9, C11, D8, E27, F9
    ],
    "Bean - 15/15": [
        A2, B3, C16, D5, E30, F19
    ],
    "Nick - 12/15": [
        A3, B1, C14, D10, E1, F48
    ],
    "Mark - 23/22": [
        A3, B4, C9, D10, E22, F25
    ],
    "Stu - 14/18": [
        A3, B6, C1, D19, E23, F12
    ],
    "Ciaran - 16/19": [
        A1, B3, C4, D15, E27, F62
    ],
    "Beeton - 14/17": [
        A2, B3, C16, D14, E24, F8
    ],
    "Jamie - 20/18": [
        A4, B3, C14, D2, E28, F63
    ],
    "Lewis - 15/11": [
        A5, B8, C17, D3, E26, F49
    ],
    "Graeme - 19/17": [
        A5, B7, C1, D18, E12, F52
    ],
    "Robert - 21/23": [
        A2, B8, C16, D18, E12, F8
    ],
    "Nicholas - 17/15": [
        A2, B8, C5, D19, E2, F64
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
#rory_birdies_or_better = calculate_birdies_or_better("Rory McIlroy")

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
st.subheader(f"Rory McIlroy Birdies or Better: 3")

display_tables(sorted_tables)

# Auto-refresh the app every 1 minute
while True:
    time.sleep(60)
    refresh_app()
