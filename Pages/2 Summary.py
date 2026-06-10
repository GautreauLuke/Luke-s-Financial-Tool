## IMPORT LIBRARIES
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Monthly Cost Summary",
    layout = "wide"
    )

st.title("Let's see your expense summary.")
st.title("")


expense_costs = pd.read_csv("assets\ExpenseCosts.csv")

## expense_costs['Debit'] = expense_costs['Debit'].str.replace(["$" , ","],"")      -- For some reason, broken. Individual replaces below work just fine.

expense_costs['Debit'] = expense_costs['Debit'].str.replace("," , "")
expense_costs['Debit'] = expense_costs['Debit'].str.replace("$" , "")
expense_costs['Debit'] = expense_costs['Debit'].fillna(0)
expense_costs['Credit'] = expense_costs['Credit'].str.replace("," , "")
expense_costs['Credit'] = expense_costs['Credit'].str.replace("$" , "")
expense_costs['Credit'] = expense_costs['Credit'].fillna(0)
expense_costs['Discover'] = expense_costs['Discover'].str.replace("," , "")
expense_costs['Discover'] = expense_costs['Discover'].str.replace("$" , "")
expense_costs['Discover'] = expense_costs['Discover'].fillna(0)

expense_costs['Debit'] = expense_costs['Debit'].astype(float)

expense_agg = expense_costs.groupby(['Person', 'Type'])['Debit'].sum()

st.dataframe(data = expense_agg, height = "content")