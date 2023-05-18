import os

from dotenv import load_dotenv
import requests
import streamlit as st
import pandas as pd
import json

from collections import defaultdict

load_dotenv()

players = {
    "Daniel": [
        "Jon Rahm",
        "Russell Henley",
        "Sam Burns",
        "Victor Perez"
    ],
    "Sean": [
        "Justin Thomas",
        "Cameron Young",
        "Patrick Reed",
        "Denny McCarthy"
    ],
    "Andy": [
        "Tony Finau",
        "Keegan Bradley",
        "Sahith Theegala",
        "Webb Simpson"
    ],
    "Marcus": [
        "Jason Day",
        "Jordan Spieth",
        "Rickie Fowler",
        "Nick Taylor"
    ],
    "Lewis": [
        "Scottie Scheffler",
        "Viktor Hovland",
        "Dustin Johnson",
        "Talor Gooch"
    ],
    "Jonty": [
        "Brooks Koepka",
        "Tyrrell Hatton",
        "Shane Lowry",
        "Thomas Pieters"
    ],
    "Bean": [
        "Rory McIlroy",
        "Cameron Smith",
        "Adam Scott",
        "Gary Woodland"
    ],
    "Phil": [
        "Collin Morikawa",
        "Patrick Cantlay",
        "Hideki Matsuyama",
        "Joel Dahmen"
    ],
    "Gary": [
        "Max Homa",
        "Matt Fitzpatrick",
        "Justin Rose",
        "Phil Mickelson"
    ],
    "Jamie": [
        "Xander Schauffele",
        "Sungjae Im",
        "Wyndham Clark",
        "Mito Pereira"
    ]
}


def fetch_golf_stats():
    with open('leaderboard.json') as json_file:
        res = json.load(json_file)
        return res['leaderboard']


def sort_golfers(golfers: list):
    output = {}
    for golfer in golfers:
        output[f"{golfer['first_name']} {golfer['last_name']}"] = golfer['score']
    return output


golf_stats = fetch_golf_stats()
golfers = sort_golfers(golf_stats)

dataframes = []

for player, golfers_list in players.items():
    player_selection = []
    total_to_par = 0
    for golfer in golfers_list:
        player_selection.append((golfer, golfers.get(golfer)))
        total_to_par += golfers.get(golfer, 0)
    df = pd.DataFrame(player_selection, columns=['Player', 'Total'])
    df = df.sort_values('Total')
    df.reset_index(drop=True, inplace=True)
    dataframes.append((player, df, total_to_par))

dataframes = sorted(dataframes, key=lambda x: x[2])

st.set_page_config(layout="centered")

st.title("PGA Championship Draft Special")

for i in range(len(dataframes)):
    if i == 0:
        st.header(f"{dataframes[i][0]} 🏆")
    else:
      st.header(dataframes[i][0])
    st.write(f"Total: {dataframes[i][2]}")
    st.dataframe(dataframes[i][1], use_container_width=True)
