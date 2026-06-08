import streamlit as st
import pandas as pd

st.set_page_config("Test page 2")
st.title("Welcome to your second test page.")

expense_costs = pd.read_csv("assets\ExpenseCosts.csv")

remainder_table = expense_costs