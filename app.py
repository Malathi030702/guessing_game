import streamlit as st
import random
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="centered")

# Header Section
st.title("Welcome to My Portfolio!")
st.write("Hi! I'm **MALATHI**, a passionate data scientist and developer.")

# About Me Section
st.header("About Me")
st.write("""
I am a MALATHI, with a focus on data analysis, machine learning, and web development. 
I have worked on several projects involving [ Python].
In my free time, I enjoy learning new technologies and solving  the problems.
""")
st.header("project1:portfolio")

st.write("""
This is a description of the project, the problem it solves, and the tools/technologies used.
- **Technologies**: Python, Streamlit

""")


# Project 2
st.subheader("Project 2:Guessing game ")
st.write("""
This is a description of the project, the problem it solves, and the tools/technologies used.
- **Technologies**: streamlit,python

""")
# Skills Section
st.header("Skills")
st.write("""
- **Programming Languages**: Python,c++
- **Tools & Technologies**: GitHub,streamlit

""")

# Contact Section
st.header("Contact Me")
st.write("""
You can reach out to me via email at:malathi030702@gmail.com .
""")

# Footer Section
st.markdown("---")
st.write("Thank you for visiting my portfolio!")


# Guessing Game Section

st.subheader(" Guessing Game")


 # Game setu
number=range(1,10)
target_number=random.choice(number)
attempts = 0
chances=5

# Input for user's guess
guess = st.number_input(label="Enter your guess from 1 to 10:",step=1,format="%d")
if chances>0:
    if st.button("submit guess"):
        attempts += 1
        if guess < target_number:
          st.warning("Try a higher number!")
          chances-=1
        
        elif guess > target_number:
          st.warning("Try a lower number!")
          chances-=1
        else:
          st.success(f"Congratulations! You've guessed the number in {attempts} attempts")
         
else:
   st.error("Game over! you've run out of chances")         
                