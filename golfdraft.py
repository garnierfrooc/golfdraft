import pandas as pd
import json
import streamlit as st
import time
from datetime import datetime, timedelta
import pytz

A1	= "Bryson Dechambeau"
A2	= "Ludvig Aberg"
A3	= "Rory McIlroy"
A4	= "Scottie Scheffler"
A5	= "Xander Schauffele"
B1	= "Brooks Koepka"
B2	= "Cameron Smith"
B3	= "Collin Morikawa"
B4	= "Jon Rahm"
B5	= "Minwoo Lee"
B6	= "Robert Macintyre"
B7	= "Shane Lowry"
B8	= "Tommy Fleetwood"
B9	= "Tyrrell Hatton"
B10	= "Viktor Hovland"
C1	= "Aaron Rai"
C2	= "Adam Scott"
C3	= "Alex Noren"
C4	= "Brian Harman"
C5	= "Cameron Young"
C6	= "Corey Conners"
C7	= "Hideki Matsuyama"
C8	= "Joaquin Niemann"
C9	= "Jordan Spieth"
C10	= "Justin Thomas"
C11	= "Matt Fitzpatrick"
C12	= "Max Homa"
C13	= "Nicolai Hojgaard"
C14	= "Patrick Cantlay"
C15	= "Ryan Fox"
C16	= "Sahith Theegala"
C17	= "Sungjae Im"
C18	= "Tom Kim"
C19	= "Tony Finau"
C20	= "Wyndham Clark"
D1	= "Abraham Ancer"
D2	= "Akshay Bhatia"
D3	= "Byeong Hun An"
D4	= "Christiaan Bezuidenhout"
D5	= "Davis Thompson"
D6	= "Dean Burmester"
D7	= "Dustin Johnson"
D8	= "Ewen Ferguson"
D9	= "Jason Day"
D10	= "Justin Rose"
D11	= "Keegan Bradley"
D12	= "Louis Oosthuizen"
D13	= "Matthieu Pavon"
D14	= "Rasmus Hojgaard"
D15	= "Rickie Fowler"
D16	= "Russell Henley"
D17	= "Sam Burns"
D18	= "Sepp Straka"
D19	= "Si Woo Kim"
D20	= "Will Zalatoris"
E1	= "Adam Hadwin"
E2	= "Adrian Meronk"
E3	= "Austin Eckroat"
E4	= "Ben Griffin"
E5	= "Billy Horschel"
E6	= "Brendon Todd"
E7	= "Chris Kirk"
E8	= "David Puig"
E9	= "Denny McCarthy"
E10	= "Dominic Clemons"
E11	= "Gary Woodland"
E12	= "Harris English"
E13	= "J.T. Poston"
E14	= "Jordan Smith"
E15	= "Kurt Kitayama"
E16	= "Mackenzie Hughes"
E17	= "Matt Wallace"
E18	= "Matteo Manassero"
E19	= "Matthew Jordan"
E20	= "Matthew Southgate"
E21	= "Padraig Harrington"
E22	= "Phil Mickelson"
E23	= "Richard Mansell"
E24	= "Romain Langasque"
E25	= "Sebastian Soderberg"
E26	= "Thorbjorn Olesen"
E27	= "Tiger Woods"
E28	= "Tom Hoge"
E29	= "Tom McKibbin"
E30	= "Victor Perez"
F1	= "Adam Schenk"
F2	= "Aguri Iwasaki"
F3	= "Alex Cejka"
F4	= "Alexander Bjork"
F5	= "Altin van der Merwe"
F6	= "Andy Ogletree"
F7	= "Angel Hidalgo"
F8	= "C.T. Pan"
F9	= "Calum Scott"
F10	= "Charlie Lindh"
F11	= "Dan Bradbury"
F12	= "Daniel Brown"
F13	= "Daniel Hillier"
F14	= "Darren Clarke"
F15	= "Darren Fichardt"
F16	= "Denwit Boriboonsub"
F17	= "Elvis Smylie"
F18	= "Emiliano Grillo"
F19	= "Eric Cole"
F20	= "Ernie Els"
F21	= "Francesco Molinari"
F22	= "Gordon Sargent"
F23	= "Guido Migliozzi"
F24	= "Guntaek Koh"
F25	= "Henrik Stenson"
F26	= "Jack McDonald"
F27	= "Jacob Skov Olesen"
F28	= "Jaime Montojo"
F29	= "Jasper Stubbs"
F30	= "Jesper Svensson"
F31	= "Jeunghun Wang"
F32	= "Joe Dean"
F33	= "John Catlin"
F34	= "John Daly"
F35	= "Joost Luiten"
F36	= "Jorge Campillo"
F37	= "Justin Leonard"
F38	= "Kazuma Kobori"
F39	= "Keita Nakajima"
F40	= "Laurie Canter"
F41	= "Liam Nolan"
F42	= "Lucas Glover"
F43	= "Luis Masaveu"
F44	= "Marcel Siem"
F45	= "Masahiro Kawamura"
F46	= "Mason Andersen"
F47	= "Matthew Dodd-Berry"
F48	= "Maverick McNealy"
F49	= "Michael Hendry"
F50	= "MinKyu Kim"
F51	= "Nacho Elvira"
F52	= "Nick Taylor"
F53	= "Rikuya Hoshino"
F54	= "Ryan Van Velzen"
F55	= "Ryo Hisatsune"
F56	= "Ryosuke Kinoshita"
F57	= "Sam Horsfield"
F58	= "Sam Hutsby"
F59	= "Sami Valimaki"
F60	= "Santiago De la Fuente"
F61	= "Sean Crocker"
F62	= "Shubhankar Sharma"
F63	= "Stephan Jaeger"
F64	= "Stewart Cink"
F65	= "Taylor Moore"
F66	= "Thriston Lawrence"
F67	= "Todd Hamilton"
F68	= "Tommy Morrison"
F69	= "Vincent Norrman"
F70	= "Yannik Paul"
F71	= "Younghan Song"
F72	= "Yuto Katsuragawa"
F73	= "Zach Johnson"

# Assuming the JSON data is stored in a variable called 'data'
with open('pga2024.json') as json_file:
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
    "Barry - 1/1": [
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
        A5, B8, C17, D3, E24, F49
    ],
    "Graeme - 19/17": [
        A5, B7, C1, D18, E12, F52
    ],
    "Robert - 21/23": [
        A2, B8, C16, D18, E12, F8
    ],
    "Nicholas - 1/1": [
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
