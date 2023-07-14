import streamlit as st
import json
import random
import pandas as pd

def load_leaderboard():
    # Load leaderboard data from a JSON file
    try:
        with open('leaderboard.json', 'r') as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []
    return leaderboard

def load_user_data():
    # Load user data from a JSON file
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}
    return user_data

def save_user_data(user_data):
    # Save user data to a JSON file
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)

def get_state(user_data):
    # Define session state variables
    if 'state' not in st.session_state:
        st.session_state['state'] = {
            'logged_in': False,
            'signup': False,
            'user_data': user_data,
            'current_round': 1,
            'pick_order': None
        }
    return st.session_state['state']

def main():
    st.title("Golf Team Picker")

    # Load leaderboard data
    leaderboard = load_leaderboard()

    # Load user data from JSON file
    user_data = load_user_data()

    # Initialize session state
    state = get_state(user_data)

    # Check if the user is logged in
    if state['logged_in']:
        if user_data[state['username']]['admin']:
            admin_menu(user_data, state)
        else:
            team_picker(leaderboard, user_data, state['username'], state['current_round'], state)
    else:
        login(user_data, state, leaderboard)

def login(user_data, state, leaderboard):
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        # Check if the username and password are correct
        if username in user_data and user_data[username]['password'] == password:
            # Set the user as logged in
            state['logged_in'] = True
            state['username'] = username
            save_user_data(user_data)
            if user_data[username]['admin']:
                admin_menu(user_data, state)
            else:
                team_picker(leaderboard, user_data, username, state['current_round'], state)
        else:
            st.warning("Incorrect username or password.")

    if st.button("Sign Up"):
        state['signup'] = True

    if state['signup']:
        signup(user_data, state, leaderboard)

def signup(user_data, state, leaderboard):
    st.subheader("Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Create Account"):
        # Check if the username is already taken
        if new_username in user_data:
            st.warning("Username already exists. Please choose a different one.")
        else:
            # Add the new user to user_data
            user_data[new_username] = {'password': new_password, 'logged_in': True, 'selected_players': [], 'admin': False}
            save_user_data(user_data)
            st.success("Account created successfully. You are now logged in.")
            state['logged_in'] = True
            state['signup'] = False
            state['username'] = new_username
            team_picker(leaderboard, user_data, new_username, state['current_round'], state)

def admin_menu(user_data, state):
    st.subheader("Admin Menu")

    if st.button("Generate Picking Order"):
        generate_picking_order(user_data)

        # Display the picking order table
        picking_order_df = generate_picking_order_table(user_data)
        st.write("Picking Order:")
        st.dataframe(picking_order_df)

    if st.button("Logout"):
        state['logged_in'] = False
        state['username'] = None
        save_user_data(user_data)

def generate_picking_order(user_data):
    users = list(user_data.keys())
    random.shuffle(users)
    num_rounds = 4

    for round_num in range(1, num_rounds + 1):
        random.shuffle(users)
        for i, user in enumerate(users):
            user_data[user][f"pick{round_num}_order"] = i + 1

    save_user_data(user_data)

    st.success("Picking order generated successfully.")

def generate_picking_order_table(user_data):
    picking_order_data = {
        "Username": list(user_data.keys()),
        "Pick 1 Order": [user_data[user].get("pick1_order", "") for user in user_data],
        "Pick 2 Order": [user_data[user].get("pick2_order", "") for user in user_data],
        "Pick 3 Order": [user_data[user].get("pick3_order", "") for user in user_data],
        "Pick 4 Order": [user_data[user].get("pick4_order", "") for user in user_data]
    }

    picking_order_df = pd.DataFrame(picking_order_data)

    return picking_order_df

def team_picker(leaderboard, user_data, username, current_round, state):
    st.subheader("Team Picker")

    # Get the list of player names for the dropdown menu
    player_names = [f"{player['first_name']} {player['last_name']}" for player in leaderboard['leaderboard']]

    # Get the list of users and their picking orders
    users = list(user_data.keys())
    pick_order = get_pick_order(user_data, current_round)
    current_user_index = users.index(username)

    # Check if it's the user's turn to pick
    if current_user_index == pick_order[current_round - 1]:
        st.info(f"It's {username}'s turn to pick a golfer.")

        # Loop through the available golfers
        for i in range(5):  # Assuming we want to select 5 golfers
            st.write(f"**Golfer {i + 1}:**")
            selected_golfer = st.selectbox(f"Select Golfer {i + 1}", options=player_names)
            
            # Check if the golfer is selected
            if st.button("Select", key=f"select_{i}"):
                # Add the selected player to the user's selected_players list
                user_data[username]['selected_players'].append(selected_golfer)
                save_user_data(user_data)
                st.success(f"Selected: {selected_golfer}")

        # Display the selected golfers
        st.subheader("Selected Golfers")
        selected_golfers = user_data.get(username, {}).get('selected_players', [])
        if selected_golfers:
            for i, golfer in enumerate(selected_golfers, start=1):
                st.write(f"{i}. {golfer}")
        else:
            st.write("No golfers selected yet.")

        # Move to the next round
        if current_round < len(users):
            current_round += 1
            state['current_round'] = current_round
    else:
        next_user = users[pick_order[current_round - 1]]
        st.info(f"Please wait for {next_user} to pick a golfer.")

def get_pick_order(user_data, current_round):
    pick_order = []
    for user in user_data:
        pick_order.append(user_data[user][f"pick{current_round}_order"])
    return pick_order

# Run the app
if __name__ == "__main__":
    main()