import random
import string
import streamlit as st
st.title('Password Generator')
sy=["@","/","#","$","&","?"]

length = st.text_input('Enter password length',placeholder="Enter a number")

placeholder="Enter a number"
def password(length):
    pas= ""
    for _ in range(int(length)):
        arr =[str(random.randint(0,9)),random.choice(string.ascii_letters),random.choice(sy)]
        ch=random.choice(arr)
        pas = pas + ch
        
    return pas
if st.button('Generate'):
    st.header(f":green[{password(length)}]")