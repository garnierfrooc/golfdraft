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
            'pick_order': None,
            'current_user_index': 0,
            'selected_golfers': []
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
            team_picker(leaderboard, user_data, state)
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
                # Ensure leaderboard is initialized
                if not leaderboard:
                    leaderboard = generate_picking_order(user_data)
                admin_menu(user_data, state, leaderboard)
            else:
                team_picker(leaderboard, user_data, state, get_pick_order(user_data, state['current_round']))
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
            team_picker(leaderboard, user_data, state, get_pick_order(user_data, state['current_round']))

def admin_menu(user_data, state, leaderboard):
    st.subheader("Admin Menu")

    if st.button("Generate Picking Order"):
        if not leaderboard:  # Check if leaderboard is empty
            leaderboard = generate_picking_order(user_data)  # Initialize leaderboard
        else:
            generate_picking_order(user_data)  # Update the existing leaderboard

        # Display the picking order table
        picking_order_df = generate_picking_order_table(user_data)
        st.write("Picking Order:")
        st.dataframe(picking_order_df)

    if st.button("Logout"):
        state['logged_in'] = False
        state['username'] = None
        save_user_data(user_data)

    # Get the current round's golfers
    current_round_golfers = leaderboard.get(state['current_round'], [])  # Use .get() method
    st.write(f"Current Round {state['current_round']} Golfers:")
    st.write(current_round_golfers)

def generate_picking_order(user_data):
    users = list(user_data.keys())
    random.shuffle(users)
    num_rounds = 4

    leaderboard = {}
    for round_num in range(1, num_rounds + 1):
        leaderboard[round_num] = []  # Initialize an empty list for each round

    for round_num in range(1, num_rounds + 1):
        random.shuffle(users)
        for i, user in enumerate(users):
            user_data[user][f"pick{round_num}_order"] = i + 1
            leaderboard[round_num].append(user)  # Add the user to the current round's leaderboard

    save_user_data(user_data)

    st.success("Picking order generated successfully.")

    return leaderboard

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

def team_picker(leaderboard, user_data, state, pick_order):
    st.subheader("Team Picker")

    # Get the current user's picking order
    current_user_index = pick_order.index(state['username'])
    current_user = pick_order[current_user_index]

    # Check if it's the user's turn to pick
    if current_user == state['username']:
        st.info(f"It's {current_user}'s turn to pick a golfer.")

        # Get the available golfers for the current round
        current_round_golfers = leaderboard[state['current_round']]

        # Loop through the available golfers for the current round
        st.write(f"**Golfer {state['current_round']}:**")
        selected_golfer = st.selectbox(f"Select Golfer", options=current_round_golfers)

        # Check if the golfer is selected
        if st.button("Select"):
            # Add the selected player to the current user's selected_players
            user_data[current_user]['selected_players'].append(selected_golfer)
            save_user_data(user_data)

            # Add the selected player to the state's selected_golfers
            state['selected_golfers'].append(selected_golfer)

            # Remove the selected golfer from the available golfers
            current_round_golfers.remove(selected_golfer)

            # Increment the current_user_index
            current_user_index += 1

            # Check if all users have made their selection for the current round
            if current_user_index == len(pick_order):
                # Reset the current_user_index for the next round
                current_user_index = 0
                state['current_round'] += 1
                state['selected_golfers'] = []

            state['current_user_index'] = current_user_index
    else:
        st.info(f"Please wait for {current_user} to pick a golfer.")

    # Display the selected golfers
    st.subheader("Selected Golfers")
    if state['selected_golfers']:
        for i, golfer in enumerate(state['selected_golfers'], start=1):
            st.write(f"{i}. {golfer}")
    else:
        st.write("No golfers selected yet.")

# Helper function to get the picking order for the current round
def get_pick_order(user_data, current_round):
    pick_order = []
    for user in user_data:
        pick_order.append((user, user_data[user][f"pick{current_round}_order"]))
    pick_order.sort(key=lambda x: x[1])  # Sort the pick order based on the pick number
    pick_order = [user[0] for user in pick_order]  # Extract the usernames from the sorted pick order
    return pick_order

# Run the app
if __name__ == "__main__":
    main()