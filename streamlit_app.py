import streamlit as st
import random 

st.header("Rock Paper Scissors ✊🖐️✌️")
st.write("Can you beat a computer at Rock-Paper-Scissors?")
st.divider()

if "click_count" not in st.session_state:
    st.session_state.click_count = 0
    st.session_state.pym = ""
    st.session_state.win = 0
    st.session_state.loss = 0
    st.session_state.tie = 0

left, middle, right = st.columns(3)
if left.button("Rock button", use_container_width=True):
    st.session_state.click_count += 1
    st.session_state.pym = "Rock"
if middle.button("Paper button", use_container_width=True):
    st.session_state.click_count += 1
    st.session_state.pym = "Paper"
if right.button("Scissors button", use_container_width=True):
    st.session_state.click_count += 1
    st.session_state.pym = "Scissors"

if st.button("Reset"):

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Win", st.session_state.win)
    col2.metric("Loss", st.session_state.loss)
    col3.metric("Tie", st.session_state.tie)
    col4.metric("Rounds", st.session_state.click_count)

    st.session_state.click_count = 0
    st.session_state.pym = ""
    st.session_state.win = 0
    st.session_state.loss = 0
    st.session_state.tie = 0
    

if st.session_state.click_count != 0:
    my_list = ["Rock", "Paper", "Scissors"]

    if st.session_state.click_count == 0:
        random_choice = ""
    else:
        random_choice = random.choice(my_list)

    player_choice = st.session_state.pym


    com_p = "https://feasibleth.com/wp-content/uploads/2025/03/Paper.png"
    com_r = "https://feasibleth.com/wp-content/uploads/2025/03/Rock.png"
    com_s = "https://feasibleth.com/wp-content/uploads/2025/03/Scissors.png"

    ply_p = "https://feasibleth.com/wp-content/uploads/2025/03/Paper-R.png"
    ply_r = "https://feasibleth.com/wp-content/uploads/2025/03/Rock-R.png"
    ply_s = "https://feasibleth.com/wp-content/uploads/2025/03/Scissors-R.png"

    if random_choice == "":
        img_comp = None
    elif random_choice == "Rock":
        img_comp = com_r
    elif random_choice == "Paper":
        img_comp = com_p
    elif random_choice == "Scissors":
        img_comp = com_s

    if player_choice == "":
        img_play = None
    elif player_choice == "Rock":
        img_play = ply_r
    elif player_choice == "Paper":
        img_play = ply_p
    elif player_choice == "Scissors":
        img_play = ply_s

    # st.write(f"Computer_move => {random_choice}")  # ผลลัพธ์ที่ได้จะแตกต่างกันไปในแต่ละครั้งที่รัน
    # st.write(f"Player_move => {player_choice}") # ผลลัพธ์จากการเลือกของผู้เล่นแต่ละครั้ง



    # if loop เฉพาะ tie กับ loss นอกนั้น win
    if (player_choice == "" and random_choice == ""):
        None
    elif (player_choice == random_choice):
        txt = "- Tie 😁 -"
        st.session_state.tie += 1
    elif (player_choice == 'Rock' and random_choice == 'Paper'):
        txt = "- You Loss 😭 -"
        st.session_state.loss += 1
    elif (player_choice == 'Paper' and random_choice == 'Scissors'):
        txt = "- You Loss 😭 -"
        st.session_state.loss += 1
    elif (player_choice == 'Scissors' and random_choice == 'Rock'):
        txt = "- You Loss 😭 -"
        st.session_state.loss += 1
    else:
        txt = "- You Win 😎 -"
        st.session_state.win += 1

    lf_, com_, ply_, rf_ = st.columns(4)
    lf_.metric("Round", st.session_state.click_count)
    lf_.metric("Tie", st.session_state.tie)
    com_.image(img_comp, caption="Computer Move")
    ply_.image(img_play, caption="Your Move")
    rf_.metric("Win", st.session_state.win)
    rf_.metric("Loss", st.session_state.loss)
    
    xx, yy, zz = st.columns(3)
    xx.write("")
    yy.metric("", txt)
    zz.write("")

## streamlit run TEST02_StreamLit.py
