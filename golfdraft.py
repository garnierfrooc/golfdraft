import pandas as pd
import json
import streamlit as st
import time
from datetime import datetime, timedelta
import pytz
import math

A1 = "Bryson Dechambeau"
A2 = "Jon Rahm"
A3 = "Justin Thomas"
A4 = "Rory McIlroy"
A5 = "Scottie Scheffler"
B1 = "Collin Morikawa"
B2 = "Hideki Matsuyama"
B3 = "Joaquin Niemann"
B4 = "Ludvig Aberg"
B5 = "Patrick Cantlay"
B6 = "Shane Lowry"
B7 = "Tommy Fleetwood"
B8 = "Tyrrell Hatton"
B9 = "Viktor Hovland"
B10 = "Xander Schauffele"
C1 = "Aaron Rai"
C2 = "Akshay Bhatia"
C3 = "Brooks Koepka"
C4 = "Cameron Smith"
C5 = "Corey Conners"
C6 = "Daniel Berger"
C7 = "Jason Day"
C8 = "Jordan Spieth"
C9 = "Justin Rose"
C10 = "Keith Mitchell"
C11 = "Maverick McNealy"
C12 = "Max Homa"
C13 = "Minwoo Lee"
C14 = "Patrick Reed"
C15 = "Russell Henley"
C16 = "Sam Burns"
C17 = "Sepp Straka"
C18 = "Sungjae Im"
C19 = "Tony Finau"
C20 = "Wyndham Clark"
D1 = "Adam Scott"
D2 = "Andrew Novak"
D3 = "Brian Harman"
D4 = "Byeong Hun An"
D5 = "Cameron Young"
D6 = "David Puig"
D7 = "Davis Thompson"
D8 = "Dean Burmester"
D9 = "Denny McCarthy"
D10 = "Dustin Johnson"
D11 = "Gary Woodland"
D12 = "Harris English"
D13 = "J.J. Spaun"
D14 = "Jacob Bridgeman"
D15 = "Keegan Bradley"
D16 = "Kurt Kitayama"
D17 = "Mackenzie Hughes"
D18 = "Matt Fitzpatrick"
D19 = "Rasmus Hojgaard"
D20 = "Rasmus Neergaard-Petersen"
D21 = "Rickie Fowler"
D22 = "Robert MacIntyre"
D23 = "Ryan Fox"
D24 = "Sahith Theegala"
D25 = "Sergio Garcia"
D26 = "Si Woo Kim"
D27 = "Stephan Jaeger"
D28 = "Taylor Pendrith"
D29 = "Thomas Detry"
D30 = "Will Zalatoris"
E1 = "Alex Noren"
E2 = "Austin Eckroat"
E3 = "Ben Griffin"
E4 = "Bud Cauley"
E5 = "Cam Davis"
E6 = "Chris Kirk"
E7 = "Erik Van Rooyen"
E8 = "Eugenio Chacarra"
E9 = "J.T. Poston"
E10 = "Jake Knapp"
E11 = "Kevin Yu"
E12 = "Lucas Glover"
E13 = "Max Greyserman"
E14 = "Michael Kim"
E15 = "Michael Thorbjornsen"
E16 = "Nick Taylor"
E17 = "Nico Echavarria"
E18 = "Nicolai Hojgaard"
E19 = "Niklas Norgaard"
E20 = "Patrick Rodgers"
E21 = "Phil Mickelson"
E22 = "Rico Hoey"
E23 = "Sam Stevens"
E24 = "Sami Valimaki"
E25 = "Seamus Power"
E26 = "Taylor Moore"
E27 = "Thorbjorn Olesen"
E28 = "Tom Hoge"
E29 = "Tom Kim"
E30 = "Tom McKibbin"
F1 = "Adam Hadwin"
F2 = "Andre Chi"
F3 = "Beau Hossler"
F4 = "Bob Sowards"
F5 = "Bobby Gates"
F6 = "Brandon Bingaman"
F7 = "Brian Bergstol"
F8 = "Brian Campbell"
F9 = "Christiaan Bezuidenhout"
F10 = "Daniel Van Tonder"
F11 = "Davis Riley"
F12 = "Dylan Newman"
F13 = "Elvis Smylie"
F14 = "Eric Cole"
F15 = "Eric Steger"
F16 = "Garrick Higgo"
F17 = "Greg Koch"
F18 = "Harry Hall"
F19 = "Jason Dufner"
F20 = "Jesse Droemer"
F21 = "Jhonattan Vegas"
F22 = "Jimmy Walker"
F23 = "Joe Highsmith"
F24 = "John Catlin"
F25 = "John Parry"
F26 = "John Somers"
F27 = "Johnny Keefer"
F28 = "Justin Hicks"
F29 = "Justin Lower"
F30 = "Karl Vilips"
F31 = "Keita Nakajima"
F32 = "Larkin Gross"
F33 = "Laurie Canter"
F34 = "Lee Hodges"
F35 = "Luke Donald"
F36 = "Marco Penge"
F37 = "Martin Kaymer"
F38 = "Matt McCarty"
F39 = "Matt Wallace"
F40 = "Matthieu Pavon"
F41 = "Max McGreevy"
F42 = "Michael Block"
F43 = "Michael Kartrude"
F44 = "Nic Ishee"
F45 = "Nick Dunlap"
F46 = "Padraig Harrington"
F47 = "Patrick Fishburn"
F48 = "Patton Kizzire"
F49 = "Rafael Campos"
F50 = "Richard Bland"
F51 = "Rupe Taylor"
F52 = "Ryan Gerard"
F53 = "Ryan Lenahan"
F54 = "Ryo Hisatsune"
F55 = "Shaun Micheel"
F56 = "Takumi Kanaya"
F57 = "Thriston Lawrence"
F58 = "Timothy Wiseman"
F59 = "Tom Johnson"
F60 = "Tyler Collet"
F61 = "Victor Perez"

# Assuming the JSON data is stored in a variable called 'data'
with open('ukopen2024.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Nick - ?/?": [
        A4, B10, C9, D5, E12, F9
    ],
    "Marc - ?/?": [
        A4, B6, C3, D19, E10, F9
    ],
    "Phil - ?/?": [
        A4, B6, C9, D24, E1, F13
    ],
    "Jonty - ?/?": [
        A4, B1, C8, D10, E21, F14
    ],
    "Gary - ?/?": [
        A4, B6, C9, D18, E29, F3
    ],
    "Stu - 17/17": [
        A4, B7, C17, D3, E16, F35
    ],
    "Graeme - 18/21": [
        A1, B6, C9, D2, E18, F1
    ],
    "Rob - 22/22": [
        A5, B6, C17, D2, E9, F1
    ],
    "Barry - 17/17": [
        A4, B8, C8, D19, E14, F35
    ],
    "Beaton - 18/19": [
        A5, B4, C17, D23, E10, F9
    ],
    "Jamie - 20/20": [
        A5, B4, C6, D2, E8, F38
    ],
    "Ian - 17/20": [
        A5, B4, C20, D23, E1, F39
    ], 
    "Darrin - 17/18": [
        A2, B1, C5, D2, E8, F61
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
