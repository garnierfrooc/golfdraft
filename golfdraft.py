import pandas as pd
import json
import streamlit as st
import time
from datetime import datetime, timedelta
import pytz

# Player names
A1 = "Brooks Koepka"
A2 = "Jon Rahm"
A3 = "Ludvig Aberg"
A4 = "Rory McIlroy"
A5 = "Xander Schauffele"
B1 = "Bryson DeChambeau"
B2 = "Cameron Smith"
B3 = "Cameron Young"
B4 = "Collin Morikawa"
B5 = "Joaquin Niemann"
B6 = "Max Homa"
B7 = "Patrick Cantlay"
B8 = "Tommy Fleetwood"
B9 = "Viktor Hovland"
B10 = "Wyndham Clark"
C1 = "Adam Scott"
C2 = "Byeong Hun An"
C3 = "Corey Conners"
C4 = "Dustin Johnson"
C5 = "Hideki Matsuyama"
C6 = "Jason Day"
C7 = "Jordan Spieth"
C8 = "Justin Thomas"
C9 = "Matt Fitzpatrick"
C10 = "Min Woo Lee"
C11 = "Russell Henley"
C12 = "Sahith Theegala"
C13 = "Sam Burns"
C14 = "Sepp Straka"
C15 = "Shane Lowry"
C16 = "Si Woo Kim"
C17 = "Sungjae Im"
C18 = "Tony Finau"
C19 = "Tyrrell Hatton"
C20 = "Will Zalatoris"
D1 = "Aaron Rai"
D2 = "Adam Hadwin"
D3 = "Adam Schenk"
D4 = "Adrian Meronk"
D5 = "Akshay Bhatia"
D6 = "Alex Noren"
D7 = "Brian Harman"
D8 = "Cameron Davis"
D9 = "Chris Kirk"
D10 = "Christiaan Bezuidenhout"
D11 = "Dean Burmester"
D12 = "Denny McCarthy"
D13 = "Erik Van Rooyen"
D14 = "Harris English"
D15 = "J.T. Poston"
D16 = "Keegan Bradley"
D17 = "Keith Mitchell"
D18 = "Kurt Kitayama"
D19 = "Mackenzie Hughes"
D20 = "Nicolai Hojgaard"
D21 = "Patrick Reed"
D22 = "Rickie Fowler"
D23 = "Ryan Fox"
D24 = "Stephan Jaeger"
D25 = "Talor Gooch"
D26 = "Taylor Moore"
D27 = "Taylor Pendrith"
D28 = "Thomas Detry"
D29 = "Tom Hoge"
D30 = "Tom Kim"
E1 = "Adam Svensson"
E2 = "Adrian Otaegui"
E3 = "Alejandro Tosti"
E4 = "Alex Smalley"
E5 = "Alexander Bjork"
E6 = "Andrew Putnam"
E7 = "Andrew Svoboda"
E8 = "Andy Ogletree"
E9 = "Austin Eckroat"
E10 = "Beau Hossler"
E11 = "Ben Griffin"
E12 = "Ben Kohles"
E13 = "Ben Polland"
E14 = "Billy Horschel"
E15 = "Brad Marek"
E16 = "Braden Shattuck"
E17 = "Brendon Todd"
E18 = "Brice Garnett"
E19 = "C.T. Pan"
E20 = "Camilo Villegas"
E21 = "Charley Hoffman"
E22 = "Chris Gotterup"
E23 = "David Puig"
E24 = "Doug Ghim"
E25 = "Emiliano Grillo"
E26 = "Eric Cole"
E27 = "Evan Bowser"
E28 = "Francesco Molinari"
E29 = "Gary Woodland"
E30 = "Grayson Murray"
E31 = "Jake Knapp"
E32 = "Jared Jones"
E33 = "Jason Dufner"
E34 = "Jeff Kellen"
E35 = "Jeremy Wells"
E36 = "Jesper Svensson"
E37 = "Jesse Mueller"
E38 = "Jimmy Walker"
E39 = "John Daly"
E40 = "John Somers"
E41 = "Jordan Smith"
E42 = "Josh Bevell"
E43 = "Josh Speight"
E44 = "Justin Rose"
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
E55 = "Mark Hubbard"
E56 = "Martin Kaymer"
E57 = "Matt Dobyns"
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
E71 = "Robert MacIntyre"
E72 = "Ryan Van Velzen"
E73 = "Ryo Hisatsune"
E74 = "S.H. Kim"
E75 = "Sami Valimaki"
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

# Assuming the JSON data is stored in a variable called 'data'
with open('pga2024.json') as json_file:
    res = json.load(json_file)
    leaderboard = res['leaderboard']

