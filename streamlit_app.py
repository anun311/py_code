import streamlit as st 
st.header("Rock Paper Scissors ✊🖐️✌️")
st.write("Can you beat a computer at Rock-Paper-Scissors?")
st.divider()

st.button("Quit", type="primary")

win, loss, tie = 0, 0, 0

left, middle, right = st.columns(3)
if left.button("Rock ✊", use_container_width=True):
    win += 1
    left.markdown("You clicked Rock ✊.")
if middle.button("Paper 🖐️", use_container_width=True):
    loss += 1
    middle.markdown("You clicked Paper 🖐️.")
if right.button("Scissors ✌️", use_container_width=True):
    tie += 1
    right.markdown("You clicked Scissors ✌️.")

st.text(f"""Your Score:: Win={win} Loss={loss} Tie={tie}""")




## streamlit run TEST02_StreamLit.py
