import pandas as pd
import json
import streamlit as st
import time
from datetime import datetime, timedelta
import pytz
import math

A1 = "Scottie Scheffler"
A2 = "Rory McIlroy"
A3 = "Jon Rahm"
A4 = "Bryson DeChambeau"
A5 = "Ludvig Åberg"
B1 = "Xander Schauffele"
B2 = "Tommy Fleetwood"
B3 = "Tyrrell Hatton"
B4 = "Viktor Hovland"
B5 = "Shane Lowry"
B6 = "Matt Fitzpatrick"
B7 = "Robert MacIntyre"
B8 = "Collin Morikawa"
B9 = "Sepp Straka"
B10 = "Justin Thomas"
C1 = "Joaquin Niemann"
C2 = "Sam Burns"
C3 = "Justin Rose"
C4 = "Ryan Fox"
C5 = "Jordan Spieth"
C6 = "Corey Conners"
C7 = "Russell Henley"
C8 = "Patrick Cantlay"
C9 = "Marco Penge"
C10 = "Adam Scott"
C11 = "Maverick McNealy"
C12 = "Aaron Rai"
C13 = "Keegan Bradley"
C14 = "Brooks Koepka"
C15 = "Patrick Reed"
D1 = "Harry Hall"
D2 = "Chris Gotterup"
D3 = "Ben Griffin"
D4 = "Jason Day"
D5 = "Hideki Matsuyama"
D6 = "J.J. Spaun"
D7 = "Cameron Young"
D8 = "Harris English"
D9 = "Tom McKibbin"
D10 = "Taylor Pendrith"
D11 = "Nick Taylor"
D12 = "Cam Smith"
D13 = "Si Woo Kim"
D14 = "Max Greyserman"
D15 = "Andrew Novak"
D16 = "Rickie Fowler"
D17 = "Min Woo Lee"
D18 = "Bud Cauley"
D19 = "Wyndham Clark"
D20 = "Brian Harman"
E1 = "Daniel Berger"
E2 = "Tom Kim"
E3 = "Nicolai Højgaard"
E4 = "Matt Wallace"
E5 = "Kevin Yu"
E6 = "Davis Thompson"
E7 = "Michael Kim"
E8 = "Thomas Detry"
E9 = "Sungjae Im"
E10 = "Jordan Smith"
E11 = "Akshay Bhatia"
E12 = "Carlos Ortiz"
E13 = "Rasmus Højgaard"
E14 = "Thriston Lawrence"
E15 = "Dustin Johnson"
E16 = "Thorbjørn Olesen"
E17 = "Denny McCarthy"
E18 = "Aldrich Potgieter"
E19 = "J.T. Poston"
E20 = "Christiaan Bezuidenhout"
E21 = "Dean Burmester"
E22 = "Louis Oosthuizen"
E23 = "Tony Finau"
E24 = "Sergio Garcia"
E25 = "Lucas Herbert"
F1 = "Adrien Saddier"
F2 = "Angel Hidalgo"
F3 = "Antoine Rozner"
F4 = "Brian Campbell"
F5 = "Bryan Newman"
F6 = "Byeong Hun An"
F7 = "Cameron Adam"
F8 = "Chris Kirk"
F9 = "Connor Graham"
F10 = "Curtis Knipes"
F11 = "Curtis Luck"
F12 = "Daniel Brown"
F13 = "Daniel Hillier"
F14 = "Daniel van Tonder"
F15 = "Daniel Young"
F16 = "Darren Clarke"
F17 = "Darren Fichardt"
F18 = "Davis Riley"
F19 = "Dylan Naidoo"
F20 = "Elvis Smylie"
F21 = "Ethan Fang"
F22 = "Filip Jakubcik"
F23 = "Francesco Molinari"
F24 = "Frazer Jones"
F25 = "George Bloor"
F26 = "Guido Migliozzi"
F27 = "Haotong Li"
F28 = "Henrik Stenson"
F29 = "Jacob Skov Olesen"
F30 = "Jason Kokrak"
F31 = "Jesper Sandborg"
F32 = "Jesper Svensson"
F33 = "Jhonattan Vegas"
F34 = "John Axelsen"
F35 = "John Catlin"
F36 = "John Parry"
F37 = "Julien Guerrier"
F38 = "Justin Hastings"
F39 = "Justin Leonard"
F40 = "Justin Suh"
F41 = "Justin Walters"
F42 = "K J Choi"
F43 = "Kristoffer Reitan"
F44 = "Laurie Canter"
F45 = "Lee Westwood"
F46 = "Lucas Glover"
F47 = "Mackenzie Hughes"
F48 = "Marc Leishman"
F49 = "Martin Couvra"
F50 = "Matt McCarty"
F51 = "Matteo Manassero"
F52 = "Matthew Jordan"
F53 = "Matthieu Pavon"
F54 = "Matti Schmid"
F55 = "Mikiya Akutsu"
F56 = "Nathan Kimsey"
F57 = "Nico Echavarria"
F58 = "Niklas Norgaard Moller"
F59 = "OJ Farrell"
F60 = "Oliver Lindell"
F61 = "Padraig Harrington"
F62 = "Phil Mickelson"
F63 = "Richard Teder"
F64 = "Riki Kawamoto"
F65 = "Rikuya Hoshino"
F66 = "Romain Langasque"
F67 = "Ryan Peake"
F68 = "Ryggs Johnston"
F69 = "Sadom Kaewkanjana"
F70 = "Sahith Theegala"
F71 = "Sampson Yunhe Zheng"
F72 = "Sebastian Cave"
F73 = "Sebastian Söderberg"
F74 = "Shaun Norris"
F75 = "Shugo Imahira"
F76 = "Stephan Jaeger"
F77 = "Stewart Cink"
F78 = "Takumi Kanaya"
F79 = "Tom Hoge"
F80 = "Younghan Song"
F81 = "Zach Johnson"

# Assuming the JSON data is stored in a variable called 'data'
with open('ukopen2024.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Jonty - 19/19": [
        A1, B5, C3, D19, E23, F28
    ],
    "Nick - 22/21": [
        A2, B3, C5, D6, E25, F58
    ],
    "Stu - 15/15": [
        A2, B9, C3, D11, E3, F44
    ],
    "Stef - 15/16": [
        A2, B6, C3, D19, E3, F43
    ],
    "Phil - 19/18": [
        A4, B1, C15, D17, E4, F61
    ],
    "Marc - 17/17": [
        A1, B3, C1, D4, E4, F28
    ],
    "Dave - 17/18": [
        A2, B7, C11, D9, E17, F47
    ],
    "Gary - 15/16": [
        A2, B6, C3, D3, E9, F54
    ],
    "Graeme - 20/14": [
        A1, B4, C7, D9, E3, F27
    ],
    "Bean - 17/16": [
        A3, B1, C10, D1, E3, F43
    ],
    "Ian - 13/15": [
        A2, B7, C3, D4, E4, F67
    ],
    "Mark - 24/25": [
        A2, B2, C3, D20, E24, F12
    ],
    "Daz - 18/18": [
        A4, B10, C2, D3, E19, F76
    ],
    "Pye - 17/19": [
        A2, B4, C10, D11, E10, F36
    ],
    "Lewis - 17/16": [
        A5, B6, C7, D1, E3, F6
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
                score *= 1.5
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
