import pandas as pd
import json
import streamlit as st
import time
from datetime import datetime, timedelta
import pytz

B1 = "Brooks Koepka"
A22 = "Jon Rahm"
B5 = "Ludvig Aberg"
A3 = "Rory McIlroy"
A5 = "Xander Schauffele"
A1 = "Bryson DeChambeau"
B2 = "Cameron Smith"
B3 = "Cameron Young"
A2 = "Collin Morikawa"
B55 = "Joaquin Niemann"
B7 = "Max Homa"
B8 = "Patrick Cantlay"
B10 = "Tommy Fleetwood"
A4 = "Viktor Hovland"
B100 = "Wyndham Clark"
C1 = "Adam Scott"
C2 = "Byeong Hun An"
C4 = "Corey Conners"
C3 = "Cameron Young"
C5 = "Hideki Matsuyama"
C6 = "Jason Day"
C7 = "Jordan Spieth"
C8 = "Justin Thomas"
B6 = "Matt Fitzpatrick"
C9 = "Min Woo Lee"
C11 = "Russell Henley"
B9 = "Sahith Theegala"
C13 = "Sam Burns"
C144 = "Sepp Straka"
C14 = "Shane Lowry"
C166 = "Si Woo Kim"
C177 = "Sungjae Im"
C17 = "Tony Finau"
C19 = "Tyrrell Hatton"
C20 = "Will Zalatoris"
D1 = "Aaron Rai"
D2 = "Adam Hadwin"
E2 = "Adam Schenk"
D44 = "Adrian Meronk"
D55 = "Akshay Bhatia"
D4 = "Alex Noren"
D10 = "Brian Harman"
E7 = "Cameron Davis"
E8 = "Chris Kirk"
D7 = "Christiaan Bezuidenhout"
D111 = "Dean Burmester"
D12 = "Denny McCarthy"
D13 = "Erik Van Rooyen"
D14 = "Harris English"
D155 = "J.T. Poston"
D166 = "Keegan Bradley"
D17 = "Keith Mitchell"
D18 = "Kurt Kitayama"
D19 = "Mackenzie Hughes"
E21 = "Nicolai Hojgaard"
D21 = "Patrick Reed"
D15 = "Rickie Fowler"
D16 = "Ryan Fox"
D24 = "Stephan Jaeger"
D25 = "Talor Gooch"
D26 = "Taylor Moore"
D27 = "Taylor Pendrith"
D28 = "Thomas Detry"
D29 = "Tom Hoge"
C16 = "Tom Kim"
E1 = "Aaron Rai"
E22 = "Adrian Otaegui"
E3 = "Alejandro Tosti"
E4 = "Alex Smalley"
E5 = "Alexander Bjork"
E6 = "Andrew Putnam"
E77 = "Andrew Svoboda"
E88 = "Andy Ogletree"
E9 = "Austin Eckroat"
E10 = "Beau Hossler"
E11 = "Davis Thompson"
E122 = "Ben Kohles"
E13 = "Ben Polland"
D5 = "Billy Horschel"
E15 = "Brad Marek"
E16 = "Braden Shattuck"
E17 = "Brendon Todd"
E18 = "Brice Garnett"
E19 = "C.T. Pan"
E20 = "Camilo Villegas"
E211 = "Charley Hoffman"
E22 = "Chris Gotterup"
E233 = "David Puig"
E24 = "Doug Ghim"
F19 = "Emiliano Grillo"
E12 = "Eric Cole"
E27 = "Evan Bowser"
E28 = "Francesco Molinari"
E29 = "Gary Woodland"
E30 = "Grayson Murray"
F31 = "Jake Knapp"
E32 = "Jared Jones"
E33 = "Jason Dufner"
E34 = "Jeff Kellen"
E35 = "Jeremy Wells"
E366 = "Jesper Svensson"
E37 = "Jesse Mueller"
E38 = "Jimmy Walker"
E39 = "John Daly"
E40 = "John Somers"
E41 = "Jordan Smith"
E42 = "Josh Bevell"
F36 = "Justin Lower"
D11 = "Justin Rose"
E45 = "K.H. Lee"
E46 = "Kazuma Kobori"
E47 = "Keita Nakajima"
E48 = "Kyle Mendoza"
E49 = "Larkin Gross"
E50 = "Lee Hodges"
E51 = "Lucas Glover"
E52 = "Lucas Herbert"
E53 = "Luke Donald"
E54 = "Luke List"
F40 = "Mark Hubbard"
E56 = "Martin Kaymer"
F41 = "Matt Kuchar"
E58 = "Matt Wallace"
E59 = "Matthieu Pavon"
E60 = "Maverick McNealy"
E61 = "Michael Block"
E62 = "Nick Dunlap"
E63 = "Nick Taylor"
E64 = "Padraig Harrington"
E65 = "Patrick Rodgers"
E66 = "Peter Malnati"
E67 = "Phil Mickelson"
E68 = "Preston Cole"
E69 = "Rasmus Hojgaard"
E70 = "Rich Beem"
C10 = "Robert Macintyre"
E72 = "Ryan Van Velzen"
E73 = "Ryo Hisatsune"
E74 = "S.H. Kim"
E23 = "Seamus Power"
E76 = "Sebastian Soderberg"
E77 = "Shaun Micheel"
E78 = "Takumi Kanaya"
E79 = "Taylor Montgomery"
E80 = "Thorbjorn Olesen"
E81 = "Thriston Lawrence"
E82 = "Tiger Woods"
E83 = "Tim Widing"
E84 = "Tracy Phillips"
E85 = "Tyler Collet"
E86 = "Victor Perez"
E87 = "Vincent Norrman"
E88 = "Wyatt Worthington"
E89 = "Y.E. Yang"
E90 = "Zac Blair"
E91 = "Zac Oakley"
F35 = "John Chin"
F23 = "Frederik Kjettrup"
F9 = "Bryan Kim"
F24 = "Gordon Sargent"

