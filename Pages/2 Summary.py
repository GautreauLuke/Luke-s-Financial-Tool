import streamlit as st

import pandas as pd

st.set_page_config(
    page_title = "Monthly Cost Summary",
    layout = "wide"
    )

st.title("Welcome to your expense summary.")

st.sidebar.success("[text]")

expense_costs = pd.read_csv(r"C:\Users\pc\Documents\GitHub\Luke's Financial Tool\assets\ExpenseCosts.csv")

## expense_costs['Debit'] = expense_costs['Debit'].str.replace(["$" , ","],"")      -- For some reason, broken. Individual replaces below work just fine.

expense_costs['Debit'] = expense_costs['Debit'].str.replace("," , "")
expense_costs['Debit'] = expense_costs['Debit'].str.replace("$" , "")

expense_costs['Debit'] = expense_costs['Debit'].astype(float)

expense_agg = expense_costs.groupby(['Person', 'Type'])['Debit'].sum()

st.dataframe(data = expense_agg, height = "content")