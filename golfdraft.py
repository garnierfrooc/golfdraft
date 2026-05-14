import pandas as pd
import json
import streamlit as st
import time
from datetime import datetime, timedelta
import pytz
import math

A1 = "Cameron Young"
A2 = "Jon Rahm"
A3 = "Rory McIlroy"
A4 = "Scottie Scheffler"
A5 = "Xander Schauffele"
B1 = "Brooks Koepka"
B2 = "Bryson DeChambeau"
B3 = "Collin Morikawa"
B4 = "Justin Thomas"
B5 = "Ludvig Åberg"
B6 = "Matt Fitzpatrick"
B7 = "Nicolai Højgaard"
B8 = "Patrick Cantlay"
B9 = "Russell Henley"
B10 = "Tommy Fleetwood"
C1 = "Adam Scott"
C2 = "Chris Gotterup"
C3 = "J.J. Spaun"
C4 = "Justin Rose"
C5 = "Kurt Kitayama"
C6 = "Maverick McNealy"
C7 = "Min Woo Lee"
C8 = "Patrick Reed"
C9 = "Rickie Fowler"
C10 = "Robert MacIntyre"
C11 = "Sam Burns"
C12 = "Shane Lowry"
C13 = "Si Woo Kim"
C14 = "Tyrrell Hatton"
C15 = "Viktor Hovland"
D1 = "Akshay Bhatia"
D2 = "Alex Fitzpatrick"
D3 = "Alex Noren"
D4 = "Alex Smalley"
D5 = "Ben Griffin"
D6 = "Brian Harman"
D7 = "Corey Conners"
D8 = "David Puig"
D9 = "Gary Woodland"
D10 = "Harris English"
D11 = "Harry Hall"
D12 = "Hideki Matsuyama"
D13 = "Jacob Bridgeman"
D14 = "Jason Day"
D15 = "Joaquin Niemann"
D16 = "Jordan Spieth"
D17 = "Keegan Bradley"
D18 = "Kristoffer Reitan"
D19 = "Matt McCarty"
D20 = "Michael Thorbjornsen"
D21 = "Pierceson Coody"
D22 = "Sepp Straka"
D23 = "Sungjae Im"
D24 = "Thomas Detry"
D25 = "Wyndham Clark"
E1 = "Aaron Rai"
E2 = "Aldrich Potgieter"
E3 = "Andrew Novak"
E4 = "Andrew Putnam"
E5 = "Angel Ayora"
E6 = "Austin Smotherman"
E7 = "Bernd Wiesberger"
E8 = "Billy Horschel"
E9 = "Bud Cauley"
E10 = "Cameron Smith"
E11 = "Christiaan Bezuidenhout"
E12 = "Daniel Berger"
E13 = "Daniel Hillier"
E14 = "Denny McCarthy"
E15 = "Dustin Johnson"
E16 = "Haotong Li"
E17 = "Ian Holt"
E18 = "J.T. Poston"
E19 = "Jayden Schaper"
E20 = "John Parry"
E21 = "Johnny Keefer"
E22 = "Jordan Smith"
E23 = "Keith Mitchell"
E24 = "Lucas Glover"
E25 = "Marco Penge"
E26 = "Matt Wallace"
E27 = "Max Greyserman"
E28 = "Max Homa"
E29 = "Max McGreevy"
E30 = "Michael Brennan"
E31 = "Michael Kim"
E32 = "Mikael Lindberg"
E33 = "Nick Taylor"
E34 = "Nico Echavarria"
E35 = "Patrick Rodgers"
E36 = "Rasmus Højgaard"
E37 = "Rasmus Neergaard-Petersen"
E38 = "Richard Hoey"
E39 = "Ricky Castillo"
E40 = "Ryan Fox"
E41 = "Ryan Gerard"
E42 = "Ryo Hisatsune"
E43 = "Sahith Theegala"
E44 = "Samuel Stevens"
E45 = "Stephan Jaeger"
E46 = "Steven Fisk"
E47 = "Stewart Cink"
E48 = "Sudarshan Yellamaraju"
E49 = "Taylor Pendrith"
E50 = "Tom McKibbin"
F1 = "Adam Schenk"
F2 = "Adrien Saddier"
F3 = "Andy Sullivan"
F4 = "Austin Hurt"
F5 = "Ben Kern"
F6 = "Ben Polland"
F7 = "Braden Shattuck"
F8 = "Brandt Snedeker"
F9 = "Brian Campbell"
F10 = "Bryce Fisher"
F11 = "Casey Jarvis"
F12 = "Chandler Blanchet"
F13 = "Chris Gabriele"
F14 = "Chris Kirk"
F15 = "Dan Brown"
F16 = "David Lipsky"
F17 = "Davis Riley"
F18 = "Derek Berg"
F19 = "Elvis Smylie"
F20 = "Emiliano Grillo"
F21 = "Francisco Bidé"
F22 = "Garrett Sapp"
F23 = "Garrick Higgo"
F24 = "Jared Jones"
F25 = "Jason Dufner"
F26 = "Jesse Droemer"
F27 = "Jhonattan Vegas"
F28 = "Jimmy Walker"
F29 = "Joe Highsmith"
F30 = "Jordan Gumberg"
F31 = "Kazuki Higa"
F32 = "Kota Kaneko"
F33 = "Luke Donald"
F34 = "Mark Geddes"
F35 = "Martin Kaymer"
F36 = "Matti Schmid"
F37 = "Michael Block"
F38 = "Michael Kartrude"
F39 = "Padraig Harrington"
F40 = "Paul McClure"
F41 = "Ryan Lenahan"
F42 = "Ryan Vermeer"
F43 = "Sami Valimaki"
F44 = "Shaun Micheel"
F45 = "Timothy Wiseman"
F46 = "Tom Hoge"
F47 = "Travis Smyth"
F48 = "Tyler Collet"
F49 = "William Mouw"
F50 = "Y.E. Yang"
F51 = "Zach Haynes"

