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
B1 = "Collin Morikawa"
B2 = "Corey Conners"
B3 = "Joaquin Niemann"
B4 = "Justin Thomas"
B5 = "Ludvig Aberg"
B6 = "Patrick Cantlay"
B7 = "Sepp Straka"
B8 = "Shane Lowry"
B9 = "Tommy Fleetwood"
B10 = "Tyrrell Hatton"
C1 = "Aaron Rai"
C2 = "Ben Griffin"
C3 = "Brooks Koepka"
C4 = "Cameron Young"
C5 = "Daniel Berger"
C6 = "Harris English"
C7 = "Hideki Matsuyama"
C8 = "Jason Day"
C9 = "Jordan Spieth"
C10 = "Justin Rose"
C11 = "Keegan Bradley"
C12 = "Matt Fitzpatrick"
C13 = "Maverick McNealy"
C14 = "Robert MacIntyre"
C15 = "Russell Henley"
C16 = "Ryan Fox"
C17 = "Sam Burns"
C18 = "Taylor Pendrith"
C19 = "Tony Finau"
C20 = "Viktor Hovland"
D1 = "Adam Scott"
D2 = "Akshay Bhatia"
D3 = "Andrew Novak"
D4 = "Brian Harman"
D5 = "Bud Cauley"
D6 = "Byeong Hun An"
D7 = "Cameron Smith"
D8 = "Carlos Ortiz"
D9 = "Davis Thompson"
D10 = "Denny McCarthy"
D11 = "Dustin Johnson"
D12 = "Gary Woodland"
D13 = "J.J. Spaun"
D14 = "J.T. Poston"
D15 = "Lucas Glover"
D16 = "Mackenzie Hughes"
D17 = "Marc Leishman"
D18 = "Matt McCarty"
D19 = "Matt Wallace"
D20 = "Max Greyserman"
D21 = "Minwoo Lee"
D22 = "Nick Taylor"
D23 = "Patrick Reed"
D24 = "Rasmus Hojgaard"
D25 = "Ryan Gerard"
D26 = "Si Woo Kim"
D27 = "Sungjae Im"
D28 = "Thomas Detry"
D29 = "Thorbjorn Olesen"
D30 = "Wyndham Clark"
E1 = "Benjamin James"
E2 = "Cam Davis"
E3 = "Chris Gotterup"
E4 = "Chris Kirk"
E5 = "Christiaan Bezuidenhout"
E6 = "Davis Riley"
E7 = "Doug Ghim"
E8 = "Emiliano Grillo"
E9 = "Eric Cole"
E10 = "Erik Van Rooyen"
E11 = "Jackson Koivun"
E12 = "Jacob Bridgeman"
E13 = "Jhonattan Vegas"
E14 = "Joe Highsmith"
E15 = "Johnny Keefer"
E16 = "Jordan Smith"
E17 = "Laurie Canter"
E18 = "Mark Hubbard"
E19 = "Matthew Jordan"
E20 = "Matthieu Pavon"
E21 = "Michael Kim"
E22 = "Nico Echavarria"
E23 = "Niklas Norgaard"
E24 = "Phil Mickelson"
E25 = "Rasmus Neergaard-Petersen"
E26 = "Sam Stevens"
E27 = "Stephan Jaeger"
E28 = "Tom Hoge"
E29 = "Tom Kim"
E30 = "Victor Perez"
F1 = "Adam Schenk"
F2 = "Alistair Docherty"
F3 = "Alvaro Ortiz"
F4 = "Andrea Pavan"
F5 = "Austen Truslow"
F6 = "Brady Calkins"
F7 = "Brian Campbell"
F8 = "Bryan Lee"
F9 = "Cameron Tankersley"
F10 = "Chandler Blanchet"
F11 = "Chase Johnson"
F12 = "Edoardo Molinari"
F13 = "Emilio Gonzalez"
F14 = "Evan Beck"
F15 = "Frankie Harris"
F16 = "Frederic Lacroix"
F17 = "George Duangmanee"
F18 = "George Kneiser"
F19 = "Grant Haefner"
F20 = "Guido Migliozzi"
F21 = "Harrison Ott"
F22 = "Jackson Buchanan"
F23 = "Jacques Kruyswijk"
F24 = "James Hahn"
F25 = "James Nicholas"
F26 = "Jinichiro Kozuma"
F27 = "Joakim Lagergren"
F28 = "Joey Herrera"
F29 = "Jose Luis Ballester"
F30 = "Justin Hastings"
F31 = "Justin Hicks"
F32 = "Justin Lower"
F33 = "Kevin Velo"
F34 = "Lance Simpson"
F35 = "Lanto Griffin"
F36 = "Mason Howell"
F37 = "Matt Vogt"
F38 = "Maxwell Moldovan"
F39 = "Michael La Sasso"
F40 = "Nick Dunlap"
F41 = "Noah Kent"
F42 = "Philip Barbaree"
F43 = "Preston Summerhays"
F44 = "Richard Bland"
F45 = "Riki Kawamoto"
F46 = "Riley Lewis"
F47 = "Roberto Diaz"
F48 = "Ryan McCormick"
F49 = "Sam Bairstow"
F50 = "Scott Vincent"
F51 = "Takumi Kanaya"
F52 = "Thriston Lawrence"
F53 = "Trent Phillips"
F54 = "Trevor Cone"
F55 = "Trevor Gutschewski"
F56 = "Tyler Weaver"
F57 = "Will Chandler"
F58 = "Yuta Sugiura"
F59 = "Zac Blair"
F60 = "Zach Bauchou"
F61 = "Zachery Pollo"

# Assuming the JSON data is stored in a variable called 'data'
with open('ukopen2024.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Nick - 15/12": [
        A3, B8, C12, D2, E13, F3
    ],
    "Marc - 20/18": [
        A4, B3, C16, D2, E2, F32
    ],
    "Phil - 18/16": [
        A4, B9, C12, D14, E24, F39
    ],
    "Jonty - 21/17": [
        A4, B8, C10, D4, E6, F50
    ],
    "Gary - 21/23": [
        A3, B1, C10, D21, E29, F1
    ],
    "Stu - 16/16": [
        A3, B9, C16, D22, E8, F39
    ],
    "Graeme - 17/14": [
        A1, B1, C4, D4, E13, F4
    ],
    "Barry - 18/14": [
        A1, B5, C20, D27, E29, F40
    ],
    "Beaton - 17/14": [
        A4, B1, C17, D2, E14, F40
    ],
    "Jamie - 15/13": [
        A4, B5, C2, D26, E28, F50
    ],
    "Ian - 20/17": [
        A1, B4, C2, D19, E6, F6
    ], 
    "Bean - 22/17": [
        A4, B3, C20, D26, E6, F44
    ],
    "Lewis - 16/13": [
        A4, B1, C6, D22, E8, F32
    ],
    "Pye - 17/18": [
        A3, B4, C10, D11, E30, F32
    ], 
    "Ant - 17/21": [
        A3, B9, C11, D21, E15, F3
    ],
    "Joe - 20/16": [
        A5, B1, C10, D19, E24, F11
    ],
    "Chaz - 14/16": [
        A1, B7, C1, D26, E12, F39
    ],
    "Stef - 16/19": [
        A4, B3, C16, D18, E30, F4
    ],
    "Tom Hambly - 14/14": [
        A4, B9, C6, D12, E29, F37
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