# Assuming the JSON data is stored in a variable called 'data'
with open('pga2024.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Nick - 24/21": [
        A5, B6, C10, D15, E2, F41
    ],
    "Marc - 24/25": [
        A5, B5, C9, D15, E21, F19
    ],
    "Lewis - 22/20": [
        A1, B7, C14, D4, E21, F31
    ],
    "Bean - 17/13": [
        A1, B5, C17, D5, E1, F40
    ],
    "Phil - 21/18": [
        A4, B9, C14, D15, E8, F35
    ],
    "Ciaran - 21/18": [
        A1, B5, C16, D15, E11, F9
    ],
    "Brocky - 23/23": [
        A3, B10, C17, D11, E1, F19
    ],
    "Jamie - 13/10": [
        A2, B5, C4, D7, E1, F19
    ],
    "Pye - 23/22": [
        A3, B1, C7, D11, E23, F36
    ],
    "Ian - 23/20": [
        A1, B8, C9, D16, E12, F23
    ],
    "Jonty - 23/22": [
        A2, B1, C3, D16, E12, F19
    ],
    "Gary - 17/18": [
        A2, B9, C3, D11, E7, F24
    ]
}

# Function to load and process the data
def load_data():
    player_tables = {}
    
    for player, selections in players.items():
        player_data = {"Name": [], "Score": []}
        filtered_data = [player_info for player_info in leaderboard if
                         player_info["first_name"] + " " + player_info["last_name"] in selections]
        sorted_data = sorted(filtered_data, key=lambda x: x["score"])
        
        num_rounds = 0
        for player_info in sorted_data:
            player_data["Name"].append(player_info["first_name"] + " " + player_info["last_name"])
            player_data["Score"].append(player_info["score"])

            rounds = player_info["rounds"]
            num_rounds = max(num_rounds, len(rounds))
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

# Load and display the initial data
sorted_tables = load_data()
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
