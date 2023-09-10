import random
import streamlit as st
weapon = ["Rock", "Paper", "Scissor"]

st.title('RPS Game')

st.header("Choose from below: ")
option = st.selectbox(
    'Select one option',
    (weapon))


def computerChoice(option):
    if option == 'Rock':
        num = 1
    elif option == 'Paper':
        num = 2
    else:
        num = 3

    n = random.randint(1, 3)
    
    st.write(f":orange[Computer chosen :] {weapon[n-1]}")
    if n == num:
        st.header(":blue[Match draw]")
    elif (num == 1 and n == 3) or (num == 3 and n == 2) or (num == 2 and n == 1):
        st.header(":green[YOU WON]")
    else:
        st.header(":red[YOU LOSS]")


if st.button('Play'):
    computerChoice(option)