players = {
    "Gary - 17/18": [
        A4, B8, C9, D20, E44
    ],
    "Richard - 18/15": [
        A4, B1, C8, D25, E22
    ],
    "Nick - 16/17": [
        A5, B1, C9, D22, E44
    ],
    "Marc - 14/8": [
        A1, B1, C9, D22, E67
    ],
    "Lewis - 24/23": [
        A3, B4, C14, D6, E26
    ],
    "Jonty - 20/18": [
        A4, B9, C8, D8, E26
    ],
    "Bean - 18/15": [
        A4, B6, C9, D27, E51
    ],
    "Phil - 21/18": [
        A3, B3, C9, D21, E44
    ],
    "Anup - 27/25": [
        A2, B10, C6, D22, E14
    ],
    "Damo - 24/22": [
        A4, B9, C18, D2, E44
    ],
    "Mark - 22/20": [
        A4, B8, C9, D7, E28
    ],
    "Rob - 24/22": [
        A5, B1, C2, D5, E31
    ],
    "Beeton - 15/14": [
        A4, B4, C6, D24, E44
    ],
    "Graeme - 18/11": [
        A5, B4, C20, D12, E44
    ],
    "Brocky - 18/16": [
        A4, B8, C18, D22, E44
    ],
    "Jamie - 18/17": [
        A4, B1, C10, D6, E11
    ],
    "Emma - 16/12": [
        A2, B2, C15, D9, E44
    ],
    "Davlar - 18/16": [
        A1, B1, C2, D25, E10
    ],
    "Pye - 23/19": [
        A4, B9, C7, D25, E44
    ],
    "Ian - 26/23": [
        A4, B8, C9, D6, E69
    ]
}

# Create a dictionary to store the separate tables for each player
player_tables = {}

# Function to load and process the data
def load_data():
    # Initialize counters for Scottie Scheffler and Rory McIlroy
    scheffler_counts = {"eagles": 0, "birdies": 0, "holes_in_one": 0}
    mcilroy_counts = {"eagles": 0, "birdies": 0, "holes_in_one": 0}

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
            player_data["Name"].append(player_info["first_name"] + " " + player_info["last_name"])
            player_data["Score"].append(player_info["score"])

            rounds = player_info["rounds"]
            # Update the maximum number of rounds played
            num_rounds = max(num_rounds, len(rounds))

            # Update counts for Scheffler and McIlroy
            if player_info["first_name"] + " " + player_info["last_name"] == "Scottie Scheffler":
                for round_info in rounds:
                    scheffler_counts["birdies"] = round_info["eagles"] + round_info["birdies"] + round_info["holes_in_one"]
            elif player_info["first_name"] + " " + player_info["last_name"] == "Rory McIlroy":
                for round_info in rounds:
                    mcilroy_counts["birdies"] = round_info["eagles"] + round_info["birdies"] + round_info["holes_in_one"]

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
        df_completed_rounds = df.dropna(subset=[f"{i} Thru" for i in range(1, num_rounds + 1)], how="any")

        # Hide the scores for incomplete rounds
        for i in range(1, num_rounds + 1):
            if not all(df_completed_rounds[f"{i} Thru"] == 18):
                df_completed_rounds[f"{i} Score"] = None

        # Remove the "Thru" column for completed rounds
        for i in range(1, num_rounds + 1):
            if all(df_completed_rounds[f"{i} Thru"] == 18):
                df_completed_rounds = df_completed_rounds.drop(columns=[f"{i} Thru"])

        # Add the DataFrame to the player_tables dictionary
        player_tables[player] = df_completed_rounds

    # Concatenate all tables into a single DataFrame
    combined_df = pd.concat(player_tables.values())

    # Sort the player_tables dictionary by the combined score in ascending order
    sorted_player_tables = sorted(player_tables.items(), key=lambda x: x[1]["Score"].sum())

    return sorted_player_tables, scheffler_counts, mcilroy_counts

# Function to display the tables in Streamlit
def display_tables(sorted_player_tables, scheffler_counts, mcilroy_counts):
    # Display the counts for Scheffler and McIlroy at the top
    st.subheader("Birdies, Eagles, and Holes-in-One Counts")
    st.write(f"**Scottie Scheffler Birdies:** {scheffler_counts['birdies']}")
    st.write(f"**Rory McIlroy Birdies:** {mcilroy_counts['birdies']}")

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
sorted_tables, scheffler_counts, mcilroy_counts = load_data()

# Function to refresh the app
def refresh_app():
    # Load and display the updated data
    st.experimental_rerun()

# Refresh button
if st.button("Refresh", key="refresh_button"):
    st.experimental_rerun()

# Refresh button
if st.button("Add Complaint", key="complaint_button"):
    st.warning("Fecking birdies")

# Load and display the initial data
sorted_tables, scheffler_counts, mcilroy_counts = load_data()
current_time = datetime.now(pytz.timezone('Europe/London')).strftime("%d-%m-%Y %H:%M")
st.title(f"Last Updated: {current_time}")
display_tables(sorted_tables, scheffler_counts, mcilroy_counts)

# Auto-refresh the app every 1 minute
while True:
    time.sleep(60)
    refresh_app()
