"""
NUMBER GUESSING GAME...
"""
import streamlit as st
from random import choice, sample

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    st.title("Number Guessing Game")
    ch = st.text_input("Input two numbers(comma separated): ")
    if ch:
        try:
            ch_numbers = list(map(int, ch.split(',')))
            if set(ch_numbers).issubset(set(numbers)):
                st.write(f"Your choice: {ch_list}")
                two_number_result = sample(numbers, 2)
            if ch_numbers == two_number_result:
                st.write(f"You GUESS RIGHT: {two_number_resukt}")
                result = sample(numbers, 5)
            if set(ch_numbers).issubset(set(result):
                st.success("CORRECT NUMBER!!!!")
                st.write(f"Result: {result}")
            else:
                st.write("Better luck next time!")
            else:
                st.error("Invalid input. Please enter two digit from the numbers.")
            execept ValueError:
                st.error("Invalid input. Enter two digit separated by a comma.")
if __name__=="__main__":
    main()