# Assuming the JSON data is stored in a variable called 'data'
with open('ukopen2024.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Mark - 17/18": [
        A3, B6, C4, D6, E10, F33
    ],
    "Nick - 16/18": [
        A3, B10, C4, D15, E15, F15
    ],
    "Stu - 16/16": [
        A4, B10, C4, D25, E1, F16
    ],
    "Marc - 20/22": [
        A3, B6, C8, D5, E1, F20
    ],
    "Jonty - 22/23": [
        A3, B4, C4, D25, E8, F46
    ],
    "Jonathon - 17/17": [
        A3, B10, C7, D22, E36, F8
    ],
    "Jamie - 18/15": [
        A4, B5, C11, D10, E11, F8
    ],
    "Graeme - 22/14": [
        A4, B2, C9, D14, E1, F3
    ],
    "Beeton - 21/17": [
        A4, B5, C10, D12, E11, F14
    ],
    "Stef - 19/17": [
        A4, B10, C3, D23, E33, F8
    ],
    "Gary - 17/18": [
        A3, B6, C4, D12, E31, F15
    ],
    "Chris - 21/16": [
        A4, B6, C9, D16, E28, F37
    ],
    "Andy - 20/17": [
        A3, B10, C14, D12, E15, F10
    ],
    "Bean - 17/17": [
        A1, B5, C14, D22, E28, F17
    ],
    "Barry - 15/16": [
        A1, B2, C14, D16, E28, F37
    ],
    "Lewis P - 19/17": [
        A1, B6, C9, D2, E25, F15
    ],
    "Phil - 13/15": [
        A3, B10, C12, D12, E40, F20
    ],
    "Lewis G - 19/21": [
        A3, B10, C4, D14, E1, F1
    ],
    "Ian - 17/19": [
        A1, B6, C9, D16, E50, F17
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